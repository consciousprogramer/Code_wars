# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 13:54:53 2018

@author: RAVI SHANKAR SINGH
"""

def positive_sum(arr):
    psum = 0
    for i in arr:
        if i >= 0:
            psum += i
    return psum


# =============================================================================
# def positive_sum(arr):
#     return sum(x for x in arr if x > 0)
# 
# =============================================================================


# =============================================================================
# def positive_sum(arr):
#     return sum(filter(lambda x: x > 0,arr))
# 
# =============================================================================
print(positive_sum([-5,100]))
    