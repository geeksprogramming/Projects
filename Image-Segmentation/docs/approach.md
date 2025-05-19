# Project Approach – U-Net Based Semantic Segmentation

This document outlines the end-to-end approach used in `Solution.ipynb`, focused on performing semantic segmentation using a U-Net model trained on a subset of the **Lyft Udacity Self-Driving Car Dataset**.

---

## Problem Scope

The goal is to classify each pixel in an image into a category (semantic segmentation). We adapt the dataset to detect three object classes — `chair`, `book`, and `laptop`.

---

## Dataset & Assumptions

- Dataset: [Lyft Udacity Challenge – CARLA Simulated Images](https://www.kaggle.com/datasets/kumaresanmanickavelu/lyft-udacity-challenge)
- Only `dataA/` is used for experimentation to reduce training time.
- Image-mask pairs are loaded from Google Drive and preprocessed before training.

---

## Data Pipeline

1. **Mount Google Drive**: Access image and mask folders.
2. **Path Extraction**: A utility function extracts image and mask file paths.
3. **Preprocessing**:
   - All images and masks are resized to `256x256`.
   - Images are normalized to [0, 1].
   - Masks are collapsed to single-channel class indices using `argmax`.

4. **Visualization**:
   - Random samples from the dataset are displayed for verification.
   - Mask overlays and colormaps are used to inspect data quality.

---

## Model Architecture – U-Net

The U-Net model is constructed using custom functions:

### Encoder (Downsampling)
- Two Conv2D → BatchNorm → ReLU layers
- MaxPooling (except at bottleneck)
- Skip connections are retained for decoder

### Decoder (Upsampling)
- Conv2DTranspose for upsampling
- Concatenation with corresponding encoder skip connection
- Two Conv2D → BatchNorm → ReLU layers

### Output
- Final `1x1 Conv2D` layer with `sigmoid` activation to predict 13 classes.

---

## Training Workflow

- Optimizer: `Adam`
- Loss: `Sparse Categorical Crossentropy`
- Callbacks: `EarlyStopping` and `ReduceLROnPlateau`
- Epochs: 30
- Batch Size: 32

Training performance is monitored using accuracy and loss curves.

---

## Evaluation Metrics

After training, true and predicted masks are generated for all datasets:

- Metrics computed per class:
  - **Precision**, **Recall**, **Specificity**
  - **IoU**, **TDR**, **F1-Score**
- Evaluation is shown for:
  - Train Set
  - Validation Set
  - Test Set

All metrics are presented in tabular format using pandas DataFrames.

---

## Prediction Visualization

A utility function `show_predictions()` displays:
- Input image
- Ground truth mask
- Predicted mask (post-processing with argmax)

This helps validate model performance visually.

---

## Summary

This notebook delivers a full segmentation pipeline:
- Modular U-Net implementation
- Realistic dataset subset
- Structured metrics
- Clear evaluation and visualization tools

It is built to serve both educational clarity and real-world deployment readiness.

