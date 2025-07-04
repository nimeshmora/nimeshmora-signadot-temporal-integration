from opentelemetry import baggage
from opentelemetry.baggage.propagation import W3CBaggagePropagator

ROUTING_KEY = "sd-routing-key"

class Baggage:    

    def extract_routing_key_from_baggage(self, baggage_header_value: str) -> str :

        if not baggage_header_value:
            return None
        
        carrier ={'baggage': baggage_header_value['baggage']}
        ctx = W3CBaggagePropagator().extract(carrier=carrier)

        return baggage.get_baggage(ROUTING_KEY, ctx)