from dash import html

import dash_bootstrap_components as dbc

from components.CallbacksPage1 import Menu
from components.CallbacksPage1 import Page1Box1
from components.CallbacksPage1 import Page1Table
from components.CallbacksPage1 import Page1Graph1

layout1 = html.Div([
    Menu,
    html.H3('Page 1'),

    dbc.Row(children=[
        Page1Box1,
        Page1Table, 
        Page1Graph1,
    ]),


], style={"padding": "0px 0px 0px 100px"})