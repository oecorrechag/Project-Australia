import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback
from pages import description, home, about, model

from pages.header import header
from pages.footer import footer

df_ts = pd.read_parquet('data/df_ts.parquet.gzip')
df_cus = pd.read_parquet('data/df_cus.parquet.gzip')
df_cir = pd.read_parquet('data/df_cir.parquet.gzip')
df_sto = pd.read_parquet('data/df_sto.parquet.gzip')
g_long_rfm = pd.read_parquet('data/g_long_rfm.parquet.gzip')
g_long_kmeans = pd.read_parquet('data/g_long_kmeans.parquet.gzip')
g_long_kmedoids = pd.read_parquet('data/g_long_kmedoids.parquet.gzip')

data_store = html.Div([dcc.Store(id="df_ts", data=df_ts.to_json()),
                       dcc.Store(id="df_cus", data=df_cus.to_json()),
                       dcc.Store(id="df_cir", data=df_cir.to_json()),
                       dcc.Store(id="df_sto", data=df_sto.to_json()),
                       dcc.Store(id="g_long_rfm", data=g_long_rfm.to_json()),
                       dcc.Store(id="g_long_kmeans", data=g_long_kmeans.to_json()),
                       dcc.Store(id="g_long_kmedoids", data=g_long_kmedoids.to_json()),
                       dcc.Store(id="intermediate")
                       ])


app = Dash(__name__, title="Segmentation",
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           suppress_callback_exceptions=True,
           )
server = app.server


app.layout = html.Div([

    dcc.Location(id='url'),
    data_store,

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
    if (path == '/home') | (path == '/'):
        return home.home
    elif path == "/description":
        return description.layout1
    elif path == "/model":
        return model.layout2
    elif path == "/about":
        return about.about

@callback(Output('header', 'children'),
          Output('footer', 'children'),
          Input('url', 'pathname'))
def display_page(path):
    return  header, footer


if __name__ == '__main__':
    app.run_server(debug=True)

# if __name__ == "__main__":
#     app.run_server(host="0.0.0.0", port=5050)