#!/usr/bin/python3
"""Doc"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Doc"""

    def __init__(self, width, height):
        """Doc"""
        if super().integer_validator("width", width):
            self.__width = width
        if super().integer_validator("height", height):
            self.__height = height

    def __str__(self):
        """Doc"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Doc"""
        return self.__width * self.__height
