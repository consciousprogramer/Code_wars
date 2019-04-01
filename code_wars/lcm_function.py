# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:28:25 2019

@author: RAVI SHANKAR SINGH
"""
import time

def primechecker(n):
    def checkby2(n):
        if n%2 == 0:
            if n == 2:
                return True
            return False
    if n == 1:
        return False
    if checkby2(n) == False:
        return False
    for k in range(3, round(n**(0.5)) + 2,2):
        if n % k == 0:
            return False
        break
    return True

def lcm (x, y):
    if (primechecker(x) or primechecker(y)) == True:
        return x * y
    
    i = 1
    factors1 = []
    factors2 = []
    while x != 1:
        i += 1
        if x % i == 0:
            x = x//i
            factors1.append(i)
            i = 1
    
    while y != 1:
        i += 1
        if y % i == 0:
            y = y//i
            factors2.append(i)
            i = 1                
    mult_sum = 1
    factors = []
    for n in factors1[:]:
        if n in factors2:
            factors.append(n)
            factors1.remove(n)
            factors2.remove(n)
        else:
            factors.append(n)
            
    for k in factors:
        mult_sum *= k
    for k in factors2:
        mult_sum *= k
    return mult_sum

t = input()
st = time.time()
ls = t.split()
print("----------------------",lcm(int(ls[0]), int(ls[1])))
print(time.time() - st)