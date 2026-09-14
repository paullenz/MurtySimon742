# Universal two-defect bridge decomposition

14 September 2026. **Candidate universal hand consequence of the canonical selected/residual bridge. External mathematical review remains OPEN.**

Two different nonnegative quantities have historically both been denoted by `E` in different parts of the project. They must be separated explicitly.

## 1. Two distinct defects

Use the canonical bridge notation

```text
r = sum_u rho_u = sum_i R_i,
S = sum_i s_i,
s_i = max(0,d_i-R_i),
t = positive surplus parameter.
```

The exact degree ledger gives

```text
sum_i d_i = 2(r+t).
```

[`../2026-09-12-exact-budget-threshold-v1/BRIDGE_REFINEMENTS.md`](../2026-09-12-exact-budget-threshold-v1/BRIDGE_REFINEMENTS.md) proves the exact demand-deficit identity

```text
S-r-2t
 = sum_{i:s_i=0}(R_i-d_i).                             (1)
```

Define the **zero-demand bridge deficit**

```text
D0 := S-r-2t
    = sum_{i:s_i=0}(R_i-d_i) >= 0.                    (2)
```

Separately, for selected label degrees write

```text
x_i=s_i+e_i,
e_i>=0.
```

The selected-incidence degree balance is

```text
sum_i x_i = sum_u q_u =: Q.                           (3)
```

Define the **selected excess**

```text
Esel := sum_i e_i = Q-S >=0.                          (4)
```

`D0` and `Esel` are different quantities. In particular, the selected-excess cap in the post-pair relational scanner uses `Esel`, while the older exact-budget bridge note used the letter `E` for `D0`.

## 2. Exact decomposition of the missing-edge load

From (2) and (4),

```text
S = r+2t+D0,
Q = S+Esel.
```

Therefore:

> **Two-defect bridge decomposition.**
>
> ```text
> Q = r + 2t + D0 + Esel.                              (5)
> ```

Every term beyond `r` on the right is nonnegative in the positive-surplus bridge regime.

Equivalently,

```text
Q-r = 2t+D0+Esel.                                     (6)
```

Thus the gap between total selected missing-edge load and residual mass is not an unspecified surplus: it is exactly the fixed structural surplus `2t` plus two named defect budgets.

## 3. Boundary cases

If every demand is positive, the zero-demand sum in (2) is empty, so

```text
D0=0,
S=r+2t,
Q=r+2t+Esel.                                          (7)
```

If selected degrees are exact, `x_i=s_i` for every label, then

```text
Esel=0,
Q=S=r+2t+D0.                                          (8)
```

If both conditions hold,

```text
Q=r+2t.                                               (9)
```

These are exact identities, not inequalities.

## 4. Global incoming-cap consequence

The canonical bridge gives the pointwise incoming bound

```text
p_u <= rho_u+b-a-1.                                   (10)
```

Every missing B-edge is oriented once, hence

```text
sum_u p_u = sum_u q_u = Q.                            (11)
```

Summing (10) over the `b` sources yields

```text
Q <= r+b(b-a-1).                                      (12)
```

Substitute (5) and cancel `r`:

> **Global two-defect budget.** Every legal bridge branch obeys
>
> ```text
> D0 + Esel + 2t <= b(b-a-1).                         (13)
> ```

Writing `delta=b-a`, this is

```text
D0 + Esel + 2t <= b(delta-1).                         (14)
```

This is a necessary condition only, but it couples the zero-demand deficit and selected excess in one scalar budget. Neither defect may be enlarged independently of the other.

### Immediate small-delta consequences

When `delta=1`, (14) forces

```text
D0=Esel=t=0,
```

so a positive-surplus branch is impossible.

When `delta=2`,

```text
D0+Esel+2t<=b.                                        (15)
```

For the current frozen N34/N35 layers, `delta` is 3 or 4, so (14) is not by itself expected to close the frontier, but it remains an exact coupling available to every later threshold argument.

## 5. Relation to target capacities

The current post-pair target cap satisfies

```text
P_u <= rho_u+b-a-1.                                   (16)
```

Thus the same aggregate calculation can be phrased inside the target-Hall relaxation:

```text
sum_u P_u <= r+b(b-a-1).                              (17)
```

If the full source set of demand `Q` is target-Hall feasible, then necessarily

```text
Q<=sum_u P_u,
```

which again implies (13).

This shows that the bridge defect budget is naturally compatible with the newer q-layer receiver formulation.

## 6. Why this matters for the q-layer attack

The q-layer threshold normal form describes how a source subset spends target capacity. Equation (5) fixes the total selected load globally:

```text
selected load
 = residual mass
 + structural surplus
 + zero-demand deficit
 + selected excess.                                   (18)
```

Any proposed all-order Hall contradiction may therefore charge scarce receiver capacity against the three non-residual terms separately rather than treating `Q-r` as an opaque parameter.

In particular, hostile q-tail counterexamples which choose `q` and the target caps independently of the `s/R/d` ledger can violate (5) even when their local target-Hall arithmetic looks Murty-like. Such examples are outside the canonical bridge domain and must not be used to refute a theorem whose hypotheses explicitly include (5).

Conversely, any proposed proof which uses (5) must state the canonical bridge hypotheses rather than presenting the decomposition as a theorem of arbitrary target-Hall instances.

## 7. Trust boundary

Equation (5) is algebraic once the following already-established bridge facts are accepted:

1. the exact demand-deficit identity (1);
2. `x_i=s_i+e_i` with `e_i>=0`;
3. the selected-incidence balance `sum x=sum q`.

Equation (13) additionally uses the canonical incoming bound (10) and the orientation balance `sum p=sum q`.

These are candidate universal bridge consequences with no fixed-order arithmetic in their derivation, but their Murty-Simon use inherits the external-review status of the canonical bridge. They do not prove graph realizability or the unrestricted conjecture.
