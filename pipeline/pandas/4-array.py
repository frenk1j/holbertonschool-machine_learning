#!/usr/bin/env python3
"""
Convert specific DataFrame columns to a numpy.ndarray
"""

import numpy as np


def array(df):
    """
    Takes a pd.DataFrame and returns the last 10 rows
    of the 'High' and 'Close' columns as a numpy.ndarray

    Args:
        df: pandas DataFrame with columns 'High' and 'Close'

    Returns:
        numpy.ndarray: array containing last 10 rows of High and Close
    """
    return df[['High', 'Close']].tail(10).to_numpy()
