import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer

print('h')

f = pd.read_csv("./data/cen_tract.csv")

#f.drop(columns=['ID', 'CensusTract','State','TotalPop','Women','IncomeErr','IncomePerCapErr','ChildPoverty'])
#f['OtherEthn']=f['Native']+f['Asian']+f['Pacific']
f=f.dropna()


#Decide Values to train
y=f.Poverty
features = ['Men','Citizen','Income','Unemployment','Hispanic','White','Black','Asian','Pacific','Drive','Walk','Professional','Service','Office','Construction','Production','IncomeErr','IncomePerCap','ChildPoverty']
x= f[features]

#print(x)
#https://scikit-learn.org/stable/modules/impute.html
# imp = SimpleImputer(missing_values=np.nan, strategy='mean')
# imp.fit(x)
# ximp=imp.transform(x)
#print(ximp.head(44))



#Divide
train_x, val_x, train_y, val_y = train_test_split(x, y, random_state=1)
#Define Model
povpr_model = RandomForestRegressor(random_state=1)
#Fit Model
povpr_model.fit(train_x, train_y)
#Calculate mean absolute error to verify results
povpr_predictions = povpr_model.predict(val_x)
povpr_mae = mean_absolute_error(povpr_predictions, val_y)

#Calculate difference to just taking average
avg=y.mean()
val_x['average']=avg
#print(val_x.average)
#print(val_y)
povpr_av = mean_absolute_error(val_x.average, val_y)


print("Random Forest MAE is: {}".format(povpr_mae))
print("Compared to MAE of just taking Average: {}".format(povpr_av))

#print(f.head(5))
