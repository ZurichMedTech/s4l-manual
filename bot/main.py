from browser_use import Agent, Browser, BrowserSession, ChatOpenAI, Tools, ActionResult
from dotenv import load_dotenv
import asyncio
import base64
import getpass
import glob
import os
import re

load_dotenv()

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS_DIR = os.path.join(REPO_ROOT, "docs")

def discover_screenshots() -> list[dict[str, str]]:
    """Scan all .md files under docs/ and extract referenced .png asset paths with context."""
    pattern = re.compile(
        r'<img[^>]+src="(assets/dashboard/help_from_dashboard.png)"',
        re.IGNORECASE,
    )
    results: dict[str, dict[str, str]] = {}

    for md_path in glob.glob(os.path.join(DOCS_DIR, "**", "*.md"), recursive=True):
        rel_doc = os.path.relpath(md_path, REPO_ROOT)
        with open(md_path, encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            for m in pattern.finditer(line):
                asset_path = m.group(1)
                if asset_path in results:
                    continue
                # Grab a few surrounding lines for context
                start = max(0, i - 3)
                end = min(len(lines), i + 4)
                context = "".join(lines[start:end]).strip()
                results[asset_path] = {
                    "path": asset_path,
                    "doc": rel_doc,
                    "context": context,
                }

    return list(results.values())


def build_screenshot_list(screenshots: list[dict[str, str]]) -> str:
    lines = []
    for s in screenshots:
        lines.append(
            f"- **{s['path']}** (referenced in `{s['doc']}`)\n"
            f"  Context:\n  ```\n  {s['context']}\n  ```"
        )
    return "\n".join(lines)


def build_task(screenshots: list[dict[str, str]]) -> str:
    return f"""
You are a screenshot updater for the Sim4Life documentation repository.
Your job is to log in to the Sim4Life platform, navigate to each relevant UI area, and
take a fresh screenshot that replaces the existing one in the repo.

## Step 1 — Log in
1. Go to https://sim4life.io
2. Log in using email x_email and password x_password.
   These are placeholders — the real values are injected securely.

## Step 2 — Take screenshots
For each screenshot listed below, follow the instructions to navigate to the right UI
state, then use the **save_screenshot** action to capture it. Pass the exact `path`
value so the file is saved to the right location.

**IMPORTANT — Stop on failure:** If you fail to save a screenshot (the save_screenshot
action returns an error, or you cannot navigate to the required UI area after a
reasonable attempt), **stop immediately**. Do NOT continue to the next screenshot.
Instead, proceed directly to Step 3 and report the failure.

### Screenshot list

- **assets/dashboard/help_from_dashboard.png**
  1. On the dashboard page, look for a question-mark icon or "?" button in the top-right
     area of the navigation bar — this is the Help / Support button. Click it.
     If you cannot find it visually, use the **evaluate** action to locate it:
     `document.querySelector('[osparc-test-id="supportButton"]')?.getBoundingClientRect()`
     then click it with:
     `document.querySelector('[osparc-test-id="supportButton"]')?.click()`
  2. Wait a moment for the support center window/dialog to appear.
  3. Use **save_screenshot** with `path="assets/dashboard/help_from_dashboard.png"` and
     `selector='[osparc-test-id="supportCenterWindow"]'` to capture only the support dialog.

**Tip:** You can use the **evaluate** action to run JavaScript at any time to inspect
the page DOM, e.g. `document.querySelector('[osparc-test-id="..."]')?.outerHTML` to
check if an element exists or to find elements by their `osparc-test-id` attribute.

## Step 3 — Report
When done (or when a failure occurs), use the **done** action and provide:
- **Completed:** list of screenshots successfully saved
- **Failed:** the screenshot that failed, with a brief explanation of what went wrong
- **Remaining:** list of screenshots not yet attempted
- **Notes:** anything unusual observed
"""


# ---------------------------------------------------------------------------
# Custom tool: save a browser screenshot to a specific repo path
# ---------------------------------------------------------------------------
tools = Tools()


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
    abs_path = os.path.join(REPO_ROOT, path)
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    if selector:
        png_bytes = await browser_session.screenshot_element(selector)
    else:
        page = await browser_session.get_current_page()
        b64_data = await page.screenshot()
        png_bytes = base64.b64decode(b64_data)
    with open(abs_path, "wb") as f:
        f.write(png_bytes)
    return ActionResult(extracted_content=f"Screenshot saved to {path}")


async def main():
    screenshots = discover_screenshots()
    print(f"Discovered {len(screenshots)} screenshot(s) referenced in docs:\n")
    for s in screenshots:
        print(f"  {s['path']}  (from {s['doc']})")
    print()

    email = input("sim4life.io email: ")
    password = getpass.getpass("sim4life.io password: ")

    browser = Browser(headless=False)
    llm = ChatOpenAI(model="gpt-4.1-mini")
    agent = Agent(
        task=build_task(screenshots),
        llm=llm,
        browser=browser,
        tools=tools,
        sensitive_data={"x_email": email, "x_password": password},
        use_vision=True,
        max_actions_per_step=3,
        generate_gif="screenshot_update.gif",
    )
    history = await agent.run(max_steps=200)

    print("\n" + "=" * 60)
    print("RESULT")
    print("=" * 60)
    result = history.final_result()
    if result:
        print(result)
    else:
        print("No final result produced.")
        for content in history.extracted_content():
            if content:
                print(content)
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
