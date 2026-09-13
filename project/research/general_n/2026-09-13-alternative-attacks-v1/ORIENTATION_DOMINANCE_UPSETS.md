# Orientation dominance and up-set Hall reduction

13 September 2026. **Candidate general reduction inside the canonical selected/residual framework. External mathematical review remains OPEN.**

This note records the useful symbolic remnant of the failed one-dimensional Ferrers hope in [`ORIENTATION_FLOW_HALL.md`](ORIENTATION_FLOW_HALL.md).

The exact directed compatibility relation is two-dimensional and its deleted diagonal prevents a literal Ferrers description. If we add the forbidden self-arcs as a deliberate relaxation, however, the resulting source-target relation is a two-dimensional dominance graph. In that relaxed graph, a maximum Hall deficiency is attained on an up-set of a natural source-hardness partial order.

This gives a symbolic family of staircase/antichain cuts. It is weaker than the exact no-loop max-flow test, but substantially more structured than arbitrary Hall subsets and may be useful in all-order arguments.

## 1. Loop-relaxed directed compatibility

Retain

```text
c_u=q_u+rho_u.
```

The exact orientation relation from [`ORIENTATION_FLOW_HALL.md`](ORIENTATION_FLOW_HALL.md) is

```text
D(u,w)
 iff u!=w,
     q_u<=c_w+1,
     q_w<=c_u.                                      (1)
```

Define the **loop-relaxed** relation by dropping only `u!=w`:

```text
D+(u,w)
 iff q_u<=c_w+1,
     q_w<=c_u.                                      (2)
```

Because `rho_u>=1` in the live `t>0` branches,

```text
c_u=q_u+rho_u>=q_u+1,
```

so every added self-arc `D+(u,u)` is indeed present.

The `D+` network contains every edge of the exact `D` network. Therefore failure of the loop-relaxed Hall system is a valid failure certificate for the exact orientation target-flow relaxation. Passing `D+` says nothing about the deleted diagonal.

## 2. Source hardness order

For two source vertices define

```text
u >=_H v
 iff q_u>=q_v and c_u<=c_v.                         (3)
```

Thus a harder source has at least as much outgoing demand but no larger cross-neighbourhood score `c`.

If `u>=_H v`, then

```text
N_D+(u) subseteq N_D+(v).                            (4)
```

Indeed, if `w in N_D+(u)`, then

```text
q_u<=c_w+1,
q_w<=c_u.
```

Since `q_v<=q_u` and `c_v>=c_u`, we also have

```text
q_v<=c_w+1,
q_w<=c_v,
```

so `w in N_D+(v)`.

At the same time the source demand obeys

```text
q_u>=q_v.                                            (5)
```

This is the monotonicity that a one-dimensional Ferrers ordering was trying, incorrectly, to obtain globally. The correct object is a two-coordinate partial order.

## 3. Capacitated Hall deficiency

Fix any nonnegative target capacities `P_w`. For a source subset `W`, put

```text
d_W(w)=|{u in W : D+(u,w)}|,

Phi(W)=sum_{u in W} q_u
       -sum_w min(P_w,d_W(w)).                       (6)
```

The loop-relaxed target-flow Hall system is feasible exactly when

```text
Phi(W)<=0                                             (7)
```

for every source subset `W`.

## 4. Up-set reduction

> **Dominance up-set lemma.** There is a source subset maximizing `Phi(W)` that is upward-closed under every **strict** hardness comparison in (3), up to arbitrary multiplicity choices inside equal `(q,c)` types.

Equivalently, after quotienting equal `(q,c)` source types, a maximum deficiency can be represented by type counts with the following property:

- if any vertex of an easier type is selected, then every available vertex of each strictly harder comparable type is selected;
- partial multiplicity can occur only on the boundary of the resulting staircase, including mutually incomparable types and equal-type classes.

### Proof

Suppose `v in W`, `u notin W`, and `u` is strictly harder than `v`:

```text
q_u>=q_v,
c_u<=c_v,
```

with at least one strict inequality. Replace `v` by `u`:

```text
W'=(W\{v}) union {u}.
```

By (5),

```text
sum_{x in W'}q_x >= sum_{x in W}q_x.                 (8)
```

By (4), for every target `w` the compatibility indicator of `u` is no larger than that of `v`. Hence

```text
d_W'(w)<=d_W(w),
```

and therefore

```text
sum_w min(P_w,d_W'(w))
 <=sum_w min(P_w,d_W(w)).                            (9)
```

Combining (8)-(9),

```text
Phi(W')>=Phi(W).                                      (10)
```

Choose a linear extension of the strict hardness poset and repeatedly perform such an upward replacement whenever possible. A finite strictly increasing rank statistic guarantees termination. The final subset is upward-closed under strict hardness and has deficiency at least the starting value. Applying this to a maximizing subset proves the claim. Equal `(q,c)` types have equal demands and equal loop-relaxed neighbourhoods, so swaps inside a type preserve `Phi`; their selected multiplicity may therefore be treated as a boundary variable. QED.

## 5. What this does and does not reduce

A one-dimensional Ferrers graph would reduce Hall to a chain of prefix cuts. That is false for the exact orientation relation, as the committed two-source counterexample shows.

The up-set lemma gives the correct weaker symbolic statement:

```text
arbitrary source subsets
        ->
hardness up-sets / two-dimensional staircases
        ->
antichain boundary plus equal-type multiplicities.   (11)
```

The number of relevant symbolic cuts is therefore governed by antichains in the `(q,c)` type poset, not by all `2^b` subsets. For fixed small `b` the exact max-flow remains preferable computationally; the value of (11) is conceptual and potentially all-order.

## 6. Deleted-diagonal warning

The proof above deliberately uses `D+`, not exact `D`. The exact relation removes `u->u`; this can break literal neighbourhood containment because two comparable sources may exchange the two diagonal positions.

Therefore one must **not** state the up-set lemma as an exact theorem for `D` without an additional diagonal argument. Safe usage is:

1. build the loop-relaxed `D+` network;
2. check only hardness up-sets using (6);
3. if one has `Phi(W)>0`, the exact no-loop network is certainly infeasible;
4. if all such cuts pass, return to the exact max-flow/Hall test.

This separation is intentional and part of the audit boundary.

## 7. Possible all-order direction

After grouping target vertices by their `(q,c,P)` type, the capacity term for an up-set `W` is exactly

```text
sum_T m_T * min(P_T, d_W(T)),                         (12)
```

with the obvious adjustment when capacities vary inside a type. The source side is similarly a sum over type multiplicities.

Thus any future symbolic orientation theorem can be sought as an inequality over a two-dimensional staircase rather than an arbitrary graph orientation. Natural next questions are:

- whether canonical `q+rho<=a` and incoming-cap inequalities restrict the width of the hardness poset;
- whether extremal staircase boundaries can be reduced to a bounded number of corners;
- whether endpoint-class Hall constraints force those corners into a narrow range;
- whether the deleted diagonal can be paid for by a small explicit correction term.

No such stronger statement is claimed here.

## Trust boundary

The up-set argument is an elementary exchange proof for the explicitly loop-relaxed bipartite network. Its Murty-Simon relevance still depends on the canonical graph-to-constraint bridge and the directed compatibility lemma. It is a necessary-condition reduction only; passing it is not graph feasibility and is not a proof of the unrestricted conjecture.
