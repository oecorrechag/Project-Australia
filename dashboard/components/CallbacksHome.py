import pandas as pd

from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc

import utils.funtionsGraph as fg 

Modal =  html.Div(
        [
            dbc.Button("Open modal", id="open-dismiss"),
            dbc.Modal(
                [
                    dbc.ModalHeader(
                        dbc.ModalTitle("Dismissing"), close_button=False
                    ),
                    dbc.ModalBody(
                        "This modal has no close button and can't be dismissed by "
                        "pressing ESC. Try clicking on the backdrop or the below "
                        "close button."
                    ),
                    dbc.ModalBody(
                        "Aca va una prueba."
                    ),
                    dbc.ModalFooter(dbc.Button("Close", id="close-dismiss")),
                ],
                id="modal-dismiss",
                keyboard=False,
                backdrop="static",
            ),
        ],
    )

@callback(
    Output("modal-dismiss", "is_open"),
    [Input("open-dismiss", "n_clicks"), Input("close-dismiss", "n_clicks")],
    [State("modal-dismiss", "is_open")],
)
def toggle_modal(n_open, n_close, is_open):
    if n_open or n_close:
        return not is_open
    return is_open



Select_model = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Segmentation", className="card-title"),
            html.H6("Some models", className="card-subtitle"),
            html.P(
                "In marketing, market segmentation is the process of dividing a broad consumer or business market, normally consisting of existing and potential customers, into sub-groups of consumers (known as segments) based on some type of shared characteristics.",
                className="card-text",
            ),
            dbc.CardLink("RFM", href="https://en.wikipedia.org/wiki/RFM_(market_research)"),
            dbc.CardLink("Kmeans", href="https://en.wikipedia.org/wiki/K-means_clustering"),
            dbc.CardLink("Kmedoids", href="https://en.wikipedia.org/wiki/K-medoids"),
        ]
    ),
)
