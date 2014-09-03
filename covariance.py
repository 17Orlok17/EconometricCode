# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 18:14:23 2014

@author: Evan

Calculate covariance.  A key requirement of the user is that the
x and y vectors be of the same length
"""
import numpy as NP
from mean import *

def covariance(xVec, yVec):
    #tester = np.vstack((xVec,yVec))
    n=len(xVec)
    xBar = mean(xVec)
    yBar = mean(yVec)
    covar = 0;
    for i in range(0,n):
        covar += float((xVec[i]-xBar)*(yVec[i]-yBar))
    #print("The python covariance is " + str(np.cov(tester)))
    #print("The N covariance is: " + str(covar/n))
    return covar/(n-1) #The sample covariance