# N29 Delta=16 threshold-tail collapse

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate simplification, internally exact-checked; independent mathematical review remains open.**  
This note does **not** modify the preserved reviewer-v3 package. It records a stronger route discovered after that package was assembled.

## Headline

For the `n=29, Delta=16` bridge, the threshold-capacity inequalities imply a demand-only tail bound strong enough to force

```text
t <= 1,
```

where

```text
t = e(G) - 208.
```

Consequently every `Delta=16` scope with

```text
e(G) >= 210   (t >= 2)
```

is impossible, assuming the universal selected/residual bridge.

This removes, for `Delta=16` at the proof-critical `m=210,211` scopes, every downstream dependency on

- demand charging enumeration,
- residual-row enumeration,
- source-capacity Hall pruning,
- supplement-cap refinement,
- the corrected late LP,
- and exact Farkas certificates.

The only finite computation in this new route is a direct exhaustive check of a 12-variable integer lemma over `1,352,078` nondecreasing demand multisets. It uses integer arithmetic only, no solver and no floating point.

## 1. Bridge inputs

Use the notation of the self-contained reviewer-v3 graph-to-model bridge:

```text
a = 12,
b = 16,
s_i = max(0,d_i-R_i),
S = sum_i s_i,
rho_u = residual degree of source u,
r = sum_u rho_u.
```

For positive surplus `t>0`, residual activity gives

```text
rho_u >= 1
```

for all `u in B`.

The exact demand ledger gives

```text
S >= r + 2t.                                      (1)
```

At every selected incidence, the pointwise forcing lemma gives

```text
s_i <= rho_u.
```

Since a selected source has `q_u>=1` and `q_u+rho_u<=a=12`, every positive demand satisfies

```text
1 <= s_i <= 11.                                  (2)
```

Thus it is enough to consider `s_i in {0,...,11}`.

## 2. Residual tail identity

For `h>=2`, put

```text
z_h = #{u in B : rho_u >= h}.
```

Because every residual degree is positive,

```text
r = b + sum_{h=2}^{12} z_h.                      (3)
```

For the lower bound below we may discard the nonnegative `z_12` term:

```text
r >= 16 + sum_{h=2}^{11} z_h.                    (4)
```

## 3. Threshold capacity converted to a scalar tail lower bound

For each `h>=2`, define

```text
W_h = sum_{i:s_i>=h} s_i.
```

The universal threshold-capacity lemma gives, whenever `W_h>0`,

```text
z_h >= h,
2 W_h <= z_h^2 - z_h + h(h+1).                  (5)
```

Define the smallest integer compatible with (5):

```text
g_h(W) =
  0,                                                if W=0;
  min { z in {h,...,16} :
        2W <= z^2-z+h(h+1) },                       if W>0.
```

If the set is empty, the demand vector is already impossible.

Every actual residual sequence therefore satisfies

```text
z_h >= g_h(W_h),
```

and hence by (4),

```text
r >= 16 + sum_{h=2}^{11} g_h(W_h).               (6)
```

Combining (1) and (6) gives the necessary demand-only inequality

```text
Q(s) := S - sum_{h=2}^{11} g_h(W_h)
      >= 16 + 2t.                                 (7)
```

The residual sequence has disappeared.

## 4. Exact finite lemma

The checker

```text
n29_delta16_threshold_tail_collapse_exact.py
```

exhausts every nondecreasing 12-tuple

```text
0 <= s_1 <= ... <= s_12 <= 11.
```

There are exactly

```text
C(23,12) = 1,352,078
```

such multisets.

Using integer arithmetic only, it finds

```text
max Q(s) = 18.                                    (8)
```

There are exactly four maximisers:

```text
(2,3^11)   with zmin tails (z_2,z_3)       = (9,8),
(3^12)     with zmin tails (z_2,z_3)       = (9,9),
(3,4^11)   with zmin tails (z_2,z_3,z_4)   = (10,10,9),
(4^12)     with zmin tails (z_2,z_3,z_4)   = (10,10,10).
```

In each case `Q=18`.

The checker also independently reconstructs the exact scaled charging table as a regression guard, but charging is **not needed** for the final contradiction.

## 5. Consequence for Delta=16

From (7) and (8),

```text
16 + 2t <= 18,
```

so

```text
t <= 1.                                           (9)
```

Therefore a positive-surplus `Delta=16` graph on 29 vertices cannot have

```text
m = 208+t >= 210.
```

In particular:

```text
m=210 (t=2): impossible,
m=211 (t=3): impossible,
and every larger m: impossible.
```

This is strictly stronger and structurally simpler than the reviewer-v3 `Delta=16` route.

## 6. Independent regeneration against the old finite frontiers

As a cross-check before deriving (8), the existing minimal preparation and residual scanner were independently regenerated.

At `t=3`, inserting the threshold-capacity family directly into the row scan rejected all `712,091` residual states before Hall/refinement was needed.

At `t=2`, the same full threshold family rejected all `3,439,716` residual states.

Those scans are corroboration only. They are not logical dependencies of the demand-only proof above.

## 7. Trust boundary and next work

The new reduction is only as sound as:

1. the graph-to-model bridge;
2. residual activity for `t>0`;
3. pointwise selected-incidence forcing `s_i<=rho_u`;
4. the threshold-capacity lemma;
5. the exact finite maximisation `Q(s)<=18`.

Items 1--4 already have internal hostile audits in the project, but independent expert review remains open. Item 5 is deliberately tiny and self-contained and should now be independently reimplemented.

The highest-value next step is to **replace the finite maximisation by a hand inequality**, if possible. The four extremisers strongly suggest that the threshold-tail score has a clean extremal description. A second priority is to parameterise

```text
Q_{a,b}(s)
```

for adjacent orders and determine whether this tail-sum mechanism is a general-N ingredient rather than an `n=29` coincidence.

No unrestricted Murty-Simon theorem is claimed here.
