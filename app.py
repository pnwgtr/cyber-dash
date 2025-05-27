import dash
from dash import html, dcc
import pandas as pd

app = dash.Dash(__name__)
server = app.server

df = pd.DataFrame({
    "Metric": ["Critical Vulns", "Phishing Emails", "MFA Adoption"],
    "Value": [11, 760, "92%"]
})

app.layout = html.Div([
    html.H1("Cybersecurity Executive Dashboard"),
    html.Ul([
        html.Li(f"{row['Metric']}: {row['Value']}") for _, row in df.iterrows()
    ])
])

if __name__ == "__main__":
    app.run(debug=True)
