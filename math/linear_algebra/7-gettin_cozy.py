#!/usr/bin/env python3
def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two 2D matrices along a specific axis"""
    # Kontrollo që janë 2D
    if not mat1 or not mat2:
        return None

    # Për concatenation vertikal (axis=0)
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    # Për concatenation horizontal (axis=1)
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [r1[:] + r2[:] for r1, r2 in zip(mat1, mat2)]

    # Nëse axis nuk është valid
    return None
