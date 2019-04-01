# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:30:16 2018

@author: RAVI SHANKAR SINGH
"""

def basic_op(operator, value1, value2):
    if operator == '*':
        return value1 * value2
    if operator == '+':
        return value1 + value2
    if operator == '-':
        return value1 - value2
    if operator == '/':
        return value1 / value2
    
# =============================================================================
# def basic_op(operator, value1, value2):
#     return eval("{}{}{}".format(value1, operator, value2))
# =============================================================================
