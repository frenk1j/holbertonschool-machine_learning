#!/usr/bin/env python3
import pandas as pd


def from_numpy(array):
    """
    Creates a pandas DataFrame from a numpy ndarray.

    Args:
        array (np.ndarray): The numpy array to convert.

    Returns:
        pd.DataFrame: DataFrame with columns labeled A, B, C, ..., Z.
    """
    # Generate column names: 'A', 'B', 'C', ...
    columns = [chr(65 + i) for i in range(array.shape[1])]
    # Create the DataFrame
    df = pd.DataFrame(array, columns=columns)
    return df
