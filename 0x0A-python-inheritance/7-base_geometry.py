#!/usr/bin/python3
"""
Module 7-base_geometry.py
"""


class BaseGeometry:
   """ Empty class """

    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that recieves the value property
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
