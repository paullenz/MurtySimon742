# Positive-slack incidence pressure

14 September 2026. **Candidate exact structural consequence inside the canonical target-Hall framework. External mathematical review and novelty assessment remain OPEN.**

The strict labelled exterior expansion of the canonical maximal witness gives a useful global first-layer inequality when singleton conditions are summed over all exterior sources.

## 1. Setup

Let `M+` be the labelled canonical maximal Hall minimizer and let

```text
O=B\M+.                                                 (1)
```

For each target `w`, write

```text
y_w=d_M+(w),
s_w=(P_w-y_w)_+,                                      (2)
```

and define the positive residual-slack target set

```text
Z={w:s_w>=1}.                                          (3)
```

Let `D(u,w)` be the usual directed numerical compatibility relation, with `u!=w`, and write

```text
d_D^-(w)=#{u:D(u,w)}.                                  (4)
```

## 2. Labelled singleton exterior expansion

Because `M+` is the union of all labelled Hall minimizers, adding any single exterior vertex `u in O` strictly raises the integer Hall margin. In the residual-slack system a single new source can contribute at most one unit to any target. Therefore

```text
|N_D^+(u) cap Z| >= q_u+1.                             (5)
```

The forbidden diagonal is already absent from `D`.

This is the labelled strengthening underlying the earlier complete-type exterior marginal theorem.

## 3. Summed incidence pressure

Summing (5) over `u in O` gives

```text
D(O)+|O|
 <= e_D(O,Z),                                          (6)
```

where

```text
D(O)=sum_{u in O}q_u.                                  (7)
```

At each target `w`, all directed-compatible sources partition between `M+` and `O`, so

```text
d_D^-(w)=y_w+k_O(w),                                   (8)
```

where `k_O(w)` is the number of exterior compatible sources. Hence

> **Positive-slack incidence pressure.**
>
> ```text
> D(O)+|O|
> <= sum_{w in Z}(d_D^-(w)-y_w).                       (9)
> ```

Equivalently, with

```text
Y_1=sum_{w in Z}y_w,                                   (10)
```

we have

```text
D(O)+|O|+Y_1
 <= sum_{w in Z} d_D^-(w).                             (11)
```

Thus every primary compatible incidence landing on a positive-slack target reduces by one the exterior incidence capacity still available there.

## 4. Exact rectangle-count form

Ignoring only the forbidden diagonal, a source `u` is directed-compatible with target `w` exactly when

```text
q_u<=c_w+1,
c_u>=q_w.                                              (12)
```

Define the full rectangle count

```text
A(w)=#{u:q_u<=c_w+1 and c_u>=q_w}.                     (13)
```

The target `w` itself is always counted in `A(w)` because `q_w<=c_w`. Therefore

```text
d_D^-(w)=A(w)-1.                                       (14)
```

and (11) becomes the exact two-dimensional counting inequality

```text
D(O)+|O|+Y_1
 <= sum_{w in Z}(A(w)-1).                              (15)
```

No flow computation remains.

## 5. One-dimensional upper projection

Let

```text
Qle(x)=#{u:q_u<=x},
Cge(x)=#{u:c_u>=x}.                                    (16)
```

Then

```text
A(w)<=min(Qle(c_w+1),Cge(q_w)).                        (17)
```

so a weaker theorem-safe scalar form is

```text
D(O)+|O|+Y_1
 <= sum_{w in Z}
      [min(Qle(c_w+1),Cge(q_w))-1].                    (18)
```

The trivial bound `d_D^-(w)<=b-1` gives

```text
D(O)+|O|+Y_1 <= (b-1)|Z|.                              (19)
```

Equation (19) is usually too coarse by itself, but it combines directly with the coupled residual-slack budget controlling `|Z|` and `Y_1`.

## 6. Coupling to residual budget

From [`COUPLED_RESIDUAL_SLACK_BUDGET.md`](COUPLED_RESIDUAL_SLACK_BUDGET.md),

```text
sum_{w in Z} max(0,y_w+a-b+1) <= r-b.                 (20)
```

Near balance:

- if `b=a+1`, then `Y_1<=r-b`;
- if `b=a`, then `Y_1+|Z|<=r-b`.

Thus the same positive-slack targets must simultaneously:

1. provide at least `D(O)+|O|` exterior compatible incidences;
2. absorb the primary incoming multiplicity `Y_1`;
3. fit within the Murty residual-excess budget.

This is the cheapest coupled primary/exterior pressure test currently available.

## 7. Trust boundary

The inequality follows from labelled canonical maximality, the exact directed compatibility relation and the definition of residual slack. The residual-budget coupling additionally uses positive-surplus residual activity. It is a necessary condition only and does not prove graph realizability or the unrestricted Murty-Simon conjecture.
