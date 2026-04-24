FROM ghcr.io/astral-sh/uv:debian

ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright
RUN uvx browser-use install

RUN useradd -m -u 1000 appuser
USER appuser

WORKDIR /app
ENTRYPOINT [ "uv" ]