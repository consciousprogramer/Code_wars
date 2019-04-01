# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:28:59 2018

@author: RAVI SHANKAR SINGH
"""
# 8kyu
def invert(lst):
    def inverse(n):   #declaring function is a good habbit 
        return n*(-1) # as it makes the program modular and 
    return list(map(inverse,lst)) # make reuseablity
print(invert([1,-1,2,5,-8]))