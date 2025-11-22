#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    a = 0
    while a < len(my_string):
        if my_string[a] == "c" or my_string[a] == "C":
            del my_string[a]
        else:
            a += 1
    return "".join(my_string)
