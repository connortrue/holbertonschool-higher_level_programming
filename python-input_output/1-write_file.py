#!/usr/bin/python3
"""Doc"""


def write_file(filename="", text=""):
    """Doc"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
