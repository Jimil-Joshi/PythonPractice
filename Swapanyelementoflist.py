# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 21:27:12 2022

@author: Jimil Joshi
"""

list = [10,12,13,15,17]

def swapnumber(list):
    size = len(list)
    temp = list[0]
    temp1 = list[1]
    list[0] = list[3]
    list[1] = list[2]
    list[3] = temp
    list[2] = temp1
    
    
    return list
print(swapnumber(list))
    