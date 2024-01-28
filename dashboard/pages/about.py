from dash import html
import dash_bootstrap_components as dbc
from utils.consts import GITHUB_PROFILE, LINKEDIN_PROFILE, about_me_text


about = dbc.Container([

    dbc.Row([
        dbc.Col(className="col col-md-10 offset-md-1 col-lg-8 offset-lg-2 pt-2", children=[

            dbc.Card(
                dbc.CardBody([
                        dbc.Row([

                            dbc.Col(className="col-12 col-md-6 mb-4", children=[

                                html.Img(className="img-fluid", src="./assets/pc.jpg" , style={"border-radius":6})

                            ]),

                            dbc.Col(className="col-12 col-md-6 mb-4", children=[

                                html.H4("Who am I?", className="card-title"),
                                html.Small("A student", className="card-subtitle"),
                                html.P(about_me_text, className="card-text"),
                                
                                html.A(html.Img(src='assets\icons\github.png', width="72px", height="72px"), id='moving', href=GITHUB_PROFILE),
                                html.A(html.Img(src='assets\icons\linkedin.png', width="90px", height="90px"), href=LINKEDIN_PROFILE),

                            ]),
                        ]),
                    ]
                ),
            )

        ])
    ]),
])










# about_page_content = html.Div(className="col-md-12 col-sm-12 col-lg-8 mb-md-0 mb-4 card-chart-container", children=[html.Div(className="card", children=[
#         html.Div(className="card-body p-0", children=[
#             html.Div(className="d-flex justify-content-between", children=[
#                 html.Div(className="card-info p-4 w-75",
#                          children=[html.H3(className="card-text", children=["Who am I?"]),
#                                    html.Div(className="mb-2 mt-2", children=[
#                                        html.P(className="card-title mb-2",
#                                             children=[about_me_text], style={"font-size":"1rem"}),
#                                    ]),
#                                    html.Small(
#                              className="card-text", children=[]),
#                              html.A(href=LINKEDIN_PROFILE,target="_blank" ,children=[
#                                 html.I(className="bx bxl-linkedin-square mt-3", style={"font-size":"2.5rem" , "color":"#0a66c2"}),]),
#                              html.A(href=GITHUB_PROFILE,target="_blank",
#                              children=[html.I(className="bx bxl-github mt-3" , style={"font-size":"2.5rem" , "color":"#24292f"})]),
#                          ]),
#                 html.Div(className="card-icon d-flex align-items-end", children=[
#                     html.Img(className="img-fluid",
#                              src="./assets/pc.jpg" , style={"border-radius":6})
#                 ]
#                 )
#             ])
#         ])
#     ])
#     ]
# )
    