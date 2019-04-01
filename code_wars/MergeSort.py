# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 12:04:11 2019

@author: RAVI SHANKAR SINGH
"""

#   merge sort

def MergeSort(ls):
    n = len(ls)
    if len(ls) == 1:
        return ls
# =============================================================================
#     elif len(ls) == 2:
#         return sorted(ls)
# =============================================================================
    else:
        sls1 = MergeSort(ls[ :n//2])
        sls2 = MergeSort(ls[n//2: ])
        retlist = []
        i1 = 0
        i2 = 0
        while True:
            if sls1[i1] >= sls2[i2]:
                retlist.append(sls2[i2])
                i2 += 1
            else:
                retlist.append(sls1[i1])
                i1 += 1
            if i1 == len(sls1):
                retlist.extend(sls2[i2: ])
                break
            if i2 == len(sls2):
                retlist.extend(sls1[i1: ])
                break
        return retlist