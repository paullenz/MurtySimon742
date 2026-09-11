# adjacent t=1,2,3: `(h_res,L)` falsified; `(h_res,J)` gives a two-scalar canonical regime key

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact finite structural diagnostic inside the already-preserved RX-Hall laboratories. This is not a general-N theorem and does not alter the independent-review trust boundary of the graph-to-profile/RX-Hall bridge or the potential lemmas.**

## Executive result

The natural two-index hypothesis

```text
(h_res, L)
```

is false in every adjacent exact finite laboratory `t=1,2,3`.

However, a different two-scalar key works exactly on all three:

```text
(h_res, G),
G = 2 rho_1 + nu_1,
rho_1 = #{u:rho_u=1},
nu_1  = #{i:s_i=1}.
```

Equivalently, if

```text
z_2 = #{u:rho_u>=2},
D_1 = #{i:s_i=1},
b   = number of residual sources,
```

then `rho_1=b-z_2` and therefore

```text
G = 2b - J,
J = 2 z_2 - D_1.
```

Since `b=16` in all three adjacent laboratories, `(h_res,G)` and `(h_res,J)` are equivalent regime keys. The `J` form is the more natural general target: it is built directly from the first nontrivial source upper tail and the unit-demand lower tail.

## Exact input laboratories

The scan uses only already-preserved exact rational-template assignments:

- `n=30,t=1`: seven hard profiles from `n30_t1_two_rational_templates_exact.py`, exact templates `A,B`, with `a=13,b=16`;
- `n=29,t=2`: complete regenerated positive-demand frontier of 902 profiles, exact templates `T0,T1,T2`, with `a=12,b=16`;
- `n=29,t=3`: complete regenerated positive-demand frontier of 94 profiles, exact templates `A0,A1,A38,A530`, with `a=12,b=16`.

The scalar-cutoff lemma is already parameterized in the number `a` of demand labels:

```text
C_u = min(a-rho_u, #{i:s_i<=rho_u}),
L = max{k>=1 : #{u:rho_u+C_u>=k-1}>=k+1}.
```

Thus using the same definition of `L` at `n=30,t=1` is an application of the existing structural lemma, not an extrapolation from `n=29`.

## 1. Exact falsification of `(h_res,L)`

### t=1

For the seven exact `n=30,t=1` hard profiles:

| `(h_res,L)` | profiles | exact labels |
|---|---:|---|
| `(3,7)` | 6 | `A:2, B:4` |
| `(3,8)` | 1 | `B:1` |

So the main pair-cell already mixes both necessary templates.

### t=2

Across all 902 exact profiles:

| `(h_res,L)` | profiles | exact labels |
|---|---:|---|
| `(4,6)` | 132 | `T0:1, T1:21, T2:110` |
| `(4,7)` | 94 | `T1:4, T2:90` |
| `(4,8)` | 11 | `T2:11` |
| `(5,7)` | 664 | `T1:51, T2:613` |
| `(5,8)` | 1 | `T2:1` |

Three of the five cells are mixed, covering 890 of the 902 profiles.

The strongest counterexample is the preserved exact lower-bound incompatibility triangle. Profiles `0`, `3`, and `77` require the three roles `T0,T1,T2`, yet all have

```text
(h_res,L)=(4,6).
```

Their low-threshold statistics are

| profile | role | `rho_1` | `nu_1` | `G` |
|---:|---|---:|---:|---:|
| 0 | `T0` | 9 | 2 | 20 |
| 3 | `T1` | 9 | 1 | 19 |
| 77 | `T2` | 9 | 0 | 18 |

### t=3

Across all 94 exact profiles:

| `(h_res,L)` | profiles | exact labels |
|---|---:|---|
| `(4,6)` | 17 | `A0:1, A1:11, A530:5` |
| `(4,7)` | 4 | `A530:4` |
| `(5,7)` | 73 | `A38:73` |

Only one pair-cell is mixed, but it contains three distinct exact regimes.

Hence `(h_res,L)` is not merely imperfect: it is exactly falsified as a deterministic regime key in all three adjacent laboratories.

## 2. The smaller replacement `(h_res,G)` is exact on t=1,2,3

Define

```text
G = 2 rho_1 + nu_1.
```

Every occupied `(h_res,G)` cell has a single canonical exact-template assignment in all three laboratories.

### t=1

```text
(3,13) B:1
(3,15) B:3
(3,16) A:1
(3,17) B:1
(3,18) A:1
```

Equivalently, on these seven profiles `G` alone separates the two assignments: the observed `A` values are even (`16,18`) and the observed `B` values are odd (`13,15,17`).

### t=2

There are 18 occupied `(h_res,G)` cells and zero mixed assignment cells:

```text
h=4:
G=10 T2:6
G=12 T2:20
G=14 T2:47
G=15 T1:2
G=16 T2:76
G=17 T1:8
G=18 T2:62
G=19 T1:15
G=20 T0:1

h=5:
G=6  T2:1
G=8  T2:13
G=10 T2:40
G=12 T2:131
G=13 T1:3
G=14 T2:215
G=15 T1:14
G=16 T2:214
G=17 T1:34
```

Again `G` alone already determines the canonical t=2 assignment:

```text
G=20        -> T0
G odd       -> T1
other G     -> T2
```

on the complete exact frontier.

### t=3

There are seven occupied `(h_res,G)` cells:

```text
(4,14) A530:2
(4,16) A530:7
(4,18) A1:11
(4,19) A0:1
(5,12) A38:7
(5,14) A38:24
(5,16) A38:42
```

So the exact finite rule is simply

```text
h_res=5              -> A38
h_res=4 and G<=16    -> A530
h_res=4 and G=18     -> A1
h_res=4 and G=19     -> A0
```

for the observed frontier.

`G` alone is insufficient at `t=3`: values `14` and `16` occur in both `A38` and `A530`. The ordinary residual h-index supplies exactly the missing distinction.

## 3. Genuine holdout check

Chronologically, `G=2rho_1+nu_1` was found while resolving the `t=2` and `t=3` collisions. Only afterwards was the parameterized scalar-cutoff lemma applied to the separate `n=30,t=1` exact laboratory.

Thus `t=1` was not used to choose the coefficient 2. The unchanged statistic then separated the `t=1` exact assignments as well. This is a genuine finite holdout test, albeit on only seven hard profiles.

## 4. Why coefficient 2 is not just arbitrary encoding

For the small primitive nonnegative family

```text
G_{a,b}=a rho_1+b nu_1,
```

adjoined to `h_res`, the exact mixed-cell counts are:

| `(a,b)` | statistic | mixed t=1 | mixed t=2 | mixed t=3 |
|---|---|---:|---:|---:|
| `(1,0)` | `rho_1` | 2 | 6 | 1 |
| `(0,1)` | `nu_1` | 0 | 0 | 1 |
| `(1,1)` | `rho_1+nu_1` | 1 | 4 | 0 |
| `(1,2)` | `rho_1+2nu_1` | 0 | 2 | 0 |
| `(2,1)` | `2rho_1+nu_1` | **0** | **0** | **0** |

So `(2,1)` is the first successful primitive nonnegative pair when ordered by maximum coefficient.

More importantly, the equivalent form

```text
J=2z_2-D_1
```

shows that the statistic lives directly in the cumulative threshold language already used by the residual ledger. This makes `J`, rather than the raw encoding `G`, the sensible symbolic object to attack next.

## 5. Important red-team caveat: this does not encode the whole template-overlap geometry

The two-scalar pair determines the **canonical valid-template assignment** used by the exact replays. It does **not** determine which other templates also happen to cover the same profile.

An exact coverage-mask red-team check found multiple overlap masks within the same `(h_res,G)` cell:

- `t=1`: 1 mixed coverage-mask cell, involving 3 of 7 profiles;
- `t=2`: 13 mixed coverage-mask cells, involving 879 of 902 profiles;
- `t=3`: 6 mixed coverage-mask cells, involving 93 of 94 profiles.

This is not a defect in the regime result: a proof needs one valid canonical template for each regime, not a reconstruction of every redundant template that also works. But it is an important boundary on what has actually been compressed.

Accordingly the safe statement is:

> `(h_res,J)` determines the preserved canonical exact-template assignment on the adjacent finite laboratories.

It does **not** determine the complete certificate coverage mask.

## 6. Reproducibility

Diagnostic:

```text
project/research/general_n/2026-09-11-regime-structure-v1/n29_t23_hL_compression_scan.py
```

CI workflow:

```text
.github/workflows/general-rx-hall-n29-t23-hL-compression.yml
```

Successful exact regeneration/replay:

```text
GitHub Actions run: 34590110191
artifact:           adjacent-t123-hL-compression
artifact id:        10195264884
artifact SHA-256:   7e2a50a7ec23e00e8479fe4dba7fbeb0e8422ffd6fc436960af06335b844e7a1
head commit:        eefb5aad86caff9bb6dc77bf6fc5cbfd6bd95305
```

The workflow imports the exact `n=30,t=1` assignment, independently regenerates the audited `n=29,t=2,3` frontiers, computes the parameterized cutoff `L`, and verifies the collision statements using integer arithmetic.

## 7. Current best general-theory target

The result changes the next priority. Rather than trying to prove a general theorem in the two shifted h-indices `(h_res,L)`, the cleaner target is now the pair

```text
h_res,
J = 2 z_2 - D_1,
```

where

```text
z_2 = #{u:rho_u>=2},
D_1 = #{i:s_i=1}.
```

The next proof questions are:

1. derive regime-wise inequalities directly from `(h_res,J)` and the cumulative residual/demand tails;
2. determine whether the coefficient 2 follows from a residual-activity or Hall ledger identity rather than finite coincidence;
3. hostile-test `(h_res,J)` on a genuinely fresh exact frontier not used in discovery;
4. prove that each resulting parameterized regime forces one fixed rational template, without attempting to reconstruct the entire overlap mask;
5. only then formulate a candidate general-N regime theorem.
