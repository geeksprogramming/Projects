# src/segmentation/evaluate_unet.py

"""
Evaluation metrics for semantic segmentation using predicted and ground-truth masks.

Supports:
- Precision, Recall, Specificity
- True Detection Rate (TDR)
- Intersection over Union (IoU)
- F1 Score (Dice coefficient)
"""

import numpy as np
import tensorflow as tf
import pandas as pd


def create_mask(dataset, model):
    """Run predictions and return arrays of predicted and true masks."""
    true_masks, predicted_masks = [], []

    for images, masks in dataset:
        pred = model.predict(images)
        pred = tf.expand_dims(tf.argmax(pred, axis=-1), axis=-1)
        true_masks.extend(masks)
        predicted_masks.extend(pred)

    return np.array(true_masks), np.array(predicted_masks)


def evaluate_model(true_masks, predicted_masks, n_classes=13, smooth=1e-6):
    """
    Computes class-wise and overall evaluation metrics for segmentation.

    Returns:
        A dictionary containing class-wise and overall evaluations.
    """
    class_metrics = {
        "Class": [],
        "TP": [], "TN": [], "FP": [], "FN": [],
        "Recall": [], "Precision": [], "Specificity": [],
        "IoU": [], "TDR": [], "F1-Score": []
    }

    for clas in range(n_classes):
        TP = TN = FP = FN = 0

        for i in range(true_masks.shape[0]):
            true = true_masks[i] == clas
            pred = predicted_masks[i] == clas

            TP += np.sum(np.logical_and(true, pred))
            TN += np.sum(np.logical_and(~true, ~pred))
            FP += np.sum(np.logical_and(~true, pred))
            FN += np.sum(np.logical_and(true, ~pred))

        recall = TP / (TP + FN + smooth)
        precision = TP / (TP + FP + smooth)
        specificity = TN / (TN + FP + smooth)
        tdr = recall
        iou = TP / (TP + FP + FN + smooth)
        f1 = 2 * (precision * recall) / (precision + recall + smooth)

        class_metrics["Class"].append(f"Class {clas}")
        class_metrics["TP"].append(TP)
        class_metrics["TN"].append(TN)
        class_metrics["FP"].append(FP)
        class_metrics["FN"].append(FN)
        class_metrics["Recall"].append(round(recall, 4))
        class_metrics["Precision"].append(round(precision, 4))
        class_metrics["Specificity"].append(round(specificity, 4))
        class_metrics["IoU"].append(round(iou, 4))
        class_metrics["TDR"].append(round(tdr, 4))
        class_metrics["F1-Score"].append(round(f1, 4))

    overall = {
        "Recall": round(np.mean(class_metrics["Recall"]), 4),
        "Precision": round(np.mean(class_metrics["Precision"]), 4),
        "Specificity": round(np.mean(class_metrics["Specificity"]), 4),
        "IoU": round(np.mean(class_metrics["IoU"]), 4),
        "TDR": round(np.mean(class_metrics["TDR"]), 4),
        "F1-Score": round(np.mean(class_metrics["F1-Score"]), 4),
    }

    return {
        "class_wise": class_metrics,
        "overall": overall
    }


def metrics_to_dataframe(metrics: dict):
    """Convert evaluation dict to pandas DataFrame."""
    df = pd.DataFrame(metrics["class_wise"])
    overall_row = pd.DataFrame([["All Classes", "", "", "", ""] + list(metrics["overall"].values())],
                               columns=df.columns)
    return pd.concat([df, overall_row], ignore_index=True)
