# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 17:59:08 2022

@author: Jimil Joshi
"""
from operator import length_hint


l1 = [2,4,6,8,10]

##Naiv Method
print("The list is" ,str(l1))
n = 0

for i in l1:
    
        n = n + 1
    
print("Length of list is: ",str(n))


##Simple method to find length 
len_list = len(l1)
print("Length of list is: ",len_list)

## Length by using Hint
lenhit = length_hint(l1)
print("Length of list using hint: ",lenhit)



a = []
a.append("Jimil")
a.append("Joshi")
a.append(5.23)
a.append(20.00)

print("The List Is: ",(a))


print("The Length of List Is: ",len(a))







