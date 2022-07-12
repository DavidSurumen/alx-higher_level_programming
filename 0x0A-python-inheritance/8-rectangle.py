#!/usr/bin/python3
"""
Module ``8-rectangle`` contains a single class: `Rectangle`
that inherits `BaseGeometry` class in `7-base_geometry` module.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Extends BaseGeometry class, and provides additional attributes of its own
    """
    def __init__(self, width, height):
        """Instatiates private instance attributes of the class
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
