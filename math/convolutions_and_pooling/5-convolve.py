#!/usr/bin/env python3
"""
Performs convolution on images using multiple kernels
"""

import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """
    Performs a convolution on images using multiple kernels

    Parameters:
    images (numpy.ndarray): shape (m, h, w, c)
    kernels (numpy.ndarray): shape (kh, kw, c, nc)
    padding (tuple, str): 'same', 'valid', or (ph, pw)
    stride (tuple): (sh, sw)

    Returns:
    numpy.ndarray: convolved images (m, h_out, w_out, nc)
    """
    m, h, w, c = images.shape
    kh, kw, kc, nc = kernels.shape
    sh, sw = stride

    if kc != c:
        raise ValueError("Kernel channels must match image channels")

    # Determine padding
    if padding == 'same':
        ph = ((h - 1) * sh + kh - h) // 2 + 1 * (
            ((h - 1) * sh + kh - h) % 2 != 0
        )
        pw = ((w - 1) * sw + kw - w) // 2 + 1 * (
            ((w - 1) * sw + kw - w) % 2 != 0
        )
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding

    # Pad images
    padded_images = np.pad(
        images,
        pad_width=((0, 0), (ph, ph), (pw, pw), (0, 0)),
        mode='constant'
    )

    # Output dimensions
    output_h = (h + 2 * ph - kh) // sh + 1
    output_w = (w + 2 * pw - kw) // sw + 1
    output = np.zeros((m, output_h, output_w, nc))

    # Convolve each kernel
    for i in range(output_h):
        for j in range(output_w):
            h_start = i * sh
            w_start = j * sw
            region = padded_images[
                :, h_start:h_start + kh, w_start:w_start + kw, :
            ]
            for k in range(nc):
                output[:, i, j, k] = np.sum(
                    region * kernels[:, :, :, k], axis=(1, 2, 3)
                )

    return output
