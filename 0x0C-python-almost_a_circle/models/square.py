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
