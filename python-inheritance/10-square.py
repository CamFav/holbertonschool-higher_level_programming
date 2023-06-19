#!/usr/bin/python3
"""Square"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """
    def __init__(self, size):
        self.__size = super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
