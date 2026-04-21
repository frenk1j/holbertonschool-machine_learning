#!/usr/bin/env python3
"""Forecast BTC price using an RNN (LSTM) model with Keras."""

import numpy as np
import tensorflow as tf
from tensorflow import keras


# Constants
WINDOW_SIZE = 24 * 60   # past 24 hours in 60-second intervals
BATCH_SIZE = 64
EPOCHS = 10
TRAIN_SPLIT = 0.8
DATA_PATH = 'btc_preprocessed.npz'


def load_data(path=DATA_PATH):
    """Load preprocessed BTC data."""
    npz = np.load(path, allow_pickle=True)
    data = npz['data']
    data_min = npz['data_min']
    data_max = npz['data_max']
    return data, data_min, data_max


def make_dataset(data, window_size=WINDOW_SIZE, batch_size=BATCH_SIZE,
                 shuffle=False):
    """Create a tf.data.Dataset of (window, label) pairs.

    Each sample uses `window_size` timesteps to predict
    the Close price of the next timestep.
    """
    # Total length needed: window + 1 target step
    total_size = window_size + 1

    dataset = tf.data.Dataset.from_tensor_slices(data)
    dataset = dataset.window(total_size, shift=1, drop_remainder=True)
    dataset = dataset.flat_map(
        lambda w: w.batch(total_size, drop_remainder=True)
    )

    # Split window into features and label
    dataset = dataset.map(
        lambda w: (w[:-1], w[-1, 0]),
        num_parallel_calls=tf.data.AUTOTUNE
    )

    if shuffle:
        dataset = dataset.shuffle(buffer_size=10000)

    dataset = dataset.batch(batch_size).prefetch(tf.data.AUTOTUNE)
    return dataset


def build_model(window_size=WINDOW_SIZE, n_features=1):
    """Build LSTM-based RNN model."""
    model = keras.Sequential([
        keras.layers.Input(shape=(window_size, n_features)),
        keras.layers.LSTM(64, return_sequences=True),
        keras.layers.Dropout(0.2),
        keras.layers.LSTM(32, return_sequences=False),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dense(1)
    ])

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=1e-3),
        loss='mse',
        metrics=['mae']
    )
    return model


def train_and_validate():
    """Main training and validation routine."""
    print("Loading data...")
    data, data_min, data_max = load_data()
    n_features = data.shape[1]

    # Train/validation split
    split_idx = int(len(data) * TRAIN_SPLIT)
    train_data = data[:split_idx]
    val_data = data[split_idx:]

    print(f"Train samples: {len(train_data)}, Val samples: {len(val_data)}")

    train_ds = make_dataset(train_data, shuffle=True)
    val_ds = make_dataset(val_data, shuffle=False)

    print("Building model...")
    model = build_model(WINDOW_SIZE, n_features)
    model.summary()

    callbacks = [
        keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=3,
            restore_best_weights=True
        ),
        keras.callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=2
        )
    ]

    print("Training model...")
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=EPOCHS,
        callbacks=callbacks
    )

    # Evaluate on validation set
    val_loss, val_mae = model.evaluate(val_ds)
    price_range = float(data_max[0] - data_min[0])
    val_rmse_usd = np.sqrt(val_loss) * price_range
    val_mae_usd = val_mae * price_range

    print(f"\nValidation MSE (normalized): {val_loss:.6f}")
    print(f"Validation RMSE (USD):       ${val_rmse_usd:.2f}")
    print(f"Validation MAE  (USD):       ${val_mae_usd:.2f}")

    model.save('btc_model.keras')
    print("Model saved to btc_model.keras")

    return model, history


if __name__ == '__main__':
    train_and_validate()
