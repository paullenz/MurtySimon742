# N34 state 382 — whole-state exclusion

13 September 2026. **Candidate hand/algebraic reduction plus exact integer enumeration; external mathematical review and independent reproduction remain OPEN.** This is the fifth whole-state exclusion produced by the alternative-geometry / selected-excess programme, after states 227, 279, 588 and 526.

The conclusion is

```text
N34 state 382 has no selected/residual realization satisfying the canonical bridge.
```

It changes the frozen generalisation record from

```text
998 exclusions / 4,580 survivors
```

to

```text
999 exclusions / 4,579 survivors.
```

The separate fixed-order N34 proof candidate was already closed and is unchanged.

## 1. State data

State 382 has

```text
a=15, b=18, t=1,
s   = 2^2,3^13,
rho = 1^6,2,3^11,
r=sum rho=41,
S=sum s=43.
```

Put

```text
e_i=x_i-s_i >= 0,
E=sum_i e_i,
Q=sum_i x_i=S+E=43+E.
```

The six `rho=1` sources have q=0. The single `rho=2` source can select only the two demand-two labels and therefore has `q<=2`. Each of the eleven `rho=3` sources has `q<=12`.

The basic incoming cap is

```text
p_u<=rho_u+b-a-1=rho_u+2.
```

Hence total incoming capacity is

```text
6*3 + 1*4 + 11*5 = 77.
```

Since `sum p_u=Q=43+E`, every realization has

```text
E<=34.                                                (1.1)
```

## 2. Endpoint/excess envelope

Put

```text
C_i=R_i+x_i,
T=sum_u q_u(q_u+p_u).
```

Endpoint load gives

```text
T <= sum_i x_i C_i.                                  (2.1)
```

Also

```text
sum_i C_i=r+Q=84+E.
```

Using coefficient three as baseline,

```text
sum_i x_i C_i
 =3(84+E)
  -sum_(s_i=2,e_i=0) C_i
  +sum_(s_i=2,e_i>=2) (e_i-1)C_i
  +sum_(s_i=3,e_i>=1) e_i C_i.                      (2.2)
```

For demand-three labels, if `q_3^(k)` is the k-th largest q among the eleven `rho=3` sources, source selected-degree forcing gives

```text
C_i <= e_i+2+q_3^(3+e_i).                            (2.3)
```

For demand-two labels, safely relaxing the `rho=2` source bound by one unit and taking the k-th largest q among all twelve `rho>=2` sources gives

```text
C_i <= e_i+2+q_all^(2+e_i).                          (2.4)
```

Thus demand-three excess is at most 8 and demand-two excess at most 10.

The selected-excess lemma and the no-isolated-C / endpoint consequence give, for every selected label at source u,

```text
L_u=max(0,p_u-rho_u+1,q_u+p_u-13) <= e_i.            (2.5)
```

The exact low-excess verifier also uses the preserved residual-budget consequence

```text
41 >= q_u max(0,q_u-x_max).                           (2.6)
```

For fixed source degrees and excess profile, incoming units are placed first on the smallest q-values up to their admissible p-caps. This exactly minimizes `sum q_u p_u` by exchange.

## 3. Exact low-excess sweep E=0,...,17

`verify_state382_low.cpp` enumerates every excess profile up to permutation within the two demand-two and thirteen demand-three labels, every possible q on the unique `rho=2` source, and every nondecreasing eleven-source `rho=3` q-vector.

Every profile is strictly excluded; there are no equality, negative or source-infeasible profiles in this range.

| E | profiles | minimum strict gap |
|---:|---:|---:|
| 0 | 1 | 3 |
| 1 | 2 | 6 |
| 2 | 5 | 13 |
| 3 | 9 | 8 |
| 4 | 17 | 7 |
| 5 | 28 | 5 |
| 6 | 47 | 3 |
| 7 | 73 | 3 |
| 8 | 114 | 7 |
| 9 | 169 | 5 |
| 10 | 250 | 8 |
| 11 | 356 | 10 |
| 12 | 505 | 4 |
| 13 | 697 | 15 |
| 14 | 956 | 18 |
| 15 | 1,284 | 17 |
| 16 | 1,713 | 17 |
| 17 | 2,246 | 21 |

Hence any realization would require

```text
E>=18.                                                (3.1)
```

## 4. Refined h_2 tail: retain the zero-demand-two correction

The earlier state-227/state-279/state-588/state-526 tail relaxations often discarded the negative term in (2.2). State 382 shows that it is profitable to retain its cheapest universal part.

If a demand-two label has zero excess, then `x_i=2`, so trivially

```text
C_i=R_i+x_i>=2.
```

Let

```text
z_0=#{i:s_i=2,e_i=0}.
```

Then every realization satisfies the strengthened necessary inequality

```text
T + 2 z_0 - P_+ <= 3(84+E),                          (4.1)
```

where `P_+` is the positive correction in (2.2) after applying the top-k upper bounds (2.3)-(2.4).

For the threshold part put

```text
h=#{i:e_i>=2}.
```

The selected-excess threshold family gives the relaxed caps

```text
rho=2: q>h => p<=2, otherwise p<=4,
rho=3: q>h => p<=3, otherwise p<=5.                  (4.2)
```

`verify_state382_tail.cpp` maximizes `P_+-2z_0` by exact dynamic programming over the excess allocations and minimizes the incoming load exactly over the q-vectors.

The resulting global minimum gaps above the right side of (4.1) are:

| E | minimizing h | minimum gap |
|---:|---:|---:|
| 16 | 4 | -1 |
| 17 | 4 | 3 |
| 18 | 4 | 6 |
| 19 | 4 | 6 |
| 20 | 5 | 5 |
| 21 | 5 | 3 |
| 22 | 5 | 2 |
| 23 | 5 | 12 |
| 24 | 5 | 14 |
| 25 | 6 | 12 |
| 26 | 6 | 13 |
| 27 | 6 | 14 |
| 28 | 6 | 15 |
| 29 | 6 | 16 |
| 30 | 6 | 20 |
| 31 | 7 | 34 |
| 32 | 7 | 34 |
| 33 | 7 | 42 |
| 34 | 7 | 38 |

Thus every `E=17,...,34` layer is excluded by the refined tail relaxation. The sole non-strict row `E=16` is already strictly excluded by the exact low-excess sweep with gap 17.

For comparison, if the `2z_0` term is discarded, the relaxed h2 gaps at `E=17,21,22` are `-1,-1,-2`; retaining the elementary zero-label contribution is therefore genuinely decisive here.

## 5. Completion and frontier update

The exact low sweep excludes `E<=17`; the refined threshold tail excludes `E=17,...,34`; and (1.1) excludes `E>=35`. Therefore every `E>=0` is impossible.

State 382 was one of the N34 equality-derived scalar survivors. Removing it changes the frozen frontier to

```text
999 exclusions / 4,579 survivors,
```

split as

```text
4,501 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

Survival in this scalar catalogue is not graph feasibility.

## 6. General-theory significance

State 382 contributes a reusable strengthening rather than merely another finite closure. In the common `s in {2,3}` baseline, the previously discarded term

```text
-sum_(s_i=2,e_i=0) C_i
```

always yields at least `-2z_0`. Retaining this in the threshold dynamic programme can convert near-miss h2 layers into strict contradictions at essentially no conceptual cost.

The next family scan should therefore use the **refined h2 + zero-label correction** as the default screen, not the older h2-only relaxation.

## 7. Trust boundary

- The argument inherits the canonical bridge, selected-edge forcing, source selected-degree forcing, endpoint load, selected-excess and the no-isolated-C consequence. External review remains open.
- The preserved replays use exact integer arithmetic only. No LP/MILP infeasibility status, floating-point tolerance or timeout is used as proof.
- Unlike states 227, 279, 588 and 526, state 382 has no hand-rigidity exception: every low profile is strictly excluded by the exact envelope, and every required tail layer has a strict exact integer gap.
- Independent computational reproduction and novelty assessment remain open.
