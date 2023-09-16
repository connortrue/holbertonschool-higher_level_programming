#!/usr/bin/python3
# 3-square.py
# Connor True
""" Define a class "Square". """


class Square:
    """This is a class to define a square"""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of said new square.
        """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculates the area of the given square

        Args:
            self (square): The square to calculate with.
        """
        return (self.__size * self.__size)
