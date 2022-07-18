#!/usr/bin/python3
"""Contains a single class, 'Square', that extends
'Rectangle'
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that extends Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """returns value of 'size'."""
        return self.width

    @size.setter
    def size(self, size):
        """sets the dimensions of 'Square'."""
        if type(size) != int:
            raise TypeError('width must be an integer')
        elif size <= 0:
            raise ValueError('width must be > 0')
        self.width = self.height = size
