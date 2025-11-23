#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = []
    for i in set_1:
        for k in set_2:
            if i == k:
                a += [k]
    set11 = list(set(list(set_1) + list(set_2)))
    f = []
    for j in set11:
        if a.count(j) == 0:
            f += [j]
    return set(f)
