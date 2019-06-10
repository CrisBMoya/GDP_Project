#Import Bokeh
from bokeh.io import output_notebook, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.sampledata.autompg import autompg_clean as df
from bokeh.transform import factor_cmap

#Import pandas
import pandas as pd

#Read DF
GDP_DF=pd.read_excel("/home/tobal/GithubProjects/Dynamic_GDP/GDP_1960_2017/GDP_From_1960_2017.xlsx")
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

#Choose USA in 2010
CHL_2000=GDP_DF[GDP_DF["Country Name"].isin(["Chile"])]["2000"]
CHL_2000-CHL_2000*0.1
CHL_2000+CHL_2000*0.1

#Search which countries have an equal GDP, independent of the year
CHL=GDP_DF_ValueOnly[(GDP_DF_ValueOnly > 277000000000) & (GDP_DF_ValueOnly < 287000000000)]

CHL.shape[1]
CHL.iloc[:,0]


RowNumbers=list()
#Usar condicional
CHL.iloc[:,1][~CHL.iloc[:,1].isnull()].shape[0] #permite evaluar largo del resultado, si es 0 no se usa

#Corregir con condicional de arriba
for i in range(0, CHL.shape[1]):
    RowNumbers.append(CHL.iloc[:,i][~CHL.iloc[:,i].isnull()].index)
pass
RowNumbers


GDP_DF.iloc[RowNumbers,]["Country Name"]
