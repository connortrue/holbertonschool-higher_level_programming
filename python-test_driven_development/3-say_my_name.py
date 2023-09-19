#!/usr/bin/python3
# 2-matrix_divided.py
# Connor True
"""Doc"""


def say_my_name(first_name, last_name=""):
    """
    Print a message with the first and last names.

    Parameters:
    first_name (str): The first name.
    last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
    TypeError: If first_name or last_name is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
