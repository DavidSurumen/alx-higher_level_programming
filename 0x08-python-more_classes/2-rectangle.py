#!/usr/bin/python3
"""
Rectangle class with private instance attributes,
and optional instantiation
"""


class Rectangle:
    """
    implementation of rectangle
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError('width must be an integer')
        elif val < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError('height must be an integer')
        elif val < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = val

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
