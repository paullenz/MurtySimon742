# State 227: exclusion of total selected excess E=1,2,3

13 September 2026. **Candidate hand reduction with finite exact arithmetic; external mathematical review OPEN.** This note continues `EXACT_DEMAND_ALL_Q.md`. For N34 state 227 it proves that no selected-incidence realization can have total selected excess

```text
E=sum_i(x_i-s_i) in {1,2,3}.
```

Together with the exact-demand result `E=0`, any surviving realization of this scalar state must satisfy `E>=4`. This is still not a whole-state exclusion.

## 1. State data and excess notation

The state is

```text
a=15, b=18, t=1,
s=2^4,3^11,
rho=1^7,2,3^10,
r=39,
S=sum s_i=41.
```

Write

```text
e_i=x_i-s_i>=0,
E=sum e_i,
Q=sum x_i=41+E.
```

All labels have positive demand. The seven `rho=1` sources therefore have `q=0` by selected-edge forcing `s_i<=rho_u`; together they can absorb at most `7*3=21` incoming units.

## 2. Excess-layer source restriction

At every selected incidence `ui`, the earlier selected-excess lemma gives

```text
p_u-rho_u+1 <= e_i.                                  (2.1)
```

On this state the no-isolated-C lemma gives `d_i<=a-2=13`. Endpoint load gives

```text
q_u+p_u <= R_i+x_i = d_i+e_i,
```

hence also

```text
q_u+p_u-13 <= e_i.                                   (2.2)
```

Therefore every label selected at source `u` has excess at least

```text
L_u=max(0,p_u-rho_u+1,q_u+p_u-13).                   (2.3)
```

Let

```text
h_l = #{i:e_i>=l},
h_l^(2) = #{i:s_i=2 and e_i>=l}.
```

Since a source selects distinct labels, (2.3) gives the selection-free necessary conditions

```text
q_u<=h_(L_u)                    for rho_u=3 and L_u>0,
q_u<=h_(L_u)^(2)                for rho_u=2 and L_u>0.    (2.4)
```

The unique `rho=2` source can select only the four demand-two labels, so always `q<=4`. A `rho=3` source has the basic capacity `q<=12`.

There is a further residual-budget cap useful in the finite arithmetic. Put `x_max=max_i x_i`. Endpoint load implies `C_i=R_i+x_i>=q_u` on every selected label, so each of the `q_u` distinct selected labels has

```text
R_i>=q_u-x_max.
```

Thus

```text
39>=q_u max(0,q_u-x_max).                             (2.5)
```

## 3. Geometry-independent weighted endpoint envelope

For every selected incidence,

```text
q_u+p_u <= C_i:=R_i+x_i.
```

Summing over all selected incidences gives

```text
T:=sum_u q_u(q_u+p_u) <= sum_i x_i C_i.              (3.1)
```

For a fixed excess profile `e`,

```text
sum_i R_i=39,
0<=R_i<=13-s_i,
C_i=R_i+x_i.
```

Hence the exact maximum of the right side of (3.1) is

```text
sum_i x_i^2 + max sum_i x_i R_i,                     (3.2)
```

where the residual budget 39 is placed greedily on labels of largest `x_i`, up to capacities 11 on demand-two labels and 10 on demand-three labels. The exchange argument for this support function is the same as in the shared-budget package.

On the source side, `sum p_u=Q`. Since the seven `rho=1` sources absorb at most 21, the remaining eleven sources must carry at least `Q-21` incoming units. For each excess profile, minimizing `T` subject to (2.3)-(2.5), source capacities and this incoming requirement is a finite exact integer recurrence.

This coarse envelope already excludes most profiles below.

## 4. Top-k sharpening for concentrated excess

The difficult profiles concentrate excess on a few labels. Their weighted endpoint contribution can be bounded more sharply.

Let `q_3^(k)` denote the k-th largest selected degree among the ten `rho=3` sources. If a demand-three label has excess `e>=1`, then its selected degree is `3+e`; it is selected by that many distinct `rho=3` sources. Source selected-degree forcing gives

```text
d_i<=q_u+2,
C_i=d_i+e<=q_u+2+e.
```

Therefore

```text
C_i<=e+2+q_3^(3+e).                                  (4.1)
```

Similarly let `q_all^(k)` be the k-th largest selected degree among the unique `rho=2` source and the ten `rho=3` sources. For a demand-two label of excess `e>=2`, selected degree is `2+e`, and relaxing the `rho=2` upper bound to the `rho=3` one gives

```text
C_i<=e+2+q_all^(2+e).                                (4.2)
```

For zero-excess demand-two labels we need a lower rather than an upper bound. If there are `z_0` such labels and the `rho=2` source has parameters `(q_2,p_2)`, it can avoid at most `4-z_0` zero-excess labels. Hence at least

```text
max(0,q_2-(4-z_0))
```

of its selected labels have zero excess. Endpoint load on each such label gives `C_i>=q_2+p_2`; together with the baseline `C_i>=2`,

```text
sum_(s_i=2,e_i=0) C_i
 >=2 z_0
   +max(0,q_2-(4-z_0)) max(0,q_2+p_2-2).             (4.3)
```

Using coefficient 3 as a baseline,

```text
sum_i x_i C_i
 =3(80+E)
  -sum_(s_i=2,e_i=0) C_i
  +sum_(s_i=2,e_i>=2) (e_i-1)C_i
  +sum_(s_i=3,e_i>=1) e_i C_i.                      (4.4)
```

Equations (4.1)-(4.4) produce a completely geometry-independent sharpened upper bound once the source degree multiset is fixed. The verifier minimizes the resulting difference over all legal source types using exact integer dynamic programming.

## 5. Complete E=1 table

Up to permutation within the two demand classes there are two profiles.

| demand-two excess | demand-three excess | method | exact lower | necessary upper | gap |
|---|---|---|---:|---:|---:|
| `0^3,1` | `0^11` | coarse support | 242 | 237 | 5 |
| `0^4` | `0^10,1` | top-k sharpened | 248 | 243 | 5 |

Both are impossible.

## 6. Complete E=2 table

There are five profiles.

| demand-two excess | demand-three excess | method | lower | upper | gap |
|---|---|---|---:|---:|---:|
| `0^4` | `0^10,2` | top-k | 255 | 246 | 9 |
| `0^4` | `0^9,1,1` | top-k | 257 | 246 | 11 |
| `0^3,1` | `0^10,1` | coarse | 257 | 254 | 3 |
| `0^3,2` | `0^11` | coarse | 258 | 255 | 3 |
| `0^2,1,1` | `0^11` | coarse | 257 | 242 | 15 |

All five are impossible.

## 7. Complete E=3 table

There are ten profiles.

| demand-two excess | demand-three excess | method | lower | upper | gap |
|---|---|---|---:|---:|---:|
| `0^4` | `0^10,3` | top-k | 256 | 249 | 7 |
| `0^4` | `0^9,1,2` | top-k | 263 | 249 | 14 |
| `0^4` | `0^8,1,1,1` | top-k | 262 | 249 | 13 |
| `0^3,1` | `0^10,2` | coarse | 274 | 273 | 1 |
| `0^3,1` | `0^9,1,1` | top-k | 267 | 249 | 18 |
| `0^3,2` | `0^10,1` | coarse | 274 | 272 | 2 |
| `0^2,1,1` | `0^10,1` | coarse | 270 | 259 | 11 |
| `0^3,3` | `0^11` | top-k | 257 | 249 | 8 |
| `0^2,1,2` | `0^11` | coarse | 274 | 260 | 14 |
| `0,1,1,1` | `0^11` | coarse | 270 | 247 | 23 |

All ten are impossible.

## 8. Conclusion and scope

The exact-demand checkpoint already rules out `E=0`. Sections 5-7 rule out every excess profile with `E=1,2,3`. Therefore any realization of N34 state 227 must satisfy

```text
sum_i(x_i-s_i)>=4.                                    (8.1)
```

This is an all-selected-geometries statement: no selected-set family with total selected excess at most three can satisfy the stated canonical forcing and endpoint consequences.

It is **not** a whole-state exclusion. Profiles with `E>=4` remain open, as do the stronger shared-residual, pair and exact-destination realization constraints. Numerical solver noncompletion is not used in this proof.
