# Django Backend Dockerfile
FROM ghcr.io/astral-sh/uv:python3.13-alpine AS builder

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev --no-install-project

COPY serviceCRM/ ./serviceCRM/
COPY manage.py ./

RUN uv sync --frozen --no-dev


FROM python:3.13-alpine

WORKDIR /app

RUN apk add --no-cache postgresql-client

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/serviceCRM/ /app/serviceCRM/
COPY --from=builder /app/manage.py /app/

RUN adduser -D -u 1000 appuser && \
    chown -R appuser:appuser /app

USER appuser

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "serviceCRM.asgi:application", "--host", "0.0.0.0", "--port", "8000"]