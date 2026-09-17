# Current structural review — 17 September 2026

The project now has two complementary structural layers.

## 1. Five-label exact block

[Five-label defect eleven is impossible](project/research/general_n/2026-09-17-d5-defect11-closure-v1/THEOREM.md) proves, under the whole-level exact-block hypothesis |T|=|H|=5,

    D >= 12,
    W >= 37,
    extras => W >= 57.

The preceding exact support-cover and pair-coverage packages supply the critical-edge machinery and independent finite checks. D=12 attainability, sharpness and external acceptance remain open.

## 2. Scope bridge via h-index saturation

[Residual h-index saturation and the exact-block equality face](project/research/general_n/2026-09-17-hindex-saturation-v1/HINDEX_SATURATION.md) revisits the general residual h-index argument. If h is the residual h-index, |{rho>=h}|=h+u, and k labels have demand h, then

    b+2t <= (a-h-u)(h-1)+k.

Equivalently, the older h-index upper bound loses exactly the explicit stability term `a-k+u(h-1)`. When u=0, receiver containment forces k<=h; k=h is precisely the square exact block. Thus the exact-block theorem is now identified as a sharp saturation face rather than an isolated hypothesis.

For h=5,u=0, the top source-saturated value `b+2t=4a-15` forces k=5, while the non-square case is at most 4a-16.

**Status:** internal candidate mathematics. The next general task is to control u>0 by coupling source omissions and destinations. Exact-block coverage is therefore narrowed but not solved. Canonical counts remain 4626 exclusions / 952 survivors / 3632 whole-state closures; no unrestricted Murty-Simon proof or catalogue promotion is claimed.

Use [CURRENT_STATE.md](CURRENT_STATE.md) for the live operational handoff. All earlier proofs, verifiers, failed routes and review material remain preserved.
