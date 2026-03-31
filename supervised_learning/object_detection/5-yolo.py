#!/usr/bin/env python3
"""YOLO object detection - Task 5: Preprocess images"""
import numpy as np
import cv2
import os
import glob
import tensorflow as tf


class Yolo:
    """Uses Darknet YOLO v3 algorithm for object detection."""

    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        """
        Initialize Yolo.

        model_path: path to Darknet Keras model
        classes_path: path to list of class names
        class_t: box score threshold for initial filtering
        nms_t: IOU threshold for non-max suppression
        anchors: anchor boxes array
        """
        self.model = tf.keras.models.load_model(model_path)
        with open(classes_path, 'r') as f:
            self.class_names = [line.strip() for line in f.readlines()]
        self.class_t = class_t
        self.nms_t = nms_t
        self.anchors = anchors

    def process_outputs(self, outputs, image_size):
        """Process Darknet model outputs."""
        boxes = []
        box_confidences = []
        box_class_probs = []

        image_h, image_w = image_size

        for i, output in enumerate(outputs):
            grid_h, grid_w, anchor_boxes, _ = output.shape

            box_conf = 1 / (1 + np.exp(-output[:, :, :, 4:5]))
            box_class_prob = 1 / (1 + np.exp(-output[:, :, :, 5:]))

            box_confidences.append(box_conf)
            box_class_probs.append(box_class_prob)

            tx = output[:, :, :, 0]
            ty = output[:, :, :, 1]
            tw = output[:, :, :, 2]
            th = output[:, :, :, 3]

            cx = np.arange(grid_w).reshape(1, grid_w)
            cx = np.repeat(cx, grid_h, axis=0)
            cy = np.arange(grid_h).reshape(grid_h, 1)
            cy = np.repeat(cy, grid_w, axis=1)

            cx = cx[:, :, np.newaxis]
            cy = cy[:, :, np.newaxis]

            bx = (1 / (1 + np.exp(-tx)) + cx) / grid_w
            by = (1 / (1 + np.exp(-ty)) + cy) / grid_h

            anchors_w = self.anchors[i, :, 0]
            anchors_h = self.anchors[i, :, 1]

            input_w = self.model.input.shape[1]
            input_h = self.model.input.shape[2]

            bw = (np.exp(tw) * anchors_w) / input_w
            bh = (np.exp(th) * anchors_h) / input_h

            x1 = (bx - bw / 2) * image_w
            y1 = (by - bh / 2) * image_h
            x2 = (bx + bw / 2) * image_w
            y2 = (by + bh / 2) * image_h

            box = np.stack([x1, y1, x2, y2], axis=-1)
            boxes.append(box)

        return boxes, box_confidences, box_class_probs

    def filter_boxes(self, boxes, box_confidences, box_class_probs):
        """Filter boxes based on class confidence score."""
        filtered_boxes = []
        filtered_scores = []
        filtered_classes = []

        for i in range(len(boxes)):
            scores = box_confidences[i] * box_class_probs[i]
            class_scores = np.max(scores, axis=-1)
            class_idx = np.argmax(scores, axis=-1)

            mask = class_scores >= self.class_t

            filtered_boxes.append(boxes[i][mask])
            filtered_scores.append(class_scores[mask])
            filtered_classes.append(class_idx[mask])

        filtered_boxes = np.concatenate(filtered_boxes, axis=0)
        filtered_scores = np.concatenate(filtered_scores, axis=0)
        filtered_classes = np.concatenate(filtered_classes, axis=0)

        return filtered_boxes, filtered_scores, filtered_classes

    def non_max_suppression(self, filtered_boxes, box_classes, box_scores):
        """Apply non-max suppression to filtered boxes."""
        kept_boxes = []
        kept_scores = []
        kept_classes = []

        unique_classes = np.unique(box_classes)

        for cls in unique_classes:
            mask = box_classes == cls
            cls_boxes = filtered_boxes[mask]
            cls_scores = box_scores[mask]

            x1 = cls_boxes[:, 0]
            y1 = cls_boxes[:, 1]
            x2 = cls_boxes[:, 2]
            y2 = cls_boxes[:, 3]

            areas = (x2 - x1 + 1) * (y2 - y1 + 1)
            order = cls_scores.argsort()[::-1]

            keep = []
            while order.size > 0:
                i = order[0]
                keep.append(i)

                xx1 = np.maximum(x1[i], x1[order[1:]])
                yy1 = np.maximum(y1[i], y1[order[1:]])
                xx2 = np.minimum(x2[i], x2[order[1:]])
                yy2 = np.minimum(y2[i], y2[order[1:]])

                inter_w = np.maximum(0, xx2 - xx1 + 1)
                inter_h = np.maximum(0, yy2 - yy1 + 1)
                inter = inter_w * inter_h

                iou = inter / (areas[i] + areas[order[1:]] - inter)
                order = order[np.where(iou <= self.nms_t)[0] + 1]

            kept_boxes.append(cls_boxes[keep])
            kept_scores.append(cls_scores[keep])
            kept_classes.append(np.full(len(keep), cls))

        kept_boxes = np.concatenate(kept_boxes, axis=0)
        kept_scores = np.concatenate(kept_scores, axis=0)
        kept_classes = np.concatenate(kept_classes, axis=0)

        return kept_boxes, kept_classes, kept_scores

    @staticmethod
    def load_images(folder_path):
        """
        Load images from a folder.

        folder_path: path to folder holding all images to load
        Returns: tuple of (images, image_paths)
        """
        image_paths = glob.glob(os.path.join(folder_path, '*'))
        images = [cv2.imread(path) for path in image_paths]
        return images, image_paths

    def preprocess_images(self, images):
        """
        Preprocess images for Darknet model input.

        images: list of images as numpy.ndarrays
        Returns: tuple of (pimages, image_shapes)
            pimages: ndarray of shape (ni, input_h, input_w, 3)
            image_shapes: ndarray of shape (ni, 2) with original (h, w)
        """
        input_h = self.model.input.shape[1]
        input_w = self.model.input.shape[2]

        pimages = []
        image_shapes = []

        for image in images:
            image_shapes.append(image.shape[:2])
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            resized = cv2.resize(
                rgb,
                (input_w, input_h),
                interpolation=cv2.INTER_CUBIC
            )
            rescaled = resized / 255.0
            pimages.append(rescaled)

        pimages = np.array(pimages)
        image_shapes = np.array(image_shapes)

        return pimages, image_shapes
