#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 02:08:15 2020

@author: root
"""

import numpy as np
from flask import Flask, requests, jsonify, render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html)

@app.route('/predict',methods=['POST'])
def predict():
    int_features=[int(x) for x in requests.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
    output=round(prediction[0],2)
    return render_template('index.html',prediction_text='Student level is {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.get_json(force=True)
    prediction=model.predict([np.array(list(data.values))])
    output=prediction[0]
    return jsonify(output)

if __name__=="__main__":
    app.run(debug=True)
 