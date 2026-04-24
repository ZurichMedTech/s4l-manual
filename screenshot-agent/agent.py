# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "browser-use",
#   "pydantic",
#   "python-dotenv",
#   "typer",
#   "tenacity",
# ]
# ///

from browser_use import Agent, Browser, BrowserProfile, BrowserSession, ChatOpenAI, Tools, ActionResult
from dataclasses import dataclass
from pydantic import BaseModel
import asyncio
import getpass
import json
from pathlib import Path
import re
from typing import Final, Optional
from urllib.parse import urlparse
from tenacity import AsyncRetrying, RetryError, retry_if_exception_type, stop_after_attempt, wait_fixed, TryAgain
import typer


_DEFAULT_RETRIES: Final[int] = 2  # how many times to retry a failed agent session before giving up on that screenshot
REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
app = typer.Typer()

# ---------------------------------------------------------------------------
# Screenshot-instruction parser
# ---------------------------------------------------------------------------

@dataclass
class ScreenshotTask:
    asset_path: str       # e.g. "assets/dashboard/help_from_dashboard.png"
    instructions: str     # the numbered steps
    source_file: Path     # which .md file it came from

class ScreenshotReport(BaseModel):
    success: bool
    message: str

@dataclass
class AgentResult:
    task: ScreenshotTask
    success: bool
    message: str

_SCREENSHOT_RE = re.compile(
    r"<!--\s*screenshot-instructions:\s*(\S+)\s*\n(.*?)-->",
    re.DOTALL,
)

_CONCURRENT_TASKS: Final[int] = 5  # how many agent sessions to run in parallel (browser instances)

def parse_screenshot_tasks(md_file: Path) -> list[ScreenshotTask]:
    """Extract all screenshot-instructions blocks from a markdown file."""
    content = md_file.read_text()
    return [
        ScreenshotTask(
            asset_path=m.group(1),
            instructions=m.group(2).strip(),
            source_file=md_file,
        )
        for m in _SCREENSHOT_RE.finditer(content)
    ]

def collect_all_tasks(docs_dir: Path) -> list[ScreenshotTask]:
    """Walk all .md files under docs_dir and collect screenshot tasks."""
    tasks: list[ScreenshotTask] = []
    for md_file in sorted(docs_dir.rglob("*.md")):
        tasks.extend(parse_screenshot_tasks(md_file))
    return tasks


def build_task(instructions_text: str, url: str) -> str:
    return f"""
You are a screenshot updater for the Sim4Life documentation repository.
Your job is to log in to the Sim4Life platform, navigate to each relevant UI area, and
take a fresh screenshot that replaces the existing one in the repo.

## Step 1 — Log in
1. Go to {url}
2. Wait for a moment for the page to load and for any popups to appear.
3. Log in using email x_email and password x_password.
   These are placeholders — the real values are injected securely.
   You might need to accept the privacy policy and licensing agreement. If so, accept them.

## Step 2 — Take screenshots
Follow the instructions below to navigate to the right UI
state, then use the **save_screenshot** action to capture it. Pass the exact `path`
value so the file is saved to the right location. You can follow the documentation for {url}
at https://zurichmedtech.github.io/s4l-manual/#/ for guidance on where/how to find each UI element.

**IMPORTANT — Stop on failure:** If you fail to save a screenshot (the save_screenshot
action returns an error, or you cannot navigate to the required UI area after a
reasonable attempt), **stop immediately**. Do NOT continue to the next screenshot.
Instead, proceed directly to Step 3 and report the failure.

## Instructions
{instructions_text}

## Step 3 — Report
When done (or when a failure occurs), use the **done** action and provide:
- **Completed:** list of screenshots successfully saved
- **Failed:** the screenshot that failed, with a brief explanation of what went wrong
- **Remaining:** list of screenshots not yet attempted
- **Notes:** anything unusual observed
"""


# ---------------------------------------------------------------------------
# Shadow-DOM-piercing JS used by custom tools
# ---------------------------------------------------------------------------
DEEP_QUERY_JS = """
function search(root, selector) {
    const el = root.querySelector(selector);
    if (el) return el;
    for (const child of root.querySelectorAll('*')) {
        if (child.shadowRoot) {
            const found = search(child.shadowRoot, selector);
            if (found) return found;
        }
    }
    return null;
}
"""

# ---------------------------------------------------------------------------
# Custom tools
# ---------------------------------------------------------------------------
tools = Tools()


@tools.action(
    description=(
        "Click an element by CSS selector, piercing shadow DOM boundaries. "
        "Use this instead of the normal click action when the target element "
        "is inside a shadow root and cannot be reached by a regular click."
    ),
)
async def deep_click(
    selector: str, browser_session: BrowserSession
) -> ActionResult:
    page = await browser_session.get_current_page()
    result = await page.evaluate(
        f"""(sel) => {{
            {DEEP_QUERY_JS}
            const el = search(document, sel);
            if (!el) return 'not found';
            const rect = el.getBoundingClientRect();
            const cx = rect.left + rect.width / 2;
            const cy = rect.top + rect.height / 2;
            const opts = {{bubbles: true, cancelable: true, clientX: cx, clientY: cy}};
            el.dispatchEvent(new PointerEvent('pointerdown', opts));
            el.dispatchEvent(new MouseEvent('mousedown', opts));
            el.dispatchEvent(new PointerEvent('pointerup', opts));
            el.dispatchEvent(new MouseEvent('mouseup', opts));
            el.dispatchEvent(new MouseEvent('click', opts));
            return 'clicked at ' + Math.round(cx) + ',' + Math.round(cy);
        }}""",
        selector,
    )
    if result == "not found":
        return ActionResult(error=f"Element not found: {selector}")
    return ActionResult(extracted_content=f"Clicked {selector} ({result})")


@tools.action(
    description=(
        "Take a screenshot and save it to the given repo-relative path "
        "(e.g. 'assets/dashboard/dashboard.png'). "
        "Optionally pass a CSS selector to capture only that element instead of "
        "the full page (e.g. '[osparc-test-id=\"supportCenterWindow\"]')."
    ),
)
async def save_screenshot(
    path: str, browser_session: BrowserSession, selector: str = ""
) -> ActionResult:
    abs_path = REPO_ROOT / path
    abs_path.parent.mkdir(parents=True, exist_ok=True)
    if selector:
        page = await browser_session.get_current_page()
        bounds_json = await page.evaluate(
            f"""(sel) => {{
                {DEEP_QUERY_JS}
                const el = search(document, sel);
                if (!el) return 'null';
                const r = el.getBoundingClientRect();
                return JSON.stringify({{x: r.x, y: r.y, width: r.width, height: r.height}});
            }}""",
            selector,
        )
        if not bounds_json or bounds_json == "null":
            return ActionResult(error=f"Element not found: {selector}")
        clip = json.loads(bounds_json)
        png_bytes = await browser_session.take_screenshot(clip=clip)
    else:
        png_bytes = await browser_session.take_screenshot()
    abs_path.write_bytes(png_bytes)
    return ActionResult(extracted_content=f"Screenshot saved to {path}")


async def run_agent(*, task: ScreenshotTask, email: str, password: str, url: str, headless: bool, retries: int) -> AgentResult:
    """Run a single agent session for one screenshot task."""
    print(f"\n{'='*60}")
    print(f"Screenshot: {task.asset_path}")
    print(f"    Source: {task.source_file.relative_to(REPO_ROOT)}")
    print(f"{'='*60}\n")

    instructions_text = f"### {task.asset_path}\n{task.instructions}"

    browser_profile = BrowserProfile(
        headless=headless,
        highlight_elements=False,
        extra_chromium_args=["--no-sandbox"], # the agent should be run inside a sandbox
        allowed_domains=[urlparse(url).hostname],
    )
    llm = ChatOpenAI(model="gpt-4.1-mini")
    task_text = build_task(instructions_text, url)
    def _create_agent(browser: Browser) -> Agent:
        return Agent(
                task=task_text,
                llm=llm,
                browser=browser,
                tools=tools,
                sensitive_data={"x_email": email, "x_password": password},
                use_vision=True,
                include_attributes=["osparc-test-id"],
                extend_system_message=(
                    "The Sim4Life dashboard uses shadow DOM. Standard click actions may "
                    "not reach elements inside shadow roots. When instructed to use "
                    "deep_click, prefer it over the normal click action."
                ),
                output_model_schema=ScreenshotReport,
                max_actions_per_step=3,
            )

    try:
        async for attempt in AsyncRetrying(
            stop=stop_after_attempt(retries),
            wait=wait_fixed(2),
            retry=retry_if_exception_type(TryAgain),
        ):
            with attempt:
                agent = _create_agent(Browser(browser_profile=browser_profile))
                history = await agent.run(max_steps=50)
                report: ScreenshotReport | None = history.structured_output
                if report is None or report.success is False:
                    raise TryAgain(f"Agent reported failure or no structured output: {report}")
    except RetryError:
        pass

    if report:
        success = report.success
        message = report.message
    else:
        success = False
        message = history.final_result() or "\n".join(
            c for c in history.extracted_content() if c
        )
    print(f"\nResult for {task.asset_path}: success={success}\n{message}")
    return AgentResult(task=task, success=success, message=message)

@app.command()
def main(
    url: str = typer.Argument(
        help="Base URL of the Sim4Life deployment, e.g. 'https://sim4life.io'.",
    ),
    asset: Optional[str] = typer.Option(
        None,
        help="Substring filter on asset path, e.g. 'help_from_dashboard'. "
        "If omitted, all screenshot tasks found in docs are run.",
    ),
    headless: bool = typer.Option(
        True,
        help="Run the browser in headless mode (no visible window).",
    ),
    retries: int = typer.Option(
        _DEFAULT_RETRIES,
        help="Number of times to retry a failed agent session before giving up on that screenshot.",
    ),
) -> None:
    """Run the screenshot-update agent for screenshot tasks embedded in docs."""
    tasks = collect_all_tasks(DOCS_DIR)
    if asset:
        tasks = [t for t in tasks if asset in t.asset_path]

    if not tasks:
        typer.echo("No screenshot tasks found.")
        raise typer.Exit(1)

    typer.echo(f"Found {len(tasks)} screenshot task(s):")
    for t in tasks:
        typer.echo(f"  {t.asset_path}  (from {t.source_file.relative_to(REPO_ROOT)})")

    email = input(f"\n{url} email: ")
    password = getpass.getpass(f"{url} password: ")

    async def run_all() -> list[AgentResult]:
        semaphore = asyncio.Semaphore(_CONCURRENT_TASKS)
        async def limited(task: ScreenshotTask) -> AgentResult:
            async with semaphore:
                return await run_agent(task=task, email=email, password=password, url=url, headless=headless, retries=retries)
        return await asyncio.gather(*(limited(t) for t in tasks))

    results = asyncio.run(run_all())

    succeeded = [r for r in results if r.success]
    failed = [r for r in results if not r.success]

    typer.echo(f"\n{'='*60}")
    typer.echo("SUMMARY")
    typer.echo(f"{'='*60}")
    typer.echo(f"{len(succeeded)}/{len(results)} screenshots updated successfully.\n")
    if succeeded:
        typer.echo("Updated:")
        for r in succeeded:
            typer.echo(f"  ✅ {r.task.asset_path}")
    if failed:
        typer.echo("\nFailed:")
        for r in failed:
            typer.echo(f"  ❌ {r.task.asset_path}")
            for line in r.message.splitlines()[:3]:
                typer.echo(f"      {line}")


if __name__ == "__main__":
    app()
