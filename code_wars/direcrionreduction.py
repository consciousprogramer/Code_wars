# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 22:39:29 2019

@author: RAVI SHANKAR SINGH
"""

def dirReduc(arr):
    x_list = []
    x_index = []
    y_list = []
    y_index = []
    count_x = 0
    count_y = 0
    length = len(arr)
    for i in range(length):
        if arr[i] == "NORTH":
            y_list.append("+")
            count_y += 1
            y_index.append(i)
            if i != 0:
                if x_list[count_y] != x_list[count_y - 1]:
                    arr.remove[arr[y_index(-1)]]
                    arr.remove[arr[y_index(-2)]]
        
        elif arr[i] == "SOUTH":
            y_list.append("-")
            count_y += 1
            y_index.append(i)
            if i != 0:
                if x_list[count_y] != x_list[count_y - 1]:
                    arr.remove[arr[y_index(-1)]]
                    arr.remove[arr[y_index(-2)]]
        
        elif arr[i] == "EAST":
            x_list.append("+")
            count_x += 1
            x_index.append(i)
            if i != 0:
                if x_list[count_x] != x_list[count_x - 1]:
                    arr.remove[arr[x_index(-1)]]
                    arr.remove[arr[x_index(-2)]]
                    
        elif arr[i] == "WEST":
            x_list.append("-")
            count_x += 1
            x_index.append(i)
            if i != 0:
                if x_list[count_x] != x_list[count_x - 1]:
                    arr.remove[arr[x_index(-1)]]
                    arr.remove[arr[x_index(-2)]]
    
    return arr
