#!/usr/bin/env python3
"""Optimum K method aka inversed elbow"""

import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """Optimal K method using variance (inversed elbow)"""
    try:
        if not isinstance(X, np.ndarray) or len(X.shape) != 2:
            return None, None
        if not isinstance(iterations, int) or iterations < 1:
            return None, None
        if kmax is not None and (not isinstance(kmax, int) or kmax < 1):
            return None, None
        if kmax is not None and kmin >= kmax:
            return None, None
        if kmax is None:
            kmax = X.shape[0]
        if not isinstance(kmin, int) or kmin < 1 or kmin >= X.shape[0]:
            return None, None

        results = []
        d_vars = []
        for k in range(kmin, kmax + 1):
            clusters, clss = kmeans(X, k, iterations)
            results.append((clusters, clss))

            var_current = variance(X, clusters)
            if k == kmin:
                var_base = var_current
            d_vars.append(var_base - var_current)

        return results, d_vars

    except Exception:
        return None, None
