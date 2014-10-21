# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 13:37:39 2014

@author: Evan

Runs a regression of Y on X and returns Yhat and Uhat,
the predicted Y's and the residual=Y-Yhat

Note: For My_Test_01-My_Test_05, I created the vector of ones for the intercept
in this program.  Now I assume that the full matrix (with the ones) is being
passed into the function
"""
import numpy as np
def predResid(Y,X,beta):
    ''' old code
    #beta = regOLS(Y,X)
    nobs = Y.shape[0]
    print("the number of obs is: " + str(nobs))
    pred = np.zeros((nobs,1))
    resid = np.zeros((nobs,1))
    ones = np.ones((nobs,1))
    shapeO = ones.shape
    print("the shape of ones is: " + str(shapeO[0]) + " x " + str(shapeO[1]))
    shapeX = X.shape
    print("the shape of X is: " + str(shapeX[0]) + " x " + str(shapeX[1]))
    XF = column_stack((ones,X)) #create the intercept - this is syntax for vertical concatenation!
    '''
    pred = np.dot(X,beta)
    resid = Y - pred
    yhatUhat = np.column_stack((pred,resid)) #np.vstack((pred,resid))
    ''' for bug diagnosing
    print(np.shape(yhatUhat))
    for i in range(0, np.shape(yhatUhat)[0]):
        print(yhatUhat[i,:])
    '''
    return yhatUhat