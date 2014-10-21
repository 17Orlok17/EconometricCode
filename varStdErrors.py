# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 10:41:20 2014

@author: Evan

Calculate the variances/standard errors of all variables used in OLS 
regression.  The primary difficulty here is that we need to run a regression to
generate an r-squared for each variable.  For each of the variables, we need the following:
- sigma squared = sum residuals of each obs / (n-k-1)
- SST(j) = sum(i=1...n) X_ij- xbar_j
- r-squared_j = r-squared from OLS regression of x_j on other indedpendent vars 
"""

import numpy as np

def varStdErrors(X,resid):
    totalResid = 0
    for i in range(0,len(resid)):
        totalResid += resid[i]
    degFreedom = len(resid) - len(X[0,:]) - 1
    sigmaSquared = totalResid / degFreedom
    Xt = X.transpose()
    XtX = np.dot(Xt,X)
    XtXinv = np.linalg.inv(XtX)
    covMat = sigmaSquared*XtXinv
    betaList = np.zeros((np.shape(X)[0],1))
    for i in range(0,np.shape(X)[1]):
        betaList[i] = covMat[i,i]
    return betaList
    
    ''' - unsure of how to do the non-vectorized version of the intercept    
    for j in range(0,len(resid)+1):
    ''' 