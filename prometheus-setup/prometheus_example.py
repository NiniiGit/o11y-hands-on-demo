from prometheus_client import start_http_server, Counter
import time

REQUEST_COUNT = Counter('myapp_requests_total', 'Total requests received')

if __name__ == '__main__':
    start_http_server(8000)  # Prometheus will scrape from this port
    while True:
        REQUEST_COUNT.inc()
        time.sleep(2)
