#!/usr/bin/python3
# 6-square.py
# Connor True
"""Define a class Square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with the given size and position.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size  # Set the size of the square
        self.position = position  # Set the position of the square

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size  # Return the size of the square

    @property
    def position(self):
        """Get the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position  # Return the position of the square

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

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position to set for the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        err_msg = "position must be a tuple of 2 positive integers"
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(val, int) for val in value) or
                not all(val >= 0 for val in value)):
            raise TypeError(err_msg)
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters.

        Args:
            self (square): The square to print.
        """
        if self.__size == 0:
            print("")  # Print a new line if the size is 0
            return
        for i in range(self.__position[1]):
            print()  # Print new lines for the vertical position
        if self.__position[0] > 0:
            for i in range(self.__size):
                for sp in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")  # Print '#' characters for the square
                print()  # Print a new line after each row
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")  # Print '#' characters for the square
                print()  # Print a new line after each row
