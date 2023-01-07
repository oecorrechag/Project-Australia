from dash import html

import dash_bootstrap_components as dbc

from components.CallbacksPage1 import Menu
from components.CallbacksPage1 import G1
from components.CallbacksPage1 import G2
from components.CallbacksPage1 import G3


layout1 = html.Div([

    dbc.Row(children=[
        dbc.Col([
            Menu,
            html.Br(),
            G1,
            html.Br(),
            G2, 
        ], md=6),
        dbc.Col(G3, md=6),
    ]),
    
], style={"padding": "0px 20px 0px 100px"})