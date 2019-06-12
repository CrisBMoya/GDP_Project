import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd

#Offline Variables
#CountryName="Estonia"
#CountryYear="2017"
#Percent=0.005

def Get_Similar_GDP(CountryName, CountryYear, Percent):
    
    #Read DF
    GDP_DF=pd.read_excel("/home/tobal/GithubProjects/Dynamic_GDP/GDP_1960_2017/API_NY.GDP.PCAP.CD_DS2_en_excel_v2_10576730.xlsx")

    #Fill NA
    GDP_DF=GDP_DF.fillna(0)

    #GDP with only values -- based in shape, so this could change
    GDP_ValueOnly=GDP_DF.select_dtypes(['number'])

    #Choose one country and find which values among all the other are the same, regardless of year
    #Choose based on variables
    Country_Choose=GDP_DF[GDP_DF["Country Name"].isin([CountryName])][CountryYear]

    #Search which countries have an equal GDP, independent of the year
    Country_GDP=GDP_ValueOnly[(GDP_ValueOnly > float(Country_Choose-(Country_Choose*Percent))) & (GDP_ValueOnly < float(Country_Choose+Country_Choose*Percent))]
    
    #List of Years
    Years=[col for col in GDP_ValueOnly.columns]
    
    #Empty dataframe to piopulate with results
    PlotDF=pd.DataFrame(columns=["Year", "RowNumber", "Country", "GDP"])
    
    #Iterate through years and indexes
    RowCounter=0
    for years in Years:
        PartialRes=Country_GDP[years][~Country_GDP[years].isnull()].index.values.astype(int)

        if(PartialRes.shape[0]!=0):
            for i in range(PartialRes.shape[0]):
                PlotDF.loc[RowCounter]=[years, PartialRes[i], GDP_DF.iloc[PartialRes[i],]["Country Name"],
                                        round(GDP_ValueOnly.iloc[PartialRes[i],][years], 2)]
                RowCounter=RowCounter+1
            pass
        pass
    pass
    
    #Delete searched country so it can be showed properly
    Searched=PlotDF[PlotDF["Country"].isin([CountryName]) & PlotDF["Year"].isin([CountryYear])]    
    PlotDF=PlotDF.drop(Searched.index[0])       
    
    #Scatter plot
    PlotData=[]
    PlotData.append(go.Scatter(x=PlotDF["Year"], y=PlotDF["Country"], text=PlotDF["GDP"], mode="markers",
                   marker=dict(color=PlotDF["RowNumber"], colorscale="Viridis"), name=""))
    PlotData.append(go.Scatter(x=Searched["Year"], y=Searched["Country"], text=Searched["GDP"], mode="markers",
                   marker=dict(color="rgb(28, 212, 224)", size=10), name=""))
    #py.iplot(PlotData, filename='GDP_Plot', sharing="public", fileopt="overwrite")    

    #Return a list with all data
    ResultList=[PlotDF, PlotData]
    return(ResultList)
pass

#Variation for dashboard
def Get_Similar_GDP_Dashboard(CountryName, CountryYear, Percent):
    
    Percent=float(Percent)
    #Read DF
    GDP_DF=pd.read_excel("/home/tobal/GithubProjects/Dynamic_GDP/GDP_1960_2017/API_NY.GDP.PCAP.CD_DS2_en_excel_v2_10576730.xlsx")

    #Fill NA
    GDP_DF=GDP_DF.fillna(0)

    #GDP with only values -- based in shape, so this could change
    GDP_ValueOnly=GDP_DF.select_dtypes(['number'])

    #Choose one country and find which values among all the other are the same, regardless of year
    #Choose based on variables
    Country_Choose=GDP_DF[GDP_DF["Country Name"].isin([CountryName])][CountryYear]

    #Search which countries have an equal GDP, independent of the year
    Country_GDP=GDP_ValueOnly[(GDP_ValueOnly > float(Country_Choose-(Country_Choose*Percent))) & (GDP_ValueOnly < float(Country_Choose+Country_Choose*Percent))]
    
    #List of Years
    Years=[col for col in GDP_ValueOnly.columns]
    
    #Empty dataframe to piopulate with results
    PlotDF=pd.DataFrame(columns=["Year", "RowNumber", "Country", "GDP"])
    
    #Iterate through years and indexes
    RowCounter=0
    for years in Years:
        PartialRes=Country_GDP[years][~Country_GDP[years].isnull()].index.values.astype(int)

        if(PartialRes.shape[0]!=0):
            for i in range(PartialRes.shape[0]):
                PlotDF.loc[RowCounter]=[years, PartialRes[i], GDP_DF.iloc[PartialRes[i],]["Country Name"],
                                        round(GDP_ValueOnly.iloc[PartialRes[i],][years], 2)]
                RowCounter=RowCounter+1
            pass
        pass
    pass
    
    #Delete searched country so it can be showed properly
    Searched=PlotDF[PlotDF["Country"].isin([CountryName]) & PlotDF["Year"].isin([CountryYear])]    
    PlotDF=PlotDF.drop(Searched.index[0])       
    
    #Scatter plot
    PlotData=[]
    PlotData.append(go.Scatter(x=PlotDF["Year"], y=PlotDF["Country"], text=PlotDF["GDP"], mode="markers",
                   marker=dict(color=PlotDF["RowNumber"], colorscale="Viridis", size=7), name=""))
    PlotData.append(go.Scatter(x=Searched["Year"], y=Searched["Country"], text=Searched["GDP"], mode="markers",
                   marker=dict(color="rgb(28, 212, 224)", size=10), name=""))
    #Layout withouth legend
    

    #Return a list with all data
    #ResultList=[PlotDF, PlotData]
    return{"data": PlotData,
          "layout": go.Layout(showlegend=False)}
pass