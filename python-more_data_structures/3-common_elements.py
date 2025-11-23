#!/usr/bin/python3
def common_elements(set_1, set_2):
    a = []
    for i in set_1:
        for k in set_2:
            if i == k:
                a += [k]
    return set(a)
