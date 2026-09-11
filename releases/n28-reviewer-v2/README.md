# n=28 Fan-free reviewer package v2

**Current PDF reviewer edition - 9 September 2026, with 11 September analytic hardening.**

Claim: `e(G) <= 196, equality exactly K(14,14)`.

Start with [N28_Reviewer_Manuscript_v2.pdf](N28_Reviewer_Manuscript_v2.pdf), then [N28_Verification_Companion_v2.pdf](N28_Verification_Companion_v2.pdf).

The v2 PDF proof remains valid. A later hand simplification reduces its computational dependency surface: for `Delta=15`, every scope with `m>=203` follows analytically from the pointwise charging cap, so the historical zero-domain computation over `m=203..210` is now corroborative rather than proof-critical. See [`ANALYTIC_HARDENING_2026-09-11.md`](../../project/reviews/n28/2026-09-09-fan-free-v2/ANALYTIC_HARDENING_2026-09-11.md) and the cross-order [`POINTWISE_CAPS.md`](../../project/research/fan-free-fixed-orders/2026-09-11-pointwise-analytic-caps-v1/POINTWISE_CAPS.md).

Fan's 1987 theorem is retained for historical attribution but is **not a logical dependency** of this edition. The previous [`n28-reviewer-v1`](../n28-reviewer-v1/README.md) package remains preserved unchanged as historical provenance.

No external acceptance or formal verification is claimed.