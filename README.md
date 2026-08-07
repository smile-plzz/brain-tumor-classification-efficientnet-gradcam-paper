# Brain Tumor Classification using EfficientNet and Grad-CAM

Reimplementation/continuation of the undergraduate thesis *"Brain Tumor Classification using EfficientNet and Grad-CAM"* (North South University, ECE Dept., Summer 2023) by MD Kawser Islam, Shamin Yeaser Shams, and MD. Ismail Hossain, supervised by Dr. Mohammad Monirujjaman Khan.

## Overview

A dense EfficientNet-based CNN classifies T1-weighted contrast-enhanced brain MRI scans into four categories: **glioma**, **meningioma**, **pituitary tumor**, and **no tumor**. Min-max normalization and data augmentation are used to improve contrast and generalization on a limited dataset. Grad-CAM is applied to visualize which regions of the MRI the model relies on for its predictions, adding interpretability to the classification decision.

Original thesis reported 99.96% training accuracy and 100% test accuracy on a 3260-image T1-weighted contrast-enhanced MRI dataset (Kaggle Brain Tumor MRI Dataset).

## Project Structure

```
.
├── src/
│   ├── data.py          # dataset loading, min-max normalization, augmentation
│   ├── model.py         # dense EfficientNet architecture (dense + dropout layers)
│   ├── train.py         # training loop
│   ├── evaluate.py      # test-set evaluation, confusion matrix, F1
│   └── gradcam.py       # Grad-CAM implementation and visualization
├── notebooks/           # exploratory analysis / experiment notebooks
├── data/
│   ├── raw/              # original dataset (not tracked in git)
│   └── processed/        # preprocessed/augmented splits
├── models/               # saved model checkpoints (not tracked in git)
├── results/              # confusion matrices, Grad-CAM outputs, metrics
├── docs/
│   └── thesis-report.docx  # original thesis writeup (reference)
└── requirements.txt
```

## Dataset

[Kaggle Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset) (or the original 3064-image T1-weighted contrast-enhanced set referenced in the thesis) — 4 classes: glioma, meningioma, pituitary, no tumor. Place the raw dataset under `data/raw/<class_name>/*.jpg`.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
# Train
python src/train.py --data-dir data/raw --epochs 50 --batch-size 32

# Evaluate
python src/evaluate.py --checkpoint models/best_model.pt --data-dir data/raw

# Grad-CAM visualization for a single image
python src/gradcam.py --checkpoint models/best_model.pt --image path/to/scan.jpg
```

## Method Summary

- **Preprocessing**: min-max normalization to enhance tumor-region contrast, resizing, data augmentation (rotation, flip, zoom).
- **Model**: EfficientNet backbone extended with dense + dropout layers to reduce overfitting on a relatively small medical imaging dataset.
- **Interpretability**: Grad-CAM highlights the image regions most responsible for the predicted class, using gradients of the classification score with respect to the final convolutional feature map.

## Reference

Original thesis report: `docs/thesis-report.docx`.
