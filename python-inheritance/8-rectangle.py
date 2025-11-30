#!/usr/bin/python3
"""kldsnjrn"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """knfkdk"""

    def __init__(self, width, height):
        """djnkjf"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
