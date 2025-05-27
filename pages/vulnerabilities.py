import dash
from dash import html, dcc
import plotly.graph_objs as go
import pandas as pd

dash.register_page(__name__, path="/vulnerabilities")

# Mock data
vuln_df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Critical Vulns": [45, 39, 31, 22, 15, 11]
})

layout = html.Div([
    html.H2("Vulnerability Remediation Trend", className="text-center"),
    dcc.Graph(
        figure=go.Figure(
            data=go.Scatter(x=vuln_df["Month"], y=vuln_df["Critical Vulns"], mode='lines+markers'),
            layout=go.Layout(title="Critical Vulnerabilities Over Time", xaxis_title="Month", yaxis_title="Count")
        )
    )
])
