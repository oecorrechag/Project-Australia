import pandas as pd
from dash import dcc, html, dash_table, Input, Output, callback
from dash_extensions.enrich import ServersideOutput
import dash_bootstrap_components as dbc

import utils.funtionsGraph as fg 

Menu = dbc.Row(children=[
    html.Div([
        html.H3('Menu'),
        dbc.Row(children=[
            dbc.Col(children=[
                dcc.Dropdown(['Day', 'Month', 'Year'], 'Month', id='Page1Select1'),
            ]),
        ]),
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
            html.H4("Units vs Customers vs Money", className="card-title"),
            html.H6("Units", className="card-subtitle"),
            dcc.Graph(id='Page1Graph1', figure={}),
        ]
    ),
)
@callback(
    Output('Page1Graph1', 'figure'),
    Input('df_cir', 'data'),
    )
def graphics(data):
    data = pd.read_json(data)
    return fg.grafico_circulo(data, 'stockcode', 'Stockcode')

G2 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Units vs Customers vs Money", className="card-title"),
            html.H6("Units", className="card-subtitle"),
            dcc.Graph(id='Page1Graph2', figure={}),
        ]
    ),
)
@callback(
    Output('Page1Graph2', 'figure'),
    Input('df_sto', 'data'),
    )
def graphics(data):
    data = pd.read_json(data)
    return fg.simple_bars_plot(data, 'stockcode', 'price', 'Stockcode', 'Price')

G3 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Units vs Customers vs Money", className="card-title"),
            html.H6("Units", className="card-subtitle"),
            dcc.Graph(id='Page1Graph3', figure={}),
            html.H6("Customers", className="card-subtitle"),
            dcc.Graph(id='Page1Graph4', figure={}),
            html.H6("Money", className="card-subtitle"),
            dcc.Graph(id='Page1Graph5', figure={}),
        ]
    ),
)
@callback(
    Output('Page1Graph3', 'figure'),
    Output('Page1Graph4', 'figure'),
    Output('Page1Graph5', 'figure'),
    Input('df_ts', 'data'),
    Input('df_cus', 'data'),
    Input('Page1Select1', 'value'),
    )
def graphics(df_ts, df_cus, Page1Select1):
    df_ts = pd.read_json(df_ts)
    df_cus = pd.read_json(df_cus)

    # diary
    if Page1Select1 == 'Day':
        fig1 = fg.simple_time_series(df_ts, x='date', y="contador", xl='Date', yl='Units')
        fig2 = fg.simple_time_series(df_cus, x='date', y="contador", xl='Date', yl='Customers')
        fig3 = fg.simple_time_series(df_ts, x='date', y="price", xl='Date', yl='Money')
    
    elif Page1Select1 == 'Month':
        df_ts2 = df_ts.copy()
        df_ts2 = df_ts2.loc[:,['date','contador']]
        df_ts2['date'] = df_ts2['date'].dt.to_period('M').astype(str)
        df_ts2 = df_ts2.groupby('date').sum().reset_index()
        fig1 = fg.simple_time_series(df_ts2, x='date', y="contador", xl='Date', yl='Units')

        df_cus2 = df_cus.copy()
        df_cus2['date'] = df_cus2['date'].dt.to_period('M').astype(str)
        df_cus2 = df_cus2.drop_duplicates()
        df_cus2 = df_cus2.groupby(['date']).sum().reset_index()
        fig2 = fg.simple_time_series(df_cus2, x='date', y="contador", xl='Date', yl='Customers')

        df_ts2 = df_ts.copy()
        df_ts2 = df_ts2.loc[:,['date','price']]
        df_ts2['date'] = df_ts2['date'].dt.to_period('M').astype(str)
        df_ts2 = df_ts2.groupby(['date']).sum().reset_index()
        fig3 = fg.simple_time_series(df_ts2, x='date', y="price", xl='Date', yl='Money')

    elif Page1Select1 == 'Year':
        df_ts2 = df_ts.copy()
        df_ts2 = df_ts2.loc[:,['date','contador']]
        df_ts2['date'] = df_ts2['date'].dt.to_period('Y').astype(str)
        df_ts2 = df_ts2.groupby('date').sum().reset_index()
        fig1 = fg.simple_time_series(df_ts2, x='date', y="contador", xl='Date', yl='Units')

        df_cus2 = df_cus.copy()
        df_cus2['date'] = df_cus2['date'].dt.to_period('Y').astype(str)
        df_cus2 = df_cus2.drop_duplicates()
        df_cus2 = df_cus2.groupby(['date']).sum().reset_index()
        fig2 = fg.simple_time_series(df_cus2, x='date', y="contador", xl='Date', yl='Customers')

        df_ts2 = df_ts.copy()
        df_ts2 = df_ts2.loc[:,['date','price']]
        df_ts2['date'] = df_ts2['date'].dt.to_period('Y').astype(str)
        df_ts2 = df_ts2.groupby(['date']).sum().reset_index()
        fig3 = fg.simple_time_series(df_ts2, x='date', y="price", xl='Date', yl='Money')

    return fig1, fig2, fig3