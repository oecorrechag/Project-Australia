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
    # print(n_open, n_close, is_open)
    if n_open or n_close:
        return not is_open
    return is_open



Select_model = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Title", className="card-title"),
            html.H6("Card subtitle", className="card-subtitle"),
            html.P(
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text",
            ),
            dbc.CardLink("Card link", href="#"),
            dbc.CardLink("External link", href="https://google.com"),
        ]
    ),
)


G1 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Title", className="card-title"),
            html.H6("Card subtitle", className="card-subtitle"),
            html.P(
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text",
            ),
            dbc.CardLink("Card link", href="#"),
            dbc.CardLink("External link", href="https://google.com"),
        ]
    ),
)

