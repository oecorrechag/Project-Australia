from dash import html
import dash_bootstrap_components as dbc

from utils.consts import GITHUB_PROFILE

footer = dbc.Container([
            dbc.Row(children=[

                html.Footer('© copyright, Build with Plotly and ❤ by'),
                html.A('Oscar', href=GITHUB_PROFILE, target="_blank"),

            ], className="row text-center"), 
        ], fluid=True, id="footer", className="pb-4 pt-4"),
        