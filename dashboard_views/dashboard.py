# import dash
# from jobs import app
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# from jobs.routes import *
# import pdb
#
#
# app.layout = html.Div([
#     html.Div(
#         html.Pre(id='lasso', style={'overflowY': 'scroll', 'height': '100vh'}),
#         className="three columns"
#     ),
#
#     html.Div(
#         className="nine columns",
#         children=dcc.Graph(
#             id='graph',
#             figure={
#                 'data': trace,
#                 'layout': {
#                     'mapbox': {
#                         'accesstoken': (
#                             'pk.eyJ1Ijoic2gtYWRvbSIsImEiOiJjamp1YzljcHQwZzMwM2xxa3ZkYmtpbmo0In0.kMpk2CVfRBtCGg5AtjELDw'
#                         )
#                     },
#                     'margin': {
#                         'l': 0, 'r': 0, 'b': 0, 't': 0
#                     },
#                 }
#             }
#         )
#     )
# ], className="row")
#
#
# app.css.append_css({
#     'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
# })
#
#
# @app.callback(
#     Output('lasso', 'children'),
#     [Input('graph', 'selectedData')])
#
#
# def display_data(selectedData):
#     return json.dumps(selectedData, indent=2)
