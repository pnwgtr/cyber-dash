import dash
from dash import html, dcc
import plotly.graph_objs as go
import pandas as pd

dash.register_page(__name__, path="/compliance")

compliance_df = pd.DataFrame({
    "Framework": ["NIST CSF", "PCI DSS"],
    "Score %": [72, 64]
})

layout = html.Div([
    html.H2("Compliance Scorecard", className="text-center"),
    dcc.Graph(
        figure=go.Figure(
            data=go.Bar(x=compliance_df["Framework"], y=compliance_df["Score %"]),
            layout=go.Layout(title="Compliance by Framework", xaxis_title="Framework", yaxis_title="Score (%)")
        )
    )
])
