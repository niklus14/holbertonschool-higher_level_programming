#!/usr/bin/python3
# This script loops through alphabet (ASCII numbers 98-122)
# except q and e
# and prints their character values.

for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    print("{:c}".format(i), end="")
