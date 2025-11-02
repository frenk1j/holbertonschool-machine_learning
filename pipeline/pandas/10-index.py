#!/usr/bin/env python3
"""
Set the 'Timestamp' column as the index of a DataFrame
"""


def index(df):
    """
    Sets the 'Timestamp' column as the index of the DataFrame.

    Args:
        df: pandas DataFrame containing a 'Timestamp' column

    Returns:
        pd.DataFrame: modified DataFrame with 'Timestamp' as index
    """
    # Vendos kolonën 'Timestamp' si indeks
    return df.set_index('Timestamp')
