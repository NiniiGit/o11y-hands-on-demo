## 🧪 Hands-on Demo Setup

This repo accompanies the blog post:  
👉 [Eliminating Observability Vendor Lock-in with OpenTelemetry](https://ninad-desai.medium.com/eliminating-observability-vendor-lock-in-with-opentelemetry-a-hands-on-demo-4be6065e0210)

It demonstrates three approaches to instrumenting a Python app:

- `apps/prometheus/`: Metrics exposed for Prometheus via native client
- `apps/elasticsearch/`: Metrics pushed manually to Elasticsearch
- `apps/otel/`: Vendor-agnostic metrics via OpenTelemetry Collector

### Prerequisites
- [Docker](https://www.docker.com/)
- [Python 3.10+](https://www.python.org/downloads/)

### 🔧 Configs & Runtime
- Prometheus scrape config: `configs/prometheus.yml`
- OTEL collector configs: `configs/otel-config-elasticsearch.yaml` & `configs/otel-config-prometheus.yaml`
