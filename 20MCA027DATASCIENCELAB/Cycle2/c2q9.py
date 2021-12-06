#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:54:21 2021

@author: sjcet
"""

import numpy as np

a= np.array([[3, 6,7,8],[10,11,12,13]])

b=np.array([[3, 6,8,7], [4, 2,1,0],[3,1,3,3],[1,1,2,2]])

x=np.diag(a)

y=np.diag(b)

print(x)

print(y)
