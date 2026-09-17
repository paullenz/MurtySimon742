# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has D>=12. Scope work now has a general quadratic endpoint-load ledger, obtained by retaining the exact selected row degrees `q_u`, and a hand closure of the entire zero-excess mixed demand-4/5 near-Turán h>=5 band at `(a,b,t)=(20,23,2)`.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_QUADRATIC_ENDPOINT_MIXED45_CLOSURE_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Critically reassessed the proposed Hall-aware mixed-demand census before executing it. The more important information loss was earlier: the recent endpoint/Hall projections retained only `q_u>0 => some selected incidence`, whereas the canonical bridge defines `q_u` to be the **exact number of selected edges sourced at u**. Restoring that exact row multiplicity makes endpoint load accumulate quadratically and eliminates the whole targeted zero-excess mixed 4/5 band without a histogram scan.

**INSPECTED PREDECESSOR:** `841bb39eed9fa632601dc71894592b0f11c8d63f`, confirmed current `main` before this transaction. Its selected-witness Hall theorem, uniform h=5 closure, excess-aware source envelope, common-margin cut, scalar obstruction, staircase/heavy-load theory, five-label D>=12 theorem and canonical counts remain preserved and unchanged.

**GENERAL LAST RESULT:** on every selected incidence `ui`, endpoint load gives `C_i=R_i+x_i >= p_u+q_u`. Because label `i` occurs in exactly `x_i` selected incidences and source `u` occurs in exactly `q_u` selected incidences, summing over the actual selected incidence matrix gives the general canonical-bridge inequality

`sum_i x_i(R_i+x_i) >= sum_u q_u(p_u+q_u)`.

This is not a one-witness inequality: every one of the `q_u` selected incidences at source `u` pays the full endpoint threshold `p_u+q_u`.

**BOUNDED CLOSURE:** fix `a=20,b=23,t=2`, zero selected excess `x_i=s_i`, and all twenty demands in `{4,5}`. Let `k` be the number of demand-five labels. Then `Q=80+k` and, because all demands are positive and `x=s`, the exact ledger gives `r=Q-2t=76+k`. Assume at least five residual sources have `rho>=5` (in particular this covers residual h-index five).

The label side of the quadratic endpoint ledger satisfies

`sum_i x_i(R_i+x_i) <= U(k)=624+13k+min(18k,76+k)`.

The source side admits the local support inequality

`10p_u+15q_u-q_u(p_u+q_u) <= 10rho_u+20+delta_k [rho_u=4]`,

where `delta_k=6` for `k<=14`, `delta_15=5`, `delta_16=2`, and `delta_k=0` for `k>=17`. Summing, using `sum p=sum q=Q`, yields

`sum_u q_u(p_u+q_u) >= 780+15k-delta_k c_4`,

with `c_4=#{u:rho_u=4}`. Positive residual activity plus five sources of residual degree at least five gives

`c_4 <= floor((33+k)/3)`.

The resulting source lower bound is strictly larger than `U(k)` for **every `k=0,...,20`**. Representative smallest gaps are still strict: k=14 gives 900>896; k=15 gives 925>910; k=16 gives 988>924. Therefore no canonical bridge profile exists in this entire zero-excess mixed 4/5 band. The previous uniform demand-four band is a special case `k=0`; heavy-load, staircase, common-margin and witness-Hall machinery are not needed for this stronger bounded conclusion.

**AUDIT:** `project/research/general_n/2026-09-17-quadratic-endpoint-v1/QUADRATIC_ENDPOINT.md` contains the hand proof. `check_quadratic_endpoint.py` independently enumerates every local integer `(p,q)` state for `rho=1..20` and `k=0..20`, verifies the exact support constants, and checks every global arithmetic gap. Local replay returned `PASS_QUADRATIC_ENDPOINT`. This remains internal derivation/replay; external mathematical review is open.

**STEP-BACK CONSEQUENCE:** the newest Hall theorem remains valid and useful, but it was not the right first tool for this frontier. The exact selected row/column multiplicities are stronger and should be retained before projecting to one-witness Hall or one-source envelopes. At the target `(20,23,2)` h>=5 scope, any remaining obstruction must now leave the zero-excess `{4,5}` band — most naturally through **positive selected excess**, a demand outside `{4,5}`, or a different residual geometry. The next high-value structural target is a weighted/excess version of the quadratic endpoint ledger, not a broad survivor census.

**FIVE-LABEL STATUS:** every actual whole exact block `|T|=|H|=5` still satisfies `D>=12`, hence `W>=37` or `W>=57` with extras.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No canonical catalogue scan, q-enumeration or theorem promotion.

**PRESERVATION:** quadratic endpoint theorem/application/checker are in `project/research/general_n/2026-09-17-quadratic-endpoint-v1/`; selected-witness Hall remains in `2026-09-17-selected-witness-hall-v1/`; the uniform-band package remains in `2026-09-17-h5-uniform-band-v1/`; the excess-aware envelope remains in `2026-09-17-excess-aware-endpoint-v1/`. Earlier proofs, obstructions and failed routes remain preserved.

**UNPRESERVED WORK:** None for the quadratic endpoint theorem/application after remote writes and local replay.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: step back again and attack positive selected excess using the exact selected row multiplicities. Seek a weighted extension of `sum x_i C_i >= sum q_u(p_u+q_u)` that trades the larger label-side budget created by excess against the selected-excess condition `e_i>=max(0,p_u-rho_u+1)` on **all q_u selected incidences**. Prefer a hand excess-penalty inequality or an exact incidence-level transport lemma; only enumerate a bounded positive-excess frontier after deriving that structural projection. Preserve strictness examples and failed coefficient choices.
<!-- CURRENT-STATUS:END -->
