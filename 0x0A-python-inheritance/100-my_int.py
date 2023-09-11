#!/usr/bin/python3
"""
Module 100-my_int.py
"""


class MyInt(int):
    """
    Method my int
    """
    def __init__(self, num):
        """initialize num"""
        self.num = num

    def __eq__(self, other):
        """
        Method that returns != check
        """
        return self.num != other

    def __ne__(self, other):
        """
        Method that returns == check 
        """
        return self.num == other
