#!/usr/bin/python3
"""Doc"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to be written to the file.
        filename: The name of the file.

    Note:
        This function uses the 'with' statement to ensure proper file handling.
        It does not handle exceptions if the object can't be serialized or file
        permission exceptions.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
