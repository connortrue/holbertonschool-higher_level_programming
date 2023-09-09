#!/usr/bin/python3
def square_matrix_simple(matrix):
    # Create an empty result matrix of the same size as the input matrix
    result = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    # Iterate over each row and column index of the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Compute the square of the element
            squared_element = matrix[i][j] ** 2
            # Store the squared element in the result matrix
            result[i][j] = squared_element

    # Return the result matrix
    return result
