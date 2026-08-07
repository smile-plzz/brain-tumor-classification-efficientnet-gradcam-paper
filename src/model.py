"""Dense EfficientNet: EfficientNet backbone + dense/dropout classification head."""
import timm
import torch.nn as nn


class DenseEfficientNet(nn.Module):
    def __init__(self, num_classes=4, backbone="efficientnet_b0", pretrained=True, dropout=0.4):
        super().__init__()
        self.backbone = timm.create_model(backbone, pretrained=pretrained, num_classes=0)
        feat_dim = self.backbone.num_features
        self.classifier = nn.Sequential(
            nn.Linear(feat_dim, 512),
            nn.ReLU(inplace=True),
            nn.Dropout(dropout),
            nn.Linear(512, 128),
            nn.ReLU(inplace=True),
            nn.Dropout(dropout),
            nn.Linear(128, num_classes),
        )

    def forward(self, x):
        features = self.backbone(x)
        return self.classifier(features)
