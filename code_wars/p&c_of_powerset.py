# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 16:15:26 2018

@author: RAVI SHANKAR SINGH
"""

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
ls = ["r","o","h","i","t"]
x = powerSet(ls)
for i in range(2*:
    print(next(x))
        

# =============================================================================
# def yieldAllCombos(items):
#     """
#         Generates all combinations of N items into two bags, whereby each 
#         item is in one or zero bags.
# 
#         Yields a tuple, (bag1, bag2), where each bag is represented as a list 
#         of which item(s) are in each bag.
#     """
#     # Your code here
# =============================================================================
