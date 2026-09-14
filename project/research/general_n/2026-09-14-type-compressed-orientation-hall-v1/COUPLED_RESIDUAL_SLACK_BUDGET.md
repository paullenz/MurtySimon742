# Coupled primary-incoming / residual-slack budget

14 September 2026. **Candidate exact Murty-specific projection inside the canonical target-Hall framework. External mathematical review and novelty assessment remain OPEN.**

The first exterior-slack layer projection bounded a residual slack layer by using only `s_w<=P_w`. That discards a key coupling: residual slack is what remains **after** the primary canonical staircase has already used `y_w` units of compatible target capacity.

This note keeps that coupling.

## 1. Pointwise residual-slack caps

Let `M+` be the primary canonical maximal Hall witness. For each labelled target `w`, write

```text
y_w = number of M+-sources directed-compatible with w,
s_w = (P_w-y_w)_+.                                     (1)
```

The canonical Murty target caps include

```text
P_w<=b-1-q_w,
P_w<=rho_w+b-a-1.                                      (2)
```

Therefore

```text
s_w
 <= max(0,b-1-q_w-y_w),                               (3)
```

and

```text
s_w
 <= max(0,rho_w+b-a-1-y_w).                           (4)
```

When the potential-pair cap is present,

```text
P_w<=d_KD(w)-q_w,                                      (5)
```

we also have

```text
s_w
 <= max(0,d_KD(w)-q_w-y_w).                           (6)
```

Thus the residual system inherits target caps which become tighter as the primary staircase sends more compatible sources into the same target.

## 2. Coupled slack-layer conditions

For integer `j>=1`, put

```text
S_j={w:s_w>=j},
sigma_j=|S_j|,
Y_j=sum_{w in S_j} y_w.                                (7)
```

If `w in S_j`, then `P_w>=y_w+j`. Combining this with (2) gives the two exact necessary inequalities

```text
q_w+y_w <= b-1-j,                                      (8)
```

and

```text
rho_w-1 >= y_w+a-b+j.                                  (9)
```

With (5), also

```text
d_KD(w)-q_w-y_w >= j.                                 (10)
```

Equation (9) is the key coupling: a target cannot simultaneously receive many primary compatible sources and retain a large residual-slack level without spending residual degree.

## 3. Residual-budget layer inequality

Assume positive surplus so residual activity gives

```text
rho_w>=1 for every w,
sum_w rho_w=r.                                         (11)
```

Then

```text
r-b=sum_w(rho_w-1).                                    (12)
```

For `w in S_j`, (9) and nonnegativity of `rho_w-1` imply

```text
rho_w-1 >= max(0,y_w+a-b+j).                           (13)
```

Summing only over `S_j` yields:

> **Coupled residual-slack layer budget.** For every `j>=1`,
>
> ```text
> sum_{w in S_j} max(0,y_w+a-b+j)
> <= r-b.                                               (14)
> ```

This strictly strengthens the earlier slack-layer bound whenever primary incoming multiplicity on the slack targets is nonzero.

If

```text
a-b+j>=0,                                              (15)
```

then (14) simplifies to

```text
Y_j+(a-b+j)sigma_j <= r-b.                             (16)
```

Hence when `a-b+j>0`,

```text
sigma_j
 <= floor((r-b-Y_j)/(a-b+j)).                          (17)
```

The right side is interpreted only when nonnegative; a negative numerator excludes the profile immediately.

At the boundary `a-b+j=0`, (16) becomes the pure correlation constraint

```text
Y_j<=r-b.                                               (18)
```

## 4. Balanced-regime specialisations

These are particularly sharp near the Turan-balanced orders that generated the current frontier.

### `b=a+1`

Then `a-b=-1`. Equation (16) gives

```text
j=1:  Y_1 <= r-b,                                      (19)

j>=2: Y_j+(j-1)sigma_j <= r-b.                         (20)
```

So every primary compatible incidence landing on a positive-slack target consumes one unit of residual excess budget already at the first residual layer.

### `b=a`

Then

```text
Y_j+j sigma_j <= r-b                                  (21)
```

for every `j>=1`.

Thus positive residual slack costs at least one unit of residual excess **per slack target plus every primary incidence into it** at level one.

## 5. Coupling to exterior strict expansion

For an exterior residual staircase `T`, strict expansion requires

```text
D(T)+1
 <= sum_j min(sigma_j,kappa_j(T)).                     (22)
```

The new budget (14) controls `sigma_j` jointly with the primary incoming mass `Y_j`. Therefore a two-staircase contradiction may use the same target set twice:

```text
primary staircase M+
  -> creates y_w
  -> y_w makes residual slack expensive through (14)
  -> exterior staircase T needs those slack layers through (22).   (23)
```

This is stronger than treating the primary and exterior layer marginals independently.

## 6. Trust boundary

Equations (3)-(10) are direct consequences of the accepted target caps and the definition of residual slack. Equation (14) additionally uses positive-surplus residual activity. The result is necessary only; it does not assert graph realizability or prove the unrestricted Murty-Simon conjecture.
