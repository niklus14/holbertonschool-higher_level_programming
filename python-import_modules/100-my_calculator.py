#!/usr/bin/python3
"""This module is calculator for terminal.It performs simple operations."""

# The "guard" block. Code only runs if the script is
# executed directly.
if __name__ == "__main__":

    # Importing tools
    import sys
    from calculator_1 import add, sub, mul, div

    # /// 1. Checking argument count \\\
    # len(sys.argv) includes the script name, it checks for 4 items
    if len(sys.argv) != 4:
        # The number of arguments is wrong. Shows error and exits.
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)  # Exits with a "failure" code

    # /// 2. Getting the arguments \\\
    # If I know it has 3 arguments, so I can safely get them.
    # I use int() to convert the text to numbers.
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    # /// 3. Checking the operator and do the math \\\
    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op == '/':
        result = div(a, b)
    else:
        # The operator is not one of the 4 allowed. Shows error and exits.
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)  # Exit with a "failure" code

    # /// 4. If it was done to here, everything was successful \\\
    # It displays the result using the .format() method
    print("{} {} {} = {}".format(a, op, b, result))
    sys.exit(0)  # Exits with a "success" code
