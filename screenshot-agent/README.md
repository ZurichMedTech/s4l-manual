# Screenshot Agent

An automated tool that keeps the Sim4Life manual screenshots up to date. It reads
special instructions embedded in the documentation Markdown files, launches a
browser, logs in to a Sim4Life deployment, navigates to the right pages, and saves
fresh screenshots.

## Prerequisites
> Note: If you are working on windows, you must use this tool via [WSL](https://learn.microsoft.com/en-us/windows/wsl/install). It is not expected to work on Windows natively.

| Requirement | Why |
|---|---|
| **Docker** | The agent runs inside a container so you don't have to install Python or any dependencies on your machine. |
| **An OpenAI API key** | The agent uses GPT-4.1-mini to decide how to navigate the UI. Ask OPS how to get an API token associated with a paid account |

## Installing Docker

### Docker

Follow the official instructions for your operating system:

- **Linux (Ubuntu/Debian):** <https://docs.docker.com/engine/install/ubuntu/>

After installing, verify it works:

```bash
docker run --rm hello-world
```

## Quick Start

### 1. Set your OpenAI API key

```bash
export OPENAI_API_KEY="sk-..."
```

### 2. Build the Docker image

From the repository root, run:

```bash
bash screenshot-agent/build.bash
```

This builds a Docker image called `s4l-agent` that contains Python, the
browser, and all required libraries.

### 3. Run the agent

> Note: The agent will need access to an account (username and passwd). It is important that the 2FA is disabled for that account. Ideally you use a designated account for the agent which has minimally required priviliges and access to no credits.

```bash
bash screenshot-agent/sandboxed-agent.bash <url>
```
with a url pointing to the deployment you are targeting (e.g. https://s4l-master-zmt.click or https://sim4life.io). 

The agent will:

1. Scan all Markdown files under `docs/` for screenshot instructions.
2. Ask you for your Sim4Life email and password (typed interactively).
3. Open a browser (inside the container), log in, and take each screenshot.
4. Save the updated images directly into the repository.

When it finishes you will see a summary showing which screenshots were updated
and which (if any) failed.

### Filtering by screenshot

To update only a specific screenshot, use `--asset` with part of the file name:

```bash
bash screenshot-agent/sandboxed-agent.bash <url> --asset help_from_dashboard
```
For further agent options, run `bash screenshot-agent/sandboxed-agent.bash --help`

## Non headless mode

> WARNING: Running the agent outside its "sandbox" will give it acces to your **entire** filesystem. That can be dangerous!

By default the agent runs in a "headless" mode. I.e. the browser window never opens on the users desktop. This is a requirement when running the agent inside the sandbox container. However, for debugging purposes it can be useful to run the agent in a non-headless mode to see how the agent is actually navigating the osparc platform.
Run `uv run screenshot-agent/agent.py` to see how to do that (you will need to have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed)

## How Screenshot Instructions Work

Each screenshot the agent knows about is defined by a special HTML comment in the
documentation Markdown files. For example in `docs/overview/shop.md`:

```markdown
<!-- screenshot-instructions: assets/shop.png
1. On the dashboard page, click the `Profile` button in the top right corner.
2. In the menu which opens, click `The Shop` button.
3. Wait a moment for the shop window to appear.
4. Use **save_screenshot** with `path="assets/shop.png"`.
-->
```

The comment contains:

- The **output path** for the screenshot (relative to the repo root).
- Numbered **steps** the agent should follow to reach the right UI state and
  capture the image.

To add a new automated screenshot, insert a comment block like the one above in
the relevant Markdown file. The agent will pick it up automatically on the next
run.