#!/usr/bin/python3
"""Define a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """initialize a square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate area of the square
        return self.__size ** 2
