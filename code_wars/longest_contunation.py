# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 21:47:35 2018

@author: RAVI SHANKAR SINGH
"""

#longest run

def longestRun(L):
    flag = False
    i = 0
    result = []
    while True:
        counter = 0
        n = i
        while flag == False:
            if n <= len(L) - 2:
                if L[n] <= L[n+1]:
                    k = L[n]
                    counter += 1
                    n += 1
                else:
                    result.append(counter)
                    break
            else:
                result.append(counter)
                flag = True
        i += 1
        if flag == True:
            break
    return max(result) + 1

L= [1,2,3,4,5,6]
print(longestRun(L))