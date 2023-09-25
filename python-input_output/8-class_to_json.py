#!/usr/bin/python3
"""Doc"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of
    an object

    Parameters:
    obj (object): an instance of a Class

    Returns:
    dict: a dictionary description of the object
    """

    return {key: value for key, value in obj.__dict__.items()
            if isinstance(value, (list, dict, str, int, bool))}
