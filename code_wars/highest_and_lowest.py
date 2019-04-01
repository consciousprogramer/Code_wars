# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:44:23 2018

@author: RAVI SHANKAR SINGH
"""

def high_and_low(numbers):
    return str(max(list(map(int,numbers.split(" "))))) +" " + str(min(list(map(int,numbers.split(" ")))))
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))