#!/usr/bin/env python3
"""13-analyze.py
Computes descriptive statistics for all columns except Timestamp
"""


def analyze(df):
    """Compute descriptive statistics for all columns except 'Timestamp'

    Args:
        df (pd.DataFrame): input dataframe

    Returns:
        pd.DataFrame: dataframe with statistics
    """
    # Exclude 'Timestamp' column if it exists
    if 'Timestamp' in df.columns:
        df = df.drop(columns=['Timestamp'])

    # Compute descriptive statistics
    stats = df.describe()

    return stats
