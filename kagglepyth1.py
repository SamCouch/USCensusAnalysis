from urllib.request import urlopen
import json
import plotly.express as px
import numpy as np
import pandas as pd
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
print("e")
numpypi=np.pi
print(numpypi)
f = pd.read_csv("./data/editedcsv.csv")
f['CensusId']=f['CensusId'].apply(lambda x: '{0:0>5}'.format(x))
foval='Walk'
# f['Men']=f['Men']/f['TotalPop']
# print(f.head(5))

fig = px.choropleth(f, geojson=counties, locations='CensusId', color=foval,
                           color_continuous_scale="Viridis",
                           #range_color=(0, 12),
                           scope="usa",
                           labels={'County':foval},
                           hover_name="County",
                           hover_data=["State","CensusId",foval]
                          )
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
