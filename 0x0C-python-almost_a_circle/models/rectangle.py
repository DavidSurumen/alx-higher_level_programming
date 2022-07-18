#!/usr/bin/python3
"""Defines a single class: 'Rectangle', that
extends 'Base'class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class extends 'Base' class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
