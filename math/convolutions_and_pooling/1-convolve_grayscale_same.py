#!/usr/bin/env python3
"""
Performs a same convolution on grayscale images
"""

import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    Performs a same convolution on grayscale images

    Parameters:
    images (numpy.ndarray): shape (m, h, w)
    kernel (numpy.ndarray): shape (kh, kw)

    Returns:
    numpy.ndarray: convolved images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    ph = kh // 2
    pw = kw // 2

    padded_images = np.pad(
        images,
        pad_width=((0, 0), (ph, ph), (pw, pw)),
        mode='constant'
    )

    output = np.zeros((m, h, w))

    for i in range(h):
        for j in range(w):
            region = padded_images[:, i:i + kh, j:j + kw]
            output[:, i, j] = np.sum(region * kernel, axis=(1, 2))

    return output
