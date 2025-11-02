#!/usr/bin/env python3
"""
Sort a DataFrame by the 'High' column in descending order
"""


def high(df):
    """
    Sorts the DataFrame by the 'High' price in descending order.

    Args:
        df: pandas DataFrame containing a 'High' column

    Returns:
        pd.DataFrame: sorted DataFrame
    """
    # Rendit sipas kolonës 'High' në mënyrë zbritëse
    return df.sort_values(by='High', ascending=False)
