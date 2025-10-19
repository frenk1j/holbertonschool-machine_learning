#!/usr/bin/env python3
"""
Module 11-the_western_exchange
Transposes a numpy.ndarray without loops or conditionals.
"""


def np_transpose(matrix):
    """Returns a new numpy.ndarray which is the transpose of the input matrix"""
    return matrix.T.copy()
