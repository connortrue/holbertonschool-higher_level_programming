#!/usr/bin/python3
"""Doc"""
import json


def to_json_string(my_obj):
    """
    This function returns the JSON representation of an object (string).

    Args:
        my_obj: The Python object to be converted into a JSON string.

    Returns:
        A JSON string that represents the Python object.

    Note:
        This function does not handle exceptions if the object can't be
        serialized.
    """
    return json.dumps(my_obj)
