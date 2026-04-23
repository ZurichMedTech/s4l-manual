#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

IMAGE_NAME="s4l-agent"
CACHE_VOLUME="s4l-agent-uv-cache"

# Run the agent
docker run --rm -it \
    -v "$REPO_ROOT:/app" \
    -v "$CACHE_VOLUME:/root/.cache" \
    -e "OPENAI_API_KEY=${OPENAI_API_KEY:-}" \
    "$IMAGE_NAME" \
    "run" \
    "agent/agent.py" \
    "$@"
