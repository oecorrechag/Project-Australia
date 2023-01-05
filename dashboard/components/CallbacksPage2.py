import pandas as pd

from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

import utils.funtionsGraph as fg 

Menu = dbc.Row(children=[
    html.Div([
        html.H3('Menu'),
        html.Br(),
        dcc.Dropdown({f'Page 2 - {i}': f'{i}' for i in ['London', 'Berlin', 'Paris']}, 'Page 2 - London', id='Page2Select1'),
        html.Br(),
    ]),
])


Page2Box1 = dbc.Row(children=[
    html.Div([
        html.Div(id='page2_info1'),
    ]),
])
@callback(
    Output('page2_info1', 'children'),
    Input('Page2Select1', 'value'),
    )
def display_value(Page2Select1):
    page2_info1 = f'You have selected {Page2Select1}'
    return page2_info1



Page2Graph1 = dbc.Row(children=[
    html.Div([
        dcc.Graph(id='page2_grafico1', figure={})
    ]),
])
@callback(
    Output('page2_grafico1', 'figure'),
    Input('intermediate', 'data'),
    )
def display_value(data):
    data = pd.read_json(data, orient='split')
    page2_grafico1 = fg.barras(data, x="Fruit", y="Amount", color="City")
    return page2_grafico1


Page2Graph2 = dbc.Row(children=[
    html.Div([
        dcc.Graph(id='page2_grafico2', figure={})
    ]),
])
@callback(
    Output('page2_grafico2', 'figure'),
    Input('intermediate', 'data'),
    )
def display_value(data):
    data = pd.read_json(data, orient='split')
    page2_grafico2 = fg.lineas(data, x="Date", y="Amount", color="City")
    return page2_grafico2
