from dash import html
import dash_bootstrap_components as dbc

from components.CallbacksHome import Select_model

home = html.Div([

    dbc.Row(children=[
        dbc.Col(Select_model, md=6),
        dbc.Col([], md=6),
    ]),


], style={"padding": "0px 20px 0px 100px"})
