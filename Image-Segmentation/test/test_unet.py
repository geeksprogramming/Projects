# tests/test_unet.py

"""
Unit tests for validating the U-Net segmentation pipeline.

This file contains tests covering:
- Correctness of the U-Net model output shape.
- Consistency and correctness of dataset loader paths.
- Structure and keys of the evaluation metrics output.
"""

import os
import pytest
import numpy as np
import tensorflow as tf

from src.segmentation.model_unet import unet_model
from src.segmentation.data_loader import get_image_mask_paths, data_generator
from src.segmentation.evaluate_unet import evaluate_model


def test_unet_model_output_shape():
    """
    Test that the U-Net model produces outputs of expected shape.
    """
    model = unet_model(input_size=(256, 256, 3), filters=32, n_classes=13)
    dummy_input = tf.random.uniform((1, 256, 256, 3))
    output = model(dummy_input)

    # Assert output shape matches expected segmentation map dimensions
    assert output.shape == (1, 256, 256, 13), \
        f"Expected shape (1, 256, 256, 13), got {output.shape}"


def test_data_loader_count():
    """
    Test the dataset loader to ensure correct count and matching of images and masks.
    """
    image_dirs = ["./data/carla/CameraRGB"]
    mask_dirs = ["./data/carla/CameraSeg"]
    image_paths, mask_paths = get_image_mask_paths(image_dirs, mask_dirs)

    # Ensure image and mask paths are retrieved successfully
    assert len(image_paths) > 0, "No image paths found."
    assert len(mask_paths) > 0, "No mask paths found."

    # Check if the number of images matches the number of masks
    assert len(image_paths) == len(mask_paths), \
        f"Mismatch: {len(image_paths)} images vs {len(mask_paths)} masks."


def test_evaluation_metrics_structure():
    """
    Validate the structure and keys of the evaluation metrics dictionary returned by evaluate_model.
    """
    # Generate dummy ground truth and predictions
    true = np.random.randint(0, 13, size=(10, 256, 256, 1))
    pred = np.random.randint(0, 13, size=(10, 256, 256, 1))

    metrics = evaluate_model(true, pred, n_classes=13)

    # Assert expected keys exist in the metrics dictionary
    assert "class_wise" in metrics, "Missing 'class_wise' key in metrics."
    assert "overall" in metrics, "Missing 'overall' key in metrics."

    # Validate the structure of metric details
    assert isinstance(metrics["class_wise"], dict), \
        "'class_wise' metrics should be a dictionary."
    assert isinstance(metrics["overall"], dict), \
        "'overall' metrics should be a dictionary."