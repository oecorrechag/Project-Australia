from dash import html
from utils.consts import GITHUB_PROFILE, LINKEDIN_PROFILE

about_me_text= "Data scientist with 2 years experience in market segmentation, building  data-intensive applications, complex challenges in multiple industries, proficient in predictive data modeling, processing, visualizing, and extracting actionable insights from data."

about_page_content = html.Div(className="col-md-12 col-sm-12 col-lg-8 mb-md-0 mb-4 card-chart-container", children=[html.Div(className="card", children=[
        html.Div(className="card-body p-0", children=[
            html.Div(className="d-flex justify-content-between", children=[
                html.Div(className="card-info p-4 w-75",
                         children=[html.H3(className="card-text", children=["Who am I?"]),
                                   html.Div(className="mb-2 mt-2", children=[
                                       html.P(className="card-title mb-2",
                                            children=[about_me_text], style={"font-size":"1rem"}),
                                   ]),
                                   html.Small(
                             className="card-text", children=[]),
                             html.A(href=LINKEDIN_PROFILE,target="_blank" ,children=[
                                html.I(className="bx bxl-linkedin-square mt-3", style={"font-size":"2.5rem" , "color":"#0a66c2"}),]),
                             html.A(href=GITHUB_PROFILE,target="_blank",
                             children=[html.I(className="bx bxl-github mt-3" , style={"font-size":"2.5rem" , "color":"#24292f"})]),
                         ]),
                html.Div(className="card-icon d-flex align-items-end", children=[
                    html.Img(className="img-fluid",
                             src="./assets/images/pc.jpg" , style={"border-radius":6})
                ]
                )
            ])
        ])
    ])
    ], style={"padding": "0px 0px 0px 100px"}
    )
    