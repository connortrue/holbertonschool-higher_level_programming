#!/usr/bin/python3
"""Doc"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Doc"""

    def __init__(self, width, height):
        self.__width = self.integer_validator(width)
        self.__height = self.integer_validator(height)

    def area(self):
        return self.__width * self.__height

    def __repr__(self):
        str_rectangle = "[" + str(self.__class__.__name__)
        str_rectangle += "] " + str(self.__width)
        str_rectangle += "/" + str(self.__height)
        return str_rectangle

    def __str__(self):
        str_rectangle = "[" + str(self.__class__.__name__)
        str_rectangle += "] " + str(self.__width)
        str_rectangle += "/" + str(self.__height)
        return str_rectangle