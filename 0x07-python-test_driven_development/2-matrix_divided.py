#!/usr/bin/python3
"""Matrix division

This module contains only one function to divide a matrix.

Example:
   matrix_divided([[2, 4, 6], [8, 10, 12]], 2)
    should give the result [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]

"""


def matrix_divided(matrix, div):
    """Divides a matrix by a number.

    Args:
        matrix (List of lists): The matrix that will be divided.
        div (int or float): Number to divide the matrix (not 0).
    Returns:
        new (List of lists): The result of dividing the matrix by the number.

    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or not matrix:
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    length = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
        length.append(len(row))
    if not len(set(length)) <= 1:
        raise TypeError("Each row of the matrix must have the same size")
    new = []
    temp = []
    for row in matrix:
        for elem in row:
            temp.append(round(elem / div, 2))
        new.append(temp.copy())
        temp.clear()
    return new
