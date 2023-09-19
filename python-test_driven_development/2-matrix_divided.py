#!/usr/bin/python3
# 2-matrix_divided.py
# Connor True
"""Doc"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Parameters:
    matrix (list of lists of int or float): The matrix to be divided.
    div (int or float): The divisor.

    Returns:
    list of lists of float: The divided matrix with elements rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a matrix of integers or floats, or if div is not a number.
    ZeroDivisionError: If div is equal to 0.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(element / div, 2) for element in row] for row in matrix]
    return result
