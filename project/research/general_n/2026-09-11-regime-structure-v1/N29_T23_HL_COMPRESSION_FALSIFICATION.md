# n=29, t=2,3: falsification of `(h_res,L)` compression and a three-scalar repair

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact finite structural diagnostic inside the already-preserved RX-Hall frontiers. This is not a general-N theorem and does not alter the independent-review trust boundary of the graph-to-profile/RX-Hall bridge or the potential lemmas.**

## Question

The supplement-cap refinement has the exact scalar-cutoff form

```text
q*_u = min(C_u,L),
C_u = min(12-rho_u, #{i:s_i <= rho_u}),
L = max{k>=1 : #{u:rho_u+C_u >= k-1} >= k+1}.
```

This makes it natural to ask whether the exact scalar-template regime of a frontier profile is already determined by two coarse source statistics:

```text
h_res = max{k : #{u:rho_u >= k} >= k},
L     = supplement cutoff above.
```

The answer is **no**, decisively.

## Exact input frontiers

The canonical audited n=29 regeneration was used:

```text
project/reviews/n29/2026-09-08-redteam-restart-v1/minimal_prepare.py
project/reviews/n29/2026-09-08-redteam-restart-v1/minimal_rows.cpp
```

The resulting positive-demand frontiers are the same ones consumed by the preserved exact rational template replays:

- `t=2`: 902 profiles, with exact deterministic labels `T0,T1,T2` from the already-verified unit-demand regime assignment;
- `t=3`: 94 profiles, with exact deterministic labels `A0,A1,A38,A530` from `n29_t3_count_tree_four_templates_exact.py`.

The labels used below are therefore not fitted classifier labels: each is an assignment to a preserved exact rational template already checked to have positive exact `fractions.Fraction` gap on the corresponding profile.

## 1. `(h_res,L)` fails already at t=2

Across all 902 exact `t=2` profiles only five `(h_res,L)` pairs occur:

| `(h_res,L)` | profiles | exact template labels in the cell |
|---|---:|---|
| `(4,6)` | 132 | `T0:1, T1:21, T2:110` |
| `(4,7)` | 94 | `T1:4, T2:90` |
| `(4,8)` | 11 | `T2:11` |
| `(5,7)` | 664 | `T1:51, T2:613` |
| `(5,8)` | 1 | `T2:1` |

Thus three of the five cells are mixed, and the cell `(4,6)` contains **all three necessary exact regimes**.

### Strongest falsification: the exact lower-bound triangle collapses to one pair

The preserved incompatibility triangle proving that fewer than three scalar templates do not suffice at `t=2` consists of profile indices `0`, `3`, and `77`. They are respectively `T0`, `T1`, and `T2` witnesses. All three have

```text
(h_res,L) = (4,6).
```

Their elementary unit counts are:

| profile | regime | demand id | `rho_1=#{u:rho_u=1}` | `nu_1=#{i:s_i=1}` | `(h_res,L)` |
|---:|---|---:|---:|---:|---|
| 0 | `T0` | 45 | 9 | 2 | `(4,6)` |
| 3 | `T1` | 70 | 9 | 1 | `(4,6)` |
| 77 | `T2` | 154 | 9 | 0 | `(4,6)` |

This is a direct finite obstruction to any claim that `(h_res,L)` alone determines the exact regime on this frontier.

## 2. `(h_res,L)` almost compresses t=3, but still fails

Across all 94 exact `t=3` profiles only three pairs occur:

| `(h_res,L)` | profiles | exact template labels in the cell |
|---|---:|---|
| `(4,6)` | 17 | `A0:1, A1:11, A530:5` |
| `(4,7)` | 4 | `A530:4` |
| `(5,7)` | 73 | `A38:73` |

So the pair is informative: `(5,7)` exactly identifies the large `A38` leaf and `(4,7)` identifies `A530`. But `(4,6)` still contains three distinct exact regimes.

Representative first profiles from that collision are:

| profile | regime | demand id | `rho_1` | `nu_1` | `(h_res,L)` |
|---:|---|---:|---:|---:|---|
| 0 | `A0` | 0 | 9 | 1 | `(4,6)` |
| 1 | `A1` | 9 | 9 | 0 | `(4,6)` |
| 5 | `A530` | 15 | 8 | 0 | `(4,6)` |

This mirrors the preserved count-tree: within the unresolved pair-cell, the remaining distinctions are precisely unit-count transitions on the source and demand sides.

## 3. A very small repair works simultaneously for t=2 and t=3

Define the weighted unit score

```text
G = 2 rho_1 + nu_1
  = 2 #{u:rho_u=1} + #{i:s_i=1}.
```

Then **every `(h_res,L,G)` cell is regime-pure on both exact frontiers**.

### t=2 exact cell census

```text
(4,6,10) T2:1
(4,6,12) T2:5
(4,6,14) T2:13
(4,6,15) T1:1
(4,6,16) T2:29
(4,6,17) T1:5
(4,6,18) T2:62
(4,6,19) T1:15
(4,6,20) T0:1

(4,7,10) T2:4
(4,7,12) T2:12
(4,7,14) T2:27
(4,7,15) T1:1
(4,7,16) T2:47
(4,7,17) T1:3

(4,8,10) T2:1
(4,8,12) T2:3
(4,8,14) T2:7

(5,7,6)  T2:1
(5,7,8)  T2:13
(5,7,10) T2:40
(5,7,12) T2:131
(5,7,13) T1:3
(5,7,14) T2:214
(5,7,15) T1:14
(5,7,16) T2:214
(5,7,17) T1:34

(5,8,14) T2:1
```

There are 28 occupied cells and zero mixed cells.

For the exact lower-bound triangle, `G` gives

```text
profile 0  (T0): G=20
profile 3  (T1): G=19
profile 77 (T2): G=18.
```

### t=3 exact cell census

```text
(4,6,14) A530:1
(4,6,16) A530:4
(4,6,18) A1:11
(4,6,19) A0:1

(4,7,14) A530:1
(4,7,16) A530:3

(5,7,12) A38:7
(5,7,14) A38:24
(5,7,16) A38:42
```

There are 9 occupied cells and zero mixed cells.

## 4. Why the coefficient 2 is non-vacuous

The obvious unweighted score

```text
rho_1 + nu_1
```

resolves all `t=3` collisions but **fails at t=2**. Likewise `nu_1` alone resolves `t=2` but fails at `t=3`.

For the small nonnegative primitive linear family

```text
G_{a,b} = a rho_1 + b nu_1,
```

the following exact comparison holds:

| `(a,b)` | statistic | mixed t=2 cells | mixed t=3 cells |
|---|---|---:|---:|
| `(1,0)` | `rho_1` | 8 | 1 |
| `(0,1)` | `nu_1` | 0 | 1 |
| `(1,1)` | `rho_1+nu_1` | 5 | 0 |
| `(1,2)` | `rho_1+2nu_1` | 2 | 0 |
| `(2,1)` | `2rho_1+nu_1` | **0** | **0** |

Consequently `(2,1)` is the first solution when primitive nonnegative integer coefficient pairs are ordered by maximum coefficient. This is a finite-frontier minimality statement only; it is not a uniqueness or general-N theorem.

The weighting is also structurally interpretable: the exact `t=3` collision separates first by the source-side unit count `rho_1` and then by the demand-side unit count `nu_1`, while the exact `t=2` regimes are indexed by `nu_1`. The score `2rho_1+nu_1` packages those two elementary transitions without losing the distinctions in either finite laboratory.

## Interpretation

The attempted two-scalar compression has been productively falsified. The evidence now supports a more precise finite structural picture:

1. the supplement cutoff `L` is a genuine structural scalar, but it is not sufficient together with the ordinary residual h-index;
2. the failures of `(h_res,L)` are concentrated in a very small number of cells;
3. the remaining distinctions are governed by elementary unit-count information on the source and demand sides;
4. on the complete exact `t=2` and `t=3` frontiers, the three scalars

```text
(h_res, L, 2 rho_1 + nu_1)
```

are sufficient to determine a valid exact-template regime label.

This is evidence for a low-dimensional parameter-generated regime theory, not yet such a theory.

## Scope caution and t=1

The adjacent exact `t=1` laboratory currently preserved in the repository is `n=30,t=1`, whereas the scalar-cutoff replay above was derived and audited in the `n=29,Delta=16` complement setting used for `t=2,3`. This note therefore does **not** silently transport the same `L` definition across that change of ambient parameters. A proper `t=1` comparison should first establish the corresponding scalar-cutoff identity in the `n=30` parameterization, then run the same collision test.

Since `(h_res,L)` is already exactly falsified at `t=2` and `t=3`, no general claim is being withheld by that caution.

## Next mathematical tests

1. derive the parameterized form of `h_res`, `L`, `rho_1`, and `nu_1` under a one-step change in `(n,Delta,t)`;
2. test whether the weighted-unit score `2rho_1+nu_1` is stable on a fresh frontier not used to discover it;
3. search for a symbolic reason that the mixed `(h_res,L)` cells have the observed unit-count stratification;
4. only after a fresh-domain falsification attempt, formulate a candidate general regime lemma;
5. retain the exact template-gap replays and graph-to-profile bridge as the independent-review trust boundary.
