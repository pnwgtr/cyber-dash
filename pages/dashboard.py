import dash
from dash import html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY])
server = app.server

# === FAKE DATA FOR KPI MINI-CHARTS ===
kpi_data = {
    "Compliance": [95, 96, 94, 97, 93, 94],
    "Phishing": [20, 18, 25, 22, 17, 15],
    "MFA Adoption": [50, 60, 65, 68, 70, 75],
    "Tooling": [12, 14, 13, 16, 15, 17],
    "Culture": [40, 42, 43, 41, 45, 46],
    "Vulnerabilities": [230, 210, 190, 220, 200, 180]
}

def create_kpi_box(title, values):
    fig = go.Figure(go.Scatter(y=values, mode="lines+markers", line=dict(color="#0066cc")))
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        height=100,
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False, visible=False),
        yaxis=dict(showgrid=False, visible=False)
    )

    return dbc.Card([
        dbc.CardBody([
            html.H6(title, className="text-center fw-bold"),
            dcc.Graph(figure=fig, config={"displayModeBar": False})
        ])
    ], className="shadow-sm p-2 m-1", style={"minWidth": "200px", "maxWidth": "250px"})

# === NAVIGATION ===
nav = dbc.Nav([
    dbc.NavLink("Dashboard", href="/", active="exact"),
    dbc.NavLink("Compliance", href="/compliance", active="exact"),
    dbc.NavLink("Phishing", href="/phishing", active="exact"),
    dbc.NavLink("MFA", href="/mfa", active="exact"),
    dbc.NavLink("Tooling", href="/tools", active="exact"),
    dbc.NavLink("Culture", href="/culture", active="exact"),
    dbc.NavLink("Vulnerabilities", href="/vulnerabilities", active="exact"),
    dbc.NavLink("Incidents", href="/incidents", active="exact"),
    dbc.NavLink("News", href="/news", active="exact")
], pills=True, justified=True, className="mb-4 fw-bold fs-5")

# === LAYOUT ===
app.layout = dbc.Container([
    dcc.Location(id="url"),
    html.Br(),
    nav,

    dash.page_container,

    html.Div([
        html.H4("Quick Metrics Overview", className="text-center text-primary my-4"),
        dbc.Row([
            dbc.Col(create_kpi_box(title, values)) for title, values in kpi_data.items()
        ], justify="center")
    ], style={"backgroundColor": "#f8f9fa", "borderRadius": "12px", "padding": "20px"})
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)
