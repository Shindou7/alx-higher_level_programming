#!/usr/bin/python3
class Square:
    """ 2-square.py
    """
    def __init__(self, size=0):
        """ Method :square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
