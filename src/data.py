"""Dataset loading, min-max normalization, and augmentation."""
import numpy as np
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms

CLASSES = ["glioma", "meningioma", "pituitary", "notumor"]


def min_max_normalize(img: np.ndarray) -> np.ndarray:
    img = img.astype(np.float32)
    lo, hi = img.min(), img.max()
    if hi - lo < 1e-6:
        return np.zeros_like(img)
    return (img - lo) / (hi - lo)


class MinMaxNormalize:
    def __call__(self, img: Image.Image) -> Image.Image:
        arr = np.array(img).astype(np.float32)
        arr = min_max_normalize(arr) * 255.0
        return Image.fromarray(arr.astype(np.uint8))


def build_transforms(image_size: int = 224, train: bool = True):
    ops = [MinMaxNormalize(), transforms.Resize((image_size, image_size))]
    if train:
        ops += [
            transforms.RandomHorizontalFlip(),
            transforms.RandomRotation(15),
            transforms.RandomAffine(degrees=0, scale=(0.9, 1.1)),
        ]
    ops += [
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
    return transforms.Compose(ops)


class BrainMRIDataset(Dataset):
    """Expects data_dir/<class_name>/*.jpg layout (ImageFolder-style)."""

    def __init__(self, data_dir, image_size=224, train=True):
        from pathlib import Path

        self.samples = []
        data_dir = Path(data_dir)
        for label, class_name in enumerate(CLASSES):
            class_dir = data_dir / class_name
            if not class_dir.exists():
                continue
            for path in class_dir.glob("*"):
                if path.suffix.lower() in {".jpg", ".jpeg", ".png"}:
                    self.samples.append((path, label))
        self.transform = build_transforms(image_size, train)

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        path, label = self.samples[idx]
        img = Image.open(path).convert("RGB")
        return self.transform(img), label
