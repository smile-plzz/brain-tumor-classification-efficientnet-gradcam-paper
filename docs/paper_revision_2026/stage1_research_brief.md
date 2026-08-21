# Research Brief — EfficientNet + Grad-CAM Brain Tumor MRI Classification (2022-2026 Update)

## RQ Brief

**RQ**: Does a dense-layer-augmented EfficientNet with Grad-CAM interpretability offer a defensible accuracy/interpretability trade-off for 4-class brain tumor MRI classification (glioma, meningioma, pituitary, no-tumor), relative to 2024-2026 CNN, hybrid, and Vision Transformer baselines?

**Scope**: In-scope — T1-weighted contrast-enhanced MRI, 4-class classification, EfficientNet family, Grad-CAM/XAI methods, CNN vs. ViT vs. hybrid benchmarks. Out-of-scope — segmentation-only work, non-MRI modalities (CT, histopathology), tumor grading/staging.

**FINER**: Feasible (public datasets, established methods) / Interesting (XAI-in-clinical-AI is an active subfield) / Novel — **thin at the CNN-only level**, see Gap below / Ethical (no new patient data, secondary/public dataset use) / Relevant (medical imaging AI, active 2024-2026 literature).

## Annotated Bibliography (selected, 2023-2026)

1. **Badza-style EfficientNetV2B3 study** — 99.39% accuracy, best accuracy/compute trade-off among EfficientNet variants. [Improved EfficientNet Architecture for Multi-Grade Brain Tumor Detection](https://www.mdpi.com/2079-9292/14/4/710) (MDPI Electronics, 2025)
2. **EfficientNetB3 fine-tuning study** — 99% test accuracy, 99% macro-F1 on CE-MRI 4-class set. [Multi-class classification of brain tumor types from MR images using EfficientNets](https://www.sciencedirect.com/science/article/abs/pii/S1746809423002100) (Biomed. Signal Process. Control, 2023)
3. **Hybrid deep learning models** — 2023-2024 hybrid CNN ensembles on the same Kaggle-derived corpus family. [Detection and classification of brain tumor using hybrid deep learning models](https://www.nature.com/articles/s41598-023-50505-6) (Scientific Reports, 2023)
4. **Grad-CAM + SHAP dual-XAI** — combines Grad-CAM with SHAP on an Xception backbone for cross-method interpretability agreement. [Enhancing interpretability in brain tumor detection: Leveraging Grad-CAM and SHAP](https://ph.pollub.pl/index.php/acs/article/view/7375) (Applied Computer Science, 2024/2025)
5. **Grad-CAM + ResNet50, clinical-marker correlation** — explicitly correlates Grad-CAM activation regions with radiological markers. [Enhancing brain tumor detection in MRI images through explainable AI using Grad-CAM with Resnet 50](https://link.springer.com/article/10.1186/s12880-024-01292-7) (BMC Medical Imaging, 2024)
6. **LIME vs. Grad-CAM comparative XAI** — direct method-vs-method interpretability comparison, a framing the 2023 thesis lacks entirely. [Brain Tumor Classification in MRI: Insights From LIME and Grad-CAM](https://ieeexplore.ieee.org/document/11142756/) (IEEE Access, 2025)
7. **38-model lightweight CNN/ViT benchmark** — large-scale benchmark across 5 merged public datasets; EfficientNet-B0 and Tiny-ViT-5M both clear 98%, establishing current SOTA floor. [Comparative evaluation of lightweight CNN and ViT models](https://www.sciencedirect.com/science/article/abs/pii/S0169743925002941) (Expert Systems w/ Applications, 2025)
8. **Hybrid CNN-Transformer + Aquila Optimization** — 97.2% accuracy, explicit interpretability claim, outperforms CNN-only and ViT-only baselines. [An Explainable Hybrid CNN-Transformer Framework with Aquila Optimization](https://www.medrxiv.org/content/10.1101/2025.10.14.25338038.full.pdf) (medRxiv, 2025)
9. **ViT-B-16 diagnostic study** — reports 99.92% accuracy, among the highest single-model figures found; flagged Grade B pending independent replication (single-study extreme value).

## Synthesis / Gap Analysis

- **Accuracy ceiling has moved past the thesis's claimed numbers.** Multiple 2024-2026 EfficientNet-variant and hybrid studies report 99.0-99.9% on comparable 4-class CE-MRI tasks — the thesis's internally-inconsistent 96-100% range (see integrity flags from thesis read) is no longer a differentiator even if the highest reported figure is accepted at face value. **Accuracy alone is not a viable novelty claim for a 2026 submission.**
- **XAI-method comparison is now the differentiator, not XAI presence.** 2023 thesis treats Grad-CAM as a novel add-on. 2024-2026 literature treats single-method Grad-CAM as baseline and compares Grad-CAM against SHAP, LIME, and Integrated Gradients, or correlates activation maps against radiological ground truth. A revised paper should reposition Grad-CAM as one XAI method among several, or add a second XAI method for comparison, to avoid reviewers flagging the interpretability contribution as dated.
- **ViT/hybrid architectures are now standard comparison baselines.** The thesis's only comparison baseline is ResNet-50. Reviewers in 2026 will expect at least one ViT or hybrid CNN-Transformer baseline in the comparison table (Table 4.3-equivalent).
- **Recommended reframing for the rewrite**: position the paper's contribution as (a) a resource-efficient dense-EfficientNet suitable for constrained clinical/deployment settings (the thesis's original hardware section — GTX1050, 8GB — supports a resource-efficiency narrative), compared against the 2025 lightweight-CNN/ViT benchmark study (#7), with (b) Grad-CAM interpretability validated qualitatively against the clinical-marker-correlation approach of #5, rather than claiming raw accuracy superiority.

## Source Quality Notes

- All 9 sources are Tier 1 (peer-reviewed journal/conference) or Tier 2 (preprint server, clearly labeled) — Nature/Scientific Reports, IEEE Access, MDPI, ScienceDirect, Springer/BMC, medRxiv.
- Source #9 (ViT-B-16, 99.92%) flagged Grade B: single-study extreme accuracy claim, no independent replication found in this quick pass — cite with a caveat if used, don't treat as settled SOTA.
- No retractions found for any cited venue/study in this pass (not a full Retraction Watch sweep — quick mode only).

## Limitations

Quick-mode pass (9 sources, ~30-min-equivalent search depth), not a systematic review. No PRISMA screening, no full-text read of primary sources (search-result abstracts/summaries only) — full-text verification of exact accuracy figures deferred to Stage 2.5 integrity check when these sources are actually cited in-text. Search performed in English only.

## AI Disclosure

Search and synthesis performed by Claude (deep-research quick mode) via web search, 2026-08-21.
