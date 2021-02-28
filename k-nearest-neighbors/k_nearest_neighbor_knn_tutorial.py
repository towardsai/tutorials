# -*- coding: utf-8 -*-
"""
#K-Nearest Neighbors (KNN) Algorithm Tutorial - Machine Learning Basics
* Tutorial: https://news.towardsai.net/knn
* Github: https://github.com/towardsai/tutorials/tree/master/k-nearest-neighbors
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

# Import the iris dataset as provided by the sklearn Python module
from sklearn.datasets import load_iris
iris = load_iris()

type(iris)

# Converting sklearn data into Pandas dataframe
# target variables imply
# 0.0 - Setosa
# 1.0 - Versicolor
# 2.0 - Virginica
iris = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])
iris.head()

"""## Checking for outliers and imbalanced data"""

# data is perfectly balanced
sns.countplot(x='target', data=iris)

# not much of outliers to br handled
for feature in ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']:
  sns.boxplot(x='target', y=feature, data=iris)
  plt.show()

"""## Plotting a 2-D graph"""

sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', data=iris, hue='target', palette="deep")

"""## Separating features and target"""

# X variable contains flower features
# Y variable contains target values
X = iris.drop(['target'], axis=1)
y = iris['target']

"""## Split the dataset into train and test sets"""

# 60% of the data will be randomly selected at training data
# remaining 40% as testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# checking accuracy score for k-value rangin from 1 to 26
k_range = list(range(1,26))
scores = []

# model fitting and calculating accuracy score
# for each k-value in the range 1-26
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))

plt.plot(k_range, scores)
plt.xlabel('Value of k')
plt.ylabel('Accuracy Score')
plt.title('Accuracy Scores for different values of k')
plt.show()

# 60% of the data will be randomly selected at training data
# remaining 40% as testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

"""## Initial model"""

# Initial model with nearest neighbor as 1(k-value)
# further, k will be replaced with optimal value
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))

"""## Finding the right k-value"""

# checking accuracy score for k-value rangin from 1 to 26
k_range = list(range(1,26))
scores = []

# model fitting and calculating accuracy score
# for each k-value in the range 1-26
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))

plt.plot(k_range, scores)
plt.xlabel('Value of k')
plt.ylabel('Accuracy Score')
plt.title('Accuracy Scores for different values of k')
plt.show()

"""## Accuracy for optimal k-value"""

# 11 is the optimal k-value for this dataset
knn = KNeighborsClassifier(n_neighbors=11)
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))

"""## Predicting class of new data"""

knn = KNeighborsClassifier(n_neighbors=11)

# fitting the entire data without splitting
# into train and test
knn.fit(iris.drop(['target'], axis=1), iris['target'])

# new data to be classified
X_new = np.array([[1, 2.9, 10, 0.2]])
prediction = knn.predict(X_new)
print(prediction)

if prediction[0] == 0.0:
  print('Setosa')
elif prediction[0] == 1.0:
  print('Versicolor')
else:
  print('Virginica')
