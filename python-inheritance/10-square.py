#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize square with validated size"""
        # size
        self.integer_validator("size", size)
        self.__size = size

        # Rectangle
        super().__init__(size, size)

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size
