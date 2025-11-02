#!/usr/bin/env python3
"""
Sort and transpose a DataFrame
"""


def flip_switch(df):
    """
    Sorts the DataFrame in reverse chronological order
    and then transposes it.

    Args:
        df: pandas DataFrame to be transformed

    Returns:
        pd.DataFrame: transposed DataFrame after sorting
    """
    # Rendit të dhënat në rend kronologjik të kundërt
    df = df.sort_index(ascending=False)
    # Transpozon DataFrame-in (rreshtat bëhen kolona dhe anasjelltas)
    return df.transpose()
