#!/usr/bin/env python3
"""
Concatenate two DataFrames and reorder MultiIndex hierarchy
"""

import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """
    Rearranges the MultiIndex so that Timestamp is the first level,
    concatenates the bitstamp and coinbase tables between timestamps
    1417411980 and 1417417980 inclusive, and ensures chronological order.

    Args:
        df1: pandas DataFrame (coinbase)
        df2: pandas DataFrame (bitstamp)

    Returns:
        pd.DataFrame: concatenated DataFrame with reordered MultiIndex
    """
    # Vendos 'Timestamp' si index për të dy DataFrames
    df1 = index(df1)
    df2 = index(df2)

    # Merr vetëm timestamp-et e kërkuara
    df1 = df1.loc[1417411980:1417417980]
    df2 = df2.loc[1417411980:1417417980]

    # Bashkon të dhënat me çelësa për secilin burim
    df = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])

    # Ndërron rendin e niveleve të MultiIndex që 'Timestamp' të jetë i pari
    df = df.reorder_levels(['Timestamp', None])

    # Sigurohet që të dhënat janë në rend kronologjik
    df = df.sort_index()

    return df
