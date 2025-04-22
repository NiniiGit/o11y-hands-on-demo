FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp
CMD ["python", "otel_app.py"]

