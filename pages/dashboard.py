
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

from plotly.subplots import make_subplots

dash.register_page(__name__, path="/")

# Mock data for mini charts
vuln_df = pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], "Count": [45, 39, 31, 22, 15, 11]})
phish_df = pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], "Count": [820, 640, 975, 1120, 900, 760]})
mfa_df = pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], "Adoption": [70, 75, 80, 85, 88, 92]})
incident_df = pd.DataFrame({"Month": ["Apr", "May"], "Incidents": [2, 3]})
compliance_df = pd.DataFrame({"Framework": ["NIST CSF", "PCI DSS"], "Score %": [72, 64]})
tools_df = pd.DataFrame({"Tool": ["CrowdStrike", "Defender", "Tenable"], "Coverage %": [100, 60, 100]})

# Helper to style each chart
card_style = {
    "padding": "5px",
    "backgroundColor": "#f8f9fa",
    "borderRadius": "10px",
    "boxShadow": "0 2px 6px rgba(0,0,0,0.1)",
    "height": "100%"
}

chart_config = {"displayModeBar": False}

def style_figure(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=10, b=10, l=10, r=10),
        font=dict(size=12),
        title=dict(x=0.5, xanchor='center'),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="#eee")
    )
    return fig

mini_charts = dbc.Row([
    dbc.Col(html.A(dbc.Card([
        html.Div("Critical Vulns", className="text-center fw-bold fs-5 mb-2"),
        dcc.Graph(figure=style_figure(px.line(vuln_df, x="Month", y="Count")), config=chart_config, style={"height": "320px", "padding": "0px 5px"})
    ], style=card_style, className="h-100 hover-shadow border-0"), href="/vulnerabilities"), md=4),

    dbc.Col(html.A(dbc.Card([
        html.Div("Phishing Volume", className="text-center fw-bold fs-5 mb-2"),
        dcc.Graph(figure=style_figure(px.bar(phish_df, x="Month", y="Count")), config=chart_config, style={"height": "320px", "padding": "0px 5px"})
    ], style=card_style, className="h-100 hover-shadow border-0"), href="/phishing"), md=4),

    dbc.Col(html.A(dbc.Card([
        html.Div("MFA Adoption", className="text-center fw-bold fs-5 mb-2"),
        dcc.Graph(figure=style_figure(px.line(mfa_df, x="Month", y="Adoption")), config=chart_config, style={"height": "320px", "padding": "0px 5px"})
    ], style=card_style, className="h-100 hover-shadow border-0"), href="/mfa"), md=4),

    dbc.Col(html.A(dbc.Card([
        html.Div("Incidents", className="text-center fw-bold fs-5 mb-2"),
        dcc.Graph(figure=style_figure(px.bar(incident_df, x="Month", y="Incidents")), config=chart_config, style={"height": "320px", "padding": "0px 5px"})
    ], style=card_style, className="h-100 hover-shadow border-0"), href="/incidents"), md=4),

    dbc.Col(html.A(dbc.Card([
        html.Div("Compliance", className="text-center fw-bold fs-5 mb-2"),
        dcc.Graph(figure=style_figure(px.bar(compliance_df, x="Framework", y="Score %")), config=chart_config, style={"height": "320px", "padding": "0px 5px"})
    ], style=card_style, className="h-100 hover-shadow border-0"), href="/compliance"), md=4),

    dbc.Col(html.A(dbc.Card([
        html.Div("Tool Coverage", className="text-center fw-bold fs-5 mb-2"),
        dcc.Graph(figure=style_figure(px.bar(tools_df, x="Coverage %", y="Tool", orientation='h')), config=chart_config, style={"height": "320px", "padding": "0px 5px"})
    ], style=card_style, className="h-100 hover-shadow border-0"), href="/tools"), md=4)
], className="gy-4")

layout = html.Div([
    html.H2("Executive Summary Dashboard", className="text-center mb-4"),
    mini_charts
])
