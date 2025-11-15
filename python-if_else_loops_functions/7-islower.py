#!/usr/bin/python3
# 7-islower.py

def islower(c):
    value = ord(c)
    if value >= 97 and value <= 122:
        return True
    else:
        return False
