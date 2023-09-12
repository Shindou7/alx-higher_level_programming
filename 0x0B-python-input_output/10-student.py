#!/usr/bin/python3
"""
Module 10-student.py
that defines the class Student
"""


class Student():
    """
    Class to create student instances
    """
    def __init__(self, first_name, last_name, age):
        """
        Special method to initialize
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        if attrs is None:
            return self.__dict__
        else:
            directory = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    directory[att] = self.__dict__[att]
            return directory
