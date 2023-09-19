#!/usr/bin/python3
# 2-matrix_divided.py
# Connor True
"""Doc"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end='')
        if char in ['.', '?', ':']:
            print("\n")
