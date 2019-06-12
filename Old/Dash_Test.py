#!/usr/bin/env python3

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash temp'),

    dcc.Dropdown(options=[
        {"label":"Letter A","value":"A"},
        {"label":"Letter B","value":"B"},
        {"label":"Letter C","value":"C"}
    ], value="B")
])


if __name__ == '__main__':
    app.run_server(debug=True, host="172.26.95.55", port=8050)

