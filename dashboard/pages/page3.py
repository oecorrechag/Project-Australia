from dash import html
import dash_bootstrap_components as dbc

from components.CallbacksPage3 import MenuOptim, OptimModel
from components.CallbacksPage3 import Page3Graph1

layout3 = html.Div([

    dbc.Row(children=[

        dbc.Col([
            
            MenuOptim

        ], md=3),

        dbc.Col([

            dbc.Row(),

        ], md=8),

    ]),

    html.Br(),

    dbc.Row(children=[

        dbc.Col([
            
            OptimModel

        ], md=3),

        dbc.Col([

            Page3Graph1

        ], md=9),

    ]),

], style={"padding": "0px 0px 0px 100px"})

