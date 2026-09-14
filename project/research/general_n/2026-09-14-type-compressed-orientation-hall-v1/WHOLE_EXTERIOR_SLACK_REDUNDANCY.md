# Whole-exterior slack inequality is globally redundant

14 September 2026. **Exact algebraic consequence inside the canonical target-Hall framework. External mathematical review remains OPEN.**

This note records a useful negative result about the strict exterior slack-expansion theorem. It prevents the research programme from spending time trying to derive a contradiction from the total residual receiver-slack mass alone.

## Setup

Let `M+` be the canonical maximal minimum Hall witness. Write

```text
D+ = D(M+),
H+ = H(M+),
delta = D+ - H+.
```

On a target-Hall failure,

```text
delta >= 1.                                             (1)
```

Let `O` be the complete-type complement of `M+`. If total source demand is

```text
Q = sum_u q_u,
```

then

```text
D(O) = Q-D+.                                            (2)
```

For each target copy `w`, the residual receiver slack left by the canonical cut is

```text
s_w=(P_w-y_w(M+))_+.
```

Put

```text
R = sum_w s_w,
Ptot = sum_w P_w.                                       (3)
```

## Exact identity

For every target copy,

```text
min(P_w,y_w)+(P_w-y_w)_+ = P_w.
```

Therefore

```text
H+ + R = Ptot,                                          (4)
```

and hence

```text
R-D(O)
 = (Ptot-H+) - (Q-D+)
 = (Ptot-Q) + (D+-H+)
 = (Ptot-Q) + delta.                                    (5)
```

This is an identity, not an inequality.

## Consequence

The canonical pair/target-capacity screening already requires

```text
Ptot >= Q.                                              (6)
```

Combining (1), (5) and (6) gives automatically

```text
R >= D(O)+1.                                            (7)
```

Thus the **whole-exterior scalar consequence** of strict slack expansion,

```text
sum_w s_w >= D(O)+1,
```

contains no additional information once total target capacity and canonical Hall deficiency are known.

More precisely, its surplus is exactly

```text
R-D(O) = global target-capacity surplus + canonical deficiency. (8)
```

If `Ptot=Q` and `delta=1`, the whole-exterior inequality is exactly tight.

## Research consequence

The nontrivial content of exterior slack expansion lies in the compatibility-restricted inequalities

```text
sum_sigma n_sigma min(s_sigma,K_T(sigma)) >= D(T)+1
```

for **proper exterior subsets** `T`, or equivalently in the target-by-target correlation between exterior compatibility and residual slack. Dropping the compatibility term and retaining only total slack cannot yield a new Murty-Simon contradiction.

This aligns with the receiver-layer pilot: marginal capacity/count distributions already explain almost all canonical Hall failures, while the remaining exceptions are correlation-sensitive.

The preferred next step is therefore to identify a small structured family of exterior subsets (or a low-dimensional correlation statistic) for which the compatibility-restricted slack inequality can be bounded from the Murty bridge.

## Trust boundary

Equation (5) is pure integer algebra inside the accepted target-capacity model. Its Murty-Simon use remains conditional on the canonical bridge and the target caps. This note does not change any frontier count and does not prove the unrestricted conjecture.
