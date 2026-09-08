# n=29 Delta=16 — cumulative-threshold verifier

8 September 2026. Built during the restarted red-team audit as a deliberately separate final-stage model for the n=29, Delta=16 cases.

## Current status

**Use `independent_threshold_model_v2.py`, not `independent_threshold_model.py`.**

A hostile dimensional audit found a genuine normalization error in the first version of this verifier. The historical v1 source and its original certificates are retained for audit history but are **not valid proof evidence**.

The corrected v2 model was cleanly replayed and again rejects the full projected frontier with exact integer Farkas certificates. A later minimal trusted-kernel route also uses the corrected v2 model and closes a larger pre-projected residual frontier directly.

This remains same-assistant independent reimplementation, not external peer review.

## The v1 normalization defect

Labels are grouped by equal demand `s`; sources by equal residual degree `rho`.

The selected source/label incidence variable is normalized per source-label pair. On the label side, v1 accidentally multiplied the cumulative selected-degree tail capacity by the label-group multiplicity `n_g` a second time.

Schematically, the correct per-label identity is

```text
sum_k n_k Z_kg = sum_h T_h,
```

not

```text
sum_k n_k Z_kg = n_g * sum_h T_h.
```

When `n_g>1`, the v1 equation can overconstrain the relaxation. Therefore all v1 cumulative-threshold infeasibility certificates are invalidated as proof evidence.

The defect does **not** occur in the original direct197-derived n=29 route or the separate fully fresh n=29 Delta=16 implementation, both of which use different final-stage machinery.

The corrected implementation is:

- `independent_threshold_model_v2.py`.

The failure and correction are also recorded in `PUBLIC_RELEASE_AUDIT.md`.

## Purpose and independence boundary

The production n=29 route reduces the two dense Delta=16 scopes to 118 projected rows at `m=211` and 1,225 projected rows at `m=210`, then uses inherited n=28 joint/LP machinery.

The corrected cumulative-threshold verifier starts at that published projected frontier and replaces the later joint/shared/typed/endpoint machinery with a different relaxation derived directly from the hand inequalities.

It imports none of the inherited `joint`, shared-LP, degree-type, local-incidence, conditional-ledger or endpoint-model code.

The main idea is to avoid exact enumeration of the selected endpoint degree `x`. For a label option `(d,R)`, introduce cumulative tails

```text
T_h = Pr(x >= h).
```

Then

```text
E[x] = sum_h T_h,
```

and the selected-slot capacity among labels satisfying `x>=h` is

```text
E[x 1{x>=h}] = (h-1)T_h + sum_{j=h}^U T_j,
```

where `U=16-R`. Nested Hall inequalities use these capacities to host selected incidences whose source endpoint type requires a minimum `x`.

## Variables and necessary constraints

Labels are grouped only by equal demand `s`; sources only by equal residual degree `rho`. This is relabelling/averaging, not an automorphism assumption.

For each label demand group the model chooses a fractional distribution over integer `(d,R)` options satisfying:

- `0<=d<=10`;
- `0<=R<=16`;
- if `s>0`, `d-R=s`;
- if `s=0`, `d<=R`;
- `x<=16-R`, represented through cumulative tails;
- `x>=s` and `d<=R+x` through the option range and mandatory lower tails.

Globally:

```text
sum d = 2(r+t),
sum R = r.
```

For each residual source group the model chooses actual source types `(q,p)` satisfying

```text
0<=q<=12-rho,
0<=p<=rho+3,
q+p<=15.
```

A separate source-to-supplement `q`-flow enforces:

- a source of selected degree `q` sends exactly `q` selected arcs;
- a target source type receives its expected supplement indegree `p`;
- an arc from source degree `q` to target degree `q2` is allowed only if `rho_target+q2>=q-1`;
- each unordered B-pair has total orientation capacity at most one.

Selected source/label incidence flow is allowed only when the pointwise necessary conditions hold:

```text
s <= rho_source,
d <= rho_source+R,
d <= rho_source+q-1,
R+x >= q+p.
```

The last condition requires

```text
x >= max(1,q+p-R).
```

The corrected label-side incidence and cumulative-tail equations are per-label; group multiplicity is used only when summing over distinct labels or sources, not twice.

## Exact proof event

SciPy/HiGHS is only a proposal mechanism. Solver status alone is never a proof event.

For a numerically infeasible model, the proposed Farkas multipliers are scaled to integers. The exact checker accepts an exclusion only after direct integer arithmetic verifies that:

1. every inequality multiplier is nonnegative;
2. equality multipliers are signed integers;
3. the combined coefficient of every nonnegative primal variable is nonnegative;
4. the combined right-hand side is strictly negative.

## Corrected v2 projected-frontier replay

The corrected v2 clean replay gives:

- `m=211`, `t=3`: **118 / 118** exact rejections, zero survivors; RHS range **-795 to -40**;
- `m=210`, `t=2`: **1,225 / 1,225** exact rejections, zero survivors; RHS range **-999801 to -1**.

Every certificate is rebuilt and re-verified after aggregation.

See:

- `INDEPENDENT_THRESHOLD_REPORT.json` — schema `n29-independent-threshold-flow-complete-v2`;
- evidence commit `18937b3ef39b1f73bac1af718c3064b257b6e53d`.

## Minimal trusted-kernel route

A later hostile audit showed that the corrected v2 model can be used after a substantially simpler early pipeline. The preferred proof-critical route now avoids the old projected screen and joint/shared/typed/endpoint stages entirely.

The clean minimal-kernel result is:

- `m=211`: 72 retained demand profiles -> 126 residual rows -> **0 survivors**;
- `m=210`: 367 retained demand profiles -> 1,467 residual rows -> **0 survivors**.

All 1,593 late exclusions are exact integer Farkas contradictions under corrected v2.

See:

- `MINIMAL_KERNEL_REPORT.json`;
- `.github/workflows/n29-minimal-kernel.yml`;
- workflow run `34274211354`.

## Files

Current proof evidence:

- `independent_threshold_model_v2.py` — corrected model;
- `run_independent_threshold.py` — projected-frontier certificate runner using v2;
- `minimal_prepare.py` — reduced demand stage;
- `minimal_rows.cpp` — reduced residual-row scanner;
- `run_minimal_kernel.py` — direct corrected-v2 certificate runner;
- `.github/workflows/n29-independent-threshold.yml`;
- `.github/workflows/n29-minimal-kernel.yml`.

Historical only:

- `independent_threshold_model.py` — **flawed v1 normalization; do not use as proof evidence**.

## Audit interpretation

The corrected cumulative-threshold route is mathematically and programmatically distinct from the original direct197 joint/shared/typed/endpoint route. The separate fully fresh n=29 implementation provides another same-assistant reconstruction.

All of these still share the graph-to-demand/quasi-edge mathematics, and all were developed by the same assistant. They therefore reduce implementation/model risk but do **not** substitute for an independent mathematician or independent external reproduction.
