#!/usr/bin/python3
from models.base import Base
"""This is documentation for a class project. Please don't read too much into
all of this, I'm only on month one of python training here."""


class Rectangle(Base):
    """
    This class inherits from Base and represents a rectangle.
    It has private attributes for width, height, x, and y, each with its own
    getter and setter.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method for the Rectangle class.

        Parameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int, optional): The x-coordinate of the rectangle. Default is 0.
        y (int, optional): The y-coordinate of the rectangle. Default is 0.
        id (int, optional): The id of the rectangle. If not provided, it will
        be incremented and assigned automatically.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
