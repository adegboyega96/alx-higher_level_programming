#!/usr/bin/python3
"""Creates square"""


class Square:
    """Create a square class"""

    def __init__(self, size=0):
        """Initializes square class"""
        self.__size = size

    @property
    def size(self):
        """Getter for square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Initializes attribute size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Calculate area of the square Returns: The square of the size"""
        return self.__size ** 2

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
