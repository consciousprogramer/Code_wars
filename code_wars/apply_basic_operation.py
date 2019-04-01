# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 07:18:32 2018

@author: RAVI SHANKAR SINGH
"""

def basic_op(operator, value1, value2):
    if operator == "*":
        return value1*value2
    elif operator == "+":
        return value1 + value2
    elif operator == "-":
       return value1 - value2
    return value1 / value2

print(basic_op("/",4,5))