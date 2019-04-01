# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 18:23:07 2018

@author: RAVI SHANKAR SINGH
"""

get_string = input("Enter a word: ")
vowelcount = 0
for i in get_string:
    if i in "aeiou":
        vowelcount += 1
print(vowelcount)
