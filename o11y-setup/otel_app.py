from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
import time

# Define metric exporter with explicit endpoint
exporter = OTLPMetricExporter(endpoint="collector:4317", insecure=True)

# Create reader and provider with service name
reader = PeriodicExportingMetricReader(exporter)
provider = MeterProvider(
    resource=Resource.create({SERVICE_NAME: "otel-app"}),
    metric_readers=[reader],
)
metrics.set_meter_provider(provider)

# Meter setup
meter = metrics.get_meter("myapp-meter")
counter = meter.create_counter("myapp_requests_total")

# Main loop
if __name__ == "__main__":
    print("Starting metric emission loop")
    while True:
        counter.add(1)
        print("Incremented metric")
        time.sleep(2)
