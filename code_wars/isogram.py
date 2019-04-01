# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 15:49:37 2018

@author: RAVI SHANKAR SINGH
"""

# funtion name is)isogram

def is_isogram(string):
    string = string.lower()
    for i in string:
        if string.count(i) > 1: 
            return False
    return True


# =============================================================================
# from collections import Counter
# def is_isogram(string):
#     new_string = string.lower()
#     c = Counter(new_string)
#     for item in c:
#         if c[item] > 1:
#             return False
#     return True
#    
# =============================================================================

# =============================================================================
# 
# def is_isogram(string):
#     string = string.lower()
#     a = [string.count(i) > 1 for i in string]
#     return not a.count(True) > 0
# =============================================================================
