#!/usr/bin/python3
"""Doc"""
import json


def from_json_string(my_str):
    """
    This function returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str: The JSON string to be converted into a Python object.

    Returns:
        A Python object that represents the JSON string.

    Note:
        This function does not handle exceptions if the JSON string doesn't represent an object.
    """
    return json.loads(my_str)
