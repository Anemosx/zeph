FROM python:3.11-slim AS builder
WORKDIR /app

RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

FROM python:3.11-slim
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn
COPY . .

EXPOSE 8088

ENV PYTHONPATH=/app

CMD ["uvicorn", "app.main:zeph_app", "--host", "0.0.0.0", "--port", "8088"]
