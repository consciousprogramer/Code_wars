# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 11:10:00 2018

@author: RAVI SHANKAR SINGH
"""

def dig_pow(n, p):
    result = []
    for i in str(n):
        result.append(int(i)**(p))
        p += 1
    if sum(result)/n == int(sum(result)/n):
        return sum(result)/n
    return -1

print(dig_pow(89, 1))