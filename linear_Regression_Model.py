# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HCqWIoPjqTs5UoVuN2ykrQpfwc6tlxel

Importing Needed Packages
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
# %matplotlib inline

"""Downloading the dataset (Fuel Consumption Dataset)"""

!wget -O FuelConsumption.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv

"""Reading the Data"""

df=pd.read_csv("FuelConsumption.csv")

df.head()

df.describe()

"""lets select some features to  explore some more"""

cdf=df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
cdf.head(9)

viz=cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
viz.hist()
plt.show()

plt.scatter(cdf.FUELCONSUMPTION_COMB,cdf.CO2EMISSIONS, color='blue')
plt.xlabel("Fuel Consumption")
plt.ylabel("Co2 Emission")
plt.show()

plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color="blue")
plt.xlabel("Engine Size")
plt.ylabel("co2 Emission")
plt.show()

plt.scatter(cdf.CYLINDERS,cdf.CO2EMISSIONS, color = 'blue')
plt.xlabel('Cylinders')
plt.ylabel('Emission')
plt.show()

"""Creating train and test datasets"""

msk=np.random.rand(len(df)) < 0.8
train=cdf[msk]
test=cdf[~msk]

len(train)

len(test)

"""**Simple Linear Regression**"""

#Train data distribution

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
plt.xlabel('Engine size')
plt.ylabel('Emission')
plt.show()

"""Modeling"""

#using sklearn package to model data
from sklearn import linear_model
regr=linear_model.LinearRegression()
train_X=np.asanyarray(train[['ENGINESIZE']])
train_y=np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(train_X, train_y)
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)

#Plot output
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
plt.plot(train_X, regr.coef_[0][0]*train_X + regr.intercept_[0],'-r')
plt.xlabel("engine size")
plt.ylabel("Emission")

from sklearn.metrics import r2_score
test_X = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_hat=regr.predict(test_X)
print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_hat - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_hat - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_hat , test_y) )
