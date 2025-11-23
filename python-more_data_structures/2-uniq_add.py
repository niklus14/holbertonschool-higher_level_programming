#!/usr/bin/python3
def uniq_add(my_list):
    total = 0
    new = []

    for k in my_list:
        if k not in new:
            new.append(k)

    for y in new:
        total += y

    return total
