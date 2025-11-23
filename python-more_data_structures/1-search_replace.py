#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for k in my_list:
        if k == search:
            new.append(replace)
        else:
            new.append(k)
    return new
