import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path="/incidents")

incidents_df = pd.DataFrame({
    "Month": ["Apr", "May"],
    "Incidents": [2, 3]
})

fig = px.bar(incidents_df, x="Month", y="Incidents", title="Incident Count Per Month")

layout = html.Div([
    html.H2("Incident History", className="text-center"),
    dcc.Graph(figure=fig)
])
