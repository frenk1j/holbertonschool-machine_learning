#!/usr/bin/env python3
"""Bayesian Information Criterion Module"""
import numpy as np
expectation_maximization = __import__('8-EM').expectation_maximization


def BIC(X, kmin=1, kmax=None, iterations=1000, tol=1e-5, verbose=False):
    """Finds the best number of clusters for a GMM using BIC"""
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None, None
    if not isinstance(kmin, int) or kmin <= 0:
        return None, None, None, None
    n, d = X.shape
    if kmax is None:
        kmax = n
    if not isinstance(kmax, int) or kmax < kmin:
        return None, None, None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None, None, None
    if not isinstance(tol, float) or tol < 0:
        return None, None, None, None
    if not isinstance(verbose, bool):
        return None, None, None, None

    k_values = list(range(kmin, kmax + 1))
    results_history = []
    lh_history = []
    bic_history = []

    for k in k_values:
        pi, m, S, g, lh = expectation_maximization(
            X, k, iterations=iterations, tol=tol, verbose=verbose
        )

        if pi is None or m is None or S is None or g is None or lh is None:
            return None, None, None, None

        # Number of parameters for GMM:
        # (k-1) priors + k*d means + k*d*(d+1)/2 covariances
        p = (k - 1) + k * d + k * d * (d + 1) / 2
        bic_value = p * np.log(n) - 2 * lh

        results_history.append((pi, m, S))
        lh_history.append(lh)
        bic_history.append(bic_value)

    min_bic_index = np.argmin(bic_history)
    best_k = k_values[min_bic_index]
    best_result = results_history[min_bic_index]

    return best_k, best_result, np.array(lh_history), np.array(bic_history)
