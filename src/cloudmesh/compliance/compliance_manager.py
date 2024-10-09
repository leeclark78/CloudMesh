import logging
from .compliance_scanner import ComplianceScanner
from .rule_engine import RuleEngine
from .recommendation_engine import RecommendationEngine
from .report_generator import ReportGenerator

class ComplianceManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.scanner = ComplianceScanner()
        self.rule_engine = RuleEngine()
        self.recommendation_engine = RecommendationEngine()
        self.report_generator = ReportGenerator()

    def run_compliance_check(self, cloud_providers, regulations):
        self.logger.info(f"Running compliance check for {', '.join(cloud_providers)} on {', '.join(regulations)}")
        
        # Scan cloud environments
        scan_results = self.scanner.scan(cloud_providers)
        
        # Evaluate compliance rules
        compliance_results = self.rule_engine.evaluate(scan_results, regulations)
        
        # Generate recommendations
        recommendations = self.recommendation_engine.generate_recommendations(compliance_results)
        
        # Generate report
        report = self.report_generator.generate_report(compliance_results, recommendations)
        
        return report
