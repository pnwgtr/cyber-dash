import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

# === Mock Data ===
vuln_df = pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], "Count": [45, 39, 31, 22, 15, 11]})
phish_df = pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], "Count": [820, 640, 975, 1120, 900, 760]})
mfa_df = pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], "Adoption": [70, 75, 80, 85, 88, 92]})
incident_df = pd.DataFrame({"Month": ["Apr", "May"], "Incidents": [2, 3]})
compliance_df = pd.DataFrame({"Framework": ["NIST CSF", "PCI DSS"], "Score %": [72, 64]})
tools_df = pd.DataFrame({"Tool": ["CrowdStrike", "Defender", "Tenable"], "Coverage %": [100, 60, 100]})

# === Styling Helpers ===
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

# === Trend Indicator Logic ===
def get_trend_arrow(current, previous):
    if current > previous:
        return "🔼", "red"
    elif current < previous:
        return "🔽", "green"
    else:
        return "➖", "gray"

# === Top Navigation ===
top_nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Dashboard", href="/")),
        dbc.NavItem(dbc.NavLink("Compliance", href="/compliance")),
        dbc.NavItem(dbc.NavLink("Culture", href="/culture")),
        dbc.NavItem(dbc.NavLink("Incidents", href="/incidents")),
        dbc.NavItem(dbc.NavLink("MFA", href="/mfa")),
        dbc.NavItem(dbc.NavLink("News", href="/news")),
        dbc.NavItem(dbc.NavLink("Phishing", href="/phishing")),
        dbc.NavItem(dbc.NavLink("Tools", href="/tools")),
        dbc.NavItem(dbc.NavLink("Vulnerabilities", href="/vulnerabilities")),
    ],
    pills=True,
    justified=True,
    className="mb-4"
)

# === Mini Chart Cards ===
mini_charts = dbc.Row([

    dbc.Col(html.A(dbc.Card([
        html.Div([
            html.Div("Critical Vulns", className="dashboard-section-title"),
            html.Span(f"{get_trend_arrow(vuln_df['Count'].iloc[-1], vuln_df['Count'].iloc[-2])[0]} {vuln_df['Count'].iloc[-1]}",
                      style={"color": get_trend_arrow(vuln_df['Count'].iloc[-1], vuln_df['Count'].iloc[-2])[1]})
        ], className="text-center mb-2"),
        dcc.Graph(figure=style_figure(px.line(vuln_df, x="Month", y="Count")), config=chart_config, style={"height": "320px"})
    ], style=card_style, className="h-100 dashboard-card border-0"), href="/vulnerabilities"), xs=12, md=4),

    dbc.Col(html.A(dbc.Card([
        html.Div([
            html.Div("Phishing Volume", className="dashboard-section-title"),
            html.Span(f"{get_trend_arrow(phish_df['Count'].iloc[-1], phish_df['Count'].iloc[-2])[0]} {phish_df['Count'].iloc[-1]}",
                      style={"color": get_trend_arrow(phish_df['Count'].iloc[-1], phish_df['Count'].iloc[-2])[1]})
        ], className="text-center mb-2"),
        dcc.Graph(figure=style_figure(px.bar(phish_df, x="Month", y="Count")), config=chart_config, style={"height": "320px"})
    ], style=card_style, className="h-100 dashboard-card border-0"), href="/phishing"), xs=12, md=4),

    dbc.Col(html.A(dbc.Card([
        html.Div([
            html.Div("MFA Adoption", className="dashboard-section-title"),
            html.Span(f"{get_trend_arrow(mfa_df['Adoption'].iloc[-1], mfa_df['Adoption'].iloc[-2])[0]} {mfa_df['Adoption'].iloc[-1]}%",
                      style={"color": get_trend_arrow(mfa_df['Adoption'].iloc[-1], mfa_df['Adoption'].iloc[-2])[1]})
        ], className="text-center mb-2"),
        dcc.Graph(figure=style_figure(px.line(mfa_df, x="Month", y="Adoption")), config=chart_config, style={"height": "320px"})
    ], style=card_style, className="h-100 dashboard-card border-0"), href="/mfa"), xs=12, md=4),

    dbc.Col(html.A(dbc.Card([
        html.Div([
            html.Div("Incidents", className="dashboard-section-title"),
            html.Span(f"{get_trend_arrow(incident_df['Incidents'].iloc[-1], incident_df['Incidents'].iloc[-2])[0]} {incident_df['Incidents'].iloc[-1]}",
                      style={"color": get_trend_arrow(incident_df['Incidents'].iloc[-1], incident_df['Incidents'].iloc[-2])[1]})
        ], className="text-center mb-2"),
        dcc.Graph(figure=style_figure(px.bar(incident_df, x="Month", y="Incidents")), config=chart_config, style={"height": "320px"})
    ], style=card_style, className="h-100 dashboard-card border-0"), href="/incidents"), xs=12, md=4),

    dbc.Col(html.A(dbc.Card([
        html.Div("Compliance", className="dashboard-section-title text-center mb-2"),
        dcc.Graph(figure=style_figure(px.bar(compliance_df, x="Framework", y="Score %")), config=chart_config, style={"height": "320px"})
    ], style=card_style, className="h-100 dashboard-card border-0"), href="/compliance"), xs=12, md=4),

    dbc.Col(html.A(dbc.Card([
        html.Div("Tool Coverage", className="dashboard-section-title text-center mb-2"),
        dcc.Graph(figure=style_figure(px.bar(tools_df, x="Coverage %", y="Tool", orientation='h')), config=chart_config, style={"height": "320px"})
    ], style=card_style, className="h-100 dashboard-card border-0"), href="/tools"), xs=12, md=4)

], className="gy-4")

# === Final Layout ===
layout = html.Div([
    html.Div([
        html.H1("Executive Summary Dashboard", className="dashboard-title"),
        html.P("A high-level view of cyber health, risks, and posture across the enterprise.", className="dashboard-subtitle"),
        html.Hr(),
        top_nav
    ]),
    mini_charts
], className="dashboard-wrapper")
