#!/usr/bin/python3
# This script displays numbers 0-99 with 2 digits and commas.

for i in range(100):
    if i == 99:
        print("{:02d}".format(i))
    else:
        print("{:02d}".format(i), end=", ")
