# n=29 reviewer-v4: threshold-tail hand simplification

11 September 2026.

This directory is the current reviewer-facing n=29 proof checkpoint. It supersedes reviewer-v3 as the preferred logical route while leaving reviewer-v3 and all earlier packages frozen.

## Headline change

For `Delta=16`, write `t=e(G)-208`. The bridge and threshold-capacity lemma imply

```text
Q(s) >= 16+2t,
```

while the new hand threshold-tail lemma proves

```text
Q(s) <= 18.
```

Therefore `t<=1`. In particular, **every Delta=16 graph with `e(G)>=210` is impossible**.

This removes all proof-critical N29 Delta=16 computation from the candidate theorem. The corrected minimal-kernel/Farkas route remains preserved as separately implemented internal corroboration.

## Start here

- [`PROOF.md`](PROOF.md) - assembled reviewer-v4 candidate proof.
- [`VERIFICATION_COMPANION.md`](VERIFICATION_COMPANION.md) - dependency map, exact regressions and audit boundary.
- [`REDTEAM_HARDENING.md`](REDTEAM_HARDENING.md) - non-blocking self-containedness hardening after the hostile v4 audit.
- [`../2026-09-11-reviewer-v4-redteam-v1/REPORT.md`](../2026-09-11-reviewer-v4-redteam-v1/REPORT.md) - full hostile audit; no blocking flaw found.
- [`../../../research/general_n/2026-09-11-threshold-tail-collapse-v1/N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md`](../../../research/general_n/2026-09-11-threshold-tail-collapse-v1/N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md) - detailed hand tail lemma.
- [`../2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md`](../2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md) - frozen self-contained graph-to-model bridge used by v4.
- [`../2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json`](../2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json) - historical corrected computational cross-check.

## Latest hostile audit

A fresh same-assistant hostile audit reconstructed the proof without treating the historical LP/Farkas stack as a dependency. A separately specified exact checker exhaustively rechecked all `1,352,078` demand multisets, every clipping stage, the threshold-capacity algebra, the Delta=15 witness maxima, the Delta=17 pointwise bound and the Delta=18..27 h-index arithmetic. GitHub Actions run `34621982241` passed.

This is **internal robustness evidence**, not external independent verification.

## Status

**Complete candidate at n=29; independent mathematical review, novelty assessment and independent reproduction remain OPEN.**

The highest-value review target is now the short universal bridge/threshold-capacity chain plus the hand clipping proof, not the historical late LP embedding.
