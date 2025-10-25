#!/usr/bin/env python3
"""Exponential distribution class"""


class Exponential:
    """Represents an exponential distribution"""

    def __init__(self, data=None, lambtha=1.):
        """Initialize the Exponential distribution
        Args:
            data (list): list of data to estimate the distribution
            lambtha (float): expected number of occurrences per time unit
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # lambtha = 1 / mean of data
            mean = sum(data) / len(data)
            self.lambtha = float(1 / mean)
