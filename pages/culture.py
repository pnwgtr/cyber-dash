import dash
from dash import html

dash.register_page(__name__, path="/culture")

layout = html.Div([
    html.H2("Security Culture Survey Results", className="text-center"),
    html.P("(Chart placeholder for culture & awareness metrics)", className="text-center text-muted")
])
