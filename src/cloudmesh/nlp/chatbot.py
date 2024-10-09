import logging
from .intent_classifier import IntentClassifier
from .entity_extractor import EntityExtractor
from .query_executor import QueryExecutor
from .response_generator import ResponseGenerator

class CloudChatbot:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.intent_classifier = IntentClassifier()
        self.entity_extractor = EntityExtractor()
        self.query_executor = QueryExecutor()
        self.response_generator = ResponseGenerator()

    def process_query(self, query):
        self.logger.info(f"Processing query: {query}")
        
        # Classify the intent of the query
        intent = self.intent_classifier.classify(query)
        
        # Extract relevant entities from the query
        entities = self.entity_extractor.extract(query)
        
        # Execute the query based on intent and entities
        result = self.query_executor.execute(intent, entities)
        
        # Generate a natural language response
        response = self.response_generator.generate(intent, result)
        
        return response
