# N34 state 279 — whole-state exclusion

13 September 2026. **Candidate hand reduction plus exact integer enumeration; external mathematical review and independent reproduction remain OPEN.** This is the second whole-state exclusion produced by the alternative-geometry / selected-excess programme, after state 227.

The conclusion is

```text
N34 state 279 has no selected/residual realization satisfying the canonical bridge.
```

It changes the frozen generalisation record from

```text
995 exclusions / 4,583 survivors
```

to

```text
996 exclusions / 4,582 survivors.
```

This is a generalisation-frontier result. The separate fixed-order N34 proof candidate was already closed and is unchanged.

## 1. State data

State 279 has

```text
a=15, b=18, t=1,
s   = 2^3,3^12,
rho = 1^7,3^11,
r=sum rho=40,
S=sum s=42.
```

Put

```text
e_i=x_i-s_i >= 0,
E=sum_i e_i,
Q=sum_i x_i=S+E=42+E.
```

Every positive-demand label has base demand at least two. Selected-edge forcing therefore gives `q_u=0` on all seven `rho=1` sources. The eleven `rho=3` sources have

```text
0<=q_u<=a-rho_u=12.
```

The basic incoming cap is

```text
p_u<=rho_u+b-a-1=rho_u+2,
```

so the seven `rho=1` sources absorb at most 21 incoming units and every `rho=3` source at most five.

## 2. Endpoint/excess envelope

For label i put

```text
C_i=R_i+x_i,
```

and put

```text
T=sum_u q_u(q_u+p_u).
```

Endpoint load on every selected incidence gives

```text
T <= sum_i x_i C_i.                                  (2.1)
```

Also

```text
sum_i C_i=r+Q=82+E.
```

Using coefficient three as baseline,

```text
sum_i x_i C_i
 =3(82+E)
  -sum_(s_i=2,e_i=0) C_i
  +sum_(s_i=2,e_i>=2) (e_i-1)C_i
  +sum_(s_i=3,e_i>=1) e_i C_i.                      (2.2)
```

### Top-k label bounds

All selected labels can use only the eleven `rho=3` sources. If a label with base demand s has excess e, then its selected degree is

```text
x=s+e.
```

Source selected-degree forcing gives, at each selected incidence,

```text
d_i<=q_u+rho_u-1=q_u+2,
```

hence

```text
C_i=d_i+e<=q_u+2+e.
```

Let `q^(k)` denote the k-th largest selected degree among the eleven `rho=3` sources. Because the label is selected by `s+e` distinct sources,

```text
C_i <= e+2+q^(s+e).                                  (2.3)
```

Consequently a demand-two label has `e<=9` and a demand-three label has `e<=8`; larger excess would require more than eleven eligible selected sources.

### Source excess restrictions

The selected-excess lemma gives on every selected incidence

```text
p_u-rho_u+1 <= e_i.
```

The no-isolated-C/endpoint consequence gives in this state

```text
q_u+p_u-13 <= e_i.
```

Thus every label selected by source u has excess at least

```text
L_u=max(0,p_u-2,q_u+p_u-13).                         (2.4)
```

If `H_l=#{i:e_i>=l}`, then for `L_u>0`

```text
q_u<=H_(L_u).                                         (2.5)
```

A residual-budget cap also follows exactly as in the state-227 package. If `x_max=max_i x_i`, then every selected label at a q-source has `R_i>=q_u-x_max`, so

```text
40 >= q_u max(0,q_u-x_max).                          (2.6)
```

## 3. Exact profile sweep through E=15

`verify_state279_low.cpp` enumerates every excess profile up to permutation within the three demand-two and twelve demand-three labels. For each profile it enumerates every nondecreasing eleven-source q-vector, applies (2.4)-(2.6), minimizes incoming load exactly by assigning required p-units first to the smallest q-values, and applies the top-k endpoint bounds (2.3).

No numerical optimizer is used.

The complete coarse-envelope table is:

| E | profiles | strict | equality | source-infeasible | minimum strict gap | minimum finite gap |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 | 0 | 2 | 2 |
| 1 | 2 | 2 | 0 | 0 | 5 | 5 |
| 2 | 5 | 5 | 0 | 0 | 11 | 11 |
| 3 | 10 | 10 | 0 | 0 | 5 | 5 |
| 4 | 19 | 19 | 0 | 0 | 5 | 5 |
| 5 | 33 | 33 | 0 | 0 | 2 | 2 |
| 6 | 57 | 55 | 1 | 0 | 6 | -2 |
| 7 | 92 | 92 | 0 | 0 | 5 | 5 |
| 8 | 147 | 147 | 0 | 0 | 2 | 2 |
| 9 | 226 | 225 | 1 | 0 | 9 | 0 |
| 10 | 341 | 341 | 0 | 0 | 7 | 7 |
| 11 | 501 | 501 | 0 | 0 | 8 | 8 |
| 12 | 726 | 726 | 0 | 0 | 6 | 6 |
| 13 | 1,028 | 1,028 | 0 | 0 | 15 | 15 |
| 14 | 1,438 | 1,438 | 0 | 0 | 17 | 17 |
| 15 | 1,977 | 1,977 | 0 | 0 | 20 | 20 |

Only three profiles are not strictly excluded by the first envelope. In each case the q-vector capable of attaining nonpositive gap is unique. They are handled next.

## 4. Rigidity of the three low-excess exceptions

All three exceptional profiles have the three demand-two labels at zero excess. Thus each such label has selected degree two. Let

```text
C_0=sum_(three demand-two labels) C_i.
```

The coarse calculation above used only `C_0>=6`.

### E=6, one excess-six demand-three label

The profile is

```text
e_2 = 0,0,0,
e_3 = 0^11,6.
```

The unique q-vector with coarse gap at most zero is

```text
q = 1,1,5,5,5,5,5,5,5,5,6.
```

The coarse minimum has gap `-2`. The eleven `rho=3` sources must carry at least

```text
Q-21=48-21=27
```

incoming units. For this excess profile a q=5 or q=6 source has `p<=2`, while each q=1 source has `p<=5`. The nine q>=5 sources can therefore absorb at most 18 incoming units, so the two q=1 sources must absorb at least nine between them. In particular each has `p>=4` except possibly one with p=4 and the other p=5; neither can select a zero-excess label because e=0 requires `p<=rho-1=2`.

Hence every selected incidence of a zero-excess demand-two label comes from a source with `q>=5`. Endpoint load gives `C_i>=q+p>=5` on every such incidence. Each of the three labels has two incidences, so

```text
C_0>=15,
```

nine units stronger than the coarse bound. The apparent `-2` escape becomes a strict contradiction by at least seven.

### E=6, two excess-three demand-three labels

The profile is

```text
e_2 = 0,0,0,
e_3 = 0^10,3,3.
```

The unique coarse equality q-vector is

```text
q = 2,2,2,2,2,6,6,6,6,7,7.
```

Coarse equality would require `C_0=6`, hence every one of the three demand-two labels would have `C_i=2`. Any source selecting such a label must then satisfy endpoint load `q+p<=2`. Since the minimum positive q is two, it must be a q=2 source with p=0.

Each q=2 source can select at most two of the three demand-two labels. Six selected incidences therefore require at least three q=2,p=0 sources. But then the remaining two q=2 sources carry at most five incoming units each, and the six q>=6 sources carry at most two each. Total incoming capacity on the eleven active sources is at most

```text
2*5 + 6*2 =22,
```

whereas `Q-21=48-21=27` is required. Contradiction. Thus `C_0>6` and the coarse equality is impossible.

### E=9, three excess-three demand-three labels

The profile is

```text
e_2 = 0,0,0,
e_3 = 0^9,3,3,3.
```

The unique coarse equality q-vector is

```text
q = 3,3,3,3,3,6,6,6,6,6,6.
```

Every source has `q>=3`. But each zero-excess demand-two label is selected twice, so endpoint load immediately gives

```text
C_i>=3
```

for each of the three labels. Hence `C_0>=9>6`, contradicting the equality requirement.

Therefore every profile with `E<=15` is impossible.

## 5. Threshold tail E=16,...,34

For the tail put

```text
h=#{i:e_i>=2}.
```

The general threshold consequence of the selected-excess lemma gives for every `rho=3` source

```text
q_u>h => p_u<=3,                                     (5.1)
```

while the basic cap remains `p_u<=5` when `q_u<=h`.

`verify_state279_tail.cpp` deliberately uses only this relaxed p-cap together with the top-k endpoint bounds. It drops the negative zero-excess demand-two term from (2.2), so any positive gap is conservative.

The exact global minimum gaps are:

| E | minimizing h | minimum gap |
|---:|---:|---:|
| 16 | 4 | 2 |
| 17 | 4 | 7 |
| 18 | 4 | 10 |
| 19 | 5 | 10 |
| 20 | 5 | 10 |
| 21 | 5 | 9 |
| 22 | 5 | 8 |
| 23 | 5 | 12 |
| 24 | 6 | 12 |
| 25 | 6 | 15 |
| 26 | 6 | 18 |
| 27 | 6 | 20 |
| 28 | 6 | 24 |
| 29 | 6 | 27 |
| 30 | 6 | 30 |
| 31 | 7 | 42 |
| 32 | 7 | 42 |
| 33 | 7 | 46 |
| 34 | 7 | 44 |

Thus any realization would require `E>=35`.

## 6. E>=35 is impossible by incoming capacity

The total basic incoming capacity is

```text
7*3 + 11*5 =76.
```

But

```text
sum p_u = Q =42+E.
```

Therefore `E>=35` would require `Q>=77>76`, impossible.

Combining Sections 3-6 excludes every `E>=0`. Hence state 279 has no realization.

## 7. Frontier update

State 279 was one of the N34 scalar survivors after state 227 had been removed. The frozen generalisation frontier therefore becomes

```text
996 exclusions / 4,582 survivors,
```

split as

```text
4,504 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

## 8. General-theory significance

State 279 is important because it is not a cosmetic variant of state 227. Its active source structure is actually cleaner:

```text
state 227: rho=1^7,2,3^10;
state 279: rho=1^7,3^11.
```

The same `h_2` threshold mechanism closes the entire high-excess tail in both states. The low-excess exceptions in state 279 are then killed by a new reusable rigidity principle: **if a zero-excess low-demand label would need a very small C-value, the incoming ledger may force every cheap-q source to carry too much p to be eligible for that label.**

This suggests a broader two-sided programme:

1. threshold counts `h_l` constrain which q-sources may carry high p;
2. zero-excess labels constrain which low-p sources must remain available;
3. the same incoming ledger cannot always satisfy both demands.

That interaction is the next natural generalisation target.

## 9. Trust boundary

- The proof depends on the canonical bridge, selected-edge/source forcing, endpoint load, the selected-excess lemma and the no-isolated-C consequence. External review remains open.
- Both verifiers use exact integer arithmetic only. Solver noncompletion/infeasibility is not used.
- The three low-excess exceptional profiles require the hand rigidity arguments in Section 4; the coarse numerical envelope alone does not exclude them.
- Independent computational reproduction and novelty assessment remain open.
