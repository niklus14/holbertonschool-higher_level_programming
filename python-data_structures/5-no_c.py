#!/usr/bin/python3
def no_c(my_string):
    a = 0
    my_string=list(my_string)
    for i in (my_string):
        if i == "c" or i == "C" :
            del my_string[a]
        a+=1
    print("{}".format(my_string))   
