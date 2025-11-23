#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary1 = {}
    for i in sorted(a_dictionary):
        a_dictionary1[i] = a_dictionary[i] * 2
    return a_dictionary1
