#!/usr/bin/env python3
"""Maximization step for EM algorithm on GMM"""

import numpy as np


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
    probs = np.sum(g, axis=0)
    if not np.isclose(probs, np.ones(n)).all():
        return None, None, None

    pi = np.zeros((k,))
    m = np.zeros((k, d))
    S = np.zeros((k, d, d))

    for i in range(k):
        pi[i] = np.sum(g[i]) / n
        m[i] = np.matmul(g[i], X) / np.sum(g[i])
        S[i] = np.matmul(g[i] * (X - m[i]).T, X - m[i]) / np.sum(g[i])

    return pi, m, S
