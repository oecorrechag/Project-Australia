import pandas as pd
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

import utils.funtionsGraph as fg 

MenuModel = dbc.Row(children=[
    html.Div([
        html.H3('Menu'),
        dbc.Row(children=[
            dbc.Col(children=[
                dcc.Dropdown(['RFM', 'Kmeans', 'Kmedoids'], 'RFM', id='Page2Select1'),
            ]),
        ]),
    ]),
])

InfoModel = dbc.Card(
    dbc.CardBody(
        [   
            html.H4(id='title_model', className="card-title"),
            dcc.Markdown(id="text_model"),
        ], 
    ),
)
@callback(
    Output('title_model', 'children'),
    Output('text_model', 'children'),
    Input('Page2Select1', 'value'),
    )
def display_value(Page2Select1):

    if Page2Select1 == 'RFM':

        title_model = 'RFM'
        text_model = """
                    - Number of segments: 8.
                    - The best buyers belong to 8 group.
                    - The worst buyers belong to 1 group.
                    """,

    elif Page2Select1 == 'Kmeans':

        title_model = 'Kmeans'
        text_model = """
                    - Number of segments: 4
                    - The best buyers belong to 0 group.
                    - The worst buyers belong to 1 group.
                    """,
                    
    elif Page2Select1 == 'Kmedoids':

        title_model = 'Kmedoids'
        text_model = """
                    - Number of segments: 4
                    - The best buyers belong to 0 group.
                    - The worst buyers belong to 2 group.
                    """,

    return title_model, text_model


MenuGraph = dbc.Row(children=[
    html.Div([
        html.H3('Metric'),
        dbc.Row(children=[
            dbc.Col(children=[
                dcc.Dropdown(['Recency','Frequency','Money'], 'Recency', id='Page2Select2'),
            ]),
        ]),
    ]),
])
Page2Graph1 = dbc.Card(
    dbc.CardBody(
        [   
            dcc.Graph(id='Page2Graph1', figure={}),
        ]
    )#, style={"height": 450, "width":850},
)
@callback(
    Output('Page2Graph1', 'figure'),
    Input('g_long_rfm', 'data'),
    Input('g_long_kmeans', 'data'),
    Input('g_long_kmedoids', 'data'),
    Input('Page2Select1', 'value'),
    )
def display_value(g_long_rfm, g_long_kmeans, g_long_kmedoids, Page2Select1):
    g_long_rfm = pd.read_json(g_long_rfm)
    g_long_kmeans = pd.read_json(g_long_kmeans)
    g_long_kmedoids = pd.read_json(g_long_kmedoids)

    if Page2Select1 == 'RFM':
        fig = fg.snake(g_long_rfm)
    elif Page2Select1 == 'Kmeans':
        fig = fg.snake(g_long_kmeans)
    elif Page2Select1 == 'Kmedoids':
        fig = fg.snake(g_long_kmedoids)

    return fig