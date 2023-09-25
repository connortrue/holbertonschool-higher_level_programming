#!/usr/bin/python3
"""Doc"""


class Square(Rectangle):
    """Doc"""

    def __init__(self, size):
        """Doc"""

        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Doc"""

        return self.__size * self.__size

    def __str__(self):
        """Doc"""

        return f"[Square] {self.__size}/{self.__size}"
