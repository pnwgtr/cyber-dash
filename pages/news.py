import dash
from dash import html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import feedparser
import datetime
import json
import os

dash.register_page(__name__, path="/news")

# File path for internal updates
DATA_FILE = os.path.join("data", "internal_updates.json")

def load_internal_updates():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_internal_update(title, body):
    updates = load_internal_updates()
    updates.insert(0, {
        "title": title,
        "date": datetime.datetime.now().strftime("%B %d, %Y"),
        "body": body
    })
    with open(DATA_FILE, "w") as f:
        json.dump(updates, f, indent=2)

# RSS feed for public news
rss_url = "https://feeds.feedburner.com/TheHackersNews"
feed = feedparser.parse(rss_url)

# Layout for internal cards
def internal_update_cards(updates):
    if not updates:
        return html.P("No internal updates yet.")
    return [
        dbc.Card([
            dbc.CardHeader(update["title"]),
            dbc.CardBody([
                html.Small(update["date"], className="text-muted"),
                html.P(update["body"])
            ])
        ], className="mb-3 shadow-sm")
        for update in updates
    ]

# Layout for public news
def public_news_cards(feed):
    return [
        dbc.Card([
            dbc.CardHeader(entry.title),
            dbc.CardBody([
                html.Small(entry.published, className="text-muted"),
                html.P(entry.summary, style={"fontSize": "0.9rem"}),
                dbc.Button("Read more", href=entry.link, target="_blank", size="sm", color="primary")
            ])
        ], className="mb-3 shadow-sm")
        for entry in feed.entries[:5]
    ]

layout = dbc.Container([
    html.H3("Internal Security Updates", className="my-4"),

    dbc.Form([
        dbc.Row([
            dbc.Col(dbc.Input(id="title-input", placeholder="Update title", type="text"), md=4),
            dbc.Col(dbc.Textarea(id="body-input", placeholder="Details about this update", rows=2), md=6),
            dbc.Col(dbc.Button("Submit", id="submit-update", color="success", className="w-100"), md=2)
        ], className="mb-4"),
        html.Div(id="form-response")
    ]),

    html.Div(id="internal-update-list", children=internal_update_cards(load_internal_updates()), className="mb-5"),

    html.H3("Cybersecurity Headlines", className="my-4"),
    html.Div(public_news_cards(feed))
], fluid=True)

# Callback to handle new post submission
@dash.callback(
    Output("internal-update-list", "children"),
    Output("form-response", "children"),
    Input("submit-update", "n_clicks"),
    State("title-input", "value"),
    State("body-input", "value"),
    prevent_initial_call=True
)
def handle_submit(n_clicks, title, body):
    if not title or not body:
        return dash.no_update, dbc.Alert("Please fill in both fields.", color="danger", dismissable=True)

    save_internal_update(title, body)
    updates = load_internal_updates()
    return internal_update_cards(updates), dbc.Alert("Update posted!", color="success", dismissable=True)
