# Type-compressed orientation Hall v1

**Updated 14 September 2026 through research commit `94cbfd966f6fd913ad9f96bdc4b0ba835c530dbb`.** Candidate structural package. External mathematical review, novelty assessment and genuinely independent third-party reproduction remain OPEN.

The former package README is preserved verbatim as [`README_EARLIER_2026-09-14.md`](README_EARLIER_2026-09-14.md), including historical audit totals, the state-226 correction and earlier priorities. Its statement that compatible-copy aggregation is the next unfinished theorem is historical, not the current research checkpoint. For the canonical finite frontier and live restart obligations see [`CURRENT_STATE.md`](../../../../CURRENT_STATE.md).

## Current exact route

The earlier chain remains indexed in the archived README: whole-type compression, exact quotient max-flow, sharp dominance, canonical antichain, moving staircase, coarse-band failure and compatible-copy refinement. Subsequent exact aggregation is in [`CANONICAL_WITNESS_COMPATIBLE_COPY_EXACTNESS.md`](CANONICAL_WITNESS_COMPATIBLE_COPY_EXACTNESS.md); exterior residual expansion is in [`CANONICAL_HALL_SLACK_EXPANSION.md`](CANONICAL_HALL_SLACK_EXPANSION.md).

The current route then uses:

1. [`Q_STRATIFIED_CROSSING_GAP_AUDIT.md`](Q_STRATIFIED_CROSSING_GAP_AUDIT.md): the exact pointwise gap U_q-H=C_q, including preserved positive-gap examples.
2. [`Q_STRATIFIED_MINCUT_EXACTNESS.md`](Q_STRATIFIED_MINCUT_EXACTNESS.md): equality of the minimum exact and q-stratified Hall margins under fixed-q cap monotonicity. This does NOT require C_q(M+)=0.
3. [`Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md`](Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md): complete-type witnesses suffice for the q-stratified minimum.
4. [`Q_LAYER_THRESHOLD_NORMAL_FORM.md`](Q_LAYER_THRESHOLD_NORMAL_FORM.md): exact cap-tail, source-order-statistic and rectangle-count formula, with frozen local finite verification.
5. [`BRIDGE_TWO_DEFECT_DECOMPOSITION.md`](BRIDGE_TWO_DEFECT_DECOMPOSITION.md): Q=r+2t+D0+Esel, separating zero-demand deficit from selected excess.
6. [`SUMMED_Q_TAIL_PRESSURE.md`](SUMMED_Q_TAIL_PRESSURE.md): weighted tail pressure and exact top-compatible moments.
7. [`SELECTED_EXCESS_TAIL_LOSS_BUDGET.md`](SELECTED_EXCESS_TAIL_LOSS_BUDGET.md): exact short tail-count representation of selected-excess cap loss and its coupling to every Hall cut.

These are results about the target-Hall model under their stated hypotheses. They do not establish graph realizability or the unrestricted conjecture. Earlier completed audit scopes remain documented in their own files; new local verification is not automatically completed remote CI.

## New exact budget

Put k=b-a-1>=0, E=Esel, z=#{i:s_i=0}, N(h)=#{u:q_u>=h}, and

```text
h_j=min(E,z)+floor(max(E-z,0)/j)+1,
L_E=sum_{j=1}^{k+1}N(h_j).
```

With additional potential-pair loss L_K, the exact global cap budget is

```text
2t+D0+E+L_E+L_K<=bk.
```

For every source set A0,

```text
H(A0)-D(A0)
 = bk-(2t+D0+E)-L_E-L_K+q_out(A0)-V(A0).
```

V is capacity unused by A0. The next analytic target is a lower bound on V-q_out beyond the available budget on hypothetical counterexample branches. This is a structural reformulation of existing cap/Hall screens, not a claim of new exclusions beyond those screens.

Reproduction: [`verify_excess_tail_loss.py`](verify_excess_tail_loss.py), [`EXCESS_TAIL_LOSS_VERIFICATION.json`](EXCESS_TAIL_LOSS_VERIFICATION.json), and [`EXCESS_TAIL_LOSS_AUDIT.md`](EXCESS_TAIL_LOSS_AUDIT.md). Local PASS covers 179,375 pointwise identities, 171,504 exhaustive source sets and 10,000 random profiles. The audit preserves its regression-fixture correction. The committed CI workflow is not being represented as a completed remote replay.

## High-q-tail boundary and queued work

The frozen 812 difficult profiles all have deficient high-q tails. The stronger universal claim is NOT proved. The [red-team correction](https://github.com/paullenz/MurtySimon742/commit/93c9e8995c57e69c238396f20641a0dc84bb4754) preserves failures under arbitrary monotone caps, the current cap formula alone and selected-incidence feasibility without the global bridge ledger. z is not constrained by z<=E.

At the last check in the recovery session, the full high-q-tail pilot `34876612516` and corrected minimum-cut replay `34878019517` remained queued. Do not claim full-pilot tail sufficiency or completed new CI from them. The finite 2,655-candidate relational cross-audit also remained queued, and the canonical frontier is unchanged at 3,607 survivors.

## Preservation and trust boundary

Preserve the earlier 812 global-layer false negatives, state-226 coarse-band exception, positive pointwise C_q examples, non-tail witnesses, ledger-domain failures and all associated verifier code. None is contradicted by equality of q-stratified minima. A failed tail conjecture would not invalidate the full exact q-layer threshold route.

The graph-to-constraint bridge, selected/quasi-edge injection and forcing remain high-value external-review targets. Hand derivation, local finite checks, internal alternative implementation, remote CI and external acceptance remain distinct.
