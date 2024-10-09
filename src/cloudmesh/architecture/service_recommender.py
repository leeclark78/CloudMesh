import logging

class ServiceRecommender:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def recommend(self, analyzed_requirements):
        self.logger.info("Recommending cloud services based on requirements")
        
        recommendations = {
            'aws': self._recommend_aws(analyzed_requirements),
            'azure': self._recommend_azure(analyzed_requirements),
            'gcp': self._recommend_gcp(analyzed_requirements)
        }
        
        return recommendations

    def _recommend_aws(self, requirements):
        services = []
        if requirements['categories'] == 'web':
            services.extend(['EC2', 'ELB', 'RDS'])
        if requirements['categories'] == 'data':
            services.extend(['S3', 'Redshift', 'EMR'])
        if requirements['categories'] == 'serverless':
            services.extend(['Lambda', 'API Gateway', 'DynamoDB'])
        if requirements['categories'] == 'ml':
            services.extend(['SageMaker', 'Comprehend', 'Rekognition'])
        return services

    def _recommend_azure(self, requirements):
        services = []
        if requirements['categories'] == 'web':
            services.extend(['Virtual Machines', 'App Service', 'Azure SQL'])
        if requirements['categories'] == 'data':
            services.extend(['Blob Storage', 'Synapse Analytics', 'HDInsight'])
        if requirements['categories'] == 'serverless':
            services.extend(['Functions', 'Logic Apps', 'Cosmos DB'])
        if requirements['categories'] == 'ml':
            services.extend(['Machine Learning', 'Cognitive Services'])
        return services

    def _recommend_gcp(self, requirements):
        services = []
        if requirements['categories'] == 'web':
            services.extend(['Compute Engine', 'Cloud Load Balancing', 'Cloud SQL'])
        if requirements['categories'] == 'data':
            services.extend(['Cloud Storage', 'BigQuery', 'Dataproc'])
        if requirements['categories'] == 'serverless':
            services.extend(['Cloud Functions', 'Cloud Run', 'Firestore'])
        if requirements['categories'] == 'ml':
            services.extend(['AI Platform', 'AutoML', 'Vision AI'])
        return services
