#!/usr/bin/python3
"""5-square.py"""


class Square:

    """class square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """class size"""
        return self.__size

    @size.setter
    def size(self, value):
        """class size self value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """class area"""
        return self.__size ** 2

    def my_print(self):
        """class print"""
        for i in range(self.size):
            print("#" * self.size)
        if not self.size:
            print()
