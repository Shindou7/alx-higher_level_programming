#!/usr/bin/python3
"""
8-rectangle
"""


class Rectangle:
    """
    Defines class rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __repr__(self):
        """ returns representation """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Detect instance deletion """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compare rectangles """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        bigger1_area = rect_1.area()
        bigger2_area = rect_2.area()

        if bigger1_area >= bigger2_area:
            return rect_1

        return rect_2
