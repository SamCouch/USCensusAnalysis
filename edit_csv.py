#For Creating a csv file that edits the csv to a better format.

#Import Modules
import numpy as np
import pandas as pd

#Read csv
f = pd.read_csv("./data/acs2015_census_tract_data.csv")

#Editing the data
f['Men']=round((f['Men']/f['TotalPop'])*100,2)
f['Women']=round((f['Women']/f['TotalPop'])*100,2)
f['Citizen']=round((f['Citizen']/f['TotalPop'])*100,2)
f['Employed']=round((f['Employed']/f['TotalPop'])*100,2)
f['CensusTract']=f['CensusTract'].apply(lambda x: '{0:0>11}'.format(x))

#Writing to a different csv
f.to_csv('./data/cen_tract.csv')
