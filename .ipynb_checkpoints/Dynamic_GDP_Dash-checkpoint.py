#!/usr/bin/env python3

import sys
import os
import plotly.plotly as py
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd

#Import main function
sys.path.append(os.getcwd())
from RequestFun import *

#Read file
GDP_DF=pd.read_excel("/home/tobal/GithubProjects/Dynamic_GDP/GDP_1960_2017/API_NY.GDP.PCAP.CD_DS2_en_excel_v2_10576730.xlsx")
GDP_ValueOnly=GDP_DF.select_dtypes(['number'])
Years=[col for col in GDP_ValueOnly.columns]



###############################
###############################
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#UI
app.layout = html.Div(children=[
    html.H1(children='Hello Dash temp'),
    
    #User Inputs
    html.Div([
        dcc.Dropdown(id="DropdownCountry", 
                     options=[{'label':Countries, 'value':Countries} for Countries in GDP_DF["Country Name"]],
                    value=GDP_DF["Country Name"][0],
                    style={'width': '50%', 'display': 'inline-block'})
    ]),
    html.Div([
        dcc.Dropdown(id="DropdownYear", 
                     options=[{'label':YearValue, 'value':YearValue} for YearValue in Years],
                    value="2017",
                    style={'width': '50%', 'display': 'inline-block'})
    ]),
    dcc.Input(id="ToSearchPercent", value=0.005, type="number"),
    
    #Graph
    html.Div([
    dcc.Graph(id="GDPGraph", style={"width": "65%", "display": "block", 
                                    "margin-left": "auto",
                                    "margin-right": "auto"})
    ])
])

#Server
@app.callback(
    Output("GDPGraph", "figure"),
    [Input("DropdownCountry", "value"),
    Input("DropdownYear", "value"),
    Input("ToSearchPercent", "value")]
)
def Dummy(Var1, Var2, Var3):
    return(Get_Similar_GDP_Dashboard(CountryName=Var1, CountryYear=Var2, Percent=Var3))

#Run server
if __name__ == '__main__':
    app.run_server(debug=True, host="172.26.95.55", port=8050)

