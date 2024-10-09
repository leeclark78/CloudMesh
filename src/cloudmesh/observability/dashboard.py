import logging
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

class ObservabilityDashboard:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.app = dash.Dash(__name__)
        self.setup_layout()

    def setup_layout(self):
        self.app.layout = html.Div([
            html.H1('CloudMesh Observability Dashboard'),
            dcc.Dropdown(
                id='cloud-provider-dropdown',
                options=[
                    {'label': 'AWS', 'value': 'aws'},
                    {'label': 'Azure', 'value': 'azure'},
                    {'label': 'GCP', 'value': 'gcp'}
                ],
                value='aws'
            ),
            dcc.Graph(id='metrics-graph')
        ])

        @self.app.callback(
            Output('metrics-graph', 'figure'),
            Input('cloud-provider-dropdown', 'value')
        )
        def update_graph(selected_provider):
            # Placeholder for real data fetching logic
            df = pd.DataFrame({
                "Metric": ["CPU", "Memory", "Network"],
                "Value": [40, 60, 80]
            })
            
            fig = px.bar(df, x="Metric", y="Value", title=f"{selected_provider.upper()} Metrics")
            return fig

    def run(self, debug=False, port=8050):
        self.logger.info(f"Starting Observability Dashboard on port {port}")
        self.app.run_server(debug=debug, port=port)
