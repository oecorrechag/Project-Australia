import pandas as pd

from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

import plotly.express as px
import utils.funtionsGraph as fg 

MenuOptim = dbc.Row(children=[
    html.Div([
        html.H3('Menu'),
        dbc.Row(children=[
            dbc.Col(children=[
                dcc.RangeSlider(0, 800, 100, count=1, value=[0, 100], id='Page3Select1'),
                dcc.RangeSlider(0, 11, 1, count=1, value=[9, 11], id='Page3Select2'),
                dcc.RangeSlider(0, 350, 50, count=50, value=[300, 350], id='Page3Select3'),
            ]),
        ]),
    ]),
])

OptimModel = dbc.Card(
    dbc.CardBody(
        [   
            html.H4("Models"),
            dcc.Markdown(id="description"),
        ], 
    ),
)

Page3Graph1 = dbc.Card(
    dbc.CardBody(
        [   
            dcc.Graph(id='Page3Graph1', figure={}),
        ]
    )#, style={"height": 450, "width":850},
)
@callback(
    Output('description', 'children'),
    Output('Page3Graph1', 'figure'),
    Input('original_data', 'data'),
    Input('Page3Select1', 'value'),
    Input('Page3Select2', 'value'),
    Input('Page3Select3', 'value'),
    )
def display_value(data, Page3Select1, Page3Select2, Page3Select3):
    data = pd.read_json(data)
    data.insert(0, 'count', 1)

    data = data.loc[:,['count','recency','frequency','monetary','rfm','kmeans','kmedoids']]
    data = data[(data['recency'] >= Page3Select1[0]) & (data['recency'] <= Page3Select1[1])]
    data = data[(data['frequency'] >= Page3Select2[0]) & (data['frequency'] <= Page3Select2[1])]
    data = data[(data['monetary'] >= Page3Select3[0]) & (data['monetary'] <= Page3Select3[1])]

    datar = data.copy()
    datar = datar.loc[:,['rfm','count']]
    datar = datar.groupby('rfm').sum()
    datar = datar.nlargest(1, 'count').reset_index()

    datak = data.copy()
    datak = datak.loc[:,['kmeans','count']]
    datak = datak.groupby('kmeans').sum()
    datak = datak.nlargest(1, 'count').reset_index()

    datakk = data.copy()
    datakk = datakk.loc[:,['kmedoids','count']]
    datakk = datakk.groupby('kmedoids').sum()
    datakk = datakk.nlargest(1, 'count').reset_index()

    # print('modelo rfm: Segment: {}, units: {}'.format(datar.loc[0, 'rfm'], datar.loc[0, 'count']))
    # print('modelo kmeans: Segment: {}, units: {}'.format(datak.loc[0, 'kmeans'], datak.loc[0, 'count']))
    # print('modelo kmedoids: Segment: {}, units: {}'.format(datakk.loc[0, 'kmedoids'], datakk.loc[0, 'count']))

    description_sub = """
                      ### RFM
                      - Segment: {}, units: {}'
                      ### Kmeans
                      - Segment: {}, units: {}'
                      ### Kmedoids
                      - Segment: {}, units: {}'
                      """.format(datar.loc[0, 'rfm'], datar.loc[0, 'count'], 
                              datak.loc[0, 'kmeans'], datak.loc[0, 'count'],
                              datakk.loc[0, 'kmedoids'], datakk.loc[0, 'count']
                              )

    fig = px.parallel_coordinates(data, 
                                  dimensions=['recency', 'frequency', 'monetary'],
                                  color_continuous_scale=px.colors.diverging.Picnic,
                                  color_continuous_midpoint=2)

    return description_sub, fig