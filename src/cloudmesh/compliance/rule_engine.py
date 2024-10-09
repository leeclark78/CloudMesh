import logging

class RuleEngine:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.rules = {
            'GDPR': self._gdpr_rules,
            'HIPAA': self._hipaa_rules
        }

    def evaluate(self, scan_results, regulations):
        self.logger.info(f"Evaluating compliance for regulations: {', '.join(regulations)}")
        compliance_results = {}
        
        for regulation in regulations:
            if regulation in self.rules:
                compliance_results[regulation] = self.rules[regulation](scan_results)
            else:
                self.logger.warning(f"Unsupported regulation: {regulation}")
        
        return compliance_results

    def _gdpr_rules(self, scan_results):
        results = {}
        for provider, provider_results in scan_results.items():
            results[provider] = {
                'data_encryption': provider_results.get('s3_encryption', False) or 
                                   provider_results.get('storage_encryption', False) or 
                                   provider_results.get('cloud_storage_encryption', False),
                'access_controls': provider_results.get('public_access_blocked', False) or 
                                   provider_results.get('network_security_groups_configured', False) or 
                                   provider_results.get('vpc_configured', False)
            }
        return results

    def _hipaa_rules(self, scan_results):
        results = {}
        for provider, provider_results in scan_results.items():
            results[provider] = {
                'data_encryption': provider_results.get('s3_encryption', False) or 
                                   provider_results.get('storage_encryption', False) or 
                                   provider_results.get('cloud_storage_encryption', False),
                'audit_logging': provider_results.get('cloudtrail_enabled', False) or 
                                 provider_results.get('activity_logs_enabled', False) or 
                                 provider_results.get('stackdriver_logging_enabled', False)
            }
        return results
