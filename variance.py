# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 15:49:48 2014

@author: Evan

The catch here is that I must specify the first dimension (the zero index)
even if the array has only one dimension!
"""

from mean import mean

def variance(xVec):
    #n=len(xVec[0])
    n=len(xVec)
    xMean = mean(xVec)
    if n <= 1:
        return None
    else:
        numer=0
        for i in range(0,n):
            #numer = numer + (xVec[0][i]-xMean)*(xVec[0][i]-xMean)
            diff = float(xVec[i])-xMean
            numer = numer + diff*diff
        return numer/(n-1)
    