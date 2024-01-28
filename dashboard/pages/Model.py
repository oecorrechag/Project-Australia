from dash import html
import dash_bootstrap_components as dbc

from components.CallbacksModel import MenuModel
from components.CallbacksModel import InfoModel
from components.CallbacksModel import Page2Graph1

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
