#Random Forest Analysis of the US Census Tract Data

#Import Modules
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


#Read the csv
f = pd.read_csv("./data/cen_tract.csv")

#Drop the rows with NaN's
f=f.dropna()

#Decide values to train (y = predicted value, features = predicting values) [CHANGE VALUES HERE] <----------------------------
y=f.Poverty
features = ['Men','Citizen','Income','Unemployment']
x= f[features]

#Divide data into training and validation data
train_x, val_x, train_y, val_y = train_test_split(x, y, random_state=1)
#Define model
povpr_model = RandomForestRegressor(random_state=1)
#Fit model
povpr_model.fit(train_x, train_y)
#Calculate mean absolute error to verify results
povpr_predictions = povpr_model.predict(val_x)
povpr_mae = mean_absolute_error(povpr_predictions, val_y)

#Calculate the method of just taking the average
avg=y.mean()
val_x['average']=avg
povpr_av = mean_absolute_error(val_x.average, val_y)

#Print the results
print("Random Forest MAE is: {}".format(povpr_mae))
print("Compared to MAE of just taking Average: {}".format(povpr_av))
