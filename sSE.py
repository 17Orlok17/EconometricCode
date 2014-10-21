# -*- coding: utf-8 -*-
"""
Created on Thu Oct 09 16:13:12 2014

@author: Evan
"""

from mean import *

def sSE(yhat,y):
    ybar = mean(y)
    sse = 0
    for i in range(0,len(yhat)):
        sse += (yhat[i]-ybar)**2
    return sse