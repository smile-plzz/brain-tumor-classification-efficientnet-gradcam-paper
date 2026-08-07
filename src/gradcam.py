"""Grad-CAM visualization for the dense EfficientNet classifier."""
import argparse

import cv2
import numpy as np
import torch
from PIL import Image
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image

from data import CLASSES, build_transforms
from model import DenseEfficientNet


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--checkpoint", required=True)
    p.add_argument("--image", required=True)
    p.add_argument("--out", default="results/gradcam_output.png")
    p.add_argument("--image-size", type=int, default=224)
    return p.parse_args()


def main():
    args = parse_args()
    device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")

    model = DenseEfficientNet(num_classes=len(CLASSES)).to(device)
    model.load_state_dict(torch.load(args.checkpoint, map_location=device))
    model.eval()

    # Last conv block of the EfficientNet backbone is the target layer for Grad-CAM.
    target_layers = [model.backbone.conv_head]

    img = Image.open(args.image).convert("RGB")
    transform = build_transforms(args.image_size, train=False)
    input_tensor = transform(img).unsqueeze(0).to(device)

    rgb_img = np.array(img.resize((args.image_size, args.image_size))).astype(np.float32) / 255.0

    with GradCAM(model=model, target_layers=target_layers) as cam:
        grayscale_cam = cam(input_tensor=input_tensor)[0]
        visualization = show_cam_on_image(rgb_img, grayscale_cam, use_rgb=True)

    with torch.no_grad():
        pred = model(input_tensor).argmax(dim=1).item()
    print(f"Predicted class: {CLASSES[pred]}")

    cv2.imwrite(args.out, cv2.cvtColor(visualization, cv2.COLOR_RGB2BGR))
    print(f"Saved Grad-CAM visualization to {args.out}")


if __name__ == "__main__":
    main()
