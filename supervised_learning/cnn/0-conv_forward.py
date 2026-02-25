#!/usr/bin/env python3
"""
Module for convolutional forward propagation.
"""
import numpy as np


def conv_forward(A_prev, W, b, activation, padding="same", stride=(1, 1)):
    """
    Performs forward propagation over a convolutional layer of a neural
    network.

    Args:
        A_prev: numpy.ndarray of shape (m, h_prev, w_prev, c_prev) containing
                the output of the previous layer
        W: numpy.ndarray of shape (kh, kw, c_prev, c_new) containing the
           kernels for the convolution
        b: numpy.ndarray of shape (1, 1, 1, c_new) containing the biases
           applied to the convolution
        activation: activation function applied to the convolution
        padding: string that is either 'same' or 'valid'
        stride: tuple of (sh, sw) containing the strides for the convolution

    Returns:
        The output of the convolutional layer
    """
    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw, _, c_new = W.shape
    sh, sw = stride

    if padding == 'same':
        h_new = int(np.ceil(h_prev / sh))
        w_new = int(np.ceil(w_prev / sw))

        ph_total = max((h_new - 1) * sh + kh - h_prev, 0)
        pw_total = max((w_new - 1) * sw + kw - w_prev, 0)

        ph_top = ph_total // 2
        ph_bottom = ph_total - ph_top
        pw_left = pw_total // 2
        pw_right = pw_total - pw_left
    else:  # valid
        h_new = (h_prev - kh) // sh + 1
        w_new = (w_prev - kw) // sw + 1
        ph_top = ph_bottom = pw_left = pw_right = 0

    A_prev_padded = np.pad(
        A_prev,
        ((0, 0), (ph_top, ph_bottom), (pw_left, pw_right), (0, 0)),
        mode='constant',
        constant_values=0
    )

    output = np.zeros((m, h_new, w_new, c_new))

    for i in range(h_new):
        for j in range(w_new):
            for k in range(c_new):
                h_start = i * sh
                w_start = j * sw
                region = A_prev_padded[:, h_start:h_start+kh,
                                       w_start:w_start+kw, :]
                output[:, i, j, k] = np.sum(region * W[:, :, :, k],
                                            axis=(1, 2, 3))

    return activation(output + b)
