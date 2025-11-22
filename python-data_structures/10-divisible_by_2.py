#!/usr/bin/python3
def divisible_by_2(my_list):
    list_result = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            list_result += [True]
        else:
            list_result += [False]
    return list_result
