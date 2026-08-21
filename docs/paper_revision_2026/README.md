# Pipeline Manifest — Brain Tumor Classification Paper (NSU Thesis → Journal Revision)

Committed to `docs/paper_revision_2026/` in this repo. Original thesis stays at `docs/thesis-report.docx` / `.pdf`, unchanged.

| Stage | File | Status |
|---|---|---|
| 1 | `stage1_research_brief.md` | 9-source 2023-2026 lit update, gap analysis |
| 2 | `paper.md` | Full rewrite (round 1) |
| 2.5 | `stage2_5_integrity_report.md` | PASS, Mode 3/6 override recorded |
| 3 | `stage3_review_round1.md` | 5-reviewer panel, MAJOR REVISION, DA-CRITICAL validated |
| 4 | `paper.md` (revised in place) + `stage4_response_to_reviewers.md` | All P0/P1/P2 items addressed |
| 3' | `stage3prime_rereview.md` | VERIFIED all items, no Stage 4' needed |
| 4.5 | `stage4_5_final_integrity.md` | PASS, zero blocking issues |
| 5 | `paper.tex`, `paper.docx`, `paper.md` (= final MD) | See below |
| 6 | Skipped | Optional Stage 6 process-summary requires interactive terminal acknowledgement; deferred |

## Stage 5 output status

- **Markdown**: `paper.md` — final content, this is the source of truth.
- **DOCX**: `paper.docx` — generated directly via python-docx (Pandoc not installed in this environment). Structurally complete (headings, sections, references) but does not carry LaTeX-level typographic polish (equations rendered as plain text, e.g. "r = (d - mn) / (mx - mn)" rather than a typeset fraction).
- **LaTeX**: `paper.tex` — full IEEEtran-class source with proper equations, table, bibliography, bilingual abstract (CJK package for zh-TW). This is the highest-fidelity output.
- **PDF**: **not produced.** No LaTeX engine (pdflatex/xelatex/tectonic) or Pandoc is installed in this environment. Per pipeline rule, PDF must be compiled from LaTeX — HTML-to-PDF conversion is prohibited, so no substitute was generated instead of silently failing this requirement.
  - **To get the PDF**: either (a) install a LaTeX distribution (e.g., MiKTeX or TeX Live) and run `pdflatex paper.tex` twice (bibliography needs a second pass), or (b) upload `paper.tex` to Overleaf and compile there — it uses the standard IEEEtran class, no exotic packages beyond CJKutf8 for the Chinese abstract.

## Honest summary of what this pipeline run actually did vs. didn't do

**Did**: rewrote thesis prose from scratch (no paraphrase-tool artifacts), reconciled 4 contradicting accuracy figures into 1 defensible number with shown reasoning, discarded off-topic Conclusion content, fixed a misapplied citation, added and CrossRef-verified 8 new 2023-2026 references, ran a full 5-reviewer simulated peer review that found and forced correction of an overclaimed "resource-efficiency" framing, added a genuine new architecture-level measurement (parameter count) to partially substantiate that framing, and disclosed every remaining gap explicitly in a 9-item Limitations section.

**Didn't do** (by design, disclosed throughout): retrain any model, measure inference time/memory, run a statistical significance test, or independently verify the original thesis's raw experimental logs (they don't exist in the repo — `results/` is empty). These are stated as Future Work, not hidden.

**Bottom line**: this is a defensible, honestly-scoped revision of a thesis with known data problems — not a paper claiming more than the available evidence supports. If you want the accuracy/significance/resource claims fully substantiated rather than disclosed-as-gaps, the model needs to actually be retrained, which is outside what this pipeline run had access to do.
