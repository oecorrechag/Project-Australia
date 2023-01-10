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
                dcc.Dropdown(['Recency','Frequency','Money'], 'Recency', id='Page2Select2'), #, 'Parallel'
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
    Input('original_data', 'data'),
    Input('Page2Select1', 'value'),
    Input('Page2Select2', 'value'),
    )
def display_value(data, Page2Select1, Page2Select2):
    data = pd.read_json(data)

    if Page2Select1 == 'RFM':
        data = data.loc[:,['recency','frequency','monetary','rfm']]
        data.rename(columns={'rfm':'model'}, inplace=True)
    elif Page2Select1 == 'Kmeans':
        data = data.loc[:,['recency','frequency','monetary','kmeans']]
        data.rename(columns={'kmeans':'model'}, inplace=True)
    elif Page2Select1 == 'Kmedoids':
        data = data.loc[:,['recency','frequency','monetary','kmedoids']]
        data.rename(columns={'kmedoids':'model'}, inplace=True)

    if Page2Select2 == 'Recency':
        fig = fg.recency_graph(data)
    elif Page2Select2 == 'Frequency':
        fig = fg.frequency_graph(data)
    elif Page2Select2 == 'Money':
        fig = fg.monetary_graph(data)
    else:
        fig = fg.recency_graph(data)

    # fig.update_layout(autosize=False, width=500, height=500)

    return fig