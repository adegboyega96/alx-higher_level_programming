#!/usr/bin/python3
"""My rectangle module"""

class Rectangle:
    """define a rectangle"""

    def __init__(self, width=0, height=0):
        """initialize the rectangle with his
        Args:
            width: width of a rectangle
            height: height of a rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
