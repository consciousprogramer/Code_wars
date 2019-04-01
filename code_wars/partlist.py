# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 11:40:57 2018

@author: RAVI SHANKAR SINGH
"""

def partlist(arr):
# =============================================================================
#     resultb = []
#     resultf = []
#     for i in range(1, len(arr)):
#         resultb.append(" ".join(arr[0:i]))
#         resultb.append(" ".join(arr[i: len(arr)]))
#         resultf.append(resultb[:])
#         resultb.remove(" ".join(arr[0:i]))
#         resultb.remove(" ".join(arr[i: len(arr)]))
#     return resultf
# =============================================================================
        
    return list(((" ".join(arr[0:n])),(" ".join(arr[n: len(arr)]))) for n in range(1,len(arr)))

    
print((partlist(["az", "toto", "picaro", "zone", "kiwi"])))