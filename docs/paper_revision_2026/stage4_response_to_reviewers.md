# Response to Reviewers — Round 1

| # | Item | Priority | Status | Where addressed |
|---|------|----------|--------|------------------|
| 1 | DA-CRITICAL: resource-efficiency framing unmeasured | P0 | **Addressed** | New §3.5 parameter-count comparison (~6.67M vs 23.5M, ~3.5×); §4.4 and Conclusion reframed to "partially-substantiated" claim; new Limitation 7 (no inference-time/memory measurement) |
| 2 | ResNet-50 sigmoid/softmax confound moved into Results, not just Limitations | P0 | **Addressed** | §3.4 expanded with explicit validity-threat statement; §4.1 Table 1 gets a "Statistical caveat" paragraph; new Limitation 9 |
| 3 | No significance test for accuracy comparison | P1 | **Addressed (disclosed, not resolved)** | §4.1 caveat paragraph + new Limitation 8: per-image records unavailable to compute retroactively; language softened from "outperforming" to "directional comparison" throughout (Abstract, §4.1, Conclusion) |
| 4 | Three-class vs four-class clinical distinction for [10] | P1 | **Addressed** | §2.2 sentence added explaining why 3-class and 4-class tasks aren't comparable |
| 5 | Preprocessing citation currency (Nayak et al. 2020) | P2 | **Addressed (disclosed gap)** | §3.2 footnote-style sentence acknowledging the 2022-2026 search didn't cover preprocessing literature |
| 6 | Consider reframing as technical note vs. full journal article | P2 (advisory, not mandated) | **Not applied** | Kept as full journal-article format per original scope decision; flagged to user as an open editorial choice rather than resolved unilaterally |

## Reviewer disagreement handling

No REVIEWER_DISAGREE status needed this round — all P0/P1 items were substantively actionable without contesting reviewer judgment. Item 6 (R1's suggestion) is acknowledged but not acted on, since it is a scope/format decision outside what a revision pass should decide unilaterally; noted for the user rather than silently applied or silently dropped.

## Net effect on paper's claims

The paper's central claim shifted from an implicit "resource-efficient and interpretable" framing to an explicit "partially measured (parameter count), partially unmeasured (inference/deployment), directional (not statistically significant) comparison" framing. This is a narrower, more defensible claim than Round 1's draft made, consistent with the DA's core challenge — we did not manufacture new experimental evidence, we scoped the claim to match the evidence that actually exists.
