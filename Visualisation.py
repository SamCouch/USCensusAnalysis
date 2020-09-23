#Visualisation of US Census Track Data

#Import Modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read the csv
f = pd.read_csv("./data/cen_tract.csv")

#Drop the rows with NaN's
f=f.dropna()

#Choose x and y data
x=f.Income
y=f.Walk

#Create Scatter Plot
plt.scatter(x,y)
plt.title('Plot of Average Income vs Percent Commuting by Walking')
plt.xlabel('Average Income')
plt.ylabel('Percent Commuting by Walking')
# plt.xscale('log')
# plt.yscale('log')
plt.show()
