#!/usr/bin/env python3
"""
1-kmeans.py
Performs K-means clustering on a dataset
"""

import numpy as np


def initialize(X, k):
    """
    Initializes centroids using a multivariate uniform distribution.

    Parameters:
    X (numpy.ndarray): Dataset of shape (n, d)
    k (int): Number of clusters

    Returns:
    numpy.ndarray: Initialized centroids of shape (k, d)
    """
    min_vals = np.min(X, axis=0)
    max_vals = np.max(X, axis=0)
    return np.random.uniform(min_vals, max_vals, size=(k, X.shape[1]))


def kmeans(X, k, iterations=1000):
    """
    Performs K-means clustering.

    Parameters:
    X (numpy.ndarray): Dataset of shape (n, d)
    k (int): Number of clusters
    iterations (int): Maximum number of iterations

    Returns:
    tuple:
        - C (numpy.ndarray): Centroids, shape (k, d)
        - clss (numpy.ndarray): Cluster index for each data point, shape (n,)
        Returns (None, None) on failure
    """
    if (not isinstance(X, np.ndarray) or X.ndim != 2
            or not isinstance(k, int) or k <= 0
            or not isinstance(iterations, int) or iterations <= 0):
        return None, None

    n, d = X.shape
    C = initialize(X, k)
    clss = np.zeros(n, dtype=int)

    for _ in range(iterations):
        old_C = C.copy()
        # Compute distances and assign clusters
        dist = np.linalg.norm(X[:, np.newaxis] - C, axis=2)
        clss = np.argmin(dist, axis=1)

        # Update centroids
        for i in range(k):
            points = X[clss == i]
            if len(points) == 0:
                # Reinitialize empty cluster centroid
                C[i] = np.random.uniform(np.min(X, axis=0), np.max(X, axis=0))
            else:
                C[i] = points.mean(axis=0)

        # Early stopping if centroids do not change
        if np.allclose(C, old_C):
            break

    return C, clss
