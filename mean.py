# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 15:58:59 2014

@author: Evan

Find the mean of a given vector
#The catch here is that I must specify the first dimension (the zero index)
#even if the array has only one dimension!
"""

def mean(xVec):
    #n=len(xVec[0])
    n=len(xVec)
    #print("n is " + str(n))
    if n==0:
        return None
    else:
        sum=0
        for i in range(0,n):
            #sum = sum + xVec[0][i]
            sum = sum + float(xVec[i])
        #print("The mean is: " + str(float(sum/n)))
        return float(sum/n)
        