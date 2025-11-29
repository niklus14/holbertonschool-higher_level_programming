#!/usr/bin/python3
"""
this module defines a class Rectangle with lifecycle management.
it demonstrates object initialization, representation, and destruction.
"""


class Rectangle:
    """
    represents a rectangle with private attributes and logic methods.
    """

    def __init__(self, width=0, height=0):
        """
        initializes the rectangle.

        args:
            width (int): the width of the rectangle. Defaults to 0.
            height (int): the height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    def __del__(self):
        """
        destructor method used to perform cleanup.
        prints a message when an instance is deleted.
        """
        print("Bye rectangle...")

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

    def area(self):
        """
        calculates and returns the area of the rectangle.

        returns:
            int: the area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculates and returns the perimeter of the rectangle.

        returns:
            int: the perimeter 2 * (width + height).
                 returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        returns the printable string representation of the Rectangle.
        represents the rectangle with the # character.

        returns:
            str: the visual representation.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = ""
        for i in range(self.__height):
            rect_str += "#" * self.__width
            if i != self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """
        returns the string representation of the rectangle definition.
        this string can be used by eval() to recreate the object.

        returns:
            str: 'Rectangle(width, height)'
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
