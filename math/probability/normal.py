#!/usr/bin/env python3
"""Normal distribution class"""


class Normal:
    """Represents a normal (Gaussian) distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize the Normal distribution
        Args:
            data (list): list of data to estimate the distribution
            mean (float): the mean of the distribution
            stddev (float): the standard deviation of the distribution
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # Calculate mean
            self.mean = float(sum(data) / len(data))

            # Calculate standard deviation
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = float(variance ** 0.5)

    def z_score(self, x):
        """Calculates the z-score of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score"""
        return (z * self.stddev) + self.mean

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value"""
        pi = 3.1415926536
        e = 2.7182818285
        coeff = 1 / (self.stddev * ((2 * pi) ** 0.5))
        exponent = e ** (-0.5 * ((x - self.mean) / self.stddev) ** 2)
        return coeff * exponent

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value
        Args:
            x (float): x-value
        Returns:
            float: CDF value for x
        """
        # Formula using the error function approximation
        pi = 3.1415926536
        z = (x - self.mean) / (self.stddev * (2 ** 0.5))
        # Approximation for error function erf(z)
        erf = (2 / (pi ** 0.5)) * (
            z - (z ** 3) / 3 + (z ** 5) / 10 - (z ** 7) / 42 + (z ** 9) / 216
        )
        return 0.5 * (1 + erf)
