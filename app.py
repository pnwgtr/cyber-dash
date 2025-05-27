import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import dash

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container([
    dbc.NavbarSimple(
        brand="Cybersecurity Dashboard",
        color="primary",
        dark=True,
        fluid=True
    ),
    dbc.Nav(
        [
            dbc.NavLink(page["name"], href=page["path"], active="exact")
            for page in dash.page_registry.values()
        ],
        pills=True,
        className="my-3"
    ),
    dash.page_container
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)
