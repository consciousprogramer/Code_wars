# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:00:23 2018

@author: RAVI SHANKAR SINGH
"""

def find_short(s):
    return min(list(map(len, s.split(" "))))
print(find_short('rohit how are'))