#!/usr/bin/python3
"""
Module '5-base_geometry' contains an empty class
"""


class BaseGeometry:
    """Class is empty.
    """
    def area(self):
        """Public instance methods that raises an exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the 'value'
        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
