# N34 state 227 — whole-state exclusion

13 September 2026. **Candidate hand reduction plus exact finite enumeration; external mathematical review and independent reproduction remain OPEN.** This note completes the state-227 programme begun in `MARGIN_CLASS_EXAMPLE.md`, `EXACT_DEMAND_ALL_Q.md`, `LOW_EXCESS_LAYERS.md` and `EXCESS_SWEEP_TO_8.md`.

The conclusion is now a **whole scalar-state exclusion**:

```text
N34 state 227 has no selected/residual realization satisfying the canonical bridge.
```

This is the first whole-state exclusion added by the alternative-geometry programme. It changes the frozen generalisation record from

```text
994 exclusions / 4,584 survivors
```

to

```text
995 exclusions / 4,583 survivors.
```

It does not prove the unrestricted Murty–Simon conjecture and it does not alter the already closed fixed-order N34 candidate proof.

## 1. State data

State 227 has

```text
a=15, b=18, t=1,
s = 2^4,3^11,
rho = 1^7,2,3^10,
r=39,
S=sum_i s_i=41.
```

Put

```text
e_i=x_i-s_i >= 0,
E=sum_i e_i,
Q=sum_i x_i=41+E.
```

Every selected label has positive demand. By selected-edge forcing `s_i<=rho_u`, the seven `rho=1` sources have `q_u=0`. The unique `rho=2` source can use only the four demand-two labels, hence

```text
0<=q_2<=4.
```

For each of the ten `rho=3` sources, A-side capacity gives

```text
0<=q_u<=a-rho_u=12.
```

The basic incoming cap is

```text
p_u<=rho_u+b-a-1=rho_u+2.
```

Thus the seven `rho=1` sources can absorb at most 21 incoming selected pairs, the `rho=2` source at most 4, and each `rho=3` source at most 5.

## 2. Reusable endpoint/excess envelope

Put

```text
C_i=R_i+x_i,
T=sum_u q_u(q_u+p_u).
```

Endpoint load on every selected incidence gives

```text
T <= sum_i x_i C_i.                                  (2.1)
```

Also

```text
sum_i C_i=r+Q=80+E.
```

Using coefficient 3 as baseline,

```text
sum_i x_i C_i
 =3(80+E)
  -sum_(s_i=2,e_i=0) C_i
  +sum_(s_i=2,e_i>=2) (e_i-1) C_i
  +sum_(s_i=3,e_i>=1) e_i C_i.                      (2.2)
```

The negative demand-two term may safely be discarded when an upper envelope is wanted.

### Top-k bound for demand-three labels

If a demand-three label has excess `e>=1`, then its selected degree is `3+e`. It can be selected only by the ten `rho=3` sources. Let `q_3^(k)` be the k-th largest selected degree among those ten sources. Source selected-degree forcing gives `d_i<=q_u+2` on every selected incidence, and because `C_i=d_i+e`,

```text
C_i <= e+2+q_3^(3+e).                                (2.3)
```

If `e>7`, the label would require more than ten eligible sources and is impossible outright.

### Top-k bound for demand-two labels

If a demand-two label has excess `e>=2`, its selected degree is `2+e`. It may use the unique `rho=2` source and the ten `rho=3` sources. Let `q_all^(k)` be the k-th largest selected degree among these eleven sources. Relaxing the `rho=2` source bound by one unit gives safely

```text
C_i <= e+2+q_all^(2+e).                              (2.4)
```

If `e>9`, more than eleven eligible sources would be required, so the profile is impossible.

For a fixed source-degree multiset and excess profile, let `P_+` be the sum of the positive correction terms in (2.2) after applying (2.3)-(2.4). Then every realization must satisfy

```text
T-P_+ <= 3(80+E),                                    (2.5)
```

and retaining the zero-excess demand-two lower term only strengthens the contradiction.

## 3. Complete exact profile sweep through E=20

The verifier `verify_state227_exact_to20.cpp` enumerates every excess profile up to permutation within the four demand-two and eleven demand-three labels. For each profile it enumerates every nondecreasing ten-source `rho=3` selected-degree vector, the `rho=2` selected degree, and the exact minimum incoming assignment compatible with the excess-layer restrictions.

No floating-point optimizer is used. Incoming load is assigned greedily to the smallest-q sources once the q-vector and source caps are fixed; the exchange argument is exact.

The complete table is:

| E | profiles | strict exclusions | equality profiles | source-infeasible | minimum strict gap |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 | 0 | 1 |
| 1 | 2 | 2 | 0 | 0 | 5 |
| 2 | 5 | 5 | 0 | 0 | 9 |
| 3 | 10 | 10 | 0 | 0 | 7 |
| 4 | 20 | 20 | 0 | 0 | 6 |
| 5 | 35 | 35 | 0 | 0 | 4 |
| 6 | 62 | 61 | 1 | 0 | 4 |
| 7 | 102 | 101 | 1 | 0 | 8 |
| 8 | 167 | 166 | 0 | 1 | 9 |
| 9 | 262 | 259 | 0 | 3 | 10 |
| 10 | 407 | 398 | 0 | 9 | 12 |
| 11 | 614 | 593 | 0 | 21 | 13 |
| 12 | 918 | 872 | 0 | 46 | 14 |
| 13 | 1,342 | 1,251 | 0 | 91 | 22 |
| 14 | 1,944 | 1,772 | 0 | 172 | 26 |
| 15 | 2,770 | 2,463 | 0 | 307 | 26 |
| 16 | 3,912 | 3,381 | 0 | 531 | 31 |
| 17 | 5,451 | 4,567 | 0 | 884 | 38 |
| 18 | 7,536 | 6,101 | 0 | 1,435 | 34 |
| 19 | 10,303 | 8,037 | 0 | 2,266 | 40 |
| 20 | 13,984 | 10,453 | 0 | 3,531 | 44 |

Totals through E=20:

```text
49,847 profiles,
40,548 strict envelope exclusions,
9,297 source-infeasible profiles,
2 equality profiles.
```

The two equality profiles are exactly the previously isolated E=6 and E=7 cases. Their equality conditions force zero-excess demand-two labels to have `C_i=2`, while too many of their selected incidences come from sources with `q>=5`; endpoint load then gives `C_i>=5`. The detailed rigidity arguments are preserved in `EXCESS_SWEEP_TO_8.md` and are unchanged.

Hence

```text
state 227 realization => E>=21.                       (3.1)
```

## 4. High-excess coupling through h_2

For the remaining tail define

```text
h = #{i:e_i>=2}.
```

The selected-excess lemma says that on every selected incidence at a source of residual degree `rho`,

```text
p_u-rho_u+1 <= e_i.
```

For a `rho=3` source, if `p_u>=4`, every one of its `q_u` distinct selected labels must therefore satisfy `e_i>=2`. Consequently

```text
p_u>=4 => q_u<=h,
```

or contrapositively

```text
q_u>h => p_u<=3.                                     (4.1)
```

Together with the basic cap `p_u<=5`, every `rho=3` source satisfies the relaxed high-excess cap

```text
p_u <= 5  if q_u<=h,
p_u <= 3  if q_u>h.                                  (4.2)
```

This deliberately ignores the stronger facts that `p=5` requires excess at least three and that large `q+p` can force still more excess.

The seven `rho=1` sources absorb at most 21 incoming units. Since

```text
sum_u p_u=sum_u q_u=Q,
```

the remaining eleven sources must absorb at least

```text
P=Q-21=20+E                                           (4.3)
```

incoming units.

For fixed `q_2`, the ten sorted `rho=3` selected degrees and `h`, the exact minimum of `T` under the relaxed caps (4.2) is obtained by assigning these P incoming units first to the smallest q-values, up to their capacities. This is again an exchange argument, not a solver claim.

## 5. Exact tail minimization, E=21,...,34

For a fixed source-degree vector and E, the positive endpoint correction `P_+` depends only on the excess values through (2.3)-(2.4). `verify_state227_tail.cpp` uses a finite dynamic programme over the four demand-two and eleven demand-three labels to maximize `P_+` subject to

```text
sum e_i=E,
#{i:e_i>=2}=h,
0<=e_i<=9 on demand-two labels,
0<=e_i<=7 on demand-three labels.
```

For each source vector and h it then computes

```text
B_relax = T_min - P_+^max.
```

Every actual realization satisfies

```text
T-P_+ >= B_relax,
```

so `B_relax>3(80+E)` excludes the entire `(E,h,q)` class. The verifier takes the minimum over all

```text
q_2 in {0,...,4},
0<=q_1<=...<=q_10<=12,
q_2+sum q_j=41+E,
h in {0,...,15}.
```

The resulting global minima are:

| E | minimizing h | minimum gap above `3(80+E)` |
|---:|---:|---:|
| 21 | 5 | 8 |
| 22 | 6 | 13 |
| 23 | 6 | 14 |
| 24 | 6 | 15 |
| 25 | 6 | 15 |
| 26 | 6 | 15 |
| 27 | 6 | 15 |
| 28 | 6 | 26 |
| 29 | 7 | 32 |
| 30 | 7 | 40 |
| 31 | 7 | 44 |
| 32 | 7 | 39 |
| 33 | 7 | 34 |
| 34 | 8 | 56 |

The weakest tail contradiction is therefore still strict by eight units.

Hence

```text
state 227 realization => E>=35.                       (5.1)
```

## 6. E>=35 is impossible by total incoming capacity

The basic incoming caps alone give

```text
sum_u p_u
 <= 7*3 + 1*4 + 10*5
 =75.
```

But `sum p_u=Q=41+E`. Therefore

```text
41+E<=75,
E<=34.                                                (6.1)
```

Equations (5.1) and (6.1) contradict each other.

Therefore state 227 has no realization.

## 7. Consequence for the frozen generalisation frontier

State 227 was one of the 4,584 scalar survivors after the compatible-routing catalogue. Its whole-state exclusion changes the record to

```text
995 exclusions / 4,583 survivors,
```

split as

```text
4,505 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

This is a frontier update in the generalisation experiment, not a new fixed-order N34 obligation: the separate N34 theorem candidate was already closed.

## 8. Trust boundary and audit notes

1. The mathematical reduction depends on the canonical bridge, especially selected-edge forcing, source selected-degree forcing, endpoint load, the exact selected/incoming ledger and the selected-excess lemma. External review of those implications remains the principal correlated correctness risk.
2. The E<=20 and E=21,...,34 computations use exact integer enumeration only. No LP/MILP infeasibility status, timeout or floating-point tolerance is used as proof.
3. The high-excess argument is deliberately relaxed: it ignores several stronger source/excess restrictions. That makes the positive tail gaps conservative.
4. The only non-strict numerical cases in E<=20 are the already preserved E=6 and E=7 equality profiles; both require the separate hand rigidity argument.
5. Independent computational reproduction and novelty assessment remain open.

## 9. General-theory lesson

The decisive new mechanism is not state-specific in form. For any excess threshold `ell>=1`, the selected-excess inequality implies that a source with

```text
p_u-rho_u+1 >= ell
```

can select only labels having `e_i>=ell`. If

```text
h_ell=#{i:e_i>=ell},
```

then necessarily

```text
q_u<=h_ell.
```

Equivalently,

```text
q_u>h_ell => p_u<=rho_u+ell-2.                       (9.1)
```

State 227 closes already at `ell=2`. Applying the full threshold family (9.1) across the remaining 4,583 frontier states is the next natural general attack.
