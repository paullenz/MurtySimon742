# State 227: exact excess-profile sweep through E=8

13 September 2026. **Candidate hand reduction plus exact integer enumeration; external mathematical review OPEN.** This note extends `LOW_EXCESS_LAYERS.md`. For N34 state 227 it excludes every selected-excess profile with

```text
E=sum_i(x_i-s_i) <= 8.
```

Together with the earlier `E=0` exact-demand exclusion, any surviving realization of state 227 must have `E>=9`. This is not yet a whole-state exclusion.

## 1. Reusable profile inequality

Keep the state data

```text
a=15, b=18, s=2^4,3^11, r=39, S=41.
```

For an excess profile `e_i=x_i-s_i`, put

```text
E=sum e_i,
Q=41+E,
C_i=R_i+x_i,
T=sum_u q_u(q_u+p_u).
```

Endpoint load summed over all selected incidences gives

```text
T <= sum_i x_i C_i.                                  (1.1)
```

Also `sum_i C_i=r+Q=80+E`. Using coefficient 3 as baseline,

```text
sum_i x_i C_i
 =3(80+E)
  -sum_(s_i=2,e_i=0) C_i
  +sum_(s_i=2,e_i>=2) (e_i-1) C_i
  +sum_(s_i=3,e_i>=1) e_i C_i.                      (1.2)
```

The excess-layer lemma from `LOW_EXCESS_LAYERS.md` gives, at every selected incidence,

```text
L_u=max(0,p_u-rho_u+1,q_u+p_u-13) <= e_i.           (1.3)
```

Thus a source with `L_u>0` may select only labels in the corresponding excess level set. The unique `rho=2` source is restricted to the four demand-two labels.

## 2. Top-k label bounds

Let `q_3^(k)` be the k-th largest selected degree among the ten `rho=3` sources. A demand-three label of excess `e>=1` has selected degree `3+e`, hence is selected by `3+e` distinct `rho=3` sources. Source forcing gives

```text
C_i=d_i+e <= q_u+2+e,
```

so

```text
C_i <= e+2+q_3^(3+e).                                (2.1)
```

Let `q_all^(k)` be the k-th largest selected degree among the unique `rho=2` source and ten `rho=3` sources. A demand-two label with `e>=2` has selected degree `2+e`. Relaxing the `rho=2` source upper bound to the `rho=3` bound gives

```text
C_i <= e+2+q_all^(2+e).                              (2.2)
```

For zero-excess demand-two labels, let `z_0` be their number and let `(q_2,p_2)` be the unique `rho=2` source parameters. It can avoid at most `4-z_0` such labels. Hence

```text
C_0:=sum_(s_i=2,e_i=0) C_i
 >= 2 z_0
    +max(0,q_2-(4-z_0)) max(0,q_2+p_2-2).            (2.3)
```

Define `P_+` by replacing every positive term in (1.2) with the upper bounds (2.1)-(2.2). Then every realization must satisfy

```text
B := T + C_0 - P_+ <= 3(80+E).                       (2.4)
```

## 3. Exact source minimization without MILP

For a fixed excess profile, the possible source selected degrees are finite. The ten `rho=3` selected degrees are enumerated as a nondecreasing integer multiset. The unique `rho=2` selected degree is enumerated separately.

For a fixed `q` multiset, (1.3) determines the largest allowed incoming degree `p_max(q)` for every source. The seven `rho=1` sources can absorb at most 21 incoming units, so the remaining sources must carry at least `Q-21` incoming units.

For fixed source degrees, minimizing the `p` contribution to

```text
T=sum q^2 + sum q p
```

is greedy and exact: assign incoming units first to sources with smallest `q`, up to each source's `p_max`. Moving an incoming unit from a larger-`q` source to a smaller-`q` unsaturated source never increases cost. Thus no numerical optimizer is involved.

The residual budget also supplies the safe source-degree cutoff

```text
39 >= q max(0,q-x_max),                                (3.1)
```

where `x_max=max_i x_i`.

`verify_excess_sweep_to_8.py` enumerates every excess profile up to permutation within the demand-two and demand-three classes and minimizes the exact lower side of (2.4).

## 4. Results by total excess

The complete counts are:

| E | profiles | finite strict exclusions | equality profiles | source-infeasible profiles | minimum finite strict gap |
|---:|---:|---:|---:|---:|---:|
| 4 | 20 | 20 | 0 | 0 | 6 |
| 5 | 35 | 35 | 0 | 0 | 4 |
| 6 | 62 | 61 | 1 | 0 | 4 |
| 7 | 102 | 101 | 1 | 0 | 8 |
| 8 | 167 | 166 | 0 | 1 | 9 |

For `E=4,5`, every profile violates (2.4) strictly. At `E=8`, 166 profiles violate it strictly; the remaining profile has one demand-three label with excess eight, hence selected degree eleven. Such a label needs eleven distinct selected sources with `rho>=3`, but this state has only ten `rho=3` sources and the `rho=2` source cannot select a demand-three label. It is therefore impossible before (2.4) is applied.

The two equality profiles at `E=6,7` are handled below.

## 5. E=6 equality rigidity

The sole non-strict profile is

```text
demand-two excess:   0,0,0,0
demand-three excess: 0^10,6.
```

Thus one demand-three label has `x=9`, all other labels have exact demand, and `Q=47`.

The exact minimum in (2.4) is equality `B=258=3(80+6)`. The minimizing source data are unique:

```text
rho=2 source: q_2=0, p_2=4,
rho=3 q multiset: 1,5,5,5,5,5,5,5,5,6.
```

The minimized terms are

```text
T=328,
C_0 lower bound=8,
P_+ upper bound=78.
```

A realization would therefore have to attain equality in every bound. In particular the four zero-excess demand-two labels would satisfy `sum C_i=8`, so each has `C_i=2`.

Each such label has selected degree `x_i=2`, giving eight selected incidences in total. The `rho=2` source is inactive. Among the ten `rho=3` sources only one has `q=1`; the other nine have `q>=5`. A source can use a label at most once, so at least seven of the eight demand-two incidences come from sources with `q>=5`. Endpoint load then gives `C_i>=q_u+p_u>=5`, contradicting `C_i=2`.

Hence the `E=6` equality profile is impossible.

## 6. E=7 equality rigidity

The sole non-strict profile is

```text
demand-two excess:   0,0,0,7
demand-three excess: 0^11.
```

One demand-two label has `x=9`; the other three demand-two labels have `x=2`; `Q=48`.

The exact minimum is equality `B=261=3(80+7)`, uniquely at

```text
rho=2 source: q_2=1, p_2=4,
rho=3 q multiset: 1,5,5,5,5,5,5,5,5,6,
T=339,
C_0 lower bound=6,
P_+ upper bound=84.
```

For the `rho=2` source, `L=max(0,p_2-rho_2+1)=3`. Its sole selected label must therefore have excess at least three; the only possibility is the unique excess-seven demand-two label. Thus it contributes no selected incidence to the three zero-excess demand-two labels.

Equality forces those three labels to have total `C=6`, hence each has `C=2`. They need six selected incidences, all from `rho=3` sources. Only one `rho=3` source has `q=1`; at least five incidences therefore come from sources with `q>=5`, again contradicting endpoint load `C_i>=q_u+p_u>=5`.

So the `E=7` equality profile is impossible.

## 7. Conclusion

Combining this sweep with the separately proved `E=0,1,2,3` results gives

```text
state 227 realization => E>=9.                       (7.1)
```

This is an all-selected-geometries restriction. It does not yet exclude state 227 because excess profiles with `E>=9` remain to be quantified. The whole-state generalisation frontier therefore remains unchanged.
