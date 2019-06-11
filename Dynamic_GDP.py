import plotly.plotly as py
import plotly.graph_objs as go
from IPython.display import IFrame
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# Create random data with numpy
import numpy as np

#Import pandas
import pandas as pd

#Read DF
GDP_DF=pd.read_excel("/home/tobal/GithubProjects/Dynamic_GDP/GDP_1960_2017/API_NY.GDP.PCAP.CD_DS2_en_excel_v2_10576730.xlsx")
GDP_DF.head()

#Fill NA
GDP_DF=GDP_DF.fillna(0)
 
#See shape
GDP_DF.shape

#Subset of dataframe with only numeric values
GDP_DF_ValueOnly=GDP_DF.iloc[:,4:62]

###############################
## A test of numeric filters ##
###############################

#Pick values in belowa GDP number for a specific year
RowNumbers=GDP_DF_ValueOnly[GDP_DF_ValueOnly > 277000000000]["2017"][~GDP_DF_ValueOnly[GDP_DF_ValueOnly > 277000000000]["2017"].isnull()]

#Search countries that fit the filter
GDP_DF.iloc[RowNumbers.index,]["Country Name"]

#Repeat the above with a range of specific values in a specific year
F1=GDP_DF_ValueOnly[(GDP_DF_ValueOnly > 277000000000) & (GDP_DF_ValueOnly < 287000000000)]["2017"]
F1=F1[~F1.isnull()]

#Return country name
GDP_DF.iloc[F1.index,]["Country Name"]

#################
## End of Test ##
#################

#Choose one country and find which values among all the other are the same, regardless of year
GDP_DF[GDP_DF["Country Name"].isin(["Chile"])]

#Choose CHL in 2000
CHL_2000=GDP_DF[GDP_DF["Country Name"].isin(["Chile"])]["2017"]
CHL_2000-CHL_2000*0.01
CHL_2000+CHL_2000*0.01


#Search which countries have an equal GDP, independent of the year
CHL=GDP_DF_ValueOnly[(GDP_DF_ValueOnly > float(CHL_2000-(CHL_2000*0.005))) & (GDP_DF_ValueOnly < float(CHL_2000+CHL_2000*0.005))]

#List of Years
Years=[col for col in GDP_DF_ValueOnly.columns]

#Iterate through years and indexes
RowPartial={}
YearOfValue={}
for years in Years:
    PartialResCHL=CHL[years][~CHL[years].isnull()].index.values.astype(int)
    
    if(PartialResCHL.shape[0]!=0):
        for i in range(PartialResCHL.shape[0]):
            #RowPartial[(str(years) + "_" + str(PartialResCHL[i]))]=GDP_DF.iloc[PartialResCHL[i],]["Country Name"]
            RowPartial[(str(years) + "_" + str(PartialResCHL[i]))]=PartialResCHL[i]
            YearOfValue[(str(years) + "_" + str(PartialResCHL[i]))]=years
        pass
    pass
pass
len(RowPartial)
#Grafico de barras
PlotList=[]
for i in range(len(RowPartial)):
    PlotList.append(go.Bar(text=str(YearOfValue[list(RowPartial)[i]]),
                   x=np.array(GDP_DF.iloc[RowPartial[list(RowPartial)[i]],]["Country Name"]),
                   y=np.array(GDP_DF_ValueOnly.iloc[RowPartial[list(RowPartial)[i]],][YearOfValue[list(RowPartial)[i]]])))
pass

#Scatter plot
PlotList=[]
for i in range(len(RowPartial)):
    PlotList.append(go.Scatter(x=np.array(YearOfValue[list(RowPartial)[i]]),
                   y=np.array(GDP_DF.iloc[RowPartial[list(RowPartial)[i]],]["Country Name"]),
                   text=np.array(GDP_DF_ValueOnly.iloc[RowPartial[list(RowPartial)[i]],][YearOfValue[list(RowPartial)[i]]])))
pass

py.iplot(PlotList, filename='GDP_Plot', sharing="public", fileopt="overwrite") 

#################################################
#################################################
#################################################
#################################################
DataPlot=go.Scatter(x=Years, y=GDP_DF_ValueOnly.iloc[168,].values)
py.iplot([DataPlot], filename='basic-line')

py.iplot([go.Scatter(x=Years, y=GDP_DF_ValueOnly)], filename="basic-line")
GDP_DF_ValueOnly.shape[1]

traces = []
for i in range(0, GDP_DF_ValueOnly.shape[1]):
    traces.append(go.Scatter(
    x=Years,
    y=GDP_DF_ValueOnly[Years[i]],
    mode="lines"
    ))
pass
fig = go.Figure(data=traces)
py.iplot(fig, filename='news-source')
