#!/usr/bin/python3
"""Lazy matrix multiplication.

This module contains just one function to multiply two matrices.

Example:
    lazy_matrix_mul([[1, 2]], [[1, 1], [2, 1]])
    Should return [[5, 3]]
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This function multiplies two matrices using numpy.

    Args:
        m_a (List of lists): First matrix.
        m_b (List of lists): Second matrix.

    Returns:
        (Matrix): Result of the multiplication of the two matrices.

    """

    return (np.matmul(m_a, m_b))
