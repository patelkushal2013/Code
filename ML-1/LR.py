# Simple Linear Regression
# Driving and Risk

# Importing the libraries
# import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('driving_risk.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Driving hours vs Risk Score (Training set)')
plt.xlabel('Driving Hours')
plt.ylabel('Risk Score')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'green')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Driving Hours vs Risk Score (Test set)')
plt.xlabel('Driving Hours')
plt.ylabel('Risk Score')
plt.show()

print("")
print("Equation of best fit line is y = ",regressor.intercept_," + ",regressor.coef_, " * X")
inputhours = 17
print("Example driving hours: ",inputhours)
print("Equation of best fit line is y = ",regressor.intercept_," + ",regressor.coef_, " * ",inputhours)
outputrisk = regressor.intercept_+regressor.coef_* inputhours
print("Output RISK Score is: ",outputrisk)