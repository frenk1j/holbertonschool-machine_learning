# BTC Price Forecasting with RNNs

## Overview

This project uses a Recurrent Neural Network (LSTM) to forecast Bitcoin (BTC)
closing prices using historical minute-level data from Coinbase and Bitstamp.

## Files

| File | Description |
|---|---|
| `preprocess_data.py` | Merges, cleans, and normalizes raw CSV datasets |
| `forecast_btc.py` | Builds, trains, and validates the LSTM model |

## Dataset

Raw CSV files (`coinbase.csv`, `bitstamp.csv`) with 60-second OHLCV windows:

- **Timestamp** – Unix time at start of window
- **Open** – Opening price (USD)
- **High** – Highest price (USD)
- **Low** – Lowest price (USD)
- **Close** – Closing price (USD)
- **Volume_BTC** – BTC volume transacted
- **Volume_Currency** – USD volume transacted
- **Weighted_Price** – VWAP (USD)

## Preprocessing (`preprocess_data.py`)

1. Loads both CSV files, drops corrupt/NaN rows
2. Merges by `Timestamp`, averaging overlapping values
3. Forward-fills remaining gaps
4. Uses **Close price** as the target feature
5. Applies **min-max normalization** (range [0, 1])
6. Saves to `btc_preprocessed.npz`

## Model (`forecast_btc.py`)

### Architecture

```
Input: (batch, 1440, 1)   ← 24 hours × 60 min/hr
  └─ LSTM(64, return_sequences=True)
  └─ Dropout(0.2)
  └─ LSTM(32)
  └─ Dropout(0.2)
  └─ Dense(16, relu)
  └─ Dense(1)             ← predicted Close price (normalized)
```

### Training Details

| Parameter | Value |
|---|---|
| Window size | 1440 timesteps (24 hours) |
| Prediction target | Close price at t+1 (next hour ≈ 60 min) |
| Loss function | Mean Squared Error (MSE) |
| Optimizer | Adam (lr=1e-3) |
| Batch size | 64 |
| Max epochs | 10 |
| Train/Val split | 80% / 20% |

### Data Pipeline

Uses `tf.data.Dataset` with:
- Sliding windows of size 1441 (1440 input + 1 target)
- Shuffling on training set
- Prefetching for performance

## Usage

```bash
# Step 1: Preprocess raw data
python3 preprocess_data.py

# Step 2: Train and validate model
python3 forecast_btc.py
```

## Dependencies

- Python 3.8+
- TensorFlow 2.x
- NumPy
- Pandas
