# -*- coding: utf-8 -*-
"""
Created on Sun Aug 03 18:19:24 2014

@author: Evan

Simple plan:
Inputs: Linearly independent matrix nxk
n - number of observations/rows
k - number of variables/columns

Outputs: kxk covariance matrix

Assumption: divide by n-1 instead of n.  Whatever!
"""
import numpy as np
from covariance import *

def covMatrix(xMat):
    dim = xMat.shape
    dim = dim[1]
    covMat = np.zeros((dim,dim))
    #Could use symmetry to fill in lower triangular form,
    #cut calls by half
    for i in range(0,dim):
        for j in range(0,dim):
            covMat[i,j] = covariance(xMat[:,i],xMat[:,j])
    return covMat