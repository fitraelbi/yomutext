
FROM python:3.12-alpine AS builder

RUN pip install --no-cache-dir uv

WORKDIR /app


COPY pyproject.toml uv.lock* ./


RUN uv pip sync --system --no-cache pyproject.toml

FROM python:3.12-alpine

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
