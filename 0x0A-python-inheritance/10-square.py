"""
Module ``10-Square`` contains a single class ``Square``
which extends the `Rectangle` class in the `9-rectangle` module.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Extends the Rectangle class, and adds one attribute
    """
    def __init__(self, size):
        """Initializes the values"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
