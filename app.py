import dash
from dash import html, page_container, page_registry
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Cybersecurity Executive Dashboard"

app.layout = dbc.Container([
    html.H1("Cybersecurity Executive Dashboard", className="text-center my-4"),
    
    dbc.Nav(
        [
            dbc.NavLink(page["name"], href=page["path"], active="exact")
            for page in page_registry.values()
        ],
        pills=True,
        className="mb-4 justify-content-center"
    ),

    page_container  # This is what renders the content of the selected page
], fluid=True)

server = app.server

if __name__ == "__main__":
    app.run(debug=True)
