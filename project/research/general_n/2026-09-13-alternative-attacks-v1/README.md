# Alternative attacks v1 — quantifier correction and independent maximum-cut route

13 September 2026. **Research checkpoint. Candidate hand lemmas; external review and novelty assessment OPEN. The unrestricted Murty-Simon conjecture is not proved.**

## Why this branch exists

The shared-residual-budget continuation rejects 4,487 of 4,584 **stored selected patterns**, but adds no whole-state exclusions because another selected geometry may exist. This checkpoint changes the attack rather than merely tightening the same fixed-geometry inequalities.

Two lines are pursued:

1. **geometry quantification / selection-free structure:** remove or explicitly quantify the selected-representative choice;
2. **maximum-cut reformulation:** maintain a genuinely independent proof architecture as insurance against limitations of the canonical A/B model.

## New hand results

See [`SELECTION_FREE.md`](SELECTION_FREE.md).

### Raw candidate capacity

For a raw candidate quasi-edge `ui->w`, let `c_u` be the source's raw A-cross degree, `mu_u` its missing degree in `H[B]`, `C_i` the label's raw B-cross degree, and `d_i=d_F(i)`. Then

```text
d_i <= c_u-1,
C_i >= mu_u.
```

These hold before a global selected/residual representative system is fixed. They define a candidate-label set `K_u`. Every subset `U subset B` necessarily satisfies

```text
e(overline{H[B]}[U]) <= sum_(u in U) |K_u|.
```

With positive surplus, residual activity sharpens the right side to `sum min(c_u-1,|K_u|)`. These are selection-independent subset capacity conditions. Their reach over the frozen frontier has not yet been quantified.

### Selected excess pays for incoming load

For every selected incidence `ui` on a positive-demand label,

```text
p_u-rho_u+1 <= x_i-s_i.
```

Summing gives

```text
sum_u q_u^+ max(0,p_u-rho_u+1)
 <= sum_(i:s_i>0) x_i(x_i-s_i).
```

In the exact-demand case `x=s`, every active source therefore satisfies the sharp bound

```text
p_u <= rho_u-1.
```

Moreover every selected label at source `u` has raw B-degree in

```text
[q_u+p_u, rho_u+q_u-1].
```

This interval structure lets us constrain **all** selected geometries with fixed margins rather than one saved witness.

## First geometry-quantified payoff

[`MARGIN_CLASS_EXAMPLE.md`](MARGIN_CLASS_EXAMPLE.md) gives a hand proof for N34 state 227. Its saved exact-demand margins are

```text
rho = 1^7,2,3^10,
q   = 0^7,4,3,3,4,4,4,4,4,4,3,4,
x=s = 2^4,3^11.
```

The proof eliminates **every selected-set family** with those row/column margins. The obstruction uses the exact-demand incoming cap, source intervals, a mod-three incidence count, and total raw B-cross degree. [`verify_margin_example.py`](verify_margin_example.py) replays the arithmetic and writes [`MARGIN_CLASS_VERIFICATION.json`](MARGIN_CLASS_VERIFICATION.json).

This is strictly stronger than a fixed-pattern rejection, but it is **not a whole-state exclusion**: other `q`-vectors and `x>s` remain possible.

## Maximum-cut route

[`MAXCUT_ROUTE.md`](MAXCUT_ROUTE.md) records the exact identity

```text
e(G)=|X||Y|+I-M,
```

where `I` is the number of internal edges of a cut and `M` the missing cross-pairs. Thus `I<=M` for some cut would prove Murty-Simon.

Reconnaissance in [`MAXCUT_RECON.json`](MAXCUT_RECON.json) records zero violations among 728 D2C instances checked through order 12 and 2,226 sampled positive `C5` blow-ups. A short hand argument proves the cut inequality for every positive independent-set blow-up of `C5`.

A tempting direct injection from maximum-cut internal edges to uniquely witnessed cross nonedges is false; an independent public order-ten obstruction confirms this. The viable maximum-cut target is therefore aggregate charging/stability, not a one-edge/one-nonedge matching.

## Geometry-model programme

[`GEOMETRY_MODEL.md`](GEOMETRY_MODEL.md) records the hierarchy:

1. fixed `q,x`, quantify all selected sets;
2. variable `q`, exact demand `x=s`;
3. variable `q` and `x>=s`, charging escape to selected excess;
4. only then add shared residual/pair/exact-destination realization.

Optimization is discovery only. Negative solver statuses are never proof unless replaced by an exact certificate or hand argument.

## Direct small-graph challenge

[`verify_selection_free_small.py`](verify_selection_free_small.py) reconstructs the complement bridge directly on 728 D2C graphs and all 1,169 minimum-degree complement roots. It checks 3,856 candidate quasi-edges, 77,696 universal candidate-set subset inequalities and 2,338 deterministic representative systems for the selected-excess bound, with zero violations; see [`SELECTION_FREE_SMALL_CHECK.json`](SELECTION_FREE_SMALL_CHECK.json). None of those small roots has `t>0`, so the sharper positive-surplus `c_u-1` subset bound is **not** exercised by this finite challenge.

## Audit / failures

[`AUDIT.md`](AUDIT.md) explicitly records:

- why abstract 2x2 selected-incidence switches are **not** automatically legal graph-level representative switches;
- the failure of the naïve maximum-cut matching injection;
- the solver-status trust boundary;
- the precise claim level of the state-227 margin exclusion;
- the dependency of the new lemmas on the canonical bridge.

## Current status and next attack

Whole-state generalisation frontier remains unchanged:

```text
994 exclusions / 4,584 survivors.
```

The next priority on this branch is to use the selected-excess inequality to quantify alternative `q` and `x>s` choices, starting with the margin-class examples where fixed-geometry shared-budget failures are strongest. In parallel, test the raw candidate-capacity subset inequality on realizable small graphs and search for a scalar/degree projection that can be applied without knowing the full graph.
