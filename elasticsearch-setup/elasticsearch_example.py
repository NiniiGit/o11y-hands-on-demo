from elasticsearch import Elasticsearch
import time

es = Elasticsearch("http://elasticsearch:9200")

if __name__ == '__main__':
    count = 0
    while True:
        count += 1
        es.index(index="my-metrics", document={
            "metric_name": "myapp_requests_total",
            "value": count,
            "timestamp": int(time.time() * 1000)
        })
        time.sleep(2)
