# -*- coding: utf-8 -*-
"""
Created on Thu Oct 09 16:33:16 2014

@author: Evan
"""

from sSE import *
from sSR import *

def rSquared(Y,yhat,uhat):
    sse = sSE(yhat,Y)
    ssr = sSR(uhat)
    sst = sse + ssr
    rsquared = sse/sst
    return rsquared