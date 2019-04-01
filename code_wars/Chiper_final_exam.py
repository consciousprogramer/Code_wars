# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 02:42:53 2018

@author: RAVI SHANKAR SINGH
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    k = 0
    result = {}
    for i in map_from:
        result[i] = map_to[k]
        k += 1
        
    s = ""
    for letter in code:
        s += result[letter]
    
    return (result, s)
print(cipher("abcd", "dcba", "dab"))

# Your code here
    
    #({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')