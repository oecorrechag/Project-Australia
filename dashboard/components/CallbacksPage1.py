from dash import dcc, html, dash_table, Input, Output, callback
from dash_extensions.enrich import ServersideOutput
import dash_bootstrap_components as dbc

import pandas as pd

import utils.funtionsGraph as fg 

Menu = dbc.Row(children=[
    html.Div([
        html.H3('Menu'),
        html.Br(),
        dbc.Row(children=[
            dbc.Col(children=[
                dcc.Dropdown(['Uno', 'Dos', 'Tres'], 'Uno', id='Page1Select1'),
            ]),
            dbc.Col(children=[
                dcc.Dropdown({f'{i}': f'{i}' for i in ['SF', 'Montreal']}, 'SF', id='Page1Select2'),
            ]),
        ]),

        html.Br(),

    ]),
])

## filtros
@callback(ServersideOutput('intermediate', 'data'), 
          Input('original_data', 'data'),
          Input('Page1Select2', 'value'),
          memoize=True 
          )
def clean_data(data, Page1Select2):
    data = pd.read_json(data)
    data = data[data['City'] == Page1Select2]
    return data.to_json(date_format='iso', orient='split')
##

Page1Box1 = dbc.Row(children=[
    html.Div([
        html.Div(id='page1_info1'),
    ]),
])
@callback(
    Output('page1_info1', 'children'),
    Input('original_data', 'data'),
    Input('Page1Select1', 'value'),
    )
def display_value(data, Page1Select1):
    data = pd.read_json(data)
    page1_info1 = Page1Select1
    return page1_info1


Page1Table = dbc.Row(children=[
    html.Div([
        html.Div(id='page1_info2'),
    ]),
])
@callback(
    Output('page1_info2', 'children'),
    Input('original_data', 'data'),
    Input('Page1Select2', 'value'),
    )
def display_value(data, Page1Select2):
    data = pd.read_json(data)
    df2 = data[data['City'] == Page1Select2]
    page1_info2 = html.Div([
        dash_table.DataTable(
            data=df2.to_dict("rows"),
            columns=[{"id": x, "name": x} for x in df2.columns],
            page_size=20,
            # style_table={'height': '400px', 'overflowY': 'auto'},
            style_cell={'textAlign': 'center'},
            style_header={
                'backgroundColor': 'white',
                'fontWeight': 'bold'
            }
        )
    ])
    return page1_info2


Page1Graph1 = dbc.Row(children=[
    html.Div([
        dcc.Graph(id='page1_grafico1', figure={})
    ]),
])
@callback(
    Output('page1_grafico1', 'figure'),
    Input('original_data', 'data'),
    Input('Page1Select2', 'value'),
    )
def display_value(data, Page1Select2):
    data = pd.read_json(data)
    df2 = data[data['City'] == Page1Select2]
    page1_grafico1 = fg.barras(df2, x="Fruit", y="Amount", color="City")
    return page1_grafico1

