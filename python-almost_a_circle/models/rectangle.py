#!/usr/bin/python3
"""This is documentation for a class project. Please don't read too much into
all of this, I'm only on month one of python training here."""
from models.base import Base


class Rectangle(Base):
    """
    This class represents a rectangle. It inherits from the Base class and has
    private attributes for width, height, x, and y, each with its own getter
    and setter. It also includes validation for the setter methods.
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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
        int: The width of the rectangle.
        """
        return self.__width

    @property
    def y(self):
        """
        Getter for the y attribute.

        Returns:
        int: The y-coordinate of the rectangle.
        """
        return self.__y

    @property
    def x(self):
        """
        Getter for the x attribute.

        Returns:
        int: The x-coordinate of the rectangle.
        """
        return self.__x

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
        int: The height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute with validation.

        Parameters:
        value (int): The new width of the rectangle.

        Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute with validation.

        Parameters:
        value (int): The new height of the rectangle.

        Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute with validation.

        Parameters:
        value (int): The new x-coordinate of the rectangle.

        Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is less than 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute with validation.

        Parameters:
        value (int): The new y-coordinate of the rectangle.

        Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is less than 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the rectangle to stdout using the character #.
        """
        for _ in range(self.height):
            print('#' * self.width)

    def __str__(self):
        """
        Returns a string representation of the rectangle in the format
        [Rectangle] (<id>) <x>/<y> - <width>/<height>.

        Returns:
        str: A string representation of the rectangle.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x, self.y,
                                                        self.width,
                                                        self.height))
