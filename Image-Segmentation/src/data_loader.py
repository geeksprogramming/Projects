# src/segmentation/data_loader.py

"""
Data loading and preprocessing functions for the U-Net segmentation task
on the CARLA self-driving car simulator dataset.

- Supports loading from local paths
- Builds TensorFlow Dataset pipelines
- Normalizes and resizes images/masks
"""

import os
import tensorflow as tf
import random


def list_image_paths(directory_paths):
    """Return list of image paths from a list of folders."""
    image_paths = []
    for directory in directory_paths:
        for filename in os.listdir(directory):
            if filename.endswith(".png"):
                image_paths.append(os.path.join(directory, filename))
    return sorted(image_paths)


def get_image_mask_paths(image_dir_list, mask_dir_list):
    """
    Return lists of aligned image and mask paths with common filenames.
    """
    image_filenames = set(os.listdir(image_dir_list[0]))
    mask_filenames = set(os.listdir(mask_dir_list[0]))
    common_filenames = sorted(list(image_filenames & mask_filenames))

    image_paths = [os.path.join(image_dir_list[0], fname) for fname in common_filenames]
    mask_paths = [os.path.join(mask_dir_list[0], fname) for fname in common_filenames]

    return image_paths, mask_paths


def read_image(image_path, mask_path, image_size=(256, 256)):
    """
    Read and preprocess image and mask files.

    Returns:
        image: float32 resized image
        mask: int mask with reduced channels
    """
    image = tf.io.read_file(image_path)
    image = tf.image.decode_png(image, channels=3)
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.image.resize(image, image_size, method='nearest')

    mask = tf.io.read_file(mask_path)
    mask = tf.image.decode_png(mask, channels=3)
    mask = tf.math.reduce_max(mask, axis=-1, keepdims=True)  # Grayscale mask
    mask = tf.image.resize(mask, image_size, method='nearest')

    return image, mask


def data_generator(image_paths, mask_paths, buffer_size=500, batch_size=32, image_size=(256, 256)):
    """
    Build tf.data.Dataset pipeline from lists of paths.

    Args:
        image_paths: list of image file paths
        mask_paths: list of corresponding mask file paths
        buffer_size: for shuffling
        batch_size: batch size for training
        image_size: target image size

    Returns:
        dataset: tf.data.Dataset object
    """
    image_list = tf.constant(image_paths)
    mask_list = tf.constant(mask_paths)
    dataset = tf.data.Dataset.from_tensor_slices((image_list, mask_list))

    def _parse(img_path, msk_path):
        return read_image(img_path, msk_path, image_size)

    dataset = dataset.map(_parse, num_parallel_calls=tf.data.AUTOTUNE)
    dataset = dataset.cache().shuffle(buffer_size).batch(batch_size).prefetch(tf.data.AUTOTUNE)

    return dataset
