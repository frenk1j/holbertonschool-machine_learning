#!/usr/bin/env python3
"""
9-sum_total.py
Module to calculate the sum of squares from 1 to n without using loops.
"""


def summation_i_squared(n):
    """
    Calculate the sum of squares from 1 to n.

    Args:
        n (int): The stopping number (must be a positive integer).

    Returns:
        int: The sum of squares from 1 to n.
        None: If n is not a valid positive integer.
    """
    if not isinstance(n, int) or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
