#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 23:31:41 2020

@author: root
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
import pickle 

data=pd.read_csv('DATASET.csv')
data.drop('Studentid',axis=1,inplace=True)
y=data.iloc[:,10:].values
X=data.iloc[:,:10].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y)
from sklearn.preprocessing import StandardScaler 
sc_x = StandardScaler() 
X_train = sc_x.fit_transform(X_train)  
X_test = sc_x.transform(X_test) 
from sklearn.linear_model import LogisticRegression 
classifier = LogisticRegression(random_state = 0) 
classifier.fit(X_train, y_train) 
y_pred = classifier.predict(X_test) 
from sklearn.metrics import confusion_matrix 
cm = confusion_matrix(y_test, y_pred) 

pickle.dump(classifier, open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))


