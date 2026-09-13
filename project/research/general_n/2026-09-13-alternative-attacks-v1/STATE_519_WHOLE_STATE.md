# N34 state 519 — whole-state exclusion

13 September 2026. **Candidate whole-state proof inside the canonical selected/residual bridge, with exact integer replay green on GitHub Actions. External mathematical review and independent computational reproduction remain OPEN. This does not prove the unrestricted Murty–Simon conjecture.**

## 1. State and target

The frozen N34 scalar state is

```text
a=15,
b=18,
t=1,
s=2,3^14,
rho=1^6,3^12,
r=42,
S=sum_i s_i=44.
```

All 15 labels have positive demand. Write

```text
e_i=x_i-s_i>=0,
E=sum_i e_i,
Q=sum_i x_i=S+E=44+E,
C_i=R_i+x_i=d_i+e_i,
T=sum_u q_u(q_u+p_u).
```

The aim is to show that **no** selected-incidence realization of this scalar state can satisfy the canonical bridge constraints, for any selected geometry, q-vector, p-vector or excess profile.

Because `s_i>=2`, a `rho=1` source cannot be selected, so its `q_u=0`. The basic incoming cap

```text
p_u<=rho_u+b-a-1=rho_u+2
```

gives total incoming capacity

```text
6*3+12*5=78.
```

But `sum p_u=Q=44+E`, hence

```text
E<=34.                                                (1)
```

Thus it suffices to exclude `E=0,...,34`.

## 2. Exact low/profile sweep, E=0,...,24

The verifier `verify_state519_low.cpp` enumerates every excess profile up to permutation within the demand classes and optimizes an exact integer necessary-condition relaxation over the source q- and p-margins.

The ingredients are all consequences already present in the canonical bridge / low-excess programme.

### 2.1 Source excess threshold

For every selected incidence `ui`, selected excess gives

```text
p_u-rho_u+1 <= e_i.                                  (2)
```

The no-isolated-C bound gives `d_i<=13`, while endpoint load gives

```text
q_u+p_u<=C_i=d_i+e_i.
```

Therefore every label selected at source `u` has

```text
e_i >= L_u:=max(0,p_u-rho_u+1,q_u+p_u-13).           (3)
```

If `h_l=#{i:e_i>=l}`, then a source with `L_u>0` must satisfy

```text
q_u<=h_(L_u).                                         (4)
```

All selected sources here have `rho=3`.

### 2.2 Residual-budget q cap

Let `x_max=max_i x_i`. Endpoint load implies `C_i>=q_u` on every label selected at source `u`, so each of its `q_u` distinct selected labels has

```text
R_i>=q_u-x_max.
```

Since `sum R_i=r=42`, necessarily

```text
42 >= q_u max(0,q_u-x_max).                          (5)
```

The verifier retains (5) exactly.

### 2.3 Two endpoint envelopes

First, from endpoint load on every selected incidence,

```text
T <= sum_i x_i C_i.                                   (6)
```

For a fixed excess profile, the coarse upper support function on the right of (6) is exact for the relaxed residual budget: put the total residual mass 42 greedily on labels of largest `x_i`, subject to

```text
R_i<=11  for the demand-two label,
R_i<=10  for a demand-three label.                    (7)
```

Second, the refined baseline-three envelope uses

```text
sum_i x_i C_i
 =3(r+Q)+sum_i(x_i-3)C_i.                             (8)
```

For a demand-three label of excess `e>=1`, its `3+e` distinct selected sources give the order-statistic upper bound

```text
C_i <= e+2+q^(3+e),                                  (9)
```

where `q^(k)` is the k-th largest selected degree among the twelve `rho=3` sources. For the unique demand-two label with `e>=2`, similarly

```text
C_i <= e+2+q^(2+e).                                  (10)
```

If the demand-two label has `e=0`, its negative baseline coefficient is retained at least as

```text
-C_i <= -2.                                           (11)
```

For each profile the verifier computes the exact minimum source-side quantity under (2)-(5) and the incoming ledger, and compares it with both endpoint envelopes (6)-(11). No floating solver status is used.

### 2.4 Exhaustive result

The green replay gives:

| E | profiles | strict | equality | negative | source-infeasible | minimum finite gap |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 | 0 | 0 | 4 |
| 1 | 2 | 2 | 0 | 0 | 0 | 9 |
| 2 | 4 | 4 | 0 | 0 | 0 | 15 |
| 3 | 7 | 7 | 0 | 0 | 0 | 7 |
| 4 | 12 | 12 | 0 | 0 | 0 | 6 |
| 5 | 19 | 19 | 0 | 0 | 0 | 3 |
| 6 | 30 | 29 | 0 | 1 | 0 | -2 |
| 7 | 45 | 45 | 0 | 0 | 0 | 3 |
| 8 | 67 | 66 | 1 | 0 | 0 | 0 |
| 9 | 97 | 96 | 0 | 1 | 0 | -2 |
| 10 | 139 | 138 | 0 | 0 | 1 | 2 |
| 11 | 195 | 191 | 0 | 0 | 4 | 6 |
| 12 | 272 | 263 | 0 | 0 | 9 | 2 |
| 13 | 371 | 355 | 0 | 0 | 16 | 8 |
| 14 | 503 | 475 | 0 | 0 | 28 | 10 |
| 15 | 672 | 626 | 0 | 0 | 46 | 7 |
| 16 | 891 | 818 | 0 | 0 | 73 | 9 |
| 17 | 1,167 | 1,055 | 0 | 0 | 112 | 3 |
| 18 | 1,519 | 1,351 | 0 | 0 | 168 | 6 |
| 19 | 1,956 | 1,709 | 0 | 0 | 247 | 12 |
| 20 | 2,504 | 2,118 | 0 | 0 | 386 | 20 |
| 21 | 3,177 | 2,478 | 0 | 0 | 699 | 13 |
| 22 | 4,007 | 3,161 | 0 | 0 | 846 | 17 |
| 23 | 5,014 | 3,228 | 0 | 0 | 1,786 | 21 |
| 24 | 6,241 | 3,816 | 0 | 0 | 2,425 | 22 |

Hence every feasible relaxed profile is already strict except for exactly one coarse profile at each of `E=6,8,9`.

## 3. The three exceptional layers: exact-demand source availability

The remaining weakness comes from replacing a zero-excess demand-two label by the universal lower bound `C_i>=2`. State 519 allows a stronger selection-free bound.

If the unique demand-two label has `e=0`, then `x=2`. Its two distinct selected sources must be `rho=3` sources, and (2) forces at both incidences

```text
p_u<=rho_u-1=2.                                      (12)
```

Endpoint load also gives

```text
C_2 >= max(q_u+p_u,q_v+p_v)                          (13)
```

for its two selected sources `u,v`.

The dedicated verifier `verify_state519_exceptions.cpp` therefore enumerates the selected pair, their allowed p-values under (12), and the remaining incoming allocation jointly. It minimizes

```text
sum_u q_u p_u + C_2                                  (14)
```

rather than minimizing `sum q_u p_u` first and then replacing `C_2` by 2. This is an exact finite implementation of the general order-statistic lemma recorded in `ZERO_EXCESS_ENDPOINT_ORDER.md`.

The verifier is deliberately conservative: it relaxes some additional incidence restrictions on the chosen pair. Therefore a positive gap remains a valid necessary-condition exclusion.

The complete exceptional-layer replay is:

| E | profiles | minimum gap |
|---:|---:|---:|
| 6 | 30 | 2 |
| 8 | 67 | 4 |
| 9 | 97 | 2 |

Every profile in all three layers is now strict. Consequently

```text
E=0,...,24 are all excluded.                          (15)
```

## 4. Refined h2 tail, E=25,...,34

Let

```text
h_2=#{i:e_i>=2}.
```

If `q_u>h_2`, at least one label selected at source `u` has excess at most one. Equation (2) then gives

```text
q_u>h_2  =>  p_u<=rho_u=3.                           (16)
```

Otherwise the basic cap is `p_u<=5`, and always `q_u+p_u<=17`.

For fixed q and `h_2`, incoming mass is assigned to the smallest q-values to obtain the exact minimum `sum q_u p_u` for this relaxation. The positive baseline-three corrections are maximized by dynamic programming over the one demand-two and fourteen demand-three labels, retaining the negative `-2` contribution whenever the demand-two label has zero excess.

`verify_state519_tail.cpp` gives:

| E | minimizing h2 | minimum gap |
|---:|---:|---:|
| 25 | 5 | 4 |
| 26 | 6 | 5 |
| 27 | 6 | 12 |
| 28 | 6 | 2 |
| 29 | 6 | 1 |
| 30 | 6 | 2 |
| 31 | 6 | 5 |
| 32 | 6 | 10 |
| 33 | 7 | 21 |
| 34 | 7 | 20 |

Every tail layer is strictly impossible. Together with (1),

```text
E>=25 is excluded.                                    (17)
```

## 5. Conclusion

Equations (15) and (17) cover every possible nonnegative selected excess. Therefore N34 state 519 has no selected-incidence realization satisfying the canonical bridge constraints.

This is the **sixth quantified whole-state exclusion** in the programme, after states 227, 279, 588, 526 and 382.

The frozen generalisation frontier moves from

```text
999 exclusions / 4,579 survivors
```

to

```text
1,000 exclusions / 4,578 survivors,
```

split as

```text
4,500 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

These are scalar-state counts in the frozen generalisation experiment, not counts of surviving graphs. The already-closed fixed-order N34 proof is unchanged.

## 6. Reproducibility and trust boundary

The proof-critical computations use exact integer arithmetic and explicit assertions. GitHub Actions run `34773463128`, at commit `99da77421870283eb8c276825097a637951ae799`, completed green on all three stages:

- low/profile sweep `E=0,...,24`;
- source-availability replay at `E=6,8,9`;
- refined tail `E=25,...,34` plus the incoming-capacity ceiling.

Replay instructions are in `STATE_519_REPLAY.md`; the compact machine summary is in `STATE_519_WHOLE_STATE_VERIFICATION.json`.

The main correlated mathematical risk remains the canonical bridge and its graph-to-selected-incidence implications. This result is internally exact **conditional on that framework**. External specialist review of the bridge, the inequalities used here and the source-availability lemma remains open, as does genuinely independent computational reproduction.
