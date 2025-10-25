#!/usr/bin/env python3
"""Binomial distribution class"""


class Binomial:
    """Represents a Binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize the Binomial distribution
        Args:
            data (list): list of data to estimate the distribution
            n (int): number of Bernoulli trials
            p (float): probability of success
        """
        if data is None:
            # No data provided → use n and p directly
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            # Data provided → estimate n and p
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # Calculate mean and variance
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)

            # Estimate p and n
            p_est = 1 - (variance / mean)
            n_est = round(mean / p_est)
            p_est = mean / n_est

            self.n = int(n_est)
            self.p = float(p_est)
