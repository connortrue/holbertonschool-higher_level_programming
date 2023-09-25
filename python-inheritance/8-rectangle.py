#!/usr/bin/python3
"""Doc"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Doc"""

    def __init__(self, width, height):
        """Doc"""

        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """Doc"""

        return self.__width * self.__height
