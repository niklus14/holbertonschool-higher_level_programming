#!/usr/bin/python3
# function that transform a string in uppercase followed by a new line.
def uppercase(str):
    for c in str:
        num = ord(c)
        if num >= 97 and num <= 122:
            num = num - 32
        print("{}".format(chr(num)), end="")
    print("")
