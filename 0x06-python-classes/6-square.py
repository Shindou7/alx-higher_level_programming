#!/usr/bin/python3

class Square:
    """6-square.py"""

    def __init__(self, size=0, position=(0, 0)):
    """ class init."""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        if not isinstance(position, tuple) or len(position) != 2 \
                or not isinstance(position[0], int) or not isinstance(position[1], int) \
                or position[0] < 0 or position[1] < 0:
             raise TypeError('position must be a tuple of 2 positive integers')
         self.size = size
         self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
    """class size"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
      """class positive"""
      if not isinstance(position, tuple) or len(position) != 2 \
                or not isinstance(position[0], int) or not isinstance(position[1], int) \
                or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
      self.__position = position


    def __check_tuple(self, position):
    """class tuple"""
        if type(position) is tuple:
            return True
        return False

    def area(self):
    """class area"""
        return self.__size ** 2

    def my_print(self):
    """class print"""
        if self.__size == 0:
            print()
            return None

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
