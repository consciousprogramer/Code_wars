# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 13:20:55 2019

@author: RAVI SHANKAR SINGH
"""
import sys

T = sys.stdin.readline()
for i in range (T):
    flag = True
    occupied = []
    index = 0
    for k in sys.stdin.readline():
        index += 1
        if k != ".":
            for n in range(index - int(k), index + int(k) + 1):
                if n in occupied:
                    flag = False
                    break
                else:
                    occupied.append(n)
    if flag == True:
        print("safe")
    else:
        print("unsafe")
    