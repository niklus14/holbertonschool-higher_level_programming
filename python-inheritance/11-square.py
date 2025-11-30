#!/usr/bin/python3
"""fbhjbrhbv"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """dkfnvknf"""

    def __init__(self, size):
        """sdlkdnfnr"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """srnfkkrj"""
        return self.__size ** 2

    def __str__(self):
        """klfnvklnf"""
        return "[Square] {}/{}".format(self.__size, self.__size)
