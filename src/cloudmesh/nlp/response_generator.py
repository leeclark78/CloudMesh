import logging

class ResponseGenerator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def generate(self, intent, result):
        self.logger.info(f"Generating response for intent: {intent}")
        
        if intent == 'cost_analysis':
            return self._generate_cost_analysis_response(result)
        elif intent == 'performance_optimization':
            return self._generate_performance_optimization_response(result)
        elif intent == 'resource_listing':
            return self._generate_resource_listing_response(result)
        elif intent == 'scaling':
            return self._generate_scaling_response(result)
        else:
            return "I'm sorry, I don't know how to respond to that query."

    def _generate_cost_analysis_response(self, result):
        return f"Your total cloud spend is ${result['total_cost']}. The most expensive service is {result['most_expensive_service']}."

    def _generate_performance_optimization_response(self, result):
        improvements = ", ".join(result['improvements'])
        return f"I've optimized your application's performance. The following improvements were made: {improvements}."

    def _generate_resource_listing_response(self, result):
        instances = ", ".join(result['instances'])
        return f"Here are your running instances: {instances}."

    def _generate_scaling_response(self, result):
        return f"I've scaled your application. The new capacity is {result['new_capacity']}."
