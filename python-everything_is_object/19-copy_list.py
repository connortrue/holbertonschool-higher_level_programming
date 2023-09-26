#!/usr/bin/python3
"""Doc"""


def copy_list(a_list):
    """
    This function returns a shallow copy of the input list.

    Parameters:
    a_list (list): The list to be copied.

    Returns:
    list: A new list that is a copy of `a_list`.

    Note:
    This function creates a shallow copy of the list. If the original list contains mutable objects and those objects are changed, those changes will be reflected in the copied list.
    """
    return list(a_list)
