#!/usr/bin/env python3
"""
Learning rate decay using inverse time decay (TensorFlow)
"""
import tensorflow as tf


def learning_rate_decay(alpha, decay_rate, decay_step):
    """
    Creates a learning rate decay operation using inverse time decay

    alpha: original learning rate
    decay_rate: decay rate
    decay_step: number of steps before decay is applied

    Returns: a learning rate decay operation
    """
    return tf.keras.optimizers.schedules.InverseTimeDecay(
        initial_learning_rate=alpha,
        decay_steps=decay_step,
        decay_rate=decay_rate,
        staircase=True
    )
