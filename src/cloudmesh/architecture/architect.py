import logging
from .requirement_analyzer import RequirementAnalyzer
from .service_recommender import ServiceRecommender
from .cost_optimizer import CostOptimizer
from .architecture_visualizer import ArchitectureVisualizer

class CloudArchitect:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.requirement_analyzer = RequirementAnalyzer()
        self.service_recommender = ServiceRecommender()
        self.cost_optimizer = CostOptimizer()
        self.visualizer = ArchitectureVisualizer()

    def design_architecture(self, requirements, budget):
        self.logger.info("Starting AI-assisted cloud architecture design")
        
        # Analyze requirements
        analyzed_requirements = self.requirement_analyzer.analyze(requirements)
        
        # Get initial service recommendations
        recommendations = self.service_recommender.recommend(analyzed_requirements)
        
        # Optimize for cost
        optimized_architecture = self.cost_optimizer.optimize(recommendations, budget)
        
        # Visualize the architecture
        visualization = self.visualizer.visualize(optimized_architecture)
        
        return {
            'architecture': optimized_architecture,
            'visualization': visualization
        }
