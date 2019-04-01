# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 22:14:56 2018

@author: RAVI SHANKAR SINGH
"""

import time
# 4 kyu kata
start_time = time.time()

def intrev(s):
    s = str(s)
    snew = int(s[::-1])
    return snew

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

counter = 1
num = 89
while counter <= 50:
    numsq = num*num
    numcub = numsq*num
    if int(str(numsq)[0]) % 2 != 0 or int(str(numcub)[0]) % 2 != 0: 
        if int(str(numsq)[0])!= 5:
            numsqrev = intrev(numsq)
            numcubrev = intrev(numsq*num)
            if primechecker(numcubrev) == "It's Prime":
                if primechecker(numsqrev) == "It's Prime":
                    print(str(counter) + " : " + str(num))
                    counter += 1
    num += 1
print("--- %s seconds ---" % (time.time() - start_time))