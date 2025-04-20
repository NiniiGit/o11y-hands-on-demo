FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install prometheus_client
CMD ["python", "prometheus_example.py"]

