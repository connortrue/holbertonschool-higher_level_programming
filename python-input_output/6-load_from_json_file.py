#!/usr/bin/python3
"""Doc"""
import json


def load_from_json_file(filename):
    """
    This function creates an object from a JSON file.

    Args:
        filename: The name of the JSON file.

    Returns:
        An object represented by the JSON string in the file.

    Note:
        This function uses the 'with' statement for proper file handling.
        It does not handle exceptions if the JSON string doesn't represent
        an object or file permission exceptions.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
