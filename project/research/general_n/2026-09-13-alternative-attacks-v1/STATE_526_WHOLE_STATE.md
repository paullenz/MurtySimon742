# N34 state 526 — whole-state exclusion

13 September 2026. **Candidate hand reduction plus exact integer enumeration; external mathematical review and independent reproduction remain OPEN.** This is the fourth whole-state exclusion produced by the alternative-geometry / selected-excess programme, after states 227, 279 and 588.

The conclusion is

```text
N34 state 526 has no selected/residual realization satisfying the canonical bridge.
```

It changes the frozen generalisation record from

```text
997 exclusions / 4,581 survivors
```

to

```text
998 exclusions / 4,580 survivors.
```

The separate fixed-order N34 proof candidate was already closed and is unchanged.

## 1. State data

State 526 has

```text
a=15, b=18, t=1,
s   = 2,3^14,
rho = 1^5,2^2,3^11,
r=sum rho=42,
S=sum s=44.
```

Put

```text
e_i=x_i-s_i >= 0,
E=sum_i e_i,
Q=sum_i x_i=S+E=44+E.
```

Every demand-three label can be selected only by the eleven `rho=3` sources. The single demand-two label may also use the two `rho=2` sources. Thus the five `rho=1` sources have `q=0`; each `rho=2` source has `q<=1`; and each `rho=3` source has `q<=12`.

The basic incoming cap is

```text
p_u<=rho_u+b-a-1=rho_u+2.
```

Hence total incoming capacity is

```text
5*3 + 2*4 + 11*5 = 78.
```

Since `sum p_u=Q=44+E`, every realization has

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
sum_i C_i=r+Q=86+E.
```

Using coefficient three as baseline,

```text
sum_i x_i C_i
 =3(86+E)
  - 1_(e_2=0) C_2
  + 1_(e_2>=2)(e_2-1)C_2
  + sum_(s_i=3,e_i>=1) e_i C_i.                     (2.2)
```

For a demand-three label with excess e, selected degree is `3+e` and all selected incidences lie on `rho=3` sources. If `q_3^(k)` is the k-th largest q among those eleven sources, source selected-degree forcing gives

```text
C_i <= e+2+q_3^(3+e).                                (2.3)
```

For the demand-two label, selected degree is `2+e`. Relaxing the `rho=2` source bound by one unit and taking the k-th largest q over all thirteen eligible `rho>=2` sources gives safely

```text
C_2 <= e+2+q_all^(2+e).                              (2.4)
```

Thus demand-three excess satisfies `e<=8`, while the demand-two excess satisfies `e<=11`.

The selected-excess lemma and the no-isolated-C / endpoint consequence give, for a selected label at source u,

```text
L_u=max(0,p_u-rho_u+1,q_u+p_u-13) <= e_i.            (2.5)
```

If `H_l` is the number of labels eligible at that source with excess at least l, `L_u>0` forces

```text
q_u<=H_(L_u).                                         (2.6)
```

The preserved residual-budget consequence is also used:

```text
42 >= q_u max(0,q_u-x_max).                           (2.7)
```

For fixed source degrees and excess profile, incoming units are placed first on the smallest q-values up to their admissible p-caps. This gives the exact minimum of `sum q_u p_u` by a simple exchange argument.

## 3. Exact low-excess sweep E=0,...,16

`verify_state526_low.cpp` enumerates every excess profile up to permutation among the fourteen demand-three labels, all three possible sorted q-patterns on the two `rho=2` sources, and every nondecreasing eleven-source `rho=3` q-vector.

The complete coarse-envelope table is:

| E | profiles | strict | equality | negative | source-infeasible | minimum strict gap |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 | 0 | 0 | 4 |
| 1 | 2 | 2 | 0 | 0 | 0 | 9 |
| 2 | 4 | 4 | 0 | 0 | 0 | 15 |
| 3 | 7 | 7 | 0 | 0 | 0 | 8 |
| 4 | 12 | 12 | 0 | 0 | 0 | 8 |
| 5 | 19 | 19 | 0 | 0 | 0 | 6 |
| 6 | 30 | 30 | 0 | 0 | 0 | 3 |
| 7 | 45 | 44 | 1 | 0 | 0 | 5 |
| 8 | 67 | 67 | 0 | 0 | 0 | 5 |
| 9 | 96 | 96 | 0 | 0 | 0 | 3 |
| 10 | 136 | 136 | 0 | 0 | 0 | 5 |
| 11 | 188 | 188 | 0 | 0 | 0 | 11 |
| 12 | 257 | 257 | 0 | 0 | 0 | 7 |
| 13 | 345 | 345 | 0 | 0 | 0 | 12 |
| 14 | 459 | 459 | 0 | 0 | 0 | 18 |
| 15 | 601 | 601 | 0 | 0 | 0 | 14 |
| 16 | 780 | 780 | 0 | 0 | 0 | 23 |

There is exactly one non-strict excess profile, and a dedicated enumeration inside the verifier confirms exactly one q-vector can attain nonpositive coarse gap:

```text
E=7,
e_2=7,
e_3=0^14,
q_(rho=2)=1,1,
q_(rho=3)=1,1,5^7,6^2.                               (3.1)
```

The coarse gap is exactly zero.

## 4. Hand rigidity of the E=7 equality

For (3.1), `Q=51`. The five `rho=1` sources can absorb at most 15 incoming units, so the thirteen `rho>=2` sources must absorb at least 36.

Under this profile the exact p-caps are:

```text
rho=2, q=1: p<=4  (two sources),
rho=3, q=1: p<=5  (two sources),
rho=3, q=5 or 6: p<=2  (nine sources).
```

Their capacities sum to

```text
2*4 + 2*5 + 9*2 = 36.
```

Therefore equality forces every one of these sources to its cap:

```text
rho=2,q=1 => p=4,
rho=3,q=1 => p=5,
rho=3,q=5 or 6 => p=2.                                (4.1)
```

There is only one positive-excess label: the demand-two label with `e=7` and hence `x=9`.

At either `rho=2,q=1,p=4` source, selected excess gives

```text
p-rho+1=3 <= e_i,
```

so its unique selected label must be the high-excess demand-two label. The same is true at either `rho=3,q=1,p=5` source. Thus the high-excess label uses all four q=1 sources and five of the nine q=5/6 sources.

Every one of the fourteen demand-three labels has zero excess. Such a selected label requires

```text
p<=rho-1=2.
```

Hence none can use either `rho=3,q=1,p=5` source; all of their selected incidences lie on the nine `rho=3` sources with q=5 or 6 and p=2.

Each zero-excess demand-three label has selected degree three. Endpoint load at any of its incidences therefore gives

```text
C_i >= q_u+p_u >= 5+2 = 7.
```

Consequently the fourteen zero-excess labels alone satisfy

```text
sum_(zero demand-three labels) C_i >= 14*7 = 98.      (4.2)
```

But the exact ledger gives

```text
sum_i C_i = r+Q = 42+51 = 93.                         (4.3)
```

Equations (4.2)-(4.3) contradict one another before the high-excess label is even counted. Hence the unique coarse equality is impossible.

Therefore every profile with `E<=16` is excluded.

## 5. h_2 tail E=16,...,34

For the tail put

```text
h=#{i:e_i>=2}.
```

The threshold family gives the relaxed caps

```text
rho=2: q>h => p<=2, otherwise p<=4,
rho=3: q>h => p<=3, otherwise p<=5.                  (5.1)
```

`verify_state526_tail.cpp` combines only these relaxed caps with the top-k endpoint bounds (2.3)-(2.4), and drops the negative zero-excess demand-two term from (2.2). Thus a positive gap is conservative.

The exact global minimum gaps are:

| E | minimizing h | minimum gap |
|---:|---:|---:|
| 16 | 4 | 0 |
| 17 | 4 | 5 |
| 18 | 4 | 8 |
| 19 | 5 | 8 |
| 20 | 5 | 8 |
| 21 | 5 | 7 |
| 22 | 5 | 6 |
| 23 | 5 | 10 |
| 24 | 6 | 10 |
| 25 | 6 | 13 |
| 26 | 6 | 16 |
| 27 | 6 | 18 |
| 28 | 6 | 22 |
| 29 | 6 | 25 |
| 30 | 6 | 28 |
| 31 | 7 | 40 |
| 32 | 7 | 40 |
| 33 | 7 | 44 |
| 34 | 7 | 42 |

The sole non-strict relaxed tail layer is `E=16`, already covered by the exact low-excess sweep with minimum strict gap 23. Therefore every `E=17,...,34` is excluded by the relaxed tail directly and `E=16` is excluded exactly.

Together with the capacity ceiling (1.1), this excludes every `E>=0`.

## 6. Frontier update

State 526 was one of the N34 equality-derived scalar survivors. Removing it changes the frozen frontier to

```text
998 exclusions / 4,580 survivors,
```

split as

```text
4,502 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

Survival in this scalar catalogue is not graph feasibility.

## 7. General-theory significance

State 526 strengthens the emerging pattern in two ways.

First, the relaxed `h_2` tail is already sufficient for every genuinely high-excess layer; only one boundary layer needs the exact profile machinery. Second, the unique low-excess equality is killed entirely by **source availability**: the incoming ledger forces the cheap q=1 sources to high p, making them unavailable to zero-excess labels and pushing all fourteen zero-excess demand-three labels onto q>=5 sources. The endpoint budget then fails immediately.

This is a particularly clean instance of the proposed threshold-plus-availability theorem template.

## 8. Trust boundary

- The argument inherits the canonical bridge, selected-edge forcing, source selected-degree forcing, endpoint load, selected-excess and the no-isolated-C consequence. External review remains open.
- The preserved replays use exact integer arithmetic only. No LP/MILP infeasibility status, floating-point tolerance or timeout is used as proof.
- The `E=7` case requires the explicit hand rigidity argument in Section 4.
- Independent computational reproduction and novelty assessment remain open.
