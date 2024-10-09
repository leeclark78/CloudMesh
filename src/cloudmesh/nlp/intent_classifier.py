import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

class IntentClassifier:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.vectorizer = TfidfVectorizer()
        self.classifier = MultinomialNB()
        self._train_classifier()

    def classify(self, query):
        self.logger.info(f"Classifying intent for query: {query}")
        vectorized_query = self.vectorizer.transform([query])
        intent = self.classifier.predict(vectorized_query)[0]
        return intent

    def _train_classifier(self):
        # Placeholder: In a real scenario, you'd train this on a large dataset of queries
        sample_queries = [
            "Show me the most expensive services",
            "Optimize the performance of my application",
            "List all running instances",
            "What's my current cloud spend",
            "Scale up my database",
        ]
        sample_intents = ['cost_analysis', 'performance_optimization', 'resource_listing', 'cost_analysis', 'scaling']
        
        vectorized = self.vectorizer.fit_transform(sample_queries)
        self.classifier.fit(vectorized, sample_intents)
