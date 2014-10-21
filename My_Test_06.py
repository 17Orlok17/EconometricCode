# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 17:06:41 2014

@author: Evan

Builds on My_Test_05 - now I want to get the variance estimates
of the parameters. As it turns out, it seems like the more asymtotically efficient 
method (in terms of runtime) is to roll everything into one package and return
all the statistics.  This obviates repeated calls.  
For regressions with small observations, this seems best.
"""

import numpy as NP
from masterOLS import *
from variance import *

#generate a vector of random numbers
X = np.random.rand(10000,3)
Y = np.zeros((10000,1))
intercept = np.ones((10000,1))

#generate an error vector
E = 10*np.random.rand(10000,1)
print("The mean error is " + str(mean(E)))
print("The variance of the error is " + str(variance(E)))

#all X vars are ints range from 0 to 9
X = np.floor(10*X)

#Generate the Y = b0 + b1x1 + b2x2 + b3x3 + eps vector
Y = 5.5*intercept[:,0] + 1.1*X[:,0] + 2.2*X[:,1] + 3.3*X[:,2] + E[:,0]
#Y = np.add(5.5*intercept[:,0],1.1*X[:,0],2.2*X[:,1],3.3*X[:,2],E[:,0])

#Now estimate
betas, predicted, resid, ssr, sse, rSquared, covMatrix, betaStdErrors = masterOLS(Y,X)
i = 0
for b in betas:
    print("Regression coefficient " + str(i) + " is " + str(betas[i]))
    print("The standard error of the coefficient is " + str(betaStdErrors[i]))
    i +=1

print("the SSE is " + str(sse))
print("the SSR is " + str(ssr))
print("The r-squared is " + str(rSquared))

#Next up - heteroskedasticity?  We'll see...
