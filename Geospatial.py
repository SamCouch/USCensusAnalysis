#File for Visualising Census County Data

#Import modules
from urllib.request import urlopen
import json
import plotly.express as px
import numpy as np
import pandas as pd

#Read github file provided by the plotly website (plotly.com/python/county-choropleth/)
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

#Assign the data
f = pd.read_csv("./data/editedcsv.csv")

#Set the number of digits to 5 for Census ID
f['CensusId']=f['CensusId'].apply(lambda x: '{0:0>5}'.format(x))

#Select the focus variable [CHANGE VALUE HERE] <----------------------------
foval='Walk'

#Create Figure
fig = px.choropleth(f, geojson=counties, locations='CensusId', color=foval,
                           color_continuous_scale="Viridis",
                           scope="usa",
                           labels={'County':foval},
                           hover_name="County",
                           hover_data=["State","CensusId",foval]
                          )
#Show figure
fig.show()
