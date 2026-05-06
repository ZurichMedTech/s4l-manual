FROM ghcr.io/astral-sh/uv:debian

ARG UID=1000
ARG GID=1000

ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright
RUN uvx browser-use install \
    && chmod -R o+rX "${PLAYWRIGHT_BROWSERS_PATH}"

RUN groupadd -g "$GID" agent || true \
    && useradd -m -u "$UID" -g "$GID" agent

USER agent
ENV UV_CACHE_DIR=/home/agent/.cache/uv
RUN mkdir -p /home/agent/.cache/uv

WORKDIR /app
ENTRYPOINT [ "uv" ]
