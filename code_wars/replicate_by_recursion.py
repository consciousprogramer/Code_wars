# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 15:56:15 2018

@author: RAVI SHANKAR SINGH
"""

# =============================================================================
# def replicate(times, number):
#     tp=(times,)
#     if times==tp[0]:
#         ls=[]
#     if times <= 0:
#         return []
#     elif times == 1:
#         return ls.append(number)
#     else:
#         return ls.append(replicate(times - 1, number))
# =============================================================================

# =============================================================================
# def replicate(times, number):
#     
#     ls = [number]
#     if times <= 0:
#         return []
#     elif times == 1:
#         return number
#     else:
#         x=(replicate(times - 1, number))
#         ls.append(x)
#         if len(ls) < times - 1:
#             return number
#         else:
#             return ls
# =============================================================================

def replicate(times, number):
    
    s = str(number)
    if times <= 0:
        return []
    elif times == 1:
        return str(number)
    else:
        s = s + replicate(times, number)
        return s

print(replicate(2,5))