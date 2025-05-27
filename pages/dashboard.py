import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path="/")

# Mock data
summary_data = pd.DataFrame({
    "Metric": ["Critical Vulns", "Phishing Emails", "MFA Adoption"],
    "Value": [11, 760, 92]
})

fig = px.bar(summary_data, x="Metric", y="Value", title="Executive Summary")

layout = html.Div([
    html.H2("Executive Summary Dashboard", className="text-center"),
    dcc.Graph(figure=fig)
])
