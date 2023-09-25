#!/usr/bin/python3
"""Doc"""
Rectangle = __import__('9-rectangle').Rectangle


class Rectangle(BaseGeometry):
    """Doc"""

    def __init__(self, width, height):
        """Doc"""

        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """Doc"""

        return self.__width * self.__height

    def __str__(self):
        """Doc"""

        return f"[Rectangle] {self.__width}/{self.__height}"
