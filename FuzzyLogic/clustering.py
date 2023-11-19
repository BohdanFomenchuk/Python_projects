import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy

# Data load and preparation
dataset = pd.read_csv("UCI_Credit_Card.csv")

dataset['BILL TOTAL'] = dataset['BILL_AMT1'] + dataset['BILL_AMT2'] + dataset['BILL_AMT3'] + dataset['BILL_AMT4'] + \
                        dataset['BILL_AMT5'] + dataset['BILL_AMT6']
print(dataset['LIMIT_BAL'].mean())
X = dataset.iloc[:, [1, 25]].values
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Data clustering with Fuzzy c-means
clustering = skfuzzy.cmeans(data=X.T, c=2, m=2, error=0.005, maxiter=1000, init=None)
predictions = clustering[1]
predictions = predictions.argmax(axis=0)

# Visualization
plt.scatter(X[predictions == 0, 0], X[predictions == 0, 1], c='red', label='Cluster 1')
plt.scatter(X[predictions == 1, 0], X[predictions == 1, 1], c='green', label='Cluster 2')
plt.scatter(X[predictions == 2, 0], X[predictions == 2, 1], c='blue', label='Cluster 3')
plt.scatter(X[predictions == 3, 0], X[predictions == 3, 1], c='yellow', label='Cluster 4')
plt.scatter(X[predictions == 4, 0], X[predictions == 4, 1], c='orange', label='Cluster 5')
plt.xlabel('Limit')
plt.ylabel('Bill amount')
plt.legend()
plt.show()

# Writing customer cluster belonging information
centers = clustering[0]
centers = scaler.inverse_transform(centers)
centers = pd.DataFrame(data=centers, columns=['Limit', 'Bill amount'])
dataset_clusters = pd.concat([dataset, pd.DataFrame({'cluster': predictions})], axis=1)
print(dataset_clusters)
