# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:35:37 2018

@author: RAVI SHANKAR SINGH
"""

def getCount(s):
    return (s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u"))
print(getCount("aeiourohituoiea"))