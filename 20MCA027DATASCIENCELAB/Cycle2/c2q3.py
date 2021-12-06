#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:50:04 2021

@author: sjcet
"""
import numpy as np

x = np.empty([2,2])
print("uninitialized array:",x)
y=np.full([2,2],1)
print("array with all elements as 1:",y)
z=np.full([2,2],0)
print("array with all elements as 0:",z)
