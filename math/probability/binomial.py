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
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)

            p_est = 1 - (variance / mean)
            n_est = round(mean / p_est)
            p_est = mean / n_est

            self.n = int(n_est)
            self.p = float(p_est)

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of 'successes'
        Args:
            k (int): number of successes
        Returns:
            float: PMF value for k, or 0 if k is out of range
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0 or k > self.n:
            return 0

        def factorial(num):
            """Helper to calculate factorial"""
            if num == 0 or num == 1:
                return 1
            result = 1
            for i in range(2, num + 1):
                result *= i
            return result

        nCk = factorial(self.n) / (factorial(k) * factorial(self.n - k))
        pmf_value = nCk * (self.p ** k) * ((1 - self.p) ** (self.n - k))
        return pmf_value

    def cdf(self, k):
        """Calculates the value of the CDF for a given number of 'successes'
        Args:
            k (int): number of successes
        Returns:
            float: CDF value for k, or 0 if k is out of range
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        if k > self.n:
            k = self.n

        # Sum of PMF values from 0 to k
        cdf_value = 0
        for i in range(k + 1):
            cdf_value += self.pmf(i)
        return cdf_value
