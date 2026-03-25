from browser_use import Agent, Browser, BrowserSession, ChatOpenAI, Tools, ActionResult
from dotenv import load_dotenv
import asyncio
import getpass
import json
from pathlib import Path

load_dotenv()

REPO_ROOT = Path(__file__).resolve().parent.parent
_SCREEN_SHOT_MARKDOWN = Path(__file__).resolve().parent / "screenshot_list.md"
assert _SCREEN_SHOT_MARKDOWN.exists()

def build_task() -> str:
    return f"""
You are a screenshot updater for the Sim4Life documentation repository.
Your job is to log in to the Sim4Life platform, navigate to each relevant UI area, and
take a fresh screenshot that replaces the existing one in the repo.

## Step 1 — Log in
1. Go to https://sim4life.io
2. Log in using email x_email and password x_password.
   These are placeholders — the real values are injected securely.
   You might need to accept the privacy policy and licensing agreement. If so, accept them.

## Step 2 — Take screenshots
For each screenshot listed below, follow the instructions to navigate to the right UI
state, then use the **save_screenshot** action to capture it. Pass the exact `path`
value so the file is saved to the right location. You can follow the documentation for sim4life.io
at https://zurichmedtech.github.io/s4l-manual/#/ for guidance on where/how to find each UI element.
After taking a screenshot you must navigate to http://sim4life.io to ensure you start in a clean state.
Note that after already logging in, you should remain logged in for subsequent screenshots, so you won't need to log in again.

**IMPORTANT — Stop on failure:** If you fail to save a screenshot (the save_screenshot
action returns an error, or you cannot navigate to the required UI area after a
reasonable attempt), **stop immediately**. Do NOT continue to the next screenshot.
Instead, proceed directly to Step 3 and report the failure.

{_SCREEN_SHOT_MARKDOWN.read_text()}

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


async def main():
    email = input("sim4life.io email: ")
    password = getpass.getpass("sim4life.io password: ")

    browser = Browser(
        headless=False,
        allowed_domains=["*.sim4life.io", "sim4life.io", "zurichmedtech.github.io"],
    )
    llm = ChatOpenAI(model="gpt-4.1-mini")
    agent = Agent(
        task=build_task(),
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
        max_actions_per_step=3,
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
