from dash import dcc, html
import dash_bootstrap_components as dbc

from components.CallbacksHome import Modal, Select_model, G1

home = html.Div([

    Modal,

    html.Br(),

    dbc.Row(children=[
        dbc.Col(Select_model, md=6),
        dbc.Col(G1, md=6),
    ]),


], style={"padding": "0px 20px 0px 100px"})
