#!/usr/bin/env python3
"""
Slice specific columns and rows from a DataFrame
"""


def slice(df):
    """
    Extracts specific columns and selects every 60th row

    Args:
        df: pandas DataFrame with columns
            'High', 'Low', 'Close', and 'Volume_(BTC)'

    Returns:
        pd.DataFrame: sliced DataFrame containing the selected columns
        and every 60th row
    """
    # Zgjedh kolonat e kërkuara
    df = df[['High', 'Low', 'Close', 'Volume_(BTC)']]
    # Merr çdo të 60-tin rresht
    return df.iloc[::60]
