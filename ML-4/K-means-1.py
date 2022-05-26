import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

X = [[0.1,0.6],[0.15,0.17],[0.08,0.9],[0.16,0.85],[0.2,0.3],[0.25,0.5],[0.24,0.1],[0.3,0.2]]

centers = np.array([[0.1,0.6],[0.3,0.2]])
print('Initial Centroids: ')
print(centers)

from sklearn.cluster import KMeans
model = KMeans(n_clusters=2, init=centers, n_init=1)
model.fit(X)

print('Labels: ')
print(model.labels_)

print('P6 belongs to cluster', model.labels_[5])

print('No. of population around cluster 2: ', np.count_nonzero(model.labels_ == 1))

print('New Centroids: ')
print(model.cluster_centers_)