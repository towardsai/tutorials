# Commented out IPython magic to ensure Python compatibility.
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

from sklearn import tree

# %matplotlib inline

"""**Read Iris Dataset**"""

data = pd.read_csv('Iris.csv')
data

data.shape

"""**Define Colunms**"""

col_names = ['id', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']


data.columns = col_names

col_names

"""**Drop Id Column**"""

data = data.drop(['id'], axis=1)

data.head()

data.info()

"""**Checking the  target categorical counts**"""

data['species'].value_counts()

"""**Check missing values in variables**"""

data.isnull().sum()

target_col = ['species']

X = data.drop(['species'], axis=1)

y = data['species']

"""**Split dataset into train and test**"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

"""**Check datatypes**"""

X_train.dtypes

"""**Decision Tree Classification based on Gini index criterion**"""

from sklearn.tree import DecisionTreeClassifier

clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)
clf_gini.fit(X_train, y_train)

y_pred_gini = clf_gini.predict(X_test)
y_pred_gini

"""**Check accurcy of model**"""

from sklearn.metrics import accuracy_score

print('Model accuracy score with criterion gini index: {0:0.4f}'. format(accuracy_score(y_test, y_pred_gini)))# y_pred_gini are the predicted class labels in the test-set.

#Compare the train-set and test-set accuracy
y_pred_train_gini = clf_gini.predict(X_train)

y_pred_train_gini

print('Training-set accuracy score: {0:0.4f}'. format(accuracy_score(y_train, y_pred_train_gini)))

#Check for overfitting and underfitting

print('Training set score: {:.4f}'.format(clf_gini.score(X_train, y_train)))

print('Test set score: {:.4f}'.format(clf_gini.score(X_test, y_test)))

"""**Pictorial representation of Decision Tree**"""

plt.figure(figsize=(12,8))
tree.plot_tree(clf_gini.fit(X_train, y_train))