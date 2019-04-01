# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 07:29:08 2018

@author: RAVI SHANKAR SINGH
"""

#marble game
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return ((blue_start - blue_pulled)/blue_start)
print(guess_blue(12, 7, 4, 3))