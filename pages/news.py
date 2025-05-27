# /pages/news.py
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

import datetime

# Register the page in Dash
dash.register_page(__name__, path="/news", name="Cyber News")

# Example mock content (you can load this from a database or JSON later)
news_items = [
    {
        "title": "FBI Warns of New Phishing Campaigns Targeting Hospitality Industry",
        "date": "2025-05-24",
        "summary": "The FBI has issued an alert regarding sophisticated phishing campaigns against casinos and hotels, urging increased email monitoring and user awareness training.",
        "link": "https://example.com/fbi-warning"
    },
    {
        "title": "MFA Rollout Update",
        "date": "2025-05-20",
        "summary": "MFA adoption has passed 90% property-wide. A follow-up audit will occur next month to ensure continued coverage and spot exceptions.",
        "link": "#"
    },
    {
        "title": "Q2 Vulnerability Scanning Results Released",
        "date": "2025-05-15",
        "summary": "The Q2 scan cycle identified fewer critical vulnerabilities, with major improvements in POS segmentation. Full results available internally.",
        "link": "#"
    }
]

# Layout
layout = html.Div([
    html.H2("Cybersecurity News & Updates", className="text-center mb-4"),
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4(item["title"], className="card-title"),
                        html.Small(item["date"], className="text-muted"),
                        html.P(item["summary"], className="card-text"),
                        dbc.Button("Read more", href=item["link"], color="primary", size="sm")
                    ])
                ], className="mb-4")
            ], width=12)
            for item in news_items
        ])
    ])
])
