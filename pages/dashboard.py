import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

# Mock summary data for mini charts
vuln_df = pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], "Count": [45, 39, 31, 22, 15, 11]})
phish_df = pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], "Count": [820, 640, 975, 1120, 900, 760]})
mfa_df = pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], "Adoption": [70, 75, 80, 85, 88, 92]})
incident_df = pd.DataFrame({"Month": ["Apr", "May"], "Incidents": [2, 3]})
compliance_df = pd.DataFrame({"Framework": ["NIST CSF", "PCI DSS"], "Score %": [72, 64]})
tools_df = pd.DataFrame({"Tool": ["CrowdStrike", "Defender", "Tenable"], "Coverage %": [100, 60, 100]})

mini_charts = dbc.Row([
    dbc.Col(dcc.Graph(figure=px.line(vuln_df, x="Month", y="Count", title="Critical Vulns"), config={"displayModeBar": False}), md=4),
    dbc.Col(dcc.Graph(figure=px.bar(phish_df, x="Month", y="Count", title="Phishing Volume"), config={"displayModeBar": False}), md=4),
    dbc.Col(dcc.Graph(figure=px.line(mfa_df, x="Month", y="Adoption", title="MFA Adoption"), config={"displayModeBar": False}), md=4),
    dbc.Col(dcc.Graph(figure=px.bar(incident_df, x="Month", y="Incidents", title="Incidents"), config={"displayModeBar": False}), md=4),
    dbc.Col(dcc.Graph(figure=px.bar(compliance_df, x="Framework", y="Score %", title="Compliance"), config={"displayModeBar": False}), md=4),
    dbc.Col(dcc.Graph(figure=px.bar(tools_df, x="Coverage %", y="Tool", orientation='h', title="Tool Coverage"), config={"displayModeBar": False}), md=4)
], className="gy-4")

layout = html.Div([
    html.H2("Executive Summary Dashboard", className="text-center mb-4"),
    mini_charts
])
