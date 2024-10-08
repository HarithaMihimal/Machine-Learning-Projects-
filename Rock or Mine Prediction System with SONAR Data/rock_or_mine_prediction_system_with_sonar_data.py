# -*- coding: utf-8 -*-
"""Rock or Mine Prediction System with SONAR Data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JX2Lx7SDdUVnpHedR-5whZrXsqN_mSwa
"""



"""Importing Dependencies"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and Data Processing"""

# Loading the Dataset into a Pandas DataFrame
sonar_data=pd.read_csv('/content/sonar data.csv' , header=None)

sonar_data.head()

# number of rows and columns
sonar_data.shape

# Describing Statistical Data Measures of the Data
sonar_data.describe()

sonar_data[60].value_counts()

"""M --> Mine
R --> Rock
"""

sonar_data.groupby(60).mean()

# Separating Data and Labels
X=sonar_data.drop(columns=60,axis=1)
Y=sonar_data[60]

print(X)
print(Y )

"""Training and Testing Data"""

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=1)

print(X.shape,X_train.shape,X_test.shape)

"""Model Training --Logistic Regression"""

model=LogisticRegression()

#training logistic reggression model
model.fit(X_train,Y_train)

"""Model Evaluation"""

# Accuracy of the data
X_train_prediction=model.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)

print('Accuracy on training data : ',training_data_accuracy)

# accurasy of test data
X_test_prediction=model.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,Y_test)

print('Accuracy on test data : ',test_data_accuracy)

"""Making  a  Predictive System"""

input_data=(0.0117,0.0069,0.0279,0.0583,0.0915,0.1267,0.1577,0.1927,0.2361,0.2169,0.1180,0.0754,0.2782,0.3758,0.5093,0.6592,0.7071,0.7532,0.8357,0.8593,0.9615,0.9838,0.8705,0.6403,0.5067,0.5395,0.6934,0.8487,0.8213,0.5962,0.2950,0.2758,0.2885,0.1893,0.1446,0.0955,0.0888,0.0836,0.0894,0.1547,0.2318,0.2225,0.1035,0.1721,0.2017,0.1787,0.1112,0.0398,0.0305,0.0084,0.0039,0.0053,0.0029,0.0020,0.0013,0.0029,0.0020,0.0062,0.0026,0.0052)
# changing the input data to a numpy array

input_data_as_numpy_array=np.asarray(input_data)
# reshape the numpy array as we are predicting for one instance

input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

prediction=model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]=='R'):
  print('The object is a Rock')
else:
  print('The object is a Mine')