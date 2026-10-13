FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock .python-version README.md ./
COPY src ./src

RUN uv sync --locked --no-dev

CMD ["uv", "run", "uvicorn", "santander_cycles_forecast.api:app", "--host", "0.0.0.0", "--port", "8000"]