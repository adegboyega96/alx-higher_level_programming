#!/usr/bin/python3
"""Define a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """initiliaze a square"""
        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    # This is the setter
    @size.setter
    def size(self, value):
        """set the size of square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Calculate area of the square Returns: The square of the size"""
        return self.__size ** 2
