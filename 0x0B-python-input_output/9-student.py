#!/usr/bin/python3
"""
Module 9-student.py
that defines the class Student
"""


class Student():
    """
    Class to create student instances
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes Special method student with full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method that returns directory description
        """
        return self.__dict__
