# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:19:33 2018

@author: RAVI SHANKAR SINGH
"""

def validate_code(code):
    return (str(code)[0] == '1' or str(code)[0] == '2' or str(code)[0] == '3')
print(validate_code(65))