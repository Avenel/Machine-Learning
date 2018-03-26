import quandl
import pickle
import pandas as pd
import numpy as np

from sklearn import svm, preprocessing, cross_validation

housing_data = pd.read_pickle('HPI_sklearn_ready.pickle')
print(housing_data)

# Feature Set
print(housing_data.drop(['label', 'Future_US_HPI'], 1))
X = np.array(housing_data.drop(['label', 'Future_US_HPI'], 1))
X = preprocessing.scale(X)

# Label
y = np.array(housing_data['label'])

# split up features (X) and labels (y) into random training and testing groups 
# train on 80% percent of the data, test on 20% of the data
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

# print(X_train)

# classifier to use
clf = svm.SVC(kernel='linear')

# train classifier
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))