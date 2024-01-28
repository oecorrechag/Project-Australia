from dash import html
import dash_bootstrap_components as dbc

from utils.consts import GITHUB_PROFILE, LINKEDIN_PROFILE


modal = html.Div(
    [
        dbc.Button("Codigo", id="open", className='btn-platzi', n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Codigo y redes sociales")),

                dbc.Row(className="m-3", children=[
                        dbc.Col(className="col-4 offset-4 center-text", children=[

                            html.A(html.Img(src='assets\icons\github.png', width="80px", height="80px"), id='moving', href=GITHUB_PROFILE),
                            html.A(html.Img(src='assets\icons\linkedin.png', width="100px", height="100px"), href=LINKEDIN_PROFILE),

                        ]),
                    ],
                ),

                dbc.ModalFooter(
                    dbc.Button(
                        "Cancelar", id="close", color="secondary", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id="modal",
            is_open=False,
        ),
    ]
)
