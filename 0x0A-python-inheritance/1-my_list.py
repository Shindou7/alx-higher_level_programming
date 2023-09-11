#!/usr/bin/python3
"""
Module 1-my_list

"""


class MyList(list):
    """class MyList that inherits from list

    """
    def print_sorted(self):
        """Method that prints the sorted list"""
        print(sorted(self))
