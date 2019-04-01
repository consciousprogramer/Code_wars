# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 08:47:06 2019

@author: RAVI SHANKAR SINGH
"""

def DFS(ls, x):
    if len(ls) == 0:
        return False
    else:
        if type(ls[0]) == list:
            result = DFS(ls[0], x)
            if result == True:
                return True
            else:
                ls.remove(ls[0])
                return DFS((ls), x)
        elif ls[0] == x:
            return True
        else:
            ls.remove(ls[0])
            return DFS((ls), x)
print(DFS([2,4,8,[[6,5]],[7,[9,[1,[15,16,[598]]]],45]], 598))