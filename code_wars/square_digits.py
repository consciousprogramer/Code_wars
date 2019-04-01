# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 20:02:18 2018

@author: RAVI SHANKAR SINGH
"""

def square_digits(num):
    result = []
    for i in list(str(num)): 
        result.append(str((int(i))**2))
    return int("".join(result))
    

print(square_digits(999))
