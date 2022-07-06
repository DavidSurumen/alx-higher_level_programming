#!/usr/bin/python3
"""
Rectangle class with private instance attributes,
and optional instantiation
"""


class Rectangle:
    """
    implementation of rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        total = ""
        if self.__height == 0 or self.__width == 0:
            return total
        for i in range(self.__height):
            total += str(self.print_symbol) * self.__width
            if i is not self.__height - 1:
                total += "\n"
        return total

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2
