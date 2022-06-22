#!/usr/bin/python3
"""
Defines a Square class
It implements value/type validation for its attributes
"""


class Square:
    """
    Square implementation
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return self.__size ** 2

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(position) != 2 \
                or not all(isinstance(elem, int) for elem in position) \
                or not all(elem > 0 for elem in position):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for x in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
