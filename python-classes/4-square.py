#!/usr/bin/python3
# 4-square.py
# Connor True
""" Define a class Square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initialize a new Square with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size  # Set the size of the square

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size  # Return the size of the square

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size to set for the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Set the size of the square to the given value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
