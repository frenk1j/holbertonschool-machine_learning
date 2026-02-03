#!/usr/bin/env python3
"""
Learning rate decay using inverse time decay (stepwise)
"""
import numpy as np


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """
    Updates the learning rate using inverse time decay in a stepwise fashion

    alpha: original learning rate
    decay_rate: decay rate
    global_step: number of gradient descent steps elapsed
    decay_step: number of steps before decay is applied

    Returns: updated learning rate
    """
    return alpha / (1 + decay_rate * (global_step // decay_step))
