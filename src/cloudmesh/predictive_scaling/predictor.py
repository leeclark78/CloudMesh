import logging
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

class ResourcePredictor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model_file = 'resource_predictor_model.joblib'

    def train(self, historical_data):
        self.logger.info("Training resource prediction model")
        
        # Prepare the data
        X = historical_data.drop(['timestamp', 'resource_usage'], axis=1)
        y = historical_data['resource_usage']
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train the model
        self.model.fit(X_train, y_train)
        
        # Evaluate the model
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        self.logger.info(f"Model Mean Squared Error: {mse}")
        
        # Save the model
        joblib.dump(self.model, self.model_file)
        self.logger.info(f"Model saved to {self.model_file}")

    def predict(self, future_features):
        self.logger.info("Predicting future resource needs")
        
        # Load the model if it's not already in memory
        if not hasattr(self, 'model') or self.model is None:
            self.model = joblib.load(self.model_file)
        
        # Make predictions
        predictions = self.model.predict(future_features)
        
        return predictions
