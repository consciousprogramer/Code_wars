# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 07:23:06 2018

@author: RAVI SHANKAR SINGH
"""
import time
def high(x):
    def score(a):return ord(a) - 96
    return x.split(" ")[[sum(list(map(score, list(i)))) for i in x.split(" ")].index(max([sum(list(map(score, list(i)))) for i in x.split(" ")]))]
 
# =============================================================================
# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
# =============================================================================

start_time = time.time()
print(high(""))
