#!/usr/bin/python3
"""A module to divide all elements of a matrix."""


def is_matrix(matrix):
    """
    Check if matrix is a valid list of lists of integers/floats.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        return False
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        return False
    return True


def validate_matrix(matrix):
    """
    Validate the matrix format.
    """
    if not is_matrix(matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div, rounded to 2 decimal places.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    validate_matrix(matrix)

    result = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        result.append(new_row)

    return result
