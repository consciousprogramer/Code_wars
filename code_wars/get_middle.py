# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 07:58:58 2018

@author: RAVI SHANKAR SINGH
"""

def get_middle(s):
    print((len(s)-1)//2)
    print(len(s)//2+1)
    return s[(len(s)-1)//2:len(s)//2+1]


# =============================================================================
# def get_middle(s):
#     if len(s)%2 == 1:
#         return s[int((len(s) - 1)/2)]
#     return s[int((len(s) - 1)/2):int((len(s) - 1)/2) + 2]
# =============================================================================
print(get_middle("rohit"))