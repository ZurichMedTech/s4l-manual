# Screenshot Agent

An automated tool that keeps the Sim4Life manual screenshots up to date. It reads
special instructions embedded in the documentation Markdown files, launches a
browser, logs in to a Sim4Life deployment, navigates to the right pages, and saves
fresh screenshots — all without any manual clicking.

## Prerequisites

| Requirement | Why |
|---|---|
| **Docker** | The agent runs inside a container so you don't have to install Python or any dependencies on your machine. |
| **gVisor (`runsc`) runtime** | The container is launched with `--runtime=runsc` for sandboxing. |
| **An OpenAI API key** | The agent uses GPT-4.1-mini to decide how to navigate the UI. |

## Installing Docker and gVisor

### Docker

Follow the official instructions for your operating system:

- **Linux (Ubuntu/Debian):** <https://docs.docker.com/engine/install/ubuntu/>
- **macOS / Windows:** Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

After installing, verify it works:

```bash
docker run --rm hello-world
```

### gVisor runtime

gVisor provides an additional sandbox layer. Install it on Linux with:

```bash
# Add the gVisor repo and install runsc
sudo apt-get update && sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
curl -fsSL https://gvisor.dev/archive.key | sudo gpg --dearmor -o /usr/share/keyrings/gvisor-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/gvisor-archive-keyring.gpg] https://storage.googleapis.com/gvisor/releases release main" | sudo tee /etc/apt/sources.list.d/gvisor.list > /dev/null
sudo apt-get update && sudo apt-get install -y runsc

# Register the runtime with Docker and restart
sudo runsc install
sudo systemctl restart docker
```

Verify the runtime is available:

```bash
docker run --rm --runtime=runsc hello-world
```

> **macOS / Windows:** gVisor is not natively supported. If you only need to run
> the agent locally without the sandbox, you can edit `sandboxed-agent.bash` and
> remove the `--runtime=runsc` flag.

## Quick Start

### 1. Set your OpenAI API key

```bash
export OPENAI_API_KEY="sk-..."
```

### 2. Build the Docker image

From the repository root, run:

```bash
screenshot-agent/build.bash
```

This builds a Docker image called `s4l-agent` that contains Python, the
browser, and all required libraries.

### 3. Run the agent

```bash
screenshot-agent/sandboxed-agent.bash https://sim4life.io
```

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
screenshot-agent/sandboxed-agent.bash https://sim4life.io --asset help_from_dashboard
```

### Headless mode

To run without a visible browser window, add `--headless`:

```bash
screenshot-agent/sandboxed-agent.bash https://sim4life.io --headless
```

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