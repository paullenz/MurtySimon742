# Type-compressed orientation Hall v1

**Updated 14 September 2026 through selected-excess research `94cbfd966f6fd913ad9f96bdc4b0ba835c530dbb` and reconciliation with interval-tail checkpoint `d1e20da87e8d8dcda3633e550b8b5556b6e7c9ee`.** External mathematical review, novelty assessment and genuinely independent third-party reproduction remain OPEN.

The earlier package README is preserved verbatim in [`README_EARLIER_2026-09-14.md`](README_EARLIER_2026-09-14.md), including historical audit totals and the state-226 band correction. Its old research priorities are superseded. For the latest frontier and restart obligations see [`CURRENT_STATE.md`](../../../../CURRENT_STATE.md).

## Exact structural chain

The earlier whole-type, quotient-flow, sharp-dominance, canonical-antichain and staircase results remain indexed in the archived README. Subsequent results include:

- [`CANONICAL_WITNESS_COMPATIBLE_COPY_EXACTNESS.md`](CANONICAL_WITNESS_COMPATIBLE_COPY_EXACTNESS.md) and [`CANONICAL_HALL_SLACK_EXPANSION.md`](CANONICAL_HALL_SLACK_EXPANSION.md): compatible-copy exactness and exterior residual expansion.
- [`Q_STRATIFIED_CROSSING_GAP_AUDIT.md`](Q_STRATIFIED_CROSSING_GAP_AUDIT.md): exact pointwise gap U_q-H=C_q, with preserved positive-gap examples.
- [`Q_STRATIFIED_MINCUT_EXACTNESS.md`](Q_STRATIFIED_MINCUT_EXACTNESS.md): equality of minimum exact/q-stratified Hall margins; this does not require C_q(M+)=0.
- [`Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md`](Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md) and [`Q_LAYER_THRESHOLD_NORMAL_FORM.md`](Q_LAYER_THRESHOLD_NORMAL_FORM.md): complete-type witnesses and exact cap-tail/order-statistic/rectangle formulas.
- [`BRIDGE_TWO_DEFECT_DECOMPOSITION.md`](BRIDGE_TWO_DEFECT_DECOMPOSITION.md) and [`SUMMED_Q_TAIL_PRESSURE.md`](SUMMED_Q_TAIL_PRESSURE.md): Q=r+2t+D0+Esel and weighted tail pressure.
- [`SELECTED_EXCESS_TAIL_LOSS_BUDGET.md`](SELECTED_EXCESS_TAIL_LOSS_BUDGET.md): exact short tail-count representation of selected-excess receiver loss and coupling to every Hall cut.

These concern the stated target-Hall model and graph-bridge assumptions, not graph realizability or an unrestricted proof. Consult individual audit files for completed scopes; local verification is not automatically completed remote CI.

## Selected losses and the interval synthesis

Set k=b-a-1>=0, E=Esel, z=#{i:s_i=0}, N(h)=#{u:q_u>=h}, and

```text
h_j=min(E,z)+floor(max(E-z,0)/j)+1,
L_E=sum_{j=1}^{k+1}N(h_j).
```

With additional potential-pair loss L_K, the necessary global budget is

```text
2t+D0+E+L_E+L_K<=bk.
```

For any source set A, exact Hall margin equals the remaining global budget plus demand outside A minus receiver vacancy V(A). This is an explicit reformulation of existing cap/Hall screens, not a new exclusion beyond them.

The [concurrent interval package](../2026-09-14-q-tail-interval-budget-v1/README.md) and its [synthesis](../2026-09-14-q-tail-interval-budget-v1/SELECTED_LOSS_SYNTHESIS.md) identify, for high-q tails, V=Omega+Xi: interval-unfillable capacity plus the exact reverse-compatibility correction. Its [committed local replay summary](../2026-09-14-q-tail-interval-budget-v1/REPLAY_SUMMARY.json) reports 205,919/205,919 frozen-pilot interval detections while preserving 32 strict interval/exact gaps. This is shared-generation local evidence, not universal exactness, a full-frontier scan or external reproduction.

Local selected-loss reproduction: [`verify_excess_tail_loss.py`](verify_excess_tail_loss.py), [`EXCESS_TAIL_LOSS_VERIFICATION.json`](EXCESS_TAIL_LOSS_VERIFICATION.json) and [`EXCESS_TAIL_LOSS_AUDIT.md`](EXCESS_TAIL_LOSS_AUDIT.md). PASS covers 179,375 pointwise identities, 171,504 exhaustive source sets and 10,000 random profiles. The audit retains its corrected regression fixture. Remote CI completion remains separate.

## Boundary and next proof obligation

[`MURTY_Q_TAIL_HALL_CONJECTURE.md`](MURTY_Q_TAIL_HALL_CONJECTURE.md) preserves failures of overbroad tail-sufficiency claims. z is NOT restricted by z<=E. Neither the current cap formula alone nor selected-incidence feasibility without the global ledger suffices. The full exact q-layer route remains available if a tail conjecture fails.

The next goal is a structural threshold-existence theorem from full bridge constraints, beyond scalar/incidence conditions already known to admit target-Hall passes. Preserve all older counterexamples, state-226 failures, positive C_q examples and verifier evidence. The canonical promoted frontier remains 3,607 survivors; the 2,655 recovered candidate exclusions remain behind their separate audit/promotion gate.
