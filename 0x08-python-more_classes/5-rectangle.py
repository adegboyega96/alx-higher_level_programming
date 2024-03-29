#!/usr/bin/python3
"""Ractangle module"""



class Rectangle:
    """Create rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Assigning a value to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Assigning a value to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Calculating the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculating the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = ""
            for rows in range(self.__height):
                rectangle += "#" * self.__width
                rectangle += "\n"
            return rectangle

    def __repr__(self):
        """String representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deleting Instances of Rectangle"""
        print("Bye rectangle...")
