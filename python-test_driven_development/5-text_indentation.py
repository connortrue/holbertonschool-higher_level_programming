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

    output = ''
    for char in text:
        output += char
        if char in ['.', '?', ':']:
            output += "\n"

    output = "\n".join([line.strip() for line in output.split("\n")])
    print(output)
