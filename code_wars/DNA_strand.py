# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 18:37:42 2018

@author: RAVI SHANKAR SINGH
"""

def DNA_strand(dna):
    ls = []
    for i in dna:
        if i == "T":
            ls.extend("A")
        elif i == "A":
            ls.extend("T")
        elif i == "C":
            ls.extend("G")
        elif i == "G":
            ls.extend("C")
    return "".join(ls)

print(DNA_strand("TAACCGG"))
