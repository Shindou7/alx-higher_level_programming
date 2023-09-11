#!/usr/bin/python3
"""
Module 10-square.py
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherits from Rectangle, who inherits from BaseGeometry """
    def __init__(self, size):
        """ initializes a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method that returns """
        return super().area()
