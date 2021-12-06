#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:05:00 2021

@author: sjcet
"""
import numpy as np 
a = np.array([[1,2,3],[4,5,6]])
b=np.array([1,2,3])
print("First array:")  
print (a) 
print("Second array")
print(b)
print ("\n")  
print ("Append elements to array:") 
print (np.append(a, [7,8,9])) 
print (np.append(b, [7,8,9]))