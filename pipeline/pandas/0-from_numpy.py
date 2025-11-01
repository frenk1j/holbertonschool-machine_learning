#!/usr/bin/env python3
"""Module that creates a pandas DataFrame from a numpy array."""

import pandas as pd


def from_numpy(array):
    """
    Creates a pandas DataFrame from a numpy ndarray.

    Args:
        array (np.ndarray): The numpy array to convert into a DataFrame.

    Returns:
        pd.DataFrame: DataFrame with columns labeled A, B, C, ...
        (up to 26 columns).
    """
    columns = [chr(65 + i) for i in range(array.shape[1])]
    df = pd.DataFrame(array, columns=columns)
    return df
