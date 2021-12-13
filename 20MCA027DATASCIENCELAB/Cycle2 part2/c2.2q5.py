#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:25:14 2021

@author: sjcet
"""
import numpy as np

matrix = np.matrix([[2, 3,6], [3, 4,5],[6,5,9]])
trans = matrix.transpose()
neg = np.negative(matrix)
print("matrix:",matrix)
print("Transpose:",trans)
print("negative transpose:",neg)
comparison = matrix == trans
comparison2 = matrix == neg
equal_array = comparison.all()
skew = comparison2.all()

if(equal_array):
    print("Symmetric Matrix")
else:
   print("not symmetric")

if(skew):
   print("Skew Symmetric")
else:
   print("Not Skew Symmetric")    