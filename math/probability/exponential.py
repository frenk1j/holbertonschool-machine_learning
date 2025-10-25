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
            mean = sum(data) / len(data)
            self.lambtha = float(1 / mean)

    def pdf(self, x):
        """Calculates the value of the PDF for a given time period
        Args:
            x (float): the time period
        Returns:
            float: PDF value for x, or 0 if x < 0
        """
        if x < 0:
            return 0

        # Formula: f(x) = λ * e^(-λx)
        e = 2.7182818285  # approximate value of e
        pdf_value = self.lambtha * (e ** (-self.lambtha * x))
        return pdf_value
