#!/usr/bin/python3
"""Doc"""


class BaseGeometry:
    """Doc"""

    def area(self):
        """Doc"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Doc"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return True
