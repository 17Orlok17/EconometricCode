# -*- coding: utf-8 -*-
"""
Created on Thu Oct 09 16:28:20 2014

@author: Evan
"""


def sSR(uhat):
    ssr = 0
    for i in range(0,len(uhat)):
        ssr += uhat[i]**2
    return ssr