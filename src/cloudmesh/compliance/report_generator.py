import logging

class ReportGenerator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def generate_report(self, compliance_results, recommendations):
        self.logger.info("Generating compliance report")
        report = "Multi-Cloud Compliance Report\n"
        report += "============================\n\n"
        
        for regulation, regulation_results in compliance_results.items():
            report += f"{regulation} Compliance:\n"
            report += "-----------------\n"
            for provider, provider_results in regulation_results.items():
                report += f"  {provider.upper()}:\n"
                for check, compliant in provider_results.items():
                    status = "Compliant" if compliant else "Non-compliant"
                    report += f"    - {check}: {status}\n"
                
                if provider in recommendations[regulation]:
                    report += "  Recommendations:\n"
                    for recommendation in recommendations[regulation][provider]:
                        report += f"    - {recommendation}\n"
                report += "\n"
            report += "\n"
        
        return report
