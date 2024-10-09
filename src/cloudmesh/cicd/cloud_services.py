import logging

class CloudServices:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_capabilities(self, cloud):
        if cloud == 'aws':
            return ['container', 'serverless', 'vm']
        elif cloud == 'azure':
            return ['container', 'serverless', 'vm']
        elif cloud == 'gcp':
            return ['container', 'serverless', 'vm']
        else:
            raise ValueError(f"Unsupported cloud provider: {cloud}")

    def get_container_registry(self, cloud):
        if cloud == 'aws':
            return 'Amazon ECR'
        elif cloud == 'azure':
            return 'Azure Container Registry'
        elif cloud == 'gcp':
            return 'Google Container Registry'
        else:
            raise ValueError(f"Unsupported cloud provider: {cloud}")

    def get_container_service(self, cloud):
        if cloud == 'aws':
            return 'Amazon ECS'
        elif cloud == 'azure':
            return 'Azure Container Instances'
        elif cloud == 'gcp':
            return 'Google Kubernetes Engine'
        else:
            raise ValueError(f"Unsupported cloud provider: {cloud}")

    def get_serverless_platform(self, cloud):
        if cloud == 'aws':
            return 'AWS Lambda'
        elif cloud == 'azure':
            return 'Azure Functions'
        elif cloud == 'gcp':
            return 'Google Cloud Functions'
        else:
            raise ValueError(f"Unsupported cloud provider: {cloud}")
