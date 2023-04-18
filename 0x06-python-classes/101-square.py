#!/usr/bin/python3
"""Creates a square"""


class Square:
    """Create a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square

        Args:
            size: length of a square side
            position: coordinates of a square"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """retrieve size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """retrieve position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position value"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Calculate area of the square Returns: The square of the size"""
        return self.__size ** 2

    def my_print(self):
        """Prints square"""
        print(self.__str__())

    def __str__(self):
        """Prints square"""
        if self.__size == 0:
            return ""
        else:
            str = "\n" * self.__position[1]
            for row in range(self.__size):
                str += " " * self.__position[0]
                str += '#' * self.__size + '\n'
            return str[:-1]
