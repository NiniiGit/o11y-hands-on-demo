FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install elasticsearch==8.12.0
CMD ["python", "elasticsearch_example.py"]
