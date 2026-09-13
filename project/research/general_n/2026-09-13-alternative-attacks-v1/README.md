# Alternative attacks v1 — quantifier correction, state-227 closure and independent maximum-cut route

13 September 2026. **Research checkpoint. Candidate hand lemmas and exact finite reductions; external review, novelty assessment and independent reproduction remain OPEN. The unrestricted Murty–Simon conjecture is not proved.**

## Why this branch exists

The shared-residual-budget continuation rejects 4,487 of 4,584 **stored selected patterns**, but initially added no whole-state exclusions because another selected geometry might exist. This branch therefore changes the attack rather than merely tightening the same fixed-geometry inequalities.

The programme has two lines:

1. **geometry quantification / selection-free structure:** remove or explicitly quantify the selected-representative choice;
2. **maximum-cut reformulation:** maintain a genuinely independent proof architecture as insurance against limitations of the canonical A/B model.

The first line has now produced its first whole-state payoff: **N34 state 227 is excluded for every admissible `q`, every selected geometry and every selected-excess profile.**

## Selection-free and excess lemmas

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

With positive surplus, residual activity sharpens the right side to `sum min(c_u-1,|K_u|)`.

### Selected excess pays for incoming load

For every selected incidence `ui` on a positive-demand label,

```text
p_u-rho_u+1 <= x_i-s_i.                              (1)
```

Summing gives

```text
sum_u q_u^+ max(0,p_u-rho_u+1)
 <= sum_(i:s_i>0) x_i(x_i-s_i).
```

In the exact-demand case `x=s`, every active source therefore satisfies

```text
p_u <= rho_u-1.
```

Moreover every selected label at source `u` has raw B-degree in

```text
[q_u+p_u, rho_u+q_u-1].
```

### Threshold form

Equation (1) has a useful quantifier-free threshold consequence. Put

```text
e_i=x_i-s_i,
h_l=#{i:e_i>=l}.
```

If a source has

```text
p_u-rho_u+1 >= l,
```

then all of its `q_u` distinct selected labels have excess at least `l`, hence

```text
q_u<=h_l.
```

Equivalently,

```text
q_u>h_l => p_u<=rho_u+l-2.                            (2)
```

This family is general. The state-227 closure below already succeeds using only `l=2` in the high-excess tail.

## State 227: from one margin class to a whole-state exclusion

The progression is now completely preserved:

1. [`MARGIN_CLASS_EXAMPLE.md`](MARGIN_CLASS_EXAMPLE.md) excluded every selected geometry for one saved exact-demand `(q,x)` margin class.
2. [`EXACT_DEMAND_ALL_Q.md`](EXACT_DEMAND_ALL_Q.md) excluded exact demand `x=s` for **every** source selected-degree vector `q`.
3. [`LOW_EXCESS_LAYERS.md`](LOW_EXCESS_LAYERS.md) excluded `E=sum(x_i-s_i)=1,2,3`.
4. [`EXCESS_SWEEP_TO_8.md`](EXCESS_SWEEP_TO_8.md) extended this through `E=8`, including hand rigidity for the two equality profiles.
5. [`STATE_227_WHOLE_STATE.md`](STATE_227_WHOLE_STATE.md) now closes **all remaining excess** and therefore the whole scalar state.

The state data are

```text
a=15, b=18, t=1,
s=2^4,3^11,
rho=1^7,2,3^10,
r=39,
S=41.
```

Write `E=sum_i(x_i-s_i)` and `Q=41+E`.

### Exact profile sweep: E=0,...,20

[`verify_state227_exact_to20.cpp`](verify_state227_exact_to20.cpp) checks every excess profile up to permutation within the two demand classes. The complete totals are

```text
49,847 profiles,
40,548 strict endpoint/excess exclusions,
9,297 source-infeasible profiles,
2 equality profiles.
```

The equality profiles are exactly the earlier E=6 and E=7 cases and are excluded by the preserved hand endpoint-rigidity arguments. Thus any realization would need `E>=21`.

### High-excess tail: E=21,...,34

Let

```text
h=#{i:e_i>=2}.
```

For a `rho=3` source, (1) gives

```text
p_u>=4 => q_u<=h,
```

hence the safe relaxed cap

```text
p_u<=5 if q_u<=h,
p_u<=3 if q_u>h.
```

The seven `rho=1` sources absorb at most 21 incoming selections. For every source-degree vector and every h, [`verify_state227_tail.cpp`](verify_state227_tail.cpp) exactly minimizes the source load and exactly maximizes the allowed top-k endpoint correction over all label excess allocations.

Every layer `E=21,...,34` is strictly impossible. The minimum contradiction gaps above the necessary endpoint envelope are:

```text
E=21:  8     E=22: 13     E=23: 14     E=24: 15
E=25: 15     E=26: 15     E=27: 15     E=28: 26
E=29: 32     E=30: 40     E=31: 44     E=32: 39
E=33: 34     E=34: 56
```

Finally the basic incoming caps give

```text
sum p_u <= 7*3 + 1*4 + 10*5 = 75,
```

whereas `sum p_u=Q=41+E`. Therefore `E>=35` is impossible independently.

Hence **state 227 has no realization**. The machine-readable summary is [`STATE_227_WHOLE_STATE_VERIFICATION.json`](STATE_227_WHOLE_STATE_VERIFICATION.json).

## Frontier update

State 227 was one of the 4,584 survivors of the frozen compatible-routing generalisation frontier. Its exclusion changes the record to

```text
995 exclusions / 4,583 survivors,
```

split as

```text
4,505 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

This is a generalisation-frontier update. The separate fixed-order N34 proof candidate was already closed and is unchanged.

## Maximum-cut route

[`MAXCUT_ROUTE.md`](MAXCUT_ROUTE.md) records the exact identity

```text
e(G)=|X||Y|+I-M,
```

where `I` is the number of internal edges of a cut and `M` the missing cross-pairs. Thus `I<=M` for some cut would prove Murty–Simon.

Reconnaissance in [`MAXCUT_RECON.json`](MAXCUT_RECON.json) records zero violations among 728 D2C instances checked through order 12 and 2,226 sampled positive `C5` blow-ups. A short hand argument proves the cut inequality for every positive independent-set blow-up of `C5`.

A tempting direct injection from maximum-cut internal edges to uniquely witnessed cross nonedges is false; an independent public order-ten obstruction confirms this. The viable maximum-cut target is aggregate charging/stability, not a one-edge/one-nonedge matching.

## Geometry-model programme

[`GEOMETRY_MODEL.md`](GEOMETRY_MODEL.md) records the hierarchy:

1. fixed `q,x`, quantify all selected sets;
2. variable `q`, exact demand `x=s`;
3. variable `q` and `x>=s`, charging escape to selected excess;
4. add shared residual/pair/exact-destination realization only after those quantifiers are controlled.

State 227 has now passed through all three first levels to a whole-state exclusion.

Optimization remains discovery only. Negative solver statuses are never proof unless replaced by exact arithmetic or a hand argument.

## Direct small-graph challenge

[`verify_selection_free_small.py`](verify_selection_free_small.py) reconstructs the bridge directly on 728 D2C graphs and all 1,169 minimum-degree complement roots. It checks 3,856 candidate quasi-edges, 77,696 universal candidate-set subset inequalities and 2,338 deterministic representative systems for the selected-excess bound, with zero violations. None of those small roots has `t>0`, so the sharper positive-surplus candidate-capacity bound is not exercised by that finite challenge.

## Audit / failures

[`AUDIT.md`](AUDIT.md) records:

- why abstract 2x2 selected-incidence switches are not automatically legal graph-level representative switches;
- the failure of the naïve maximum-cut matching injection;
- the solver-status trust boundary;
- the dependency of the excess lemmas on the canonical bridge;
- the distinction between fixed-pattern, margin-class and whole-state exclusions;
- the state-227 closure and its two non-strict low-excess profiles.

## Current status and next attack

The whole-state generalisation frontier is now

```text
995 exclusions / 4,583 survivors.
```

The next priority is to apply the threshold family

```text
q_u>h_l => p_u<=rho_u+l-2
```

systematically to the remaining frozen frontier, beginning with `l=1,2,3` and retaining the top-k endpoint envelope. The aim is to discover whether state 227 is an isolated success or the first member of a sizeable family of whole-state exclusions.

In parallel, continue the raw candidate-capacity projection and retain the maximum-cut route as an independent architecture. Do not revert to fixed-pattern refinement as the default attack unless a quantified margin/profile restriction first justifies it.
