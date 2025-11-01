#!/usr/bin/env python3
"""
3-rename.py
Renames the 'Timestamp' column to 'Datetime', converts it to datetime,
and keeps only 'Datetime' and 'Close' columns.
"""

import pandas as pd


def rename(df):
    """
    Renames the 'Timestamp' column to 'Datetime',
    converts it to datetime format, and keeps only 'Datetime' and 'Close'.

    Args:
        df (pd.DataFrame): DataFrame containing a 'Timestamp' column.

    Returns:
        pd.DataFrame: Modified DataFrame with 'Datetime' and 'Close' columns.
    """
    # Rename the column
    df = df.rename(columns={'Timestamp': 'Datetime'})
    # Convert timestamp to datetime
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')
    # Keep only Datetime and Close columns
    df = df[['Datetime', 'Close']]
    return df
