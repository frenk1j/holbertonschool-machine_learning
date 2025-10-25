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
        """Calculates the z-score of a given x-value
        Args:
            x (float): x-value
        Returns:
            float: z-score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score
        Args:
            z (float): z-score
        Returns:
            float: x-value corresponding to z
        """
        return (z * self.stddev) + self.mean
