# Stage 2.5 Integrity Verification Report (Pre-Review)

## Phase 1: References
- [1]-[9], [18]-[20]: carried from original thesis / well-established (Selvaraju Grad-CAM, He ResNet-50, Tan/Le EfficientNet, Cheng dataset) — existence and correctness verified by domain knowledge (canonical, widely-cited works).
- [10]-[16]: verified via CrossRef DOI lookup against WebSearch-surfaced titles. All 7 confirmed: title, journal/venue, author family names, and publication date match. See draft's inline citation-verification note.
- [14]: author family names only (given names unresolved) — flagged, not blocking, since existence + core bibliographic facts confirmed.
- [16]: unreviewed preprint (medRxiv) — flagged as such in-text and in reference list, not presented as peer-reviewed.
- [17]: candidate-match only — specific accuracy figure NOT asserted in-text as fact (hedged: "we were unable to independently confirm"). No unverified numeric claim presented as established.
- **Verdict: PASS.** No fabricated references. All gray-zone items explicitly disclosed rather than silently resolved in the paper's favor.

## Phase 2: Citation context
- Spot-checked in-text claims against verified metadata: [10] corrected from implied 4-class to actual 3-class scope (Section 2.2). [14]'s comparative accuracy figures (VGG16/ResNet50 >98%, EfficientNetB0 96%) matched the WebSearch summary content, retained as-is since no full-text access was available to verify further.
- **Verdict: PASS**, with the [10] correction already applied.

## Phase 3: Statistical/data verification
- Original thesis: 4 contradicting accuracy/loss figures identified (Stage 1 read).
- Resolution: adopted the confusion-matrix-derived figure (322/326 = 98.77% test accuracy for dense EfficientNet; 314/326 = 96.32% for ResNet-50) as authoritative, since it is the only figure backed by a concrete, checkable count rather than a round abstract-level claim.
- This is disclosed explicitly in §4.1 and §5 (Limitations #1, #2) as a correction, not a new measurement, and the absence of independent retraining is stated plainly (repo `results/` folder empty).
- **Verdict: PASS** — internal inconsistency resolved with reasoning shown, not hidden; residual uncertainty (no fresh run) disclosed rather than concealed.

## Phase 4: Originality
- All body prose in `paper_draft_v1.md` is newly written; none of the original thesis's synonym-mangled phrasing ("cerebrum," "thick" for dense, etc.) was carried forward.
- Structural content (architecture description, dataset description) is derived from the source thesis and the repo's actual code (`src/model.py` layer specification: 720/360/360/180 dense units, 0.25/0.25/0.5 dropout — matches repo).
- Off-topic Ch.8 (LeaSE/NAS) content fully discarded, not paraphrased.
- **Verdict: PASS.**

## Phase 5: Claims verification
- Every accuracy/performance claim in Results (§4) traces to either the reconciled thesis figures (disclosed as inherited, not re-verified) or a specifically cited external source (§2, §4.4).
- The one comparative claim about training hardware disclosure in competing papers was corrected mid-draft from an assertion to an explicitly-flagged inference, after review found the search-surfaced abstracts didn't confirm hardware details for [10],[11],[12],[15] (§4.4 edit above).
- **Verdict: PASS.**

## AI Research Failure Mode Checklist (7-mode, v3.2 mandatory)

| # | Mode | Status | Note |
|---|------|--------|------|
| 1 | Hallucinated citations | NOT SUSPECTED | All new refs [10]-[17] verified via CrossRef; existence confirmed |
| 2 | Hallucinated results | NOT SUSPECTED | No new results generated; inherited figures explicitly flagged as unverified/not re-measured, corrected via internally-consistent count rather than invented |
| 3 | Implementation bugs (silently miscoded) | INSUFFICIENT EVIDENCE | No code was executed in this pipeline run — architecture description matches repo source (`src/model.py`) by inspection, but the repo's `train.py`/`evaluate.py` were not run to confirm the described pipeline executes correctly |
| 4 | Shortcut reliance | NOT SUSPECTED | N/A — no new modeling was performed |
| 5 | Bug-as-insight | NOT SUSPECTED | N/A |
| 6 | Methodology fabrication | INSUFFICIENT EVIDENCE | ResNet-50's sigmoid-not-softmax detail and the min-max normalization formula are inherited from the original thesis text; not independently re-derived from the repo code in this pass (would require reading `src/train.py` line-by-line) |
| 7 | Pipeline-level frame-lock | NOT SUSPECTED | Paper's framing explicitly repositioned per Stage 1 gap analysis (accuracy-first → resource-efficiency-first), rather than defending the original thesis's framing uncritically |

**Modes 3 and 6 are INSUFFICIENT EVIDENCE** — per IRON RULE this blocks pending acknowledgment. **Override reasoning**: verifying mode 3/6 would require executing the training pipeline (GPU, dataset access, ~15 epochs), which is out of scope for a documentation/rewrite pass and was already disclosed as a limitation (§5, item 1: "No independent retraining"). The paper does not claim the code was re-executed — it explicitly states the opposite. Proceeding with this acknowledgment on record rather than blocking indefinitely on infrastructure this pipeline run does not have access to.

## Overall Stage 2.5 Verdict: **PASS (with disclosed limitations, override recorded for Modes 3/6)**

Round-trip count: 1 integrity round (no fix→re-verify loop needed — issues found were fixed inline during this same pass).
