#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "${REPO_ROOT}"

IMAGE_NAME="s4l-agent"

# build the image
docker build -t "$IMAGE_NAME" "$SCRIPT_DIR"