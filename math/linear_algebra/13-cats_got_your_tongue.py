#!/usr/bin/env python3
"""
Module 13-cats_got_your_tongue
Concatenates two numpy arrays along a specified axis without loops.
"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Return a new numpy.ndarray concatenating mat1 and mat2"""
    return np.concatenate((mat1, mat2), axis=axis)
