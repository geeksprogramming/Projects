# Problem Statements

In this project, the objective is to build a semantic segmentation model using the U-Net architecture to classify each pixel in images captured from the CARLA self-driving simulator. The dataset is sourced from the Lyft–Udacity Perception Challenge and contains RGB images paired with segmentation masks. To simplify the workflow and reduce training time, only the dataA subset is used. All images are resized and normalized, and the masks are reduced to single-channel class maps using argmax.

The model is implemented in TensorFlow/Keras and trained using standard callbacks like early stopping and learning rate reduction. Once trained, it's evaluated using metrics such as accuracy, IoU, F1 score, precision, recall, and specificity. Visual results are also generated to compare the model’s predictions with the actual masks. The output includes the trained model file, performance plots, and sample prediction visuals

## Problem : Semantic Segmentation with U-Net (CARLA Dataset)
Goal:
Train and evaluate a U-Net model for segmenting images captured from the CARLA self-driving car simulator.

Model: U-Net implemented from scratch using TensorFlow/Keras.

Pipeline:
Load and preprocess data from multiple directories (dataA to dataE).
Split into train/validation/test sets.
Build efficient input pipelines using tf.data.Dataset.
Implement U-Net (encoding, bottleneck, decoding).
Train and evaluate the model using:
Accuracy, Precision, Recall, Specificity
IoU, F1 Score (Dice), TDR
Visualize predictions and compare with ground truth.
Save the trained model (.h5 format) and use plots to analyze training curves.
