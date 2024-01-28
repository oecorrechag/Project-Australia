from dash import html, Input, Output, State, callback
import dash_bootstrap_components as dbc

from utils.consts import LOGO, TITLE
from components.CallbacksHeader import modal


header = html.Nav([
            dbc.Navbar(
                dbc.Container(
                    [
                        html.A(
                            dbc.Row(
                                [
                                    dbc.Col(html.Img(src=LOGO, height="30px")),
                                    dbc.Col(dbc.NavbarBrand(TITLE, className="ms-2")),
                                ],
                                align="center",
                                className="g-0",
                            ),
                            href="/",
                            style={"textDecoration": "none"},
                        ),
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(className="navbar", children=[

                            dbc.NavLink("Home", href="/home", active="partial"),
                            
                            dbc.NavLink("Description", href="/description", active="partial"),

                            dbc.NavLink("Model", href="/model", active="partial"),

                            dbc.NavLink("About", href="/about", active="partial"),

                            modal,

                        ], id="navbar-collapse", is_open=False, navbar=True,
                        ),
                    ]
                ),
                color="dark",
                dark=True,
            ), 

    ], className='fixed-top'),


@callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
    