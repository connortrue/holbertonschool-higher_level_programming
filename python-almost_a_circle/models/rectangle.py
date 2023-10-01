#!/usr/bin/python3
"""This is documentation for a class project. Please don't read too much into
all of this, I'm only on month one of python training here."""
from models.base import Base


class Rectangle(Base):
    """
    This class represents a rectangle. It inherits from the Base class and has
    private attributes for width, height, x, and y, each with its own getter
    and setter.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method for the Rectangle class.

        Parameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int, optional): The x-coordinate of the rectangle. Default is 0.
        y (int, optional): The y-coordinate of the rectangle. Default is 0.
        id (int, optional): The id of the rectangle. If not provided, it
        will be incremented and assigned automatically.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Parameters:
        value (int): The new width of the rectangle.
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
        int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Parameters:
        value (int): The new height of the rectangle.
        """
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.

        Returns:
        int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Parameters:
        value (int): The new x-coordinate of the rectangle.
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.

        Returns:
        int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Parameters:
        value (int): The new y-coordinate of the rectangle.
        """
        self.__y = value
