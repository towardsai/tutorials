# Import important libraries
import numpy as np
import pylab as plt
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

load_iris = datasets.load_iris()
iris_df = pd.DataFrame(load_iris.data, columns=[load_iris.feature_names])

print(iris_df.head())

print(load_iris.data.shape)

standardized_x = StandardScaler().fit_transform(load_iris.data)
print(standardized_x[:2])

print(standardized_x.T)

covariance_matrix_x = np.cov(standardized_x.T)
print(covariance_matrix_x)

eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix_x)

print(eigenvalues)

print(eigenvectors)

total_of_eigenvalues = sum(eigenvalues)
varariance = [(i / total_of_eigenvalues)*100 for i in sorted(eigenvalues, reverse=True)]

print(varariance)

eigenpairs = [(np.abs(eigenvalues[i]), eigenvectors[:,i]) for i in range(len(eigenvalues))]

# Sorting from Higher values to lower value
eigenpairs.sort(key=lambda x: x[0], reverse=True)
print(eigenpairs)

matrix_weighing = np.hstack((eigenpairs[0][1].reshape(4,1),
                      eigenpairs[1][1].reshape(4,1)))
print(matrix_weighing)

Y = standardized_x.dot(matrix_weighing)
print(Y)

plt.figure()
target_names = load_iris.target_names
y = load_iris.target
for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
    plt.scatter(Y[y==i,0], Y[y==i,1], c=c, label=target_name)

plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.legend()
plt.title('PCA')
plt.show()

