# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 11:42:51 2018

@author: RAVI SHANKAR SINGH
"""

def persistence(n):
    count = 0
    while n >= 10:
        ls = str(n)
        mult = 1
        for i in ls:
            mult = mult*int(i)
        n = mult
        count += 1
    return count
print(persistence())