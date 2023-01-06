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
    # data = data[data['City'] == Page1Select2]
    return data.to_json(date_format='iso', orient='split')
##

G1 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Title", className="card-title"),
            html.H6("Units", className="card-subtitle"),
            dcc.Graph(id='Page1Graph1', figure={}),
            html.H6("Customers", className="card-subtitle"),
            dcc.Graph(id='Page1Graph2', figure={}),
            html.H6("Money", className="card-subtitle"),
            dcc.Graph(id='Page1Graph3', figure={}),
        ]
    ),
)
@callback(
    Output('Page1Graph1', 'figure'),
    Output('Page1Graph2', 'figure'),
    Output('Page1Graph3', 'figure'),
    Input('original_data', 'data'),
    )
def graphics(data):
    df = pd.read_json(data)

    # units
    df_ts = df.copy()
    df_ts = df_ts.loc[:,['date','contador']]
    df_ts = df_ts.groupby('date').sum().reset_index()
    fig1 = fg.simple_time_series(df_ts, x='date', y="contador", xl='Date', yl='Units')

    # customers
    df_ts = df.copy()
    df_ts = df_ts.loc[:,['date','customer_id','contador']]
    df_ts = df_ts.drop_duplicates()
    df_ts = df_ts.groupby(['date']).sum().reset_index()
    fig2 = fg.simple_time_series(df_ts, x='date', y="contador", xl='Date', yl='Units')

    # money
    df_ts = df.copy()
    df_ts = df_ts.loc[:,['date','price']]
    df_ts = df_ts.groupby(['date']).sum().reset_index()
    fig3 = fg.simple_time_series(df_ts, x='date', y="price", xl='Date', yl='Units')

    return fig1, fig2, fig3


