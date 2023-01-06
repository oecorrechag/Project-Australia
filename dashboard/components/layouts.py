from dash import html
import dash_bootstrap_components as dbc

header = html.Div([
    html.H1('Segmentation - Project Australian'),
    html.Div([
        # html.P('Dash converts Python classes into HTML'),
        # html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
        ]),
    ], style={"padding": "10px 0px 0px 100px"})

footer = html.Div([
     html.Br(),
     html.Footer('© copyright, Build with Plotly and ❤ by'),
     html.A('Oscar', href='https://github.com/oecorrechag', target="_blank")
     ], style={"padding": "10px 0px 0px 100px", "text-align":"center"})

sidebar = html.Div(
    [
        html.Div(
            [
                html.Img(src="./assets/images/hora.png", style={"width": "3rem"}),
                html.H4("Main Menu", className="m-0"),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="tf-icons bx bx-trophy fas fa-home"), html.Span("Home" , className="me-2")],
                    href="/",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bx-group"),
                        html.Span("Page Description"),
                    ],
                    href="/page1",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bx-info-circle"),
                        html.Span("Page Model"),
                    ],
                    href="/page2",
                    active="exact",
                    className="pe-3",
                ),
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bx-wink-smile"),
                        html.Span("About"),
                    ],
                    href="/about",
                    active="exact",
                    className="pe-3",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar bg-menu-theme",
)