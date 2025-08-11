FROM python:3.12-slim AS builder

RUN pip install --upgrade pip

RUN pip install uv

WORKDIR /app

COPY pyproject.toml uv.lock* ./

RUN uv pip install --system --no-cache .

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
