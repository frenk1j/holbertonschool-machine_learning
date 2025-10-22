#!/usr/bin/env python3
"""Calculates the integral of a polynomial"""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial"""
    if (not isinstance(poly, list) or
            len(poly) == 0 or
            not all(isinstance(x, (int, float)) for x in poly) or
            not isinstance(C, (int, float))):
        return None

    # fillojmë me konstanten C
    integral = [C]

    # për çdo element të poly, ndajmë me (index + 1)
    for i in range(len(poly)):
        value = poly[i] / (i + 1)
        # ktheje në int nëse është numër i plotë
        if value.is_integer():
            value = int(value)
        integral.append(value)

    # hiq zerot e panevojshme në fund
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
