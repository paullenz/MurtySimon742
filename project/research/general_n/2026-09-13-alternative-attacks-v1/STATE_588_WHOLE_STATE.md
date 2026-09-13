# N34 state 588 — whole-state exclusion

13 September 2026. **Candidate hand reduction plus exact integer enumeration; external mathematical review and independent reproduction remain OPEN.** This is the third whole-state exclusion produced by the alternative-geometry / selected-excess programme, after states 227 and 279.

The conclusion is

```text
N34 state 588 has no selected/residual realization satisfying the canonical bridge.
```

It changes the frozen generalisation record from

```text
996 exclusions / 4,582 survivors
```

to

```text
997 exclusions / 4,581 survivors.
```

The separate fixed-order N34 proof candidate was already closed and is unchanged.

## 1. State data

State 588 has

```text
a=15, b=18, t=1,
s   = 3^15,
rho = 1^5,2,3^12,
r=sum rho=43,
S=sum s=45.
```

Put

```text
e_i=x_i-s_i >= 0,
E=sum_i e_i,
Q=sum_i x_i=S+E=45+E.
```

Every selected label has base demand three. By selected-edge forcing `s_i<=rho_u`, the five `rho=1` sources and the unique `rho=2` source have `q_u=0`. Only the twelve `rho=3` sources can be active, and each has

```text
0<=q_u<=a-rho_u=12.
```

The basic incoming cap is

```text
p_u<=rho_u+b-a-1=rho_u+2.
```

Hence the inactive sources absorb at most

```text
5*3 + 1*4 = 19
```

incoming units, while each active source absorbs at most five. The total incoming capacity is therefore

```text
19+12*5=79.
```

Since `sum p_u=Q=45+E`, every realization has

```text
E<=34.                                                (1.1)
```

## 2. Endpoint/excess envelope

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
sum_i C_i=r+Q=88+E.
```

Because every base demand is exactly three,

```text
sum_i x_i C_i
 =3(88+E) + sum_i e_i C_i.                           (2.2)
```

If label i has excess e, then `x_i=3+e`. It can be selected only by the twelve `rho=3` sources. Source selected-degree forcing gives on every selected incidence

```text
d_i<=q_u+2,
C_i=d_i+e<=q_u+2+e.
```

Let `q^(k)` be the k-th largest selected degree among the twelve active sources. Therefore

```text
C_i <= e+2+q^(3+e).                                  (2.3)
```

In particular `e<=9`.

The selected-excess lemma and the no-isolated-C / endpoint consequence used in states 227 and 279 give, for a selected label at an active source,

```text
L_u=max(0,p_u-2,q_u+p_u-13) <= e_i.                  (2.4)
```

If `H_l=#{i:e_i>=l}`, then `L_u>0` forces

```text
q_u<=H_(L_u).                                         (2.5)
```

The preserved residual-budget bound also gives, with `x_max=max_i(3+e_i)`,

```text
43 >= q_u max(0,q_u-x_max).                          (2.6)
```

For a fixed excess profile and q-vector, the minimum possible incoming contribution `sum q_u p_u` is obtained by placing required incoming units first on the smallest q-values, subject to the exact caps (2.4)-(2.5). This is an exchange argument and uses integer arithmetic only.

## 3. Exact low-excess sweep E=0,...,15

`verify_state588_low.cpp` enumerates every excess partition of E among the fifteen demand-three labels and every nondecreasing twelve-source q-vector. The result is:

| E | profiles | strict | equality | negative | source-infeasible | minimum strict gap |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 | 0 | 0 | 6 |
| 1 | 1 | 1 | 0 | 0 | 0 | 12 |
| 2 | 2 | 2 | 0 | 0 | 0 | 17 |
| 3 | 3 | 3 | 0 | 0 | 0 | 10 |
| 4 | 5 | 5 | 0 | 0 | 0 | 9 |
| 5 | 7 | 7 | 0 | 0 | 0 | 8 |
| 6 | 11 | 11 | 0 | 0 | 0 | 3 |
| 7 | 15 | 15 | 0 | 0 | 0 | 4 |
| 8 | 22 | 22 | 0 | 0 | 0 | 5 |
| 9 | 30 | 29 | 1 | 0 | 0 | 12 |
| 10 | 41 | 41 | 0 | 0 | 0 | 7 |
| 11 | 54 | 54 | 0 | 0 | 0 | 8 |
| 12 | 73 | 73 | 0 | 0 | 0 | 6 |
| 13 | 94 | 94 | 0 | 0 | 0 | 15 |
| 14 | 123 | 123 | 0 | 0 | 0 | 16 |
| 15 | 157 | 157 | 0 | 0 | 0 | 8 |

There is exactly one non-strict profile and exactly one q-vector capable of attaining the coarse equality:

```text
E=9,
e = 0^12,3^3,
q = 3^6,6^6.                                         (3.1)
```

### Hand rigidity for the E=9 equality profile

For (3.1), equality in the incoming minimization forces all six `q=3` sources to carry `p=5`; the remaining five incoming units lie on the six `q=6` sources.

At a `rho=3`, `p=5` source the selected-excess lemma forces every selected label to have excess at least three. There are exactly three such labels, and the source has q=3, so every `q=3,p=5` source selects exactly those three high-excess labels. Each high-excess label has selected degree `x=6`, hence it is selected by all six `q=3` sources and by no `q=6` source.

Consequently all 36 selected incidences from the six `q=6` sources belong to the twelve zero-excess labels. Each zero-excess label has selected degree three.

Endpoint load now gives two lower bounds on the raw B-cross degrees. Each high-excess label is selected at a `q=3,p=5` source, so

```text
sum_(high) C_i >= 3*8 =24.                            (3.2)
```

For the zero-excess labels, sum endpoint load over the 36 selected incidences from the `q=6` sources. Since each zero-excess label occurs exactly three times,

```text
3 sum_(zero) C_i
 >= sum_(q=6 sources) q_u(q_u+p_u)
 = 6*6*6 + 6*5
 =246,
```

so

```text
sum_(zero) C_i >=82.                                  (3.3)
```

Equations (3.2)-(3.3) imply

```text
sum_i C_i >=106,
```

contradicting the exact ledger `sum_i C_i=88+9=97`.

Thus every profile with `E<=15` is impossible.

## 4. h_2 tail relaxation and its two exceptions

For the tail put

```text
h=#{i:e_i>=2}.
```

At an active `rho=3` source the threshold family gives

```text
q_u>h => p_u<=3,                                     (4.1)
```

while the basic cap is `p_u<=5`. `verify_state588_tail.cpp` deliberately retains only this relaxed h2 cap and the top-k bound (2.3). It obtains the following global minimum gaps above `3(88+E)`:

| E | minimizing h | gap |
|---:|---:|---:|
| 16 | 4 | -3 |
| 17 | 4 | 1 |
| 18 | 4 | 6 |
| 19 | 5 | 8 |
| 20 | 5 | 8 |
| 21 | 5 | 6 |
| 22 | 5 | 6 |
| 23 | 5 | 4 |
| 24 | 5 | 0 |
| 25 | 5 | 14 |
| 26 | 6 | 13 |
| 27 | 6 | 6 |
| 28 | 6 | 7 |
| 29 | 6 | 8 |
| 30 | 6 | 12 |
| 31 | 6 | 18 |
| 32 | 6 | 26 |
| 33 | 7 | 31 |
| 34 | 7 | 30 |

Thus the conservative h2 relaxation excludes every tail layer except `E=16` and `E=24`.

## 5. Exact replay of E=16 and E=24

`verify_state588_exact_16_24.cpp` returns to the full exact profile restrictions (2.4)-(2.6) for the two non-strict h2 layers.

```text
E=16: 200 profiles, all 200 strictly excluded, minimum gap 17.
E=24: 1,009 profiles, 793 strictly excluded, 216 source-infeasible,
      minimum strict gap 32.
```

There are no equality or negative profiles in either layer. Therefore every `E=16,...,34` layer is impossible.

Together with the capacity ceiling (1.1), this excludes every `E>=0` and proves the state-588 whole-state exclusion within the canonical bridge.

## 6. Frontier update

State 588 was one of the N34 equality-derived scalar survivors. Removing it changes the frozen frontier to

```text
997 exclusions / 4,581 survivors,
```

split as

```text
4,503 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

Survival in this scalar catalogue is not graph feasibility.

## 7. General-theory lesson

State 588 is structurally cleaner than states 227 and 279 because every base demand is three. It confirms that the threshold mechanism is not tied to demand-two correction terms. It also exposes a useful pattern for future automation:

1. use a cheap h2 relaxation to cover almost the entire excess range;
2. exact-enumerate only the few non-strict layers;
3. isolate any surviving low-excess equality and convert its equality conditions into an incidence-rigidity contradiction.

This suggests the next scan should rank remaining states by the number of non-strict h2 layers rather than attempting full exact enumeration everywhere.

## 8. Trust boundary

- The argument inherits the canonical bridge, selected-edge forcing, source selected-degree forcing, endpoint load, selected-excess and the no-isolated-C consequence. External review remains open.
- All preserved replays use exact integer arithmetic only. No LP/MILP infeasibility status, floating-point tolerance or timeout is used as proof.
- The E=9 case requires the explicit hand rigidity argument in Section 3.
- Independent reproduction and novelty assessment remain open.
