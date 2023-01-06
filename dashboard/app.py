
import pandas as pd

import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback
from components.layouts import header, footer, sidebar
from pages import home, page1, page2, about

import warnings
warnings.filterwarnings("ignore")

# import glob
# import os
# ROOT_FOLDER = os.path.abspath(os.path.join(
#     os.path.dirname(os.path.abspath(__file__)), os.pardir))
# SRC_FOLDER = os.path.join(ROOT_FOLDER, "src/")
# DATA_FOLDER = os.path.join(ROOT_FOLDER, "data/")
# ASSETS_FOLDER = os.path.join(SRC_FOLDER, "assets")

df = pd.read_parquet('data/data.parquet.gzip')
df_ts = pd.read_parquet('data/df_ts.parquet.gzip')
df_cus = pd.read_parquet('data/df_cus.parquet.gzip')
df_cir = pd.read_parquet('data/df_cir.parquet.gzip')
df_sto = pd.read_parquet('data/df_sto.parquet.gzip')

data_store = html.Div([dcc.Store(id="original_data", data=df.to_json()),
                       dcc.Store(id="df_ts", data=df_ts.to_json()),
                       dcc.Store(id="df_cus", data=df_cus.to_json()),
                       dcc.Store(id="df_cir", data=df_cir.to_json()),
                       dcc.Store(id="df_sto", data=df_sto.to_json()),
                       dcc.Store(id="intermediate")
                       ])


# external_style_sheet = glob.glob(os.path.join(
#     ASSETS_FOLDER, "bootstrap/css") + "/*.css")
# external_style_sheet += glob.glob(os.path.join(ASSETS_FOLDER,
#                                   "css") + "/*.css")
# external_style_sheet += glob.glob(os.path.join(ASSETS_FOLDER,
#                                   "fonts") + "/*.css")

app = dash.Dash(__name__, title="Segmentation",
                # external_stylesheets=[
                #     dbc.themes.BOOTSTRAP] + external_style_sheet,
                suppress_callback_exceptions=True,
                )

server = app.server



app.layout = html.Div([

    dcc.Location(id='url'),
    data_store,

    # Menu
    html.Aside(className="", children=[sidebar]),

    # Header
    html.Div(id='header'),

    # Pagina
    html.Div(id='page-content'),

    # Footer
    html.Div(id='footer'),

])


@callback(
    Output(component_id='page-content', component_property='children'),
    Input(component_id='url', component_property='pathname')
)
def routing(path):
    if path == "/":
        return home.home
    elif path == "/page1":
        return page1.layout1
    # elif path == "/page2":
    #     return page2.layout2
    # elif path == "/about":
    #     return about.about_page_content


@callback(Output('header', 'children'),
          Output('footer', 'children'),
          Input('url', 'pathname'))
def display_page(path):
    return  header, footer


if __name__ == '__main__':
    app.run_server(debug=True)