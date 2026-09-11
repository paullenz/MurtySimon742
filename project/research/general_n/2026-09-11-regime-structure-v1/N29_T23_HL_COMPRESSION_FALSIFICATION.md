# adjacent t=1,2,3: falsification of `(h_res,L)` compression and a three-scalar repair

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact finite structural diagnostic inside the already-preserved RX-Hall laboratories. This is not a general-N theorem and does not alter the independent-review trust boundary of the graph-to-profile/RX-Hall bridge or the potential lemmas.**

## Question

The supplement-cap refinement has the structural scalar-cutoff form

```text
q*_u = min(C_u,L),
C_u = min(a-rho_u, #{i:s_i <= rho_u}),
L = max{k>=1 : #{u:rho_u+C_u >= k-1} >= k+1}.
```

The scalar-cutoff lemma is already proved for arbitrary demand count `a`; it is not specific to `n=29`.

This makes it natural to ask whether the exact scalar-template regime of a frontier profile is determined by

```text
h_res = max{k : #{u:rho_u >= k} >= k},
L     = supplement cutoff above.
```

The answer is **no in each of the three adjacent exact finite laboratories**. A very small third scalar repairs all three.

## Exact input laboratories

The scan uses only already-preserved exact regime assignments:

- `n=30,t=1`: the seven hard profiles from `n30_t1_two_rational_templates_exact.py`, with two exact rational templates `A,B`; here `a=13`, `b=16`;
- `n=29,t=2`: the complete regenerated positive-demand frontier of 902 profiles, with exact deterministic labels `T0,T1,T2`; here `a=12`, `b=16`;
- `n=29,t=3`: the complete regenerated positive-demand frontier of 94 profiles, with exact deterministic labels `A0,A1,A38,A530`; here `a=12`, `b=16`.

For `t=2,3`, the canonical audited regeneration is

```text
project/reviews/n29/2026-09-08-redteam-restart-v1/minimal_prepare.py
project/reviews/n29/2026-09-08-redteam-restart-v1/minimal_rows.cpp
```

The labels are not classifier output: they are assignments to preserved exact rational templates already checked to have strictly positive exact certificate gap.

## 1. `(h_res,L)` fails at t=1

For the seven exact `n=30,t=1` hard profiles:

| `(h_res,L)` | profiles | exact labels |
|---|---:|---|
| `(3,7)` | 6 | `A:2, B:4` |
| `(3,8)` | 1 | `B:1` |

Thus the main `(3,7)` cell mixes both necessary regimes.

Profile-level values are:

| profile | template | `rho_1` | `nu_1` | `(h_res,L)` | `G=2rho_1+nu_1` |
|---:|---|---:|---:|---|---:|
| 0 | A | 8 | 2 | `(3,7)` | 18 |
| 1 | A | 7 | 2 | `(3,7)` | 16 |
| 2 | B | 8 | 1 | `(3,7)` | 17 |
| 3 | B | 7 | 1 | `(3,7)` | 15 |
| 4 | B | 7 | 1 | `(3,7)` | 15 |
| 5 | B | 7 | 1 | `(3,8)` | 15 |
| 6 | B | 6 | 1 | `(3,7)` | 13 |

So the same two-index hypothesis already fails in the smallest adjacent laboratory.

## 2. `(h_res,L)` fails decisively at t=2

Across all 902 exact `t=2` profiles only five pairs occur:

| `(h_res,L)` | profiles | exact template labels |
|---|---:|---|
| `(4,6)` | 132 | `T0:1, T1:21, T2:110` |
| `(4,7)` | 94 | `T1:4, T2:90` |
| `(4,8)` | 11 | `T2:11` |
| `(5,7)` | 664 | `T1:51, T2:613` |
| `(5,8)` | 1 | `T2:1` |

Three of the five cells are mixed.

### Exact lower-bound triangle collapses to one pair

The preserved incompatibility triangle proving that fewer than three scalar templates do not suffice at `t=2` consists of profile indices `0`, `3`, and `77`. They are `T0`, `T1`, and `T2` witnesses respectively. All three have

```text
(h_res,L) = (4,6).
```

Their unit counts are

| profile | regime | demand id | `rho_1` | `nu_1` | `G` |
|---:|---|---:|---:|---:|---:|
| 0 | `T0` | 45 | 9 | 2 | 20 |
| 3 | `T1` | 70 | 9 | 1 | 19 |
| 77 | `T2` | 154 | 9 | 0 | 18 |

This is a particularly clean obstruction to any claim that `(h_res,L)` alone determines the exact regime.

## 3. `(h_res,L)` nearly compresses t=3, but still fails

Across all 94 exact `t=3` profiles only three pairs occur:

| `(h_res,L)` | profiles | exact template labels |
|---|---:|---|
| `(4,6)` | 17 | `A0:1, A1:11, A530:5` |
| `(4,7)` | 4 | `A530:4` |
| `(5,7)` | 73 | `A38:73` |

The pair is highly informative: `(5,7)` exactly identifies `A38` and `(4,7)` identifies `A530`. But `(4,6)` still contains three exact regimes.

Representative first profiles from that collision are:

| profile | regime | demand id | `rho_1` | `nu_1` | `G` |
|---:|---|---:|---:|---:|---:|
| 0 | `A0` | 0 | 9 | 1 | 19 |
| 1 | `A1` | 9 | 9 | 0 | 18 |
| 5 | `A530` | 15 | 8 | 0 | 16 |

This mirrors the preserved t=3 count tree: within the unresolved pair-cell, the remaining distinctions are elementary unit-count transitions on the source and demand sides.

## 4. One weighted unit score repairs t=1,2,3

Define

```text
rho_1 = #{u : rho_u = 1},
nu_1  = #{i : s_i = 1},
G      = 2 rho_1 + nu_1.
```

Then **every occupied `(h_res,L,G)` cell is exact-regime-pure in all three laboratories**.

The occupied t=1 cells are

```text
(3,7,13) B:1
(3,7,15) B:2
(3,7,16) A:1
(3,7,17) B:1
(3,7,18) A:1
(3,8,15) B:1
```

The `t=2` scan has 28 occupied `(h_res,L,G)` cells and zero mixed cells.

The `t=3` scan has 9 occupied cells:

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

and again zero mixed cells.

## 5. The coefficient 2 is non-vacuous

Consider the small nonnegative primitive linear family

```text
G_{a,b} = a rho_1 + b nu_1.
```

Exact collision counts after adjoining the statistic to `(h_res,L)` are:

| `(a,b)` | statistic | mixed t=1 cells | mixed t=2 cells | mixed t=3 cells |
|---|---|---:|---:|---:|
| `(1,0)` | `rho_1` | 2 | 8 | 1 |
| `(0,1)` | `nu_1` | 0 | 0 | 1 |
| `(1,1)` | `rho_1+nu_1` | 1 | 5 | 0 |
| `(1,2)` | `rho_1+2nu_1` | 0 | 2 | 0 |
| `(2,1)` | `2rho_1+nu_1` | **0** | **0** | **0** |

Therefore `(2,1)` is the first solution when primitive nonnegative integer coefficient pairs are ordered by maximum coefficient. This is a finite-laboratory minimality statement, not a uniqueness or general-N theorem.

The weighting is structurally meaningful rather than a base-encoding trick: `rho_1` resolves the source-side split left by the t=3 `(h,L)` collision, while `nu_1` indexes the demand-side transition already visible at t=1 and exactly controls the t=2 regime assignment.

## Interpretation

The two-index idea has been productively falsified and replaced by a sharper finite hypothesis:

```text
(h_res, L, 2 rho_1 + nu_1).
```

Across the adjacent exact `t=1,2,3` laboratories this triple determines a valid exact-template regime label, whereas `(h_res,L)` fails in every laboratory.

This gives four concrete structural facts:

1. `L` is a genuine parameterized structural scalar, not an n=29 artefact.
2. `h_res` and `L` together are insufficient.
3. Their failures are concentrated in a few low-dimensional cells.
4. One elementary weighted unit-count statistic removes every observed collision across `t=1,2,3`.

That is substantially stronger evidence for a low-dimensional parameter-generated regime theory than the earlier raw `2,3,4` template census, but it is **not yet the theory**.

## Reproducibility

Diagnostic:

```text
project/research/general_n/2026-09-11-regime-structure-v1/n29_t23_hL_compression_scan.py
```

CI:

```text
.github/workflows/general-rx-hall-n29-t23-hL-compression.yml
```

The replay imports the exact `n=30,t=1` profile/template assignment, independently regenerates the audited `n=29,t=2,3` frontiers, computes the parameterized scalar cutoff `L`, and checks all occupied cells exactly using integer arithmetic.

## Next mathematical tests

1. attack `G=2rho_1+nu_1` on a genuinely fresh exact frontier not used to discover it;
2. derive a symbolic reason that the mixed `(h_res,L)` cells stratify by this weighted unit count;
3. express the regime boundaries directly in the cumulative demand/source tails underlying `h_res` and `L`;
4. test whether the coefficient 2 has a combinatorial origin in the residual ledger or is only a finite-domain coincidence;
5. only after a fresh-domain hostile test, formulate a candidate parameterized regime lemma.
