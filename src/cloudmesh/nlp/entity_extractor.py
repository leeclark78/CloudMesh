import logging
import spacy

class EntityExtractor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.nlp = spacy.load("en_core_web_sm")

    def extract(self, query):
        self.logger.info(f"Extracting entities from query: {query}")
        doc = self.nlp(query)
        
        entities = {
            'cloud_providers': self._extract_cloud_providers(doc),
            'services': self._extract_services(doc),
            'applications': self._extract_applications(doc),
            'metrics': self._extract_metrics(doc)
        }
        
        return entities

    def _extract_cloud_providers(self, doc):
        cloud_providers = ['aws', 'azure', 'gcp']
        return [token.text.lower() for token in doc if token.text.lower() in cloud_providers]

    def _extract_services(self, doc):
        # Placeholder: In a real scenario, you'd have a more comprehensive list of services
        services = ['ec2', 'lambda', 'S3', 'virtual machines', 'functions', 'storage']
        return [token.text for token in doc if token.text.lower() in services]

    def _extract_applications(self, doc):
        return [ent.text for ent in doc.ents if ent.label_ == 'PRODUCT']

    def _extract_metrics(self, doc):
        metrics = ['cost', 'performance', 'latency', 'throughput']
        return [token.text for token in doc if token.text.lower() in metrics]
