#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:27:19 2021

@author: sjcet
"""

import numpy as np
a = np.array([[1, 2, 3,4], [4, 5, 6,5], [7, 8, 9,6], [10, 11, 12,7]])
b = np.array([[1, 2, 3,4],[7, 8, 9,6] , [4, 5, 6,5], [10, 11, 12,7]])
print("Addition:\n",np.add(a,b))
print("Subtraction:\n",np.subtract(a,b))
print("Multiply the individual elements:\n",np.multiply(a,b))
print("Divide:\n",np.divide(a,b))
print("Multiply:\n",np.dot(a,b))
print("Transpose:\n",np.transpose(a))
print("Sum of Diagonal Elements:\n",np.trace(a))