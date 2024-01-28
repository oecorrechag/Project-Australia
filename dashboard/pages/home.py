from dash import html
import dash_bootstrap_components as dbc

from components.CallbacksHome import Select_model

home = dbc.Container([

    html.Br(),
    html.H3('Home Page'),

    dbc.Row([
        dbc.Col(className="col col-md-10 offset-md-1 col-lg-8 offset-lg-2 pt-2", children=[

            Select_model,

            ])
    ]),

    html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),

])
