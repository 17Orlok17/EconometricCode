# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 13:07:19 2014

@author: Evan
Goal: Take in a vector Y and a matrix X, calculate the regression 
coefficients.  Assume there is an intercept calculated as well
"""

import numpy as np
from numpy import linalg as LA

def regOLS(Y,X):
    rowCol = np.shape(X)
    uno = np.ones(rowCol[0],1)
    X = np.hstack(uno,X)
    Xt = X.T
    beta = LA.inv(Xt*X)*Xt*Y
    
    return beta

