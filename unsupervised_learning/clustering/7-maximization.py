#!/usr/bin/env python3
"""Maximization step for EM algorithm on GMM"""

import numpy as np
kmeans = __import__('1-kmeans').kmeans

def maximization(X, g):
    """Calculates the maximization step in the EM algorithm for a GMM"""
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None
    if not isinstance(g, np.ndarray) or len(g.shape) != 2:
        return None, None, None
    if X.shape[0] != g.shape[1]:
        return None, None, None

    n, d = X.shape
    k = g.shape[0]

    # Validate probabilities sum to 1 for each point
    if not np.isclose(np.sum(g, axis=0), np.ones(n)).all():
        return None, None, None

    pi = np.sum(g, axis=1) / n            # shape (k,)
    m = np.dot(g, X) / np.sum(g, axis=1)[:, np.newaxis]  # shape (k,d)

    S = np.zeros((k, d, d))
    for i in range(k):  # Only one loop allowed
        X_centered = X - m[i]
        S[i] = (g[i][:, np.newaxis] * X_centered).T @ X_centered / np.sum(g[i])

    return pi, m, S
