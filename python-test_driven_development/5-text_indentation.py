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

    sentences = []
    start = 0
    for i, char in enumerate(text):
        if char in ['.', '?', ':']:
            sentences.append(text[start:i+1].strip())
            start = i+1
    sentences.append(text[start:].strip())

    print("\n\n".join(sentences), end="")
