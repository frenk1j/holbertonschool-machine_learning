#!/usr/bin/env python3
"""
Module 8-ridin_bareback
Performs matrix multiplication between two 2D matrices.
"""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication between two 2D matrices"""
    # Kontrollojmë nëse numri i kolonave në mat1
    # është i barabartë me rreshtat e mat2
    if len(mat1[0]) != len(mat2):
        return None

    result = []
    for i in range(len(mat1)):  # për çdo rresht në mat1
        row = []
        for j in range(len(mat2[0])):  # për çdo kolonë në mat2
            value = sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2)))
            row.append(value)
        result.append(row)

    return result
