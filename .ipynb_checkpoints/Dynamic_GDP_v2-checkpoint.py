import sys
import os
import plotly.plotly as py
import plotly.graph_objs as go

#Import main function
sys.path.append(os.getcwd())
from RequestFun import *

#Test
Test=Get_Similar_GDP(CountryName="Germany", CountryYear="2000", Percent=0.005)
py.iplot(go.Figure(data=Test[1], layout=go.Layout(showlegend=False)), filename='GDP_Plot', sharing="public", fileopt="overwrite") 
