# Counterexample — q-only receiver stratification is not universally exact

14 September 2026. **Preserved negative result.**

The q-stratified crossing-gap identity must not be simplified to a claim that q-only stratification is always exact. The following five-copy profile gives a canonical maximal Hall witness with a one-unit q-only rearrangement gap.

## Profile

Take `a=4`, `b=5` and five labelled copies

```text
copy   q   c   rho   P
A      0   4    4    4
B1     3   4    1    1
B2     3   4    1    1
B3     3   4    1    1
C      0   2    2    2
```

Directed numerical compatibility is

```text
D(u,w) iff u!=w,
            q_u<=c_w+1,
            q_w<=c_u.
```

The profile satisfies the basic Murty pointwise restrictions

```text
rho>=1,
c=q+rho<=a,
q<=a-rho,
P<=rho+b-a-1,
P<=b-1-q.
```

The potential missing-pair graph is complete on the five copies here, so the potential-degree cap also permits all listed capacities:

```text
d_K(A)-q_A   = 4,
d_K(Bi)-q_Bi = 1,
d_K(C)-q_C   = 4.
```

This is a Hall-profile counterexample, not a claim that the profile survives every earlier Murty bridge/frontier constraint.

## Canonical Hall minimizers

Direct enumeration of all labelled source subsets gives minimum Hall margin `-1`, attained exactly by

```text
{B1,B2,B3}
{A,B1,B2,B3}.
```

Hence the unique maximal minimizer is

```text
M+={A,B1,B2,B3}.                                       (1)
```

Its demand is

```text
D(M+)=9.                                                (2)
```

The incoming counts at targets `(A,B1,B2,B3,C)` are

```text
(3,3,3,3,4).                                           (3)
```

Therefore the exact receiver capacity is

```text
min(4,3)
+3 min(1,3)
+min(2,4)
=3+3+2
=8,                                                     (4)
```

so the exact Hall margin is `8-9=-1`.

## q-only rearrangement gap

At `q=3`, all three B targets contribute exactly `3` in total.

At `q=0`, the two targets are

```text
C: P=2, y=4, unselected,
A: P=4, y=3, selected.                                 (5)
```

The exact q=0 capacity is

```text
min(2,4)+min(4,3)=2+3=5.                               (6)
```

But the q-only comonotone rearrangement pairs the larger incoming value with the larger cap:

```text
min(2,3)+min(4,4)=2+4=6.                               (7)
```

Thus

```text
U_q(M+)=6+3=9,
H(M+)=8,
U_q(M+)-H(M+)=1.                                       (8)
```

The q-only upper bound reaches the demand and therefore misses this exact Hall failure.

## Crossing statistic

Before diagonal deletion, both q=0 targets have

```text
m=4.                                                    (9)
```

Inside the `(q,m)=(0,4)` block:

- `A` is selected and has `P_A=4>=m`;
- `C` is unselected and has `P_C=2<=m-1`.

Hence

```text
H^S_{0,4}=1,
L^O_{0,4}=1,
C_q=min(1,1)=1,                                        (10)
```

exactly matching the one-unit rearrangement gap in (8).

## Research consequence

Any all-order use of q-only receiver layers must control the crossing statistic rather than assume it vanishes. The current Murty frozen-pilot residue is interesting precisely because its 812 global-layer false negatives have `C_q=0`; that empirical fact needs a Murty-specific explanation, not an abstract Hall argument.
