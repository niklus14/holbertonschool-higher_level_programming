#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# --- 1. here I find the last digit ---
if number < 0:
    # If number is -626, this makes last_digit = -6
    last_digit = (abs(number) % 10) * -1
else:
    # If number is 4205, this makes last_digit = 5
    last_digit = number % 10

# --- 2. here I build the output ---

# I use an f-string to build the first part of the sentence.
# I add 'end=" "' to stop print from making a new line.
print(f"Last digit of {number} is {last_digit} ", end="")

# --- 3. Here is making the decision (the "if" block) ---
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    # This covers everything else (less than 6 and not 0)
    print("and is less than 6 and not 0")
