#!/usr/bin/python3
"""Doc"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n

    Parameters:
    n (int): The number of rows in the Pascal's triangle

    Returns:
    list: A list of lists representing the Pascal's triangle
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        last_row = triangle[i - 1]
        row += [last_row[j] + last_row[j + 1] for
                j in range(len(last_row) - 1)]
        row.append(1)
        triangle.append(row)

    return triangle
