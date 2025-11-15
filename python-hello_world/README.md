-----

Project # Python - Hello, World

This repository is for hosting scripts and task resolutions for the "Python - Hello, World" project.

-----

## General Requirements

### Python Scripts

All Python scripts in this project must adhere to the following requirements:

  * Allowed Editors: `vi`, `vim`, `emacs`
  * Interpreter: All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.\*).
  * File Ending: All files must end with a new line.
  * Shebang: The first line of all files must be exactly `#!/usr/bin/python3`.
  * README: A `README.md` file at the root of the project folder is mandatory.
  * Style Check: Code must use `pycodestyle` (version 2.7.\*).
  * Permissions: All files must be executable.
  * File Length: The length of your files will be tested using `wc`.

-----

## Tasks

### 0\. Hello, print

  * File: `2-print.py`

> Write a Python script that prints exactly `"Programming is like building a multilingual puzzle"`, followed by a new line.
>
>   * Note: You must use the `print` function.

-----

### 1\. Print integer

  * File: `3-print_number.py`

> Complete the source code to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

Given Code:

```python
#!/usr/bin/python3
number = 98
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
```

Requirements:

  * The output must be: `[number] Battery street\n`
  * You are not allowed to cast the `number` variable into a string.
  * Your code must be 3 lines long.
  * You must use f-strings.

-----

### 2\. Print float

  * File: `4-print_float.py`

> Complete the source code to print the float stored in the variable `number` with a precision of 2 digits.

Given Code:

```python
#!/usr/bin/python3
number = 3.14159
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
```

Requirements:

  * The output must be: `Float: [float_with_2_digits]\n`
  * You are not allowed to cast `number` to a string.
  * You must use f-strings.

-----

### 3\. Print string

  * File: `5-print_string.py`

> Complete this source code to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

Given Code:

```python
#!/usr/bin/python3
str = "Holberton School"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
```

Requirements:

  * The output must be the value of `str` 3 times, followed by a new line, followed by the first 9 characters of `str`, followed by a new line.
  * You are not allowed to use any loops or conditional statements.
  * Your program should be a maximum of 5 lines long.

-----

### 4\. Play with strings

  * File: `6-concat.py`

> Complete this source code to print `Welcome to Holberton School!`

Given Code:

```python
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(f"Welcome to {str1}!")
```

Requirements:

  * You are not allowed to use any loops or conditional statements.
  * You must use the variables `str1` and `str2` in your new line of code.
  * Your program should be exactly 5 lines long.

-----

### 5\. Copy - Cut - Paste

  * File: `7-edges.py`

> Complete this source code.

Given Code:

```python
#!/usr/bin/python3
word = "Holberton"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
```

Requirements:

  * You are not allowed to use any loops or conditional statements.
  * Your program should be exactly 8 lines long.
  * `word_first_3` must contain the first 3 letters of `word`.
  * `word_last_2` must contain the last 2 letters of `word`.
  * `middle_word` must contain the value of `word` without the first and last letters.

-----

### 6\. Create a new sentence

  * File: `8-concat_edges.py`

> Complete this source code to print `object-oriented programming with Python`, followed by a new line.

Given Code:

```python
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(str)
```

Requirements:

  * You are not allowed to use any loops or conditional statements.
  * Your program should be exactly 5 lines long.
  * You are not allowed to create new variables.
  * You are not allowed to use string literals (you must slice the `str` variable).

-----

### 7\. Easter Egg

  * File: `9-easter_egg.py`

> Write a Python script that prints `"The Zen of Python", by Tim Peters`, followed by a new line.
>
>   * Your script should be a maximum of 98 characters long.
