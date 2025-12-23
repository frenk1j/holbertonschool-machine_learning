#!/usr/bin/env python3
"""
0-initialize.py
Initializes cluster centroids for K-means
"""

import numpy as np


def initialize(X, k):
    """
    Initializes cluster centroids using a multivariate uniform distribution.

    Parameters:
    X (numpy.ndarray): Dataset of shape (n, d)
    k (int): Number of clusters

    Returns:
    numpy.ndarray: Initialized centroids of shape (k, d) or None on failure
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None
    if not isinstance(k, int) or k <= 0:
        return None
    if k > X.shape[0]:
        return None

    min_vals = np.min(X, axis=0)
    max_vals = np.max(X, axis=0)

    return np.random.uniform(min_vals, max_vals, size=(k, X.shape[1]))
