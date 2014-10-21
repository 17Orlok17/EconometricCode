# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 13:07:19 2014

@author: Evan
Goal: Take in a vector Y and a matrix X, calculate the regression 
coefficients.  Assume there is an intercept calculated as well.

Note: For My_Test_01-My_Test_05, I created the vector of ones for the intercept
in this program.  Now I assume that the full matrix (with the ones) is being
passed into the function
"""

import numpy as np
from numpy import linalg as LA

def regOLS(Y,X):
    #rowCol = np.shape(X)
    #print(rowCol)
    #create a vector of ones to estimate the intercept
    #uno = np.ones((rowCol[0],1))
    #X = np.hstack((uno,X))
    Xt = X.transpose()
    XtX = np.dot(Xt,X)
    XtXinv = np.linalg.inv(XtX)
    allMat = [XtXinv,Xt,Y]
    beta = reduce(np.dot, allMat)
    #beta = np.dot(XtXinv,Xt,Y)
    
    return beta

