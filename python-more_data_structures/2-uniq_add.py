#!/usr/bin/python3
def uniq_add(my_list):
    x = 1
    new = []
    for k in my_list:
        for i in new:
            if k != i:
                new = new.append(k)
    for y in new:
        x = x * y
    return x
