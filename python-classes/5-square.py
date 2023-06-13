#!/usr/bin/python3
"""Square
"""


class Square:
    """
    : square size
    : square area
    : square print
    : square debug
    """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()

        for elements in range(self.__size):
            for row in range(self.__size):
                print("#", end="")
            print()
       
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
