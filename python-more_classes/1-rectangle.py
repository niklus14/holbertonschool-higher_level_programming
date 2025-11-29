#!/usr/bin/python3
"""
this module defines a class Rectangle.
it demonstrates the use of getters and setters for data validation.
"""


class Rectangle:
    """
    represents a rectangle with private attributes for width and height.
    """

    def __init__(self, width=0, height=0):
        """
       initializes the rectangle.

        args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        # note: We assign to self.width (the setter), not self.__width.
        # this ensures the validation logic runs even during initialization.
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieves the width of the rectangle.

        returns:
            int: the private width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle with validation.

        args:
            value (int): the new width.

        raises:
            TypeError: if width is not an integer.
            ValueError: if width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        retrieves the height of the rectangle.

        returns:
            int: the private height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of the rectangle with validation.

        args:
            value (int): the new height.

        raises:
            TypeError: if height is not an integer.
            ValueError: if height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
