from dash import dcc, html
import dash_bootstrap_components as dbc

from components.CallbacksHome import Modal, Select_model

home = html.Div([

    Modal,

    html.Br(),

    dbc.Row(children=[
        dbc.Col(Select_model, md=6),
        dbc.Col([], md=6),
    ]),


], style={"padding": "0px 20px 0px 100px"})
