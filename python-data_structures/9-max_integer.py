#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None    
    for k in (my_list):
        h = 0
        for i in (my_list):
            if k >= i:
                hm += 1
        if h == len(my_list):
            return k
