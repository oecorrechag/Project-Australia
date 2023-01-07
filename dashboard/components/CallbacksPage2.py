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
            html.P(id='text_model', className="card-text"),
        ]
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
        text_model = "Lorem ipsum dolor sit alaip amet consectetur, adipisicing elit. Adipisci, illo eos ad inventore reiciendis alias impedit repellendus dolorum. Itaque cum perspiciatis nihil magni, voluptatem quibusdam asperiores aperiam animi ipsa iure! Tenetur eligendi blanditiis soluta necessitatibus consectetur sit laudantium ipsum iste explicabo architecto velit vel aperiam nesciunt ut asperiores commodi dignissimos delectus mollitia adipisci est reprehenderit a, autem placeat qui. Fugit?",

    elif Page2Select1 == 'Kmeans':

        title_model = 'Kmeans'
        text_model = "Lorem ipsum dolor sit asdw amet consectetur, adipisicing elit. Adipisci, illo eos ad inventore reiciendis alias impedit repellendus dolorum. Itaque cum perspiciatis nihil magni, voluptatem quibusdam asperiores aperiam animi ipsa iure! Tenetur eligendi blanditiis soluta necessitatibus consectetur sit laudantium ipsum iste explicabo architecto velit vel aperiam nesciunt ut asperiores commodi dignissimos delectus mollitia adipisci est reprehenderit a, autem placeat qui. Fugit?",

    elif Page2Select1 == 'Kmedoids':

        title_model = 'Kmedoids'
        text_model = "Lorem ipsum dolor sit ee eramet consectetur, adipisicing elit. Adipisci, illo eos ad inventore reiciendis alias impedit repellendus dolorum. Itaque cum perspiciatis nihil magni, voluptatem quibusdam asperiores aperiam animi ipsa iure! Tenetur eligendi blanditiis soluta necessitatibus consectetur sit laudantium ipsum iste explicabo architecto velit vel aperiam nesciunt ut asperiores commodi dignissimos delectus mollitia adipisci est reprehenderit a, autem placeat qui. Fugit?",

    return title_model, text_model


MenuGraph = dbc.Row(children=[
    html.Div([
        html.H3('Metric'),
        dbc.Row(children=[
            dbc.Col(children=[
                dcc.Dropdown(['Recency', 'Frequency', 'Money', 'Parallel'], 'Recency', id='Page2Select2'),
            ]),
        ]),
    ]),
])



# Page2Box1 = dbc.Row(children=[
#     html.Div([
#         html.Div(id='page2_info1'),
#     ]),
# ])
# @callback(
#     Output('page2_info1', 'children'),
#     Input('Page2Select1', 'value'),
#     )
# def display_value(Page2Select1):
#     page2_info1 = f'You have selected {Page2Select1}'
#     return page2_info1



# Page2Graph1 = dbc.Row(children=[
#     html.Div([
#         dcc.Graph(id='page2_grafico1', figure={})
#     ]),
# ])
# @callback(
#     Output('page2_grafico1', 'figure'),
#     Input('intermediate', 'data'),
#     )
# def display_value(data):
#     data = pd.read_json(data, orient='split')
#     page2_grafico1 = fg.barras(data, x="Fruit", y="Amount", color="City")
#     return page2_grafico1


# Page2Graph2 = dbc.Row(children=[
#     html.Div([
#         dcc.Graph(id='page2_grafico2', figure={})
#     ]),
# ])
# @callback(
#     Output('page2_grafico2', 'figure'),
#     Input('intermediate', 'data'),
#     )
# def display_value(data):
#     data = pd.read_json(data, orient='split')
#     page2_grafico2 = fg.lineas(data, x="Date", y="Amount", color="City")
#     return page2_grafico2
