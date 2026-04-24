FROM ghcr.io/astral-sh/uv:debian

ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright
ENV UV_CACHE_DIR=/uv-cache
RUN uvx browser-use install \
    && chmod -R o+rX "${PLAYWRIGHT_BROWSERS_PATH}"

WORKDIR /app
ENTRYPOINT [ "uv" ]
