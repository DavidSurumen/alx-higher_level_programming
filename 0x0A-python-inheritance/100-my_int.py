#!/usr/bin/python3
"""Module ``100-my_int`` contains a single class: `MyInt`
"""


class MyInt(int):
    """This class extends the `int` class, and inverts equality operators.
    """
    def __init__(self, value):
        """Initializes an integer value.
        """
        self.value = value

    def __ne__(self, x):
        """compares inequality. (inverted)"""
        if self.value == x:
            return True

    def __eq__(self, x):
        """compares equality. (inverted)"""
        return not self.__ne__(x)
