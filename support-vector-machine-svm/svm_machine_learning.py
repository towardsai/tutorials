# -*- coding: utf-8 -*-
"""
#Support Vector Machines (SVM) Introduction - Machine Learning

* Tutorial: https://news.towardsai.net/svm
* Github: https://github.com/towardsai/tutorials/tree/master/support-vector-machine-svm
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#classic datasets from sklearn library
from sklearn import datasets

from sklearn.model_selection import train_test_split

#Support Vector Classification-wrapper around SVM
from sklearn.svm import SVC

#different matrices to score model performance
from sklearn import metrics
from sklearn.metrics import classification_report,confusion_matrix

"""## Load data"""

#loading WINE dataset
cancer_data = datasets.load_wine()

#converting into DataFrame
df = pd.DataFrame(cancer_data.data, columns = cancer_data.feature_names)
df['target'] = cancer_data.target
df.head()

"""## Exploratory data analysis"""

#analysing target variable
sns.countplot(df.target)
plt.show()

#visualizing datapoints seperability
fig, axes = plt.subplots(4, 3, figsize=(22,14))
axes = [ax for axes_rows in axes for ax in axes_rows]
columns = list(df.columns)
columns.remove('target')
columns.remove('alcohol')

#looping through every columns of data
#and plotting against alcohol
for i, col in enumerate(columns):
  sns.scatterplot(data=df, x='alcohol', y=col, hue='target', palette="deep", ax=axes[i])

"""## Splitting data"""

#splitting data into 80:20 train test ratio
X = df.drop('target', axis=1)
y = df.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

"""## Model training and performance evaluation"""

#training SVM model with linear kernel
model = SVC(kernel='linear',random_state = 10)
model.fit(X_train, y_train)

#predicting output for test data
pred = model.predict(X_test)

#building confusion matrix
cm = confusion_matrix(y_test, pred)

#defining the size of the canvas
plt.rcParams['figure.figsize'] = [15,8]

#confusion matrix to DataFrame
conf_matrix = pd.DataFrame(data = cm,columns = ['Predicted:0','Predicted:1', 'Predicted:2'], index = ['Actual:0','Actual:1', 'Actual:2'])

#plotting the confusion matrix
sns.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = 'Paired', cbar = False,
            linewidths = 0.1, annot_kws = {'size':25})
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.show()

print(classification_report(y_test,pred))
