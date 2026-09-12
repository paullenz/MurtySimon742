# N32 t=1 sole full-RX survivor: hand contradiction

12 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate hand lemma inside the established selected/residual bridge. Independent mathematical review remains OPEN.**

The exact full RX/Hall replay leaves one positive-demand arithmetic state:

```text
s   = 1^2, 2^12,
rho = 1^10, 2^7.
```

We show directly that no selected quasi-edge configuration can realize it.

## 1. Tight threshold capacity

Let

```text
Z = {u in B : rho_u >= 2}.
```

Then `|Z|=7`. The twelve demand-two labels have total threshold demand

```text
W_2 = 12*2 = 24.
```

The threshold-capacity bound is exact because

```text
C_2(7) = [7*6 + 2*3]/2 = 24.
```

Use the notation from the threshold-capacity proof. Let `ell_u` be the number of actual selected incidences from source `u` to demand-at-least-two labels, and put

```text
J={u in Z: ell_u>2},
j=|J|.
```

The proof gives

```text
W_2 <= sum_{u in Z} ell_u
    <= (7-j)*2 + 7j - j(j+1)/2
    <= C_2(7)=24.
```

All inequalities are therefore equalities. In particular

```text
sum_{u in Z} ell_u=24.
```

The final capacity-gap identity is

```text
[(2*7)+C(7-2,2)] - [(7-j)*2+7j-j(j+1)/2]
  = (5-j)(4-j)/2.
```

Equality forces

```text
j=4 or 5.
```

## 2. At least 18 exceptions land back in Z

For a source in `J`, the threshold-capacity proof shows that every supplement of one of its heavy selected arcs belongs to `Z`. Selection is injective on unordered B-pairs.

The number of heavy arcs contributed by `J` is forced to its pair-capacity maximum

```text
j*7-j(j+1)/2.
```

For `j=4` this is 18; for `j=5` it is 20. Hence at least 18 selected arcs have supplement in `Z`, so

```text
sum_{u in Z} p_u >= 18.                 (2.1)
```

## 3. Every high source has p_u<=1

Because `sum_{u in Z} ell_u=24` and there are exactly twelve demand-two labels, each of which has selected degree at least two, every demand-two label has selected degree exactly two:

```text
x_i=2
```

for each such label. Equality also forces every source in `Z` to be heavy-active: sources outside `J` have exactly two heavy incidences, while sources in `J` have more than two.

Fix any `u in Z` and one of its demand-two selected labels `i`. Since the demand is positive,

```text
s_i=d_i-R_i=2,
```

hence

```text
d_i=R_i+2.
```

Endpoint load gives

```text
q_u+p_u <= R_i+x_i = R_i+2 = d_i.
```

Source-degree forcing at the same selected incidence gives

```text
d_i <= rho_u+q_u-1 = q_u+1,
```

because `rho_u=2`. Therefore

```text
q_u+p_u <= q_u+1,
```

so

```text
p_u<=1.
```

There are seven sources in `Z`, hence

```text
sum_{u in Z} p_u <= 7.                  (3.1)
```

Equations (2.1) and (3.1) contradict one another.

Therefore the sole full-RX/Hall survivor is impossible.

## 4. Trust boundary

The argument uses only:

- selected-incidence forcing;
- the written threshold-capacity proof and its equality case;
- injectivity of selection on unordered B-pairs;
- endpoint load;
- source-degree forcing;
- the definition of positive demand.

No numerical solver, LP infeasibility or saved certificate is used in this final exceptional case.
