#!/usr/bin/python3
"""Doc"""


def inherits_from(obj, a_class):
    """Doc"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
