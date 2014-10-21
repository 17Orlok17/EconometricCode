# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 11:05:56 2014

@author: Evan

Goal is to provide the most efficient recovery of all the key statistics from an OLS 
regression; without storing all the information in one local place I found myself
having to repeatedly call functions and recreate matrices.
"""

import numpy as NP
from regOLS import *
from predResid import *
from sSR import *
from sSE import *
from rSquared import *
from covMatrix import *
from varStdErrors import *

def masterOLS(Y,X):
    #First, need to add a vector of ones to estimate intercept
    uno = np.ones((np.shape(X)[0],1))
    #Add this to get the 'full matrix estimated)
    XF = np.hstack((uno,X))
    betas = regOLS(Y,XF)
    yhatUhat = predResid(Y,XF,betas)
    print(yhatUhat)
    predicted = yhatUhat[:,0]
    resid = yhatUhat[:,1]
    ssr = sSR(predicted)
    sse = sSE(resid,Y)
    rSqrd = rSquared(Y,predicted,resid)
    covMat = covMatrix(X)
    #Right now there's an overlap in the role between covMatrix and the following
    betaStdErrors = varStdErrors(XF,resid)
    return (betas, predicted, resid, ssr, sse, rSqrd, covMat, betaStdErrors)