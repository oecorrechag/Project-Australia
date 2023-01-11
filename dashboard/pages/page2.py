from dash import html
import dash_bootstrap_components as dbc

from components.CallbacksPage2 import MenuModel
from components.CallbacksPage2 import InfoModel
from components.CallbacksPage2 import MenuGraph
from components.CallbacksPage2 import Page2Graph1

layout2 = html.Div([

    dbc.Row(children=[

        dbc.Col([
            
            MenuModel,

            html.Br(),
            
            InfoModel,

        ], md=3),

        dbc.Col([

            Page2Graph1,

        ], md=8),
    ]),

], style={"padding": "0px 0px 0px 100px"})

