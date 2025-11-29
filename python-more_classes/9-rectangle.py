#!/usr/bin/python3
"""
this module defines a class Rectangle with a square factory method.
it demonstrates the class method pattern used in object factories.
"""


class Rectangle:
    """
    represents a rectangle.

    attributes:
        number_of_instances (int): the number of active instances.
        print_symbol (any): the symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initializes the rectangle and increments the instance counter.

        args:
            width (int): the width of the rectangle. defaults to 0.
            height (int): the height of the rectangle. defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        destructor method used to perform cleanup.
        decrements the instance counter when an object is deleted.
        """
        Rectangle.number_of_instances -= 1
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
            value (int): The new width.

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
            ValueError: if height is negative
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
        uses the print_symbol attribute for drawing.

        returns:
            str: the visual representation.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = ""
        symbol = str(self.print_symbol)

        for i in range(self.__height):
            rect_str += symbol * self.__width
            if i != self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """
        returns the string representation of the rectangle definition.
        this string can be used by eval() to recreate the object.

        Returns:
            str: 'Rectangle(width, height)'
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area.

        args:
            rect_1 (Rectangle): the first rectangle.
            rect_2 (Rectangle): the second rectangle.

        returns:
            Rectangle: the bigger rectangle, or rect_1 if they are equal.

        raises:
            TypeError: if rect_1 or rect_2 are not instances of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        returns a new Rectangle instance with width == height == size.

        args:
            size (int): the size of the square. defaults to 0.

        returns:
            Rectangle: a new instance of Rectangle.
        """
        # 'cls' refers to the class 'Rectangle'.
        # Calling cls(size, size) is the same as calling Rectangle(size, size).
        return cls(size, size)
