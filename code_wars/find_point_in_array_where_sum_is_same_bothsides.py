# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 17:38:51 2018

@author: RAVI SHANKAR SINGH
"""

def find_even_index(arr):
    ll = len(arr)
    counter = 0
    while counter <= ll:
        sum1 = 0
        sum2 = 0
        for i in range(counter):
            sum1 += arr[i]
        for n in range(counter + 1,ll):
            sum2 += arr[n]
        if sum1 == sum2:
            return counter
        counter += 1
    return -1

print(find_even_index([29*-0,10,-80,10,10,15,35]))