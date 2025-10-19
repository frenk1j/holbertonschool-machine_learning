#!/usr/bin/env python3
"""
Module 11-the_western_exchange
Transposes a matrix without importing any module.
"""


def np_transpose(matrix):
    """Returns the transpose of a matrix"""
    try:
        return [
            [matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))
        ]
    except (TypeError, IndexError):
        return matrix
