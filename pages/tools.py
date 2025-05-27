import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path="/tools")

tools_df = pd.DataFrame({
    "Tool": ["CrowdStrike", "Defender", "Tenable"],
    "Coverage %": [100, 60, 100]
})

fig = px.bar(tools_df, x="Coverage %", y="Tool", orientation='h', title="Tool Coverage")

layout = html.Div([
    html.H2("Tool Inventory Coverage", className="text-center"),
    dcc.Graph(figure=fig)
])
