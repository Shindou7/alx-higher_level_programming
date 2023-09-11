#!/usr/bin/python3
"""
Module 9-rectangle.py
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that defines a rectangle inherits from BaseGeometry """

    def __init__(self, width, height):
        """ validate and initialize width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ extends parent's empty method and returns area"""
        return self.__width * self.__height

    def __str__(self):
        """ <width>/<height> """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
