#This file determines how much the US Census Tract Data variables correlate with each other

#Import Modules
import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt


#Read the csv
f = pd.read_csv("./data/cen_tract.csv")

#Drop the rows with NaN's
f=f.dropna()
#Drop Identifying Columns
f=f.drop(columns=['ID','CensusTract','State','County'])

#Create Correlation Matrix
corrMatrix=f.corr()
#Create Array for just Poverty Correlation
corrPov=corrMatrix.Poverty

#Print Poverty Correlation
print(corrPov)

#Write to csv
corrMatrix.to_csv('./data/corrMatrix.csv')

#Show heatmap
sn.heatmap(corrMatrix, annot=True)
#Show heatmap
plt.show()
