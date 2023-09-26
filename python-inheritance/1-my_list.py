#!/usr/bin/python3
"""MyList is a custom list class that provides additional functionality,
such as printing the list elements sorted."""


class MyList(list):
    """
    MyList is a custom list class that provides additional functionality,
    such as printing the list elements sorted.
    """

    def print_sorted(self):
        """
        Prints the sorted elements of the list.
        """
        print(sorted(list(self)))
