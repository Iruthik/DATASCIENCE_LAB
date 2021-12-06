#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:14:07 2021

@author: sjcet
"""

import numpy as np

#create numpy array
a = np.array([1,2,8,9,3,4,5,6,7])
print(a)
array_copy = np.sort(a)[::-1]
print(array_copy[4:10])
