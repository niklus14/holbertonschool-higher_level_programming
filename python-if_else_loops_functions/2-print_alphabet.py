#!/usr/bin/python3
# This script loops through alphabet (ASCII numbers 98-122)
# 98 is a, 99 is b, 100 is c, etc
# and prints their character values.

for i in range(97, 123):
    #  "{:c}" is a format code that means "convert this
    #  number to its character equivalent"
    print("{:c}".format(i), end="")
