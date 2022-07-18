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
        if type(width) != int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the
        character '#'"""
        for m in range(self.y):
            print()
        for m in range(self.height):
            print(' ' * self.x, end="")
            print('#' * self.width)

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates the value of attributes"""

        keys = ["id", "width", "height", "x", "y"]
        if args and len(args) != 0:
            for index, val in enumerate(args):
                setattr(self, keys[index], val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """returns the dictionary representation of a 'Rectangle'."""
        return {"id": self.id, "width": self.width, 
                "height": self.height, "x": self.x, "y": self.y}
