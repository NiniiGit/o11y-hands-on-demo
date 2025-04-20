from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
import time

metric_reader = PeriodicExportingMetricReader(
    OTLPMetricExporter(endpoint="collector:4317", insecure=True)
)
provider = MeterProvider(metric_readers=[metric_reader])
metrics.set_meter_provider(provider)

meter = metrics.get_meter("myapp-meter")
request_counter = meter.create_counter("myapp_requests_total")

if __name__ == '__main__':
    while True:
        request_counter.add(1)
        time.sleep(2)
