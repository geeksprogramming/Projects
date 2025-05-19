# src/segmentation/model_unet.py

"""
Modular U-Net model implementation for semantic segmentation.

- Encoding blocks with optional max pooling
- Decoding blocks with transposed convolutions and skip connections
- Final model builder for flexible input shapes and class counts
"""

import tensorflow as tf
from tensorflow.keras.layers import (Input, Conv2D, BatchNormalization, ReLU,
                                     MaxPooling2D, Conv2DTranspose,
                                     Cropping2D, concatenate)
from tensorflow.keras.models import Model


def encoding_block(inputs, filters, max_pooling=True):
    """
    Create an encoding block with 2 Conv2D layers, BatchNorm, ReLU, and optional MaxPooling.

    Returns:
        next_layer: output after pooling
        skip_connection: pre-pooled tensor for skip connection
    """
    x = Conv2D(filters, kernel_size=(3, 3), padding='same', kernel_initializer='he_normal')(inputs)
    x = BatchNormalization()(x)
    x = ReLU()(x)

    x = Conv2D(filters, kernel_size=(3, 3), padding='same', kernel_initializer='he_normal')(x)
    x = BatchNormalization()(x)
    x = ReLU()(x)

    skip_connection = x

    if max_pooling:
        next_layer = MaxPooling2D(pool_size=(2, 2))(skip_connection)
    else:
        next_layer = skip_connection

    return next_layer, skip_connection


def decoding_block(inputs, skip_connection_input, filters):
    """
    Create a decoding block with Conv2DTranspose, concatenation, and 2 Conv2D layers.

    Returns:
        x: output tensor of this block
    """
    x = Conv2DTranspose(filters, kernel_size=(3, 3), strides=(2, 2),
                        padding='same', kernel_initializer='he_normal')(inputs)

    # Optional cropping if shapes mismatch slightly
    crop_height = (x.shape[1] - skip_connection_input.shape[1]) // 2
    crop_width = (x.shape[2] - skip_connection_input.shape[2]) // 2

    if crop_height > 0 or crop_width > 0:
        x = Cropping2D(((crop_height, crop_height), (crop_width, crop_width)))(x)

    x = concatenate([x, skip_connection_input], axis=3)

    x = Conv2D(filters, kernel_size=(3, 3), padding='same', kernel_initializer='he_normal')(x)
    x = BatchNormalization()(x)
    x = ReLU()(x)

    x = Conv2D(filters, kernel_size=(3, 3), padding='same', kernel_initializer='he_normal')(x)
    x = BatchNormalization()(x)
    x = ReLU()(x)

    return x


def unet_model(input_size=(256, 256, 3), filters=32, n_classes=13):
    """
    Build the full U-Net model.

    Args:
        input_size: tuple, image input shape
        filters: base number of filters
        n_classes: number of segmentation classes

    Returns:
        model: compiled tf.keras.Model
    """
    inputs = Input(input_size)

    # Encoding path
    c1, skip1 = encoding_block(inputs, filters)
    c2, skip2 = encoding_block(c1, filters * 2)
    c3, skip3 = encoding_block(c2, filters * 4)
    c4, skip4 = encoding_block(c3, filters * 8, max_pooling=False)

    # Decoding path
    d1 = decoding_block(c4, skip4, filters * 8)
    d2 = decoding_block(d1, skip3, filters * 4)
    d3 = decoding_block(d2, skip2, filters * 2)
    d4 = decoding_block(d3, skip1, filters)

    # Final segmentation layer
    outputs = Conv2D(filters=n_classes, kernel_size=(1, 1),
                     activation='softmax', padding='same')(d4)

    model = Model(inputs=inputs, outputs=outputs)
    return model
