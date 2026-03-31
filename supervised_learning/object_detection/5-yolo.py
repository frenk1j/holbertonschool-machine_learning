#!/usr/bin/env python3
"""Module for YOLO v3 object detection - Task 5: Preprocess Images."""

import cv2
import numpy as np


class Yolo:
    """Class that uses the Yolo v3 algorithm to perform object detection."""

    def preprocess_images(self, images):
        """Preprocess images for input to the Darknet model.

        Resizes images with inter-cubic interpolation and rescales pixel
        values to the range [0, 1].

        Args:
            images: list of images as numpy.ndarrays

        Returns:
            tuple of (pimages, image_shapes):
                pimages: numpy.ndarray of shape (ni, input_h, input_w, 3)
                image_shapes: numpy.ndarray of shape (ni, 2)
        """
        input_h = int(self.model.input.shape[1])
        input_w = int(self.model.input.shape[2])

        pimages = []
        image_shapes = []

        for image in images:
            image_shapes.append(image.shape[:2])

            resized = cv2.resize(
                image,
                (input_w, input_h),
                interpolation=cv2.INTER_CUBIC
            )

            resized = resized[..., ::-1]
            resized = resized / 255.0

            pimages.append(resized)

        pimages = np.array(pimages, dtype=np.float32)
        image_shapes = np.array(image_shapes)

        return pimages, image_shapes
