# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 13:01:17 2018

@author: RAVI SHANKAR SINGH
"""

def solution(number):
    ls = []
    for i in range(number):
        if i % 3 == 0:
            ls.append(i)
        else:
            if i % 5 == 0:
                ls.append(i)
    return sum(ls)
print(solution(10))