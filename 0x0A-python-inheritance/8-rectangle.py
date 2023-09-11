#!/usr/bin/python3
"""
Module 8-rectangle.py
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that defines a rectangle from inherits from BaseGeometry """

    def __init__(self, width, height):
        """ validate and initialize width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
