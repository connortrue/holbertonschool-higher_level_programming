#!/usr/bin/python3
"""Doc"""
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

    def __str__(self):
        """
        Overloaded method that returns a string representation of the square.

        Returns:
        str: A string that represents the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
