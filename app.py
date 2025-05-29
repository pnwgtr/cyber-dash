import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

# Initialize the Dash app with support for multipage
app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
server = app.server  # For deployment (e.g., with Render)

# Layout definition
app.layout = dbc.Container([
    # Header / Navbar
    dbc.NavbarSimple(
        brand="Cybersecurity Dashboard",
        color="primary",
        dark=True,
        fluid=True
    ),

    # Navigation links for each registered page
    dbc.Nav(
        [
            dbc.NavLink(page["name"], href=page["path"], active="exact")
            for page in dash.page_registry.values()
        ],
        pills=True,
        className="my-3"
    ),

    # Main content (the currently selected page)
    dash.page_container
], fluid=True)

# Run the app locally
if __name__ == "__main__":
    app.run(debug=True)
