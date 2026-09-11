# n=30 Fan-free reviewer package v2

**Current PDF reviewer edition - 9 September 2026, with 11 September analytic hardening.**

Claim: `e(G) <= 225, equality exactly K(15,15)`.

Start with [N30_Reviewer_Manuscript_v2.pdf](N30_Reviewer_Manuscript_v2.pdf), then [N30_Verification_Companion_v2.pdf](N30_Verification_Companion_v2.pdf).

The v2 PDF proof remains valid. Later pointwise charging caps reduce its computational dependency surface: every `Delta=17` scope with `m>=228` and every `Delta=16` scope with `m>=234` are now excluded analytically, so those historical zero-domain scans are corroborative rather than proof-critical. See [`ANALYTIC_HARDENING_2026-09-11.md`](../../project/reviews/n30/2026-09-09-fan-free-v2/ANALYTIC_HARDENING_2026-09-11.md) and the cross-order [`POINTWISE_CAPS.md`](../../project/research/fan-free-fixed-orders/2026-09-11-pointwise-analytic-caps-v1/POINTWISE_CAPS.md).

Fan's 1987 theorem is retained for historical attribution but is **not a logical dependency** of this edition. The previous [`n30-reviewer-v1`](../n30-reviewer-v1/README.md) package remains preserved unchanged as historical provenance.

No external acceptance or formal verification is claimed.