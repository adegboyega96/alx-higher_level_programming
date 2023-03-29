class Square:

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    # This is the setter
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Calculate area of the square Returns: The square of the size"""
        return self.__size ** 2
