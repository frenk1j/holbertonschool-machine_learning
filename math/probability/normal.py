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
