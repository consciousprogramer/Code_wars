# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 11:29:45 2018

@author: RAVI SHANKAR SINGH
"""

# Can you help the association by writing a method to create a random Bingo card?
#A Bingo card contains 24 unique and random numbers according to this scheme:
#5 numbers from the B column in the range 1 to 15
#5 numbers from the I column in the range 16 to 30
#4 numbers from the N column in the range 31 to 45
#5 numbers from the G column in the range 46 to 60
#5 numbers from the O column in the range 61 to 75
from random import randint
def get_bingo_card():
    s = "BINGO"
    offset = 0
    final_store = []
    dublicate_checker = []
    n_rec = 0
    for b in s:
        for n in range(5):
            x = randint(1 + offset, 15 + offset)
            dublicate_checker.append(x)
            if x in dublicate_checker:
                while x in dublicate_checker:
                    x = randint(1 + offset, 15 + offset)
                dublicate_checker.append(x)
            app_str = str(b) + str(x)
            final_store.append(app_str)
            if n_rec == 2:
                if n == 3:
                    break
        n_rec += 1
        offset += 15
    return final_store
print(get_bingo_card())