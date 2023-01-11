from dash import dcc, html
import dash_bootstrap_components as dbc

Select_model = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Segmentation", className="card-title"),
            html.H6("Some models", className="card-subtitle"),
            html.P(
                "In marketing, market segmentation is the process of dividing a broad consumer or business market, normally consisting of existing and potential customers, into sub-groups of consumers (known as segments) based on some type of shared characteristics.",
                className="card-text",
            ),
            dcc.Markdown("""
                         - Number of invoices: 100.000
                         - Number of clients: 33.004
                         - Space of time: 2 years
                         """),
            dbc.CardLink("RFM", href="https://en.wikipedia.org/wiki/RFM_(market_research)"),
            dbc.CardLink("Kmeans", href="https://en.wikipedia.org/wiki/K-means_clustering"),
            dbc.CardLink("Kmedoids", href="https://en.wikipedia.org/wiki/K-medoids"),
        ]
    ),
)
