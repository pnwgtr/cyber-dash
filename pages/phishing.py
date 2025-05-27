import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path="/phishing")

phishing_df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Phishing Emails": [820, 640, 975, 1120, 900, 760]
})

fig = px.bar(phishing_df, x="Month", y="Phishing Emails", title="Phishing Emails Blocked by Month")

layout = html.Div([
    html.H2("Phishing Detection Trend", className="text-center"),
    dcc.Graph(figure=fig)
])
