#!/usr/bin/python3
# 9-print_last_digit.py - outputs and returns the last digit.

def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")

    # 3. Fulfill the "return" job.
    return last_digit
