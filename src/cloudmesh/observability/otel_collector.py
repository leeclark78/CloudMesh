import logging
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

class OTELCollector:
    def __init__(self, service_name):
        self.logger = logging.getLogger(__name__)
        self.service_name = service_name
        self.resource = Resource.create({"service.name": service_name})
        
        # Set up tracing
        trace.set_tracer_provider(TracerProvider(resource=self.resource))
        otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317")
        span_processor = BatchSpanProcessor(otlp_exporter)
        trace.get_tracer_provider().add_span_processor(span_processor)
        
        # Set up metrics
        metric_reader = PeriodicExportingMetricReader(
            OTLPMetricExporter(endpoint="http://localhost:4317")
        )
        self.meter_provider = MeterProvider(resource=self.resource, metric_readers=[metric_reader])
        
        self.logger.info(f"OTEL Collector initialized for service: {service_name}")

    def get_tracer(self):
        return trace.get_tracer(self.service_name)

    def get_meter(self):
        return self.meter_provider.get_meter(self.service_name)
