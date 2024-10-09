import logging
import boto3
from azure.mgmt.consumption import ConsumptionManagementClient
from google.cloud import billing

class CostAnalyzer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.aws_client = boto3.client('ce')  # AWS Cost Explorer
        self.azure_client = ConsumptionManagementClient(credentials, subscription_id)
        self.gcp_client = billing.CloudBillingClient()

    def get_costs(self, start_date, end_date):
        costs = {
            'aws': self._get_aws_costs(start_date, end_date),
            'azure': self._get_azure_costs(start_date, end_date),
            'gcp': self._get_gcp_costs(start_date, end_date)
        }
        return costs

    def _get_aws_costs(self, start_date, end_date):
        try:
            response = self.aws_client.get_cost_and_usage(
                TimePeriod={
                    'Start': start_date,
                    'End': end_date
                },
                Granularity='DAILY',
                Metrics=['UnblendedCost']
            )
            return response['ResultsByTime']
        except Exception as e:
            self.logger.error(f"Error fetching AWS costs: {str(e)}")
            return []

    def _get_azure_costs(self, start_date, end_date):
        try:
            costs = self.azure_client.usage_details.list(
                scope=f"/subscriptions/{subscription_id}",
                filter=f"usageStart ge '{start_date}' and usageEnd le '{end_date}'"
            )
            return list(costs)
        except Exception as e:
            self.logger.error(f"Error fetching Azure costs: {str(e)}")
            return []

    def _get_gcp_costs(self, start_date, end_date):
        try:
            billing_account = self.gcp_client.billing_account_path(billing_account_id)
            request = billing.QueryCostsRequest(
                billing_account=billing_account,
                date_range={
                    'start_date': {'year': start_date.year, 'month': start_date.month, 'day': start_date.day},
                    'end_date': {'year': end_date.year, 'month': end_date.month, 'day': end_date.day}
                }
            )
            response = self.gcp_client.query_costs(request)
            return response.cost_result
        except Exception as e:
            self.logger.error(f"Error fetching GCP costs: {str(e)}")
            return []
