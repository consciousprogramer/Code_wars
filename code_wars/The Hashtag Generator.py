# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 18:33:50 2018

@author: RAVI SHANKAR SINGH
"""
def mix(s1, s2):
    L1={}
    L2={}
    s1=s1.replace(' ','')
    s2=s2.replace(' ','')
    
    #Remove all capital letter
    for i in s1:
        if(ord(1) <= 65 or ord(1) >= 90):
            s1.replace('i','')          
    for i in s2:
        if(ord(1) <= 65 or ord(1) >= 90):
            s2.replace('i','')
    
        