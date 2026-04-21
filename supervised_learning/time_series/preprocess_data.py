#!/usr/bin/env python3
"""Preprocess BTC data from Coinbase and Bitstamp datasets."""

import numpy as np
import pandas as pd


def load_and_clean(filepath):
    """Load CSV and clean missing/NaN rows."""
    df = pd.read_csv(
        filepath,
        names=[
            'Timestamp', 'Open', 'High', 'Low', 'Close',
            'Volume_BTC', 'Volume_Currency', 'Weighted_Price'
        ]
    )
    # Drop header row if present
    df = df[df['Timestamp'] != 'Timestamp']
    df['Timestamp'] = pd.to_numeric(df['Timestamp'], errors='coerce')
    df = df.dropna(subset=['Timestamp'])
    df['Timestamp'] = df['Timestamp'].astype(int)

    # Replace NaN strings and drop rows with missing close price
    df.replace('NaN', np.nan, inplace=True)
    df = df.astype(float)
    df = df[df['Timestamp'] != 0]

    # Forward-fill missing values
    df.sort_values('Timestamp', inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.fillna(method='ffill', inplace=True)
    df.dropna(inplace=True)

    return df


def merge_datasets(cb_path, bs_path):
    """Merge Coinbase and Bitstamp datasets by timestamp."""
    df_cb = load_and_clean(cb_path)
    df_bs = load_and_clean(bs_path)

    # Merge on Timestamp, average overlapping values
    merged = pd.merge(
        df_cb, df_bs,
        on='Timestamp',
        suffixes=('_cb', '_bs'),
        how='outer'
    )
    merged.sort_values('Timestamp', inplace=True)
    merged.reset_index(drop=True, inplace=True)

    # Average the two sources where both exist
    for col in ['Open', 'High', 'Low', 'Close',
                'Volume_BTC', 'Volume_Currency', 'Weighted_Price']:
        col_cb = col + '_cb'
        col_bs = col + '_bs'
        merged[col] = merged[[col_cb, col_bs]].mean(axis=1)
        merged.drop([col_cb, col_bs], axis=1, inplace=True)

    merged.fillna(method='ffill', inplace=True)
    merged.dropna(inplace=True)

    return merged


def preprocess(cb_path='coinbase.csv', bs_path='bitstamp.csv',
               output_path='btc_preprocessed.npz'):
    """Full preprocessing pipeline."""
    print("Loading and merging datasets...")
    df = merge_datasets(cb_path, bs_path)

    # Use only Close price for forecasting (univariate)
    # Could also use [Open, High, Low, Close, Volume_BTC]
    features = ['Close']
    data = df[features].values.astype(np.float32)

    # Min-max normalization
    data_min = data.min(axis=0)
    data_max = data.max(axis=0)
    data_norm = (data - data_min) / (data_max - data_min + 1e-8)

    print(f"Total timesteps: {len(data_norm)}")
    print(f"Features: {features}")
    print(f"Close price range: [{data_min[0]:.2f}, {data_max[0]:.2f}]")

    # Save preprocessed data and normalization params
    np.savez(
        output_path,
        data=data_norm,
        data_min=data_min,
        data_max=data_max,
        features=np.array(features)
    )
    print(f"Saved preprocessed data to {output_path}")

    return data_norm, data_min, data_max


if __name__ == '__main__':
    preprocess()
