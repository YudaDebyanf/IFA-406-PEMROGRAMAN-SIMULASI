# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 16:20:20 2021

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x**np.sin(x) + 2
ndata = 5000
a = 1.0
b = 25.0

x = np.linspace(a,b,ndata)
y = func(x)
fmax = np.max(y)

count = 0
xin = []
yin = []
xout = []
yout = []
for i in range(ndata):
    xrand = np.random.uniform(a,b)
    yrand = np.random.uniform()*fmax
    if yrand < func(xrand):
        count +=1
        xin.append(xrand)
        yin.append(yrand)
    else:
        xout.append(xrand)
        yout.append(yrand)
        
integral = float (count/ndata)*fmax*(b-a)
print(integral)
plt.plot(xin,yin,'x',color='r')
plt.plot(xout,yout,'x',color='k')
plt.show