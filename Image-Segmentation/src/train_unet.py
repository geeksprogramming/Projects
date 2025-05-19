# src/segmentation/train_unet.py

"""
Training pipeline for U-Net segmentation model on the CARLA dataset.

- Compiles the model with sparse categorical crossentropy
- Uses EarlyStopping and ReduceLROnPlateau
- Plots training history
- Saves the trained model in HDF5 format
"""

import os
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

from src.segmentation.model_unet import unet_model
from src.segmentation.data_loader import data_generator, get_image_mask_paths


def compile_unet(input_size=(256, 256, 3), filters=32, n_classes=13):
    """Returns a compiled U-Net model."""
    model = unet_model(input_size=input_size, filters=filters, n_classes=n_classes)
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model


def plot_history(history, output_dir="outputs"):
    """Plot accuracy and loss curves."""
    os.makedirs(output_dir, exist_ok=True)

    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    plt.figure(figsize=(10, 8))

    plt.subplot(2, 1, 1)
    plt.plot(acc, label='Train Acc')
    plt.plot(val_acc, label='Val Acc')
    plt.legend()
    plt.title('Accuracy')

    plt.subplot(2, 1, 2)
    plt.plot(loss, label='Train Loss')
    plt.plot(val_loss, label='Val Loss')
    plt.legend()
    plt.title('Loss')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'training_curves.png'))
    plt.show()


def main():
    # Adjust paths as per your machine setup
    image_dirs = ["./data/carla/CameraRGB"]
    mask_dirs = ["./data/carla/CameraSeg"]

    image_paths, mask_paths = get_image_mask_paths(image_dirs, mask_dirs)

    # Split into train/val/test
    train_size = int(0.8 * len(image_paths))
    val_size = int(0.16 * len(image_paths))

    train_image_paths = image_paths[:train_size]
    train_mask_paths = mask_paths[:train_size]

    val_image_paths = image_paths[train_size:train_size + val_size]
    val_mask_paths = mask_paths[train_size:train_size + val_size]

    test_image_paths = image_paths[train_size + val_size:]
    test_mask_paths = mask_paths[train_size + val_size:]

    # Build datasets
    train_ds = data_generator(train_image_paths, train_mask_paths)
    val_ds = data_generator(val_image_paths, val_mask_paths)
    test_ds = data_generator(test_image_paths, test_mask_paths)

    # Compile model
    model = compile_unet()

    # Define callbacks
    callbacks = [
        EarlyStopping(monitor='val_accuracy', patience=20, restore_best_weights=True),
        ReduceLROnPlateau(monitor='val_accuracy', factor=1e-1, patience=5, verbose=1, min_lr=2e-6)
    ]

    # Train
    history = model.fit(train_ds,
                        validation_data=val_ds,
                        epochs=30,
                        callbacks=callbacks,
                        verbose=1)

    # Save model
    os.makedirs("models", exist_ok=True)
    model.save("models/carla_segmentation_unet.h5")

    # Plot
    plot_history(history)


if __name__ == "__main__":
    main()
