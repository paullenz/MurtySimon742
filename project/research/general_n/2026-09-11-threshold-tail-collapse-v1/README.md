# N29 Delta=16 threshold-tail collapse

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate simplification with a hand proof of the scalar tail bound and independent exact regression checks; independent mathematical review remains open.**  
This note does **not** erase or rewrite the preserved reviewer-v3 package. It records a stronger route discovered after that package was assembled.

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

This removes, for `Delta=16` at the proof-critical `m=210,211` scopes, every downstream logical dependency on

- demand charging enumeration,
- residual-row enumeration,
- source-capacity Hall pruning,
- supplement-cap refinement,
- the corrected late LP,
- exact Farkas certificates,
- **and now the earlier 1,352,078-demand-multiset maximisation.**

The scalar bound `Q(s)<=18` now has a direct hand proof in

```text
N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md
```

with a small exact local-obligation checker

```text
n29_delta16_threshold_tail_hand_check.py
```

The original exhaustive checker

```text
n29_delta16_threshold_tail_collapse_exact.py
```

is retained as an independent full-domain regression and equality-case audit rather than a logical premise. Both paths pass together in GitHub Actions run `34617844004`.

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

If the set is empty, the demand vector is already impossible and requires no further treatment.

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

## 4. Hand lemma: Q(s)<=18

The new hand proof writes

```text
N_h = #{i:s_i>=h},
p   = N_1,
d_h = N_h-g_h(W_h),
D(s)=sum_{h=2}^{11} d_h.
```

The Ferrers-tail identity gives

```text
S = p + sum_{h=2}^{11} N_h,
```

so

```text
Q(s)=p+D(s).                                      (8)
```

The hand argument proves

```text
D(s)<=6.                                          (9)
```

Its structure is:

1. for every `h>=7`, `d_h<=0`;
2. clipping every demand above six down to six cannot decrease `D`;
3. clipping `6->5`, `5->4`, and `4->3` cannot decrease `D`, except for tiny endpoint configurations that are checked explicitly and satisfy the same bound;
4. after reduction to demands in `{0,1,2,3}`, put `x=N_2`, `y=N_3`; then

   ```text
   D=x+y-g_2(2x+y)-g_3(3y),
   ```

   and three elementary ranges `y<=6`, `7<=y<=10`, `y>=11` give `D<=6`.

Since `p<=12`, (8)--(9) give

```text
boxed: Q(s)<=18.                                  (10)
```

The detailed algebra, including every exceptional clipping case, is in `N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md`.

The local hand obligations are separately regression-checked by `n29_delta16_threshold_tail_hand_check.py`; it uses only exact integer arithmetic, no solver and no floating point. It checks the finite endpoint tables plus the final 91 integer pairs `0<=y<=x<=12`, rather than enumerating demand multisets.

## 5. Independent exhaustive audit

The older checker

```text
n29_delta16_threshold_tail_collapse_exact.py
```

still exhausts every nondecreasing 12-tuple

```text
0 <= s_1 <= ... <= s_12 <= 11.
```

There are exactly

```text
C(23,12) = 1,352,078
```

such multisets.

Using integer arithmetic only, it independently finds

```text
max Q(s) = 18.                                    (11)
```

There are exactly four maximisers:

```text
(2,3^11)   with zmin tails (z_2,z_3)       = (9,8),
(3^12)     with zmin tails (z_2,z_3)       = (9,9),
(3,4^11)   with zmin tails (z_2,z_3,z_4)   = (10,10,9),
(4^12)     with zmin tails (z_2,z_3,z_4)   = (10,10,10).
```

In each case `Q=18`.

This equality classification is not needed by the hand proof, so it remains useful independent finite evidence rather than a premise.

## 6. Consequence for Delta=16

From (7) and (10),

```text
16 + 2t <= 18,
```

so

```text
t <= 1.                                           (12)
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

## 7. Independent regeneration against the old finite frontiers

The existing minimal preparation and residual scanner were also independently regenerated as a cross-check.

At `t=3`, inserting the threshold-capacity family directly into the full row scan rejected all `712,091` residual states before Hall/refinement was needed.

At `t=2`, the same full threshold family rejected all `3,439,716` residual states.

A further independent audit in `n29_t3_rowwise_threshold_audit_exact.py` starts from the already reduced 126-row `t=3` minimal kernel and applies the written threshold family literally. All 126 are rejected, including all 94 positive zero-slack RX-Hall research profiles; each already violates the `h=2` threshold. GitHub Actions run `34616219528` passed.

These scans are corroboration only. They are not logical dependencies of the demand-only hand proof.

## 8. Trust boundary and next work

The reduction is only as sound as:

1. the graph-to-model bridge;
2. residual activity for `t>0`;
3. pointwise selected-incidence forcing `s_i<=rho_u`;
4. the threshold-capacity lemma;
5. the hand inequality `D(s)<=6`.

Items 1--4 have internal hostile audits and partial Lean formalisation elsewhere in the repository; independent expert review remains open. Item 5 now has both a direct written proof and an independent exact local-obligation checker, plus the older full-domain exhaustive regression.

The highest-value next step is to parameterise

```text
Q_{a,b}(s)
```

for adjacent `(a,b)` and determine whether the tail-sum mechanism is a genuine general-N ingredient rather than an `n=29` coincidence. In particular, `(a,b)=(13,16)` is the natural next laboratory because it is the `Delta=16` boundary appearing at `n=30`.

No unrestricted Murty-Simon theorem is claimed here.
