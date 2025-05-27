import dash
from dash import html, dcc
import plotly.graph_objs as go
import pandas as pd

dash.register_page(__name__, path="/mfa")

mfa_df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Adoption %": [70, 75, 80, 85, 88, 92]
})

layout = html.Div([
    html.H2("MFA Adoption Trend", className="text-center"),
    dcc.Graph(
        figure=go.Figure(
            data=go.Scatter(x=mfa_df["Month"], y=mfa_df["Adoption %"], mode='lines+markers'),
            layout=go.Layout(title="MFA Adoption Over Time", xaxis_title="Month", yaxis_title="% Adoption")
        )
    )
])
