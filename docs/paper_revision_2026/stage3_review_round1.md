# Stage 3 — Round 1 Peer Review

## Phase 0: Field Analysis / Reviewer Configuration

- **Primary discipline**: Biomedical engineering / medical imaging AI
- **Secondary discipline**: Machine learning (computer vision)
- **Methodology type**: Empirical, single-dataset comparative model evaluation with post-hoc interpretability analysis
- **Target tier**: Mid-tier applied ML/biomedical engineering journal (e.g., Electronics, Applied Sciences, Biomedical Signal Processing and Control tier — not Nature/Science tier)
- **Paper maturity**: Revision of an undergraduate thesis, first submission-level review

**Reviewer Configuration**:
- EIC: editor at a mid-tier biomedical-AI applications journal, prioritizes clinical relevance and honest scope claims over SOTA chasing
- R1 (Methodology): ML methodology reviewer, focus on train/test protocol rigor, statistical reporting, reproducibility
- R2 (Domain): medical imaging / radiology-adjacent reviewer, focus on literature coverage and clinical framing accuracy
- R3 (Perspective): deployment/health-systems reviewer, focus on the resource-constraint framing's practical credibility
- Devil's Advocate: challenges the core "resource-efficiency, not accuracy" reframing itself

---

## R1 — Editor-in-Chief Report

**Journal fit**: Reasonable fit for a mid-tier applied biomedical AI journal. Not competitive for a top-tier venue given no new experiments.

**Originality**: Low novelty on the technical contribution (architecture is a 2023-era design, already surpassed per the paper's own Section 2). The paper's honesty about this — explicitly repositioning around resource efficiency rather than overclaiming SOTA — is a genuine strength that raises its credibility, but reviewers will still ask "what is the paper's actual new contribution beyond the 2023 thesis?"

**Significance**: The resource-efficiency angle (single 8GB consumer GPU) is a real and underexplored framing in this specific subfield per the paper's own lit review (Section 2.4). This is the paper's strongest asset — it should be foregrounded even more than it currently is.

**Overall**: MAJOR REVISION. The paper's honesty about limitations (Section 5) is unusually strong for a thesis-derived submission, but the core issue is that no new experiment was run — the entire quantitative contribution is a 2023 result with 2026 framing. An editor will ask whether that's enough for a "new" journal submission versus a technical note / short communication.

---

## R2 — Methodology Review Report

**Research design**: The corrected accuracy figure (98.77%, from 322/326) is well-justified given the internal inconsistency found in the source thesis — I credit the authors for showing the reconciliation logic in §4.1 rather than picking whichever number looked best. This is good practice.

**Reproducibility — MAJOR issue**: The paper states no independent retraining was performed and the repo's `results/` directory is empty (§5, item 1). This means **zero results in this paper are independently verifiable by a reader**. For a methods paper, this is a serious gap. At minimum, the paper should either (a) actually run the training pipeline once to produce a verifiable results artifact, or (b) be reframed more explicitly as a "historical re-analysis with corrected reporting" rather than presenting results in a Results section formatted like fresh experimental output.

**Statistical validity — MAJOR issue**: n=326 test images with only 4-12 misclassifications is a small test set; no confidence intervals or statistical test (e.g., McNemar's test between the two models' error patterns) are reported, so the claim "outperforms ResNet-50" (98.77% vs 96.32%) is not statistically substantiated. With this small an n, a handful of images either way is not necessarily a significant difference. Recommend either computing McNemar's test on the corrected confusion-matrix counts or explicitly softening the comparative language.

**ResNet-50 sigmoid/softmax issue**: Good that this was flagged as a limitation (§5, item 3) rather than silently fixed or silently ignored, but as flagged, it undermines the head-to-head model comparison in §4.1's Table 1 — a mismatched activation function is not a fair baseline comparison. This should be described more prominently as a threat to the validity of the *comparison*, not just a footnote-level limitation.

**Verdict**: MAJOR REVISION.

---

## R3 — Domain Review Report

**Literature coverage**: Good — the 2022-2026 update (Section 2) is a real strength relative to what a straight thesis-to-paper conversion would have produced. Citation verification work (CrossRef cross-checks, flagged uncertainties for [14],[16],[17]) is more rigorous than typical.

**Domain framing accuracy**: One issue — Section 2.2's correction that [10] is a three-class (not four-class) study is good catch-and-fix, but I'd like the text to also note explicitly *why* removing the "no tumor" class matters clinically (a three-class classifier assumes a tumor is already known to be present, which is a materially easier task than four-class screening). This is currently implicit.

**Missing reference**: The paper does not cite any of the original 2023 thesis's own literature on min-max normalization beyond Nayak et al. [19] — worth checking whether more recent (2022+) preprocessing-method papers exist, since Section 2 otherwise updates every other subtopic to 2022-2026 but preprocessing methodology citations remain 2020-vintage.

**Verdict**: MINOR-to-MAJOR REVISION (borderline; the missing preprocessing-literature update is a MINOR gap, but combined with R1/R2's concerns pushes toward MAJOR at the editorial level).

---

## R4 — Perspective Review Report (Deployment/Health-Systems Angle)

**Practical credibility of the resource-efficiency claim**: The paper's central reframed contribution — that this architecture is viable on an 8GB consumer GPU — is asserted but not benchmarked against what the field considers "resource-constrained." A GTX 1050 (2016-era, 8GB) is now nearly a decade old; a genuinely useful resource-constrained claim in 2026 would benchmark against currently-available low-cost hardware (e.g., a modern entry-level GPU, or explicitly an edge/embedded inference scenario), not just report what hardware happened to be used in 2023. As written, this reads as a post-hoc reframing of a hardware constraint that was originally just "what the students had access to," not a deliberate resource-efficiency study design.

**Practical impact**: The paper does not report inference time or memory footprint at deployment — only training hardware. A deployment-relevant resource-efficiency paper needs inference-side numbers (latency, memory), which are entirely absent.

**Verdict**: MAJOR REVISION — the resource-efficiency framing, while a good instinct, is currently asserted rather than substantiated with any resource-specific measurement beyond "we used this GPU to train."

---

## R5 — Devil's Advocate Report

**Strongest counter-argument**: The paper's entire value proposition rests on a reframe — "we're not claiming SOTA accuracy, we're claiming resource efficiency and honest reporting" — but this reframe was applied *after* the fact by the current AI-assisted revision, not something the original 2023 experimental design was built to test. The paper does not report the one thing that would make the resource-efficiency claim real: a controlled comparison showing this architecture achieves comparable accuracy to higher-resource competitors *specifically because of* an efficiency-oriented design choice, versus simply being an older architecture that happens to have been trained on modest hardware. Correlation (trained on a GTX 1050) is being presented adjacent to causation (therefore "resource-efficient") without the paper establishing the causal link. A skeptical reader could conclude this is scope-narrowing to salvage a paper from a now-uncompetitive accuracy result, not a genuine resource-efficiency contribution.

**Issue list**:
- **CRITICAL**: No experiment isolates "resource efficiency" as an independent variable. The paper reports what hardware was used, not what happens if you constrain hardware for a competing method too, or what the minimum viable hardware actually is. Without a controlled comparison, "resource-efficient" is a narrative label, not a measured property.
- **MAJOR**: The paper never states inference-time/deployment resource requirements (see R4), which is the resource metric that would actually matter for the claimed contribution.
- **MAJOR**: Statistical significance not established for the EfficientNet-vs-ResNet50 comparison (R2's point) — compounds the CRITICAL issue, since even the modest accuracy edge over ResNet-50 that remains after the honest reframing is not shown to be real.
- **MINOR**: The paper's own Limitations section is thorough and largely pre-empts softer versions of these criticisms — credit where due, but pre-emptive disclosure of a limitation does not resolve the limitation itself.

**Ignored alternative explanation**: The 98.77%-vs-96.32% gap could plausibly be explained by the ResNet-50 baseline's flawed sigmoid-output configuration (R2's finding) rather than any genuine EfficientNet architectural advantage — the paper does not test this alternative explanation (e.g., by also reporting a softmax-corrected ResNet-50 baseline).

**"So what?" test**: If this paper is accepted as-is, a reader learns "an old architecture, trained on old hardware, gets a re-corrected accuracy number, with a narrative about efficiency that isn't independently measured." That's a thin contribution for a 2026 journal submission, however honest the framing.

**Verdict**: The CRITICAL issue must be addressed — either add a real resource-efficiency measurement (inference latency/memory, or a controlled hardware-constrained comparison) or scale back the framing from "resource-efficiency contribution" to "we report a corrected historical result and note resource constraints as context," which is a more modest but more honest claim.

---

## Phase 2: Editorial Synthesis & Decision

**Consensus across reviewers**:
1. No independent retraining/verification of any reported number (R1, R2, DA) — the paper's single biggest credibility gap.
2. ResNet-50 baseline's sigmoid/softmax mismatch undermines the head-to-head comparison (R2, DA).
3. Resource-efficiency framing is asserted, not measured (R3 implicitly, R4, DA explicitly — DA elevates to CRITICAL).
4. The paper's transparency/honesty about its own limitations is a genuine, unusual strength (R1, R2) that should be preserved, not walked back, in revision.

**Disagreement**: R3 rated MINOR-to-MAJOR; others converge on MAJOR. Resolved toward MAJOR given the DA CRITICAL issue must be adjudicated.

**Devil's Advocate CRITICAL adjudication**: VALIDATED. The resource-efficiency framing is the paper's central reframed contribution (per the Stage 1 gap analysis that motivated it), and the DA is correct that no measurement currently substantiates it as a property of the method rather than an incidental fact about 2023 hardware availability. This blocks Accept and requires a Revision Roadmap item.

## Editorial Decision: **MAJOR REVISION**

## Revision Roadmap (prioritized)

1. **[P0 / DA-CRITICAL]** Add at least one resource-efficiency measurement beyond training-hardware disclosure: parameter count comparison against baseline/competing architectures (cheap to compute from existing model definitions, no retraining needed) and, if feasible, an inference-time/memory estimate. If a full controlled hardware-constrained comparison isn't feasible, explicitly soften the framing from "resource-efficiency contribution" to "a corrected historical result reported with resource context," per DA's alternative framing.
2. **[P0]** Fix or explicitly caveat the ResNet-50 sigmoid/softmax mismatch as a stated threat to the model-comparison's validity in the Results section itself (not just Limitations) — move this out of the footnote-level Limitations framing R2 flagged.
3. **[P1]** Add a statistical test (e.g., McNemar's) on the two models' confusion-matrix counts, or explicitly soften "outperforms" language given small n and no significance test (R2, DA).
4. **[P1]** Clarify the three-class-vs-four-class distinction's clinical implication for [10] (R3).
5. **[P2]** Update preprocessing-methodology citation currency, or note explicitly that no more recent preprocessing-method literature was found (R3).
6. **[P2]** Consider reframing as a "technical note / corrected re-analysis" if a full new-contribution framing cannot be sustained without new experiments (R1) — user's call, flagged not mandated.

**Acknowledged Limitations carried forward unchanged** (already well-disclosed, no action required): no independent retraining, single dataset/split, qualitative-only Grad-CAM check.
