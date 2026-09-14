# Sharpened dominance-upset structure for orientation Hall

14 September 2026. **Candidate structural theorem. External mathematical review and novelty assessment remain OPEN.**

This note strictly strengthens [`DOMINANCE_UPSET_HALL.md`](DOMINANCE_UPSET_HALL.md). The earlier theorem used the sufficient order

```text
q_x>=q_y,
c_x<=c_y,
P_x>=P_y.
```

The target-capacity comparison is only needed in the equal-demand case.

## 1. Sharp hardness order

For distinct labelled vertices `x,y`, define

```text
x >=_* y
```

when

```text
c_x <= c_y,
```

and either

```text
q_x > q_y,                                             (1a)
```

or

```text
q_x = q_y and P_x >= P_y.                              (1b)
```

Because demands are integers, (1a) gives `q_x-q_y>=1`.

This relation is transitive: strict demand dominance composes automatically, while equal-demand comparisons use the transitive `P` order. Identical `(q,c,P)` vertices dominate one another in both directions.

## 2. One-unit diagonal-loss lemma

Let `T` contain neither `x` nor `y` and suppose

```text
q_x>=q_y,
c_x<=c_y.
```

Then source and target intervals satisfy

```text
I_x=[q_x,c_x] subseteq I_y=[q_y,c_y],
J_x=[q_x,c_x+1] subseteq J_y=[q_y,c_y+1].
```

For every target `w` other than `x,y`, compatibility of `x` with `w` implies compatibility of `y` with `w`. Hence the capacity increment caused by adding `x` is no larger than the increment caused by adding `y` on all ordinary targets.

Both cross-arcs `x->y` and `y->x` exist. On the two special targets, adding `x` can beat adding `y` by **at most one unit** because each special increment is binary. Therefore, writing `Delta_z(T)=F(T union {z})-F(T)`,

```text
Delta_x(T)-Delta_y(T)
 <= 1-(q_x-q_y).                                      (2)
```

This inequality needs no comparison between `P_x` and `P_y`.

### Equal-demand refinement

If `q_x=q_y` and `P_x>=P_y`, the nested target intervals give

```text
d_T(x)<=d_T(y).
```

If adding `x` gains a unit at target `y`, then

```text
d_T(y)<P_y<=P_x,
```

so adding `y` also gains a unit at target `x`. Thus the special-target increment for `x` is no larger than that for `y`, and

```text
Delta_x(T)<=Delta_y(T).                                (3)
```

Combining (2) and (3):

> **Sharp exchange lemma.** If `x>=_*y`, then for every background set `T` disjoint from `{x,y}`,
>
> ```text
> Delta_x(T)<=Delta_y(T).                              (4)
> ```

## 3. Sharp up-set theorem

As before, the labelled Hall margin

```text
F(W)=sum_w min(P_w,d_W(w))-sum_{u in W}q_u
```

is submodular.

Choose a minimum-margin set `W*` of maximum cardinality. If `y in W*`, `x notin W*`, and `x>=_*y`, exchange `y` for `x`. Equation (4) produces another minimizer. Submodularity then makes the union `W* union {x}` a larger minimizer, contradiction.

Therefore:

> **Sharp dominance-upset theorem.** A maximum-cardinality minimum Hall witness can be chosen as an up-set under `>=_*`.

Since identical vertices dominate one another, the witness is again a union of complete `(q,c,P)` type classes.

At type level the order is

```text
(q,c,P) >=_* (q',c',P')
iff c<=c'
    and [q>q' or (q=q' and P>=P')].                    (5)
```

This is strictly stronger than the earlier 3D product order because when `q>q'`, no `P` comparison is required.

## 4. Mandatory closure for demand gap at least two

Equation (2) gives more when

```text
q_x >= q_y+2,
c_x <= c_y.
```

Then

```text
Delta_x(T) <= Delta_y(T)-1.                            (6)
```

Suppose a global minimizer contained `y` but not `x`. Replacing `y` by `x` would strictly reduce `F`, contradicting minimality.

Hence:

> **Strict-gap closure corollary.** If `q_x>=q_y+2` and `c_x<=c_y`, then **every** minimum Hall witness containing `y` also contains `x`, irrespective of `P_x,P_y`.

The maximum-cardinality tie-break is needed only for the boundary cases `q_x=q_y+1` and equal demand.

## 5. Dominance-closed max-flow

The exact quotient max-flow network may therefore be augmented by closure arcs of capacity `Q+1` from `y_L` to `x_L` for every relation `x>=_*y`. The same proof as in [`DOMINANCE_CLOSED_MAXFLOW.md`](DOMINANCE_CLOSED_MAXFLOW.md) shows that these arcs do not change the min-cut value.

Using the sharper order gives a stronger closure DAG and a smaller antichain boundary than the earlier 3D order.

## 6. Principal sharp up-sets

For a generator type `g`, its principal sharp up-set is

```text
up_*(g) = {
  a : c_a<=c_g
      and [q_a>q_g or (q_a=q_g and P_a>=P_g)]
}.                                                       (7)
```

Testing only these principal sets is a useful cheap necessary family, but is **not** exact in general. Multi-generator counterexamples remain possible; [`PRINCIPAL_UPSET_COUNTEREXAMPLE.md`](PRINCIPAL_UPSET_COUNTEREXAMPLE.md) already supplies the smallest warning family for the earlier order, and the same three-type `V` remains a multi-generator up-set under the sharp order.

## 7. Verification boundary

The strengthened statement should be checked independently by replacing the earlier dominance predicate in [`verify_dominance_upset_hall.py`](verify_dominance_upset_hall.py) with (5) and rerunning:

- exhaustive small profiles;
- broad deterministic random profiles;
- every dominance exchange against every background subset;
- global-minimum versus sharp-up-set minimum.

The hand proof above does not depend on computation.

## 8. Trust boundary

This remains an exact theorem only for the directed target-capacity Hall relaxation. It inherits the Murty-Simon bridge and target-capacity assumptions and does not prove graph realizability or the unrestricted conjecture.
