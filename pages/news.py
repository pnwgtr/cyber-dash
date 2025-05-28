import feedparser
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/news", name="Cyber News")

# --- RSS Feed Source ---
FEED_URL = "https://www.darkreading.com/rss.xml"
feed = feedparser.parse(FEED_URL)

# --- Create cards from entries ---
def make_news_card(entry):
    return dbc.Card(
        dbc.CardBody([
            html.H4(entry.title, className="card-title mb-1"),
            html.P(entry.published, className="text-muted", style={"fontSize": "0.8rem"}),
            html.P(entry.summary, className="card-text", style={"fontSize": "0.9rem", "lineHeight": "1.4"}),
            dbc.Button("Read more", href=entry.link, target="_blank", size="sm", color="info", className="mt-2")
        ]),
        className="shadow-sm mb-4",
        style={
            "borderLeft": "4px solid #0d6efd",
            "backgroundColor": "#f8f9fa"
        }
    )

news_cards = [make_news_card(entry) for entry in feed.entries[:6]]

# --- Page layout ---
layout = dbc.Container([
    html.H2("Cybersecurity News Feed", className="text-center my-4 fw-bold"),
    html.Div(
        dbc.Row([dbc.Col(card, md=6) for card in news_cards], className="gy-4"),
        className="px-3"
    )
])
