# K-Nearest Neighbors (K-NN)

# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 2].values

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X,y)

X_test =  np.array([6,6])
y_pred = classifier.predict([X_test])
print ('General KNN: ' + y_pred)

classifier = KNeighborsClassifier(n_neighbors=3 , weights='distance')
classifier.fit(X,y)

X_test = np.array([6, 6])
y_pred = classifier.predict([X_test])

print('Distance Weighted KNN: ' + y_pred)