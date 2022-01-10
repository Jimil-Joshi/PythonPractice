# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 18:29:23 2022

@author: Jimil Joshi
"""
from operator import length_hint
import time





l1 = [ 1, 4, 5, 7, 8]

strat_time_len  = time.time()
lenl = len(l1)
end_time_len = str (time.time() - strat_time_len)


start_time_naiv = time.time()
n =  0 
for i in l1 :
    n = n+1

end_time_naiv = str(time.time() - start_time_naiv)



start_time_hint = time.time()
hintlen = length_hint(l1)
end_time_hint = str(time.time() - start_time_hint)



print("Length of list is: ",(n))
print("Length of list using hint: ",hintlen)
print("Length is : ", lenl)


print("Time taken by simple len: ",end_time_len)
print("Time taken by  naiv: ",end_time_naiv)
print("Time taken by hint: ",end_time_hint)