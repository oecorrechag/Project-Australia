from dash import html

from components.CallbacksPage2 import Menu
from components.CallbacksPage2 import Page2Box1
from components.CallbacksPage2 import Page2Graph1
from components.CallbacksPage2 import Page2Graph2

layout2 = html.Div([
    Menu,
    html.H3('Page 2'),
    Page2Box1,
    Page2Graph1,
    Page2Graph2,

], style={"padding": "0px 0px 0px 100px"})

