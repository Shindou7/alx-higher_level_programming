#!/usr/bin/python3
"4-square.py"

class Square:
    """class Square
    """

    def __init__(self, size=0):
        """square def init
        """
        self.size = size

    def area(self):
        """class area
        """
        return self.__size ** 2


    @property
    def size(self):
        """class size self
        """
        return self.__size

    @size.setter
    def size(self, value):
        """class size self value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
