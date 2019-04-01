# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 08:44:18 2018

@author: RAVI SHANKAR SINGH
"""
import time
def sq_cub_rev_prime(n):

    def intrev(n):
        n = str(n)
        snew = int(n[::-1])
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
    while counter <= n:
        numsqrev = intrev(num**2)
        numcubrev = intrev(num**3)
        if primechecker(numcubrev) == "It's Prime":
            if primechecker(numsqrev) == "It's Prime":
                counter += 1
        num += 1
    return num - 1
st = time.time()
print(sq_cub_rev_prime(95668465165))
print(time.time() - st)