#!/usr/bin/python3
# 0-rectangle.py
# Connor True <6676@holbertonstudents.com>
"""Define a class - Rectangle."""


class Rectangle:
    """
    Rectangle class defined by width and height
    """

    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle instance with width and height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle
        """

        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle
        """

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle
        """

        if self.width == 0 or self.height == 0:
            return ""
        return ('\n'.join(['#' * self.width for _ in range(self.height)]))

    def __repr__(self):
        """
        Return a string representation of the rectangle for recreation
        """

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted
        """

        print("Bye rectangle...")
