#!/usr/bin/env python3
"""
Module 11-the_western_exchange
Transposes a numpy.ndarray without loops or conditionals.
"""


def np_transpose(matrix):
    """Return a new numpy.ndarray which is the transpose of the input"""
    return matrix.T.copy()
