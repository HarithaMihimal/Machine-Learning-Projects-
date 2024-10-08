# -*- coding: utf-8 -*-
"""Diabetes Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gajapXbvLf_PpWi_CNjk7joER1nCIAfr
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""PIMA diabetes dataset"""

# prompt: import /content/sample_data/diabetes.csv

diabetes_data = pd.read_csv('/content/sample_data/diabetes.csv')

diabetes_data.head()

diabetes_data.shape

diabetes_data.describe()

diabetes_data['Outcome'].value_counts()

"""0 --> non diabetic

1 --> diabetic
"""

diabetes_data.groupby('Outcome').mean()

from os import X_OK
# separating data and labels
X= diabetes_data.drop(columns='Outcome',axis=1)
Y=diabetes_data['Outcome']

print(X)

print(Y)

"""Data Standeriezation"""

scaler = StandardScaler()

scaler.fit(X)

StandardScaler(copy=True, with_mean=True,with_std=True)

standardized_data = scaler.transform(X)

print(standardized_data)

X= standardized_data
Y=diabetes_data['Outcome']

print(X)
print(Y)

"""Train Test Split"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Training the Model"""

classifier = svm.SVC(kernel='linear')

# training the sm=vm Classifier
classifier.fit(X_train, Y_train)

"""Model Evaluation

Accuracy Score
"""

# accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy score of the training data : ', training_data_accuracy)

# accuracy score for the test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy score of the test data : ', test_data_accuracy)

"""Making a Predictive System"""

input_data = (3,78,50,32,88,31,0.248,26)

#change the input data to nmpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

input_data_reshaped

# standardized the input data

std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)
if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

input_data=(10,115,0,0,0,35.3,0.134,29) #input data
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
std_data=scaler.transform(input_data_reshaped)
prediction=classifier.predict(std_data)
print(prediction)
if(prediction[0]==0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

