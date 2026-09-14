# Canonical equal-q swap rigidity

14 September 2026. **Candidate exact structural lemma inside the canonical target-Hall framework. External mathematical review remains OPEN.**

The q-stratified crossing statistic isolates the only source of q-only rearrangement loss. For the **canonical maximal Hall minimizer** `M+`, every such crossing is forced into a rigid saturation configuration.

## 1. Setup

Let `M+` be the union of all labelled minimum Hall witnesses, hence the unique maximal labelled minimizer.

Take two distinct labelled copies `x,y` with

```text
q_x=q_y=q,
c_x<c_y,                                                (1)
```

such that

```text
x notin M+,
y in M+.                                                 (2)
```

Write

```text
y_w = number of M+-sources directed-compatible with target w.       (3)
```

Let

```text
M'=(M+\{y}) union {x}.                                  (4)
```

The total source demand is unchanged because `q_x=q_y`.

## 2. Source-neighborhood containment

For any third target `w` distinct from `x,y`,

```text
D(x,w) => D(y,w).                                       (5)
```

Indeed the first compatibility condition `q<=c_w+1` is identical for `x` and `y`, while

```text
q_w<=c_x<c_y                                            (6)
```

implies the second condition for `y` whenever it holds for `x`.

Thus replacing `y` by `x` cannot create a new compatible incidence at any third target.

At the two swapped targets themselves:

- target `y` **gains** the incidence `x->y`, because `y` previously could not contribute to itself;
- target `x` **loses** the incidence `y->x`, because `x` after the swap cannot contribute to itself.

Therefore the receiver-capacity change under the swap is at most `+1`.

## 3. Maximal-minimizer forcing

Because `M+` is a minimum Hall witness,

```text
F(M') >= F(M+).                                         (7)
```

If equality held, then `M'` would also be a minimum Hall witness. But `x in M'`, so `x` would belong to the union of all minimizers, namely `M+`, contradicting (2).

Hence

```text
F(M') >= F(M+)+1.                                       (8)
```

The source demand is unchanged and the receiver-capacity change is at most `+1`, so integrality forces

> **Equal-q swap rigidity.**
>
> ```text
> F(M')=F(M+)+1.                                        (9)
> ```

Every possible unit of receiver loss under the swap must therefore be invisible to the capped receiver sum, while the unique possible gain at target `y` must contribute exactly one unit.

## 4. Saturation consequences

The gain at target `y` is effective iff `y` is unsaturated before the swap. Thus

```text
y_y < P_y.                                              (10)
```

Equivalently, since values are integral,

```text
y_y <= P_y-1.                                           (11)
```

For target `x`, incoming falls from `y_x` to `y_x-1`. That loss must not lower receiver capacity, so

```text
y_x >= P_x+1.                                           (12)
```

More generally, every third target `w` with

```text
D(y,w)=1,
D(x,w)=0                                                (13)
```

loses one incoming incidence under the swap. Each such target must satisfy

```text
y_w >= P_w+1.                                           (14)
```

Thus a selected higher-`c` source can sit above an unselected equal-`q` source only if its entire extra receiver neighborhood is already strictly over-saturated, while its own target is under-saturated.

## 5. Extra-neighborhood interval

In the positive-surplus Murty regime, residual activity gives `rho_x>=1`, hence

```text
c_x=q+rho_x>=q+1.                                       (15)
```

For a third target `w`, the difference condition in (13) then reduces to

```text
c_x < q_w <= c_y.                                       (16)
```

Indeed `q_w>c_x>=q+1` implies `c_w>=q_w>q`, so the common condition `q<=c_w+1` is automatic.

Consequently every target whose demand lies in the interval

```text
q_w in {c_x+1,...,c_y}                                  (17)
```

must be over-saturated as in (14).

This gives a direct bridge from an equal-q crossing to a whole interval of forced receiver saturation.

## 6. Relation to the crossing statistic

A positive contribution to the q-stratified crossing statistic occurs inside an equal-`q`, equal-preincoming block when there are both

```text
selected y with P_y>=m,
unselected x with P_x<m.                                (18)
```

Fixed-q monotonicity of `P` and equality of the preincoming value force such a crossing pair to occur with `c_x<c_y`. Equations (11)-(14) then hold automatically; indeed in the equal-preincoming block,

```text
y_x=m,
y_y=m-1,                                              (19)
```

and (18) already gives the endpoint saturation inequalities.

The new content of the swap lemma is that **all additional targets reached by `y` but not `x` are also forced over-saturated**.

## 7. Research target

To rule out positive crossing count it is enough to show that the Murty residual/source-cap budgets cannot support the saturation wall

```text
selected y target:             y_y <= P_y-1,
extra-neighborhood targets:    y_w >= P_w+1
                               for c_x<q_w<=c_y.        (20)
```

This is substantially more structured than an arbitrary target-correlation problem and is the next analytic target after the 812-residue diagnosis.

## 8. Trust boundary

The swap argument is exact inside the labelled target-Hall relaxation and uses only canonical maximal-minimizer status, equal source demand, directed compatibility, and integrality. The interval form (16) additionally uses positive-surplus residual activity.

It does not by itself prove that crossings are impossible under all Murty constraints, does not promote any whole-state exclusion, and does not prove the unrestricted conjecture.
