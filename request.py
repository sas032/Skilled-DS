#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 02:23:02 2020

@author: root
"""

import requests
url='http://localhost:5000/predict_api'
r=requests.post(url,json={'Q1':1,'Q2':1,'Q3':1,'Q4':1,'Q5':1,'Q6':1,'Q7':1,'Q8':1,'Q9':1,'Q10':1})
print(r)
