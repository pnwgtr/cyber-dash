import dash
from dash import html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import feedparser
import datetime
import json
import os
import time
from urllib.parse import urlparse


dash.register_page(__name__, path="/news")

DATA_FILE = os.path.join("data", "internal_updates.json")

# === HELPERS ===
def load_internal_updates():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading internal updates: {e}")
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

# === MULTIPLE RSS FEEDS ===
rss_urls = [
    "https://isc.sans.edu/rssfeed_full.xml",
    "https://feeds.feedburner.com/TheHackersNews?format=xml",
    "https://www.bleepingcomputer.com/feed/"
]

source_labels = {
    "isc.sans.edu": "SANS",
    "feeds.feedburner.com": "The Hacker News",
    "bleepingcomputer.com": "Bleeping Computer"
}

combined_entries = []

for url in rss_urls:
    try:
        parsed = feedparser.parse(url)
        for entry in parsed.entries:
            source = urlparse(url).netloc.replace("www.", "")
            entry.source = source
            entry.source_label = source_labels.get(source, source)
        combined_entries.extend(parsed.entries)
    except Exception as e:
        print(f"Error fetching feed from {url}: {e}")

# Sort entries by published date if available
def get_published(entry):
    pub = entry.get("published_parsed")
    return pub if pub is not None else time.gmtime(0)  # fallback to epoch if missing

combined_entries = sorted(combined_entries, key=get_published, reverse=True)

# === UI COMPONENTS ===
def internal_update_cards(updates):
    if not updates:
        return html.P("No internal updates yet.")
    return [
        dbc.Card([
            dbc.CardHeader([
                html.Span("🔒 Internal", className="badge bg-success me-2"),
                html.Strong(update["title"])
            ]),
            dbc.CardBody([
                html.Small(update["date"], className="text-muted"),
                html.P(update["body"], style={"fontSize": "0.9rem"})
            ])
        ], className="mb-3 shadow-sm border-start border-4 border-success")
        for update in updates
    ]

def public_news_cards(entries):
    return [
        dbc.Card([
            dbc.CardHeader([
                html.Span("🌐 Industry", className="badge bg-secondary me-2"),
                html.Strong(entry.title)
            ]),
            dbc.CardBody([
                html.Small(getattr(entry, "published", "No date"), className="text-muted d-block mb-1"),
                html.Small(f"Source: {entry.source_label}", className="text-muted mb-2 d-block"),
                html.P(getattr(entry, "summary", "No summary available."), style={"fontSize": "0.9rem"}),
                dbc.Button("Read more", href=entry.link, target="_blank", size="sm", color="primary")
            ])
        ], className="mb-3 shadow-sm border-start border-4 border-secondary")
        for entry in entries
    ]

layout = dbc.Container([
    dcc.Location(id="url"),
    html.H3("Internal Security Updates", className="my-4 fw-bold text-success"),
    html.Div(id="admin-form"),
    html.Div(id="internal-update-list", children=internal_update_cards(load_internal_updates()), className="mb-5"),

    html.H3("Cybersecurity News Headlines", className="my-4 fw-bold text-secondary"),
    dbc.Input(id="search-input", placeholder="Search industry news...", type="text", className="mb-3"),
    dcc.Tabs(id="source-tabs", value="all", children=[
        dcc.Tab(label="All", value="all")
    ] + [dcc.Tab(label=label, value=source) for source, label in source_labels.items()]),
    html.Div(id="news-list"),
    dbc.Button("Load More", id="load-more", color="secondary", className="my-3")
], fluid=True)

@dash.callback(
    Output("admin-form", "children"),
    Input("url", "search")
)
def toggle_admin_form(search):
    if "admin=true" not in (search or ""):
        return None

    return dbc.Form([
        dbc.Row([
            dbc.Col(dbc.Input(id="title-input", placeholder="Update title", type="text"), md=4),
            dbc.Col(dbc.Textarea(id="body-input", placeholder="Details about this update", rows=2), md=6),
            dbc.Col(dbc.Button("Submit", id="submit-update", color="success", className="w-100"), md=2)
        ], className="mb-4"),
        html.Div(id="form-response")
    ])

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

@dash.callback(
    Output("news-list", "children"),
    Input("search-input", "value"),
    Input("source-tabs", "value"),
    Input("load-more", "n_clicks")
)
def update_news_list(search_text, selected_source, n_clicks):
    limit = (n_clicks or 0) * 10 + 10
    filtered = combined_entries

    if selected_source != "all":
        filtered = [entry for entry in filtered if entry.source == selected_source]

    if search_text:
        search_text = search_text.lower()
        filtered = [entry for entry in filtered if search_text in entry.title.lower() or search_text in getattr(entry, "summary", "").lower()]

    return public_news_cards(filtered[:limit])
