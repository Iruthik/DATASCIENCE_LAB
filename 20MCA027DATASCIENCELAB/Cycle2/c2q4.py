#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:59:40 2021

@author: sjcet
"""

import numpy as np
a=np.arange(1,11,1)
print(a)
a1=a[:4]
print("First 4 elements:",a1)
a2=a[6:]
print("Last 6 Elements:",a2)
a3=a[2:7]
print("Elements from index 2 to 7:",a3)