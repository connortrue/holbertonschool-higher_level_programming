#!/usr/bin/python3
"""This is documentation for a class project. Please don't read too much into
all of this, I'm only on month one of python training here."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a square. It inherits from the Rectangle class and
    has the same attributes and methods.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method for the Square class.

        Parameters:
        size (int): The size of the square.
        x (int, optional): The x-coordinate of the square. Default is 0.
        y (int, optional): The y-coordinate of the square. Default is 0.
        id (int, optional): The id of the square. If not provided, it will be
        incremented and assigned automatically.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
        int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute with validation.

        Parameters:
        value (int): The new size of the square.

        Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overloaded method that returns a string representation of the square.

        Returns:
        str: A string that represents the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Update method for the Square class.

        Parameters:
        *args (tuple): A tuple of arguments.
        **kwargs (dict): A dictionary of keyword arguments.

        Returns:
        None

        Raises:
        ValueError: If the number of arguments is not 4.
        """
        if args:
            self.id, self.size, self.x, self.y = args
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            raise ValueError("No arguments provided")
