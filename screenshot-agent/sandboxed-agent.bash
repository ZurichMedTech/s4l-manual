#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT_DIR_NAME="$(basename "$SCRIPT_DIR")"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

IMAGE_NAME="s4l-agent"
CACHE_VOLUME="s4l-agent-uv-cache"

# Run the agent
docker run --rm -it \
    --pids-limit=1000 \
    --security-opt=no-new-privileges \
    --cap-drop=ALL \
    --user="$(id -u):$(id -g)" \
    -v "$REPO_ROOT:/app" \
    -v "$CACHE_VOLUME:/.cache" \
    --tmpfs /.config \
    -e "OPENAI_API_KEY=${OPENAI_API_KEY:-}" \
    "$IMAGE_NAME" \
    "run" \
    "$SCRIPT_DIR_NAME/agent.py" \
    "--headless" \
    "$@"
