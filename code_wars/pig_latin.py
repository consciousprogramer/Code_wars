# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:10:12 2019

@author: RAVI SHANKAR SINGH
"""
for n in range(int(input())):
    s = input()
    s2 = s.split(" ")
    s2c = s2[:]
    for i in range(len(s2)):
            s2c[i] = s2[i][1:] + str(s2[i][0]) + "ay"
    s2c[0] = s2c[0].capitalize()
    s3 = " ".join(s2c)
    print(s3)