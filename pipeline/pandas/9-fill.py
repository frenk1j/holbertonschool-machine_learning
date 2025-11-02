#!/usr/bin/env python3
"""
Clean and fill missing values in a DataFrame
"""


def fill(df):
    """
    Removes the 'Weighted_Price' column and fills missing values
    according to the specified rules.

    Args:
        df: pandas DataFrame with columns including
            'Open', 'High', 'Low', 'Close',
            'Volume_(BTC)', and 'Volume_(Currency)'

    Returns:
        pd.DataFrame: modified DataFrame
    """
    # 1. Heq kolonën 'Weighted_Price'
    df = df.drop(columns=['Weighted_Price'])

    # 2. Plotëson vlerat mungese te 'Close' me vlerën e mëparshme
    df['Close'] = df['Close'].fillna(method='ffill')

    # 3. Plotëson 'High', 'Low' dhe 'Open' me vlerën e 'Close' të rreshtit
    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])
    df['Open'] = df['Open'].fillna(df['Close'])

    # 4. Vendos 0 për vlerat mungese në 'Volume_(BTC)' dhe 'Volume_(Currency)'
    df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
    df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

    return df
