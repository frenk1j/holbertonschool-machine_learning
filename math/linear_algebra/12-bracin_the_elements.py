#!/usr/bin/env python3
"""
Module 12-bracin_the_elements
Performs element-wise addition, subtraction, multiplication,
and division on two numpy arrays or array-like objects.
"""


def np_elementwise(mat1, mat2):
    """Return a tuple: element-wise sum, difference, product, and quotient"""
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
