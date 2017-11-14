import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()

# f(x) = y
X = iris.data
y = iris.target

# split the data for training and testing
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size = 0.5 )

cls = DecisionTreeClassifier()
cls.fit( X_train, y_train )

predictions = cls.predict( X_test )
print( 'Decision Tree:', accuracy_score( y_test, predictions ) )

cls = KNeighborsClassifier()
cls.fit( X_train, y_train )

predictions = cls.predict( X_test )
print( 'K Nearest Neighbour:', accuracy_score( y_test, predictions ) )
