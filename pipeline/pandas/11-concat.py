#!/usr/bin/env python3
"""
Concatenate two DataFrames with labeled keys
"""


def concat(df1, df2):
    """
    Indexes both DataFrames on 'Timestamp',
    selects rows from df2 up to timestamp 1417411920,
    concatenates them on top of df1,
    and labels the sources as 'bitstamp' and 'coinbase'.

    Args:
        df1: pandas DataFrame (coinbase)
        df2: pandas DataFrame (bitstamp)

    Returns:
        pd.DataFrame: concatenated DataFrame with hierarchical index
    """
    index = __import__('10-index').index

    # Vendos 'Timestamp' si index për të dy DataFrames
    df1 = index(df1)
    df2 = index(df2)

    # Merr vetëm rreshtat nga df2 me Timestamp <= 1417411920
    df2 = df2.loc[:1417411920]

    # Bashkon të dhënat, me çelësa për secilin burim
    return df2.append(df1, keys=['bitstamp', 'coinbase'])
