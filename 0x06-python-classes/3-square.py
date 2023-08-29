#!/usr/bin/python3
""" 3-square.py """

class Square:
    """  class square """
    
    def __init__(self, size=0) -> None:
    """ class init """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
    """area square"""
        return self.__size ** 2
