import logging
import pandas as pd
from datetime import datetime, timedelta

class DataCollector:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def collect_historical_data(self, days=30):
        self.logger.info(f"Collecting historical data for the past {days} days")
        
        # Placeholder: In a real scenario, you'd fetch this data from your cloud providers
        data = []
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        current_date = start_date
        while current_date <= end_date:
            data.append({
                'timestamp': current_date,
                'day_of_week': current_date.weekday(),
                'hour_of_day': current_date.hour,
                'is_weekend': 1 if current_date.weekday() >= 5 else 0,
                'resource_usage': self._mock_resource_usage(current_date)
            })
            current_date += timedelta(hours=1)
        
        return pd.DataFrame(data)

    def _mock_resource_usage(self, timestamp):
        # Placeholder: Generate mock resource usage data
        # In a real scenario, this would be actual usage data from your cloud providers
        base_usage = 50
        day_factor = 10 if timestamp.weekday() < 5 else -10
        hour_factor = 5 * (timestamp.hour - 12)
        return max(0, min(100, base_usage + day_factor + hour_factor + timestamp.minute / 2))

    def prepare_future_features(self, days=7):
        self.logger.info(f"Preparing future features for the next {days} days")
        
        future_data = []
        start_date = datetime.now()
        end_date = start_date + timedelta(days=days)
        
        current_date = start_date
        while current_date <= end_date:
            future_data.append({
                'day_of_week': current_date.weekday(),
                'hour_of_day': current_date.hour,
                'is_weekend': 1 if current_date.weekday() >= 5 else 0
            })
            current_date += timedelta(hours=1)
        
        return pd.DataFrame(future_data)
