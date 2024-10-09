import logging

class RecommendationEngine:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def generate_recommendations(self, compliance_results):
        self.logger.info("Generating compliance recommendations")
        recommendations = {}
        
        for regulation, regulation_results in compliance_results.items():
            recommendations[regulation] = self._generate_regulation_recommendations(regulation, regulation_results)
        
        return recommendations

    def _generate_regulation_recommendations(self, regulation, regulation_results):
        recommendations = {}
        for provider, provider_results in regulation_results.items():
            provider_recommendations = []
            for check, compliant in provider_results.items():
                if not compliant:
                    recommendation = self._get_recommendation(regulation, provider, check)
                    provider_recommendations.append(recommendation)
            recommendations[provider] = provider_recommendations
        return recommendations

    def _get_recommendation(self, regulation, provider, check):
        # Placeholder: In a real scenario, you'd have more sophisticated logic here
        # possibly using AI to generate context-aware recommendations
        return f"To comply with {regulation} on {provider}, ensure {check} is properly configured."
