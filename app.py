import dash
from dash import html, dcc, page_container, page_registry
import dash_bootstrap_components as dbc

# Initialize Dash with page support
app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
server = app.server

# Define the main layout with navigation and content
app.layout = dbc.Container([
    html.H2("Cybersecurity Executive Dashboard", className="my-4 text-center fw-bold"),
    
    dbc.Nav(
        [
            dbc.NavLink(page["name"], href=page["relative_path"], active="exact")
            for page in page_registry.values()
        ],
        pills=True,
        justified=True,
        className="mb-4"
    ),

    page_container
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)
