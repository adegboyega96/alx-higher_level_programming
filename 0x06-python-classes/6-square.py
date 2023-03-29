#!/usr/bin/python3
"""Define a square"""

class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """property of the coordinates of this Square
        Raises:
            TypeError: if value != a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Calculate area of the square Returns: The square of the size"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for a in range(self.__size):
            print(" " * self.__position[0], end="")
            for b in range(self.__size):
                print("#", end="")
            print()
