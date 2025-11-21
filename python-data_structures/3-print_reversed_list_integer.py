#!/usr/bin/python3
def print_reversed_list_integer(my_list):
    n=(-1)*len(my_list)
    for i in my_list:
        if n==-1:
            print("{:d}".format(i))
        else:
            print("{:d}".format(my_list[n]))
        n+=1
