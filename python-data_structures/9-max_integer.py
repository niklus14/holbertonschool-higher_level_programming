#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None    
    for k in range(my_list):
        for i in range(my_list):
            hm = 0:
            if k >= i:
                hm +=1
        if hm == len(my_list):
            return k
