from dash import dcc, html, Input, Output, callback

footer = html.Div([
     html.Br(),
     html.Footer('© copyright, Build with Plotly and ❤ by'),
     html.A('Oscar', href='https://github.com/oecorrechag', target="_blank")
     ])
