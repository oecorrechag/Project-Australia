from dash import html

import dash_bootstrap_components as dbc

from components.CallbacksPage1 import Menu, G1


layout1 = html.Div([

    dbc.Row(children=[
        dbc.Col([Menu], md=6),
        dbc.Col(G1, md=6),
    ]),


], style={"padding": "0px 20px 0px 100px"})