#!/usr/bin/python3
# 5-square.py
# Connor True
""" Define a class Square"""


class Square:
    """This is an empty class to define square"""

    def __init__(self, size=0):
        """Initializes a new "Square".

        Args:
            size (int): The size of said new square.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of Square

        Args:
            self (square): The square to get the size of
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size value of the Square

        Args:
            self (square): The given Square
            value (int): The size of to set to Square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the given square

        Args:
            self (square): THe square to calculate with.        """
        return (self.__size * self.__size)

    def my_print(self):
        """ prints the square using #

        Args:
            self (square): The square to rpint
        """
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
