#!/usr/bin/env python3
"""
Module 11-the_western_exchange
Transposes a 2D matrix without loops, conditionals, or imports.
"""


def np_transpose(matrix):
    """Returns the transpose of a 2D matrix"""
    return list(map(list, zip(*matrix)))
