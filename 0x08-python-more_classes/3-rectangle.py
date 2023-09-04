#!/usr/bin/python3
"""
3-rectangle
"""


class Rectangle:
    """
    Defines class rectangle
    """
    def __init__(self, width=0, height=0):
        """ Method that initializes the instance """
        self.width = width
        self.height = height  

    @property
    def width(self):
        """ width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that returns the value of the height """
        return self.__height


    @height.setter
    def height(self, value):
        """ Setter sets height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


      def area(self):
        """ calculates Rectangle area """
  
        return self.width * self.height


    def perimeter(self):
        """ calculates the Rectangle perimeter """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)


    def __str__(self):
        """ Prints rectangle with # """

        string = ""

        if self.width == 0 or self.height == 0:
            return string

        for i in range(self.height):
            string += ("#" * self.width) + "\n"

        return string[:-1]
