#!/usr/bin/env python3
"""
Remove rows with NaN values in the 'Close' column
"""


def prune(df):
    """
    Removes any entries where 'Close' has NaN values.

    Args:
        df: pandas DataFrame containing a 'Close' column

    Returns:
        pd.DataFrame: DataFrame without NaN values in 'Close'
    """
    # Heq të gjitha rreshtat ku 'Close' është NaN
    return df.dropna(subset=['Close'])
