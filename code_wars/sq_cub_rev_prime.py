# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:18:28 2018

@author: RAVI SHANKAR SINGH
"""
import time
# 4 kyu kata
def primechecker(n):
    def checkby2(n):
        if n%2 == 0:
            if n == 2:
                return "It's Prime"
            return "Not Prime"
    if n == 1:
        return "Not Prime"
    if checkby2(n) == "Not Prime":
        return "Not Prime"
    for k in range(3, round(n**(0.5)) + 2,2):
        if n % k == 0:
            return "Not Prime"
            break
    return "It's Prime"
start_time = time.time()
print(primechecker(1159309966517))
print("--- %s seconds ---" % (time.time() - start_time))