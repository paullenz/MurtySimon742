# Dominance-upset structure for minimum orientation-Hall cuts

14 September 2026. **Candidate structural theorem inside the directed target-flow relaxation. External mathematical review and novelty assessment remain OPEN.**

## 1. Interval representation

For every labelled source/target vertex `u`, write

```text
q_u = selected source demand,
c_u = q_u + rho_u,
P_u = target-capacity upper bound.
```

The directed numerical compatibility relation used by the orientation-Hall network is

```text
D(u,w) iff u!=w,
            q_u <= c_w+1,
            q_w <= c_u.
```

Define intervals

```text
I_u = [q_u,c_u]       (source interval),
J_w = [q_w,c_w+1]     (target interval).
```

Then, before deleting the diagonal,

```text
D(u,w) iff I_u intersects J_w.                         (1)
```

Thus the compatibility matrix is an interval-digraph / interval-bigraph incidence matrix in the standard sense. This terminology is classical; see for example

```text
https://doi.org/10.1016/0012-365X(93)90290-A
https://doi.org/10.1016/S0166-218X(97)00027-9
```

No novelty claim is made for the interval representation itself.

## 2. Labelled Hall margin

For a source subset `W subseteq B`, let

```text
d_W(w) = #{u in W : D(u,w)}.
```

The capacitated Hall margin is

```text
F(W) = sum_w min(P_w,d_W(w)) - sum_{u in W} q_u.       (2)
```

The directed target-flow relaxation is feasible exactly when

```text
F(W) >= 0                                               (3)
```

for every source subset `W`.

Each `d_W(w)` is a nonnegative modular set function of `W`, and `x -> min(P_w,x)` is nondecreasing and concave. Hence each target term in (2) is submodular. The demand term is modular. Therefore:

> **Submodularity.** `F` is a submodular set function on labelled source vertices.

This is the labelled counterpart of the type-level submodularity proved in [`TYPE_LEVEL_MAXFLOW_COROLLARY.md`](TYPE_LEVEL_MAXFLOW_COROLLARY.md).

## 3. Hardness dominance

For distinct labelled vertices `x,y`, say that **`x` dominates `y` in Hall hardness**, written

```text
x >=_H y,
```

when

```text
q_x >= q_y,
c_x <= c_y,
P_x >= P_y.                                            (4)
```

Geometrically,

```text
I_x subseteq I_y,
J_x subseteq J_y,
```

while `x` carries at least as much source demand and its own target has at least as much capacity.

The order has the intended interpretation: `x` is a no-easier source than `y` to route, while exchanging `y` for `x` does not gain a favourable diagonal-capacity exception.

## 4. Exchange lemma

> **Dominance exchange lemma.** Let `T` be any source subset containing neither `x` nor `y`. If `x >=_H y`, then
>
> ```text
> F(T union {x}) - F(T)
> <=
> F(T union {y}) - F(T).                               (5)
> ```

### Proof

Write

```text
a_w = d_T(w).
```

First consider a target `w` different from `x,y`. Since `I_x subseteq I_y`, compatibility of `x` with `w` implies compatibility of `y` with `w`. Hence the one-step increment

```text
min(P_w,a_w + 1_{D(x,w)}) - min(P_w,a_w)
```

is at most the corresponding increment for `y`.

It remains to compare the two diagonal-swapped targets `x` and `y`.

Because `I_x subseteq I_y`, conditions (4) imply

```text
q_y <= q_x <= c_x <= c_y,
```

so both cross-arcs exist:

```text
D(x,y)=D(y,x)=1.                                       (6)
```

Also `J_x subseteq J_y`. Therefore every source in `T` compatible with target `x` is compatible with target `y`, and

```text
a_x <= a_y.                                            (7)
```

Adding `x` cannot contribute to target `x` itself, but contributes one unit to target `y`; its special increment is therefore

```text
1_{a_y < P_y}.                                         (8)
```

Adding `y` cannot contribute to target `y` itself, but contributes one unit to target `x`; its special increment is

```text
1_{a_x < P_x}.                                         (9)
```

If (8) equals one, then by (7) and `P_x>=P_y`,

```text
a_x <= a_y < P_y <= P_x,
```

so (9) also equals one. Thus the special increment for `x` is at most that for `y`.

Summing all target increments shows that adding `x` increases the capacity term of (2) no more than adding `y`. Finally `q_x>=q_y`, so subtracting source demand preserves the same inequality. This proves (5). QED.

## 5. Maximum-cardinality minimizer theorem

Let

```text
m = min_{W subseteq B} F(W).
```

Choose, among all minimizers `F(W)=m`, one with maximum cardinality.

> **Dominance-upset Hall theorem.** Such a maximum-cardinality minimizer `W*` is an up-set under `>=_H`:
>
> ```text
> y in W*, x >=_H y  =>  x in W*.                     (10)
> ```

### Proof

Suppose instead that

```text
y in W*,
x notin W*,
x >=_H y.
```

Put

```text
T = W* \ {y},
W' = T union {x}.
```

The exchange lemma gives

```text
F(W') - F(T) <= F(W*) - F(T),
```

hence

```text
F(W') <= F(W*) = m.
```

By minimality of `m`, equality holds, so `W'` is another minimizer.

Now use submodularity on the two minimizers `W*` and `W'`:

```text
F(W* intersect W') + F(W* union W')
 <= F(W*) + F(W') = 2m.                               (11)
```

Every set has margin at least `m`, so both terms on the left of (11) must equal `m`. In particular

```text
W* union W' = W* union {x}
```

is a minimizer of cardinality `|W*|+1`, contradicting the maximal choice of `W*`.

Therefore no such pair exists, proving (10). QED.

## 6. Whole-type consequence

Vertices having the same `(q,c,P)` triple dominate one another in both directions. Therefore an up-set under `>=_H` cannot contain only part of an identical type class.

Consequently:

> **Type-upset corollary.** There exists a minimum Hall-margin witness which is simultaneously
>
> 1. a union of complete `(q,c,P)` type classes; and
> 2. an up-set in the partial order
>
> ```text
> (q,c,P) >=_H (q',c',P')
> iff q>=q', c<=c', P>=P'.                             (12)
> ```

This strengthens the search-space interpretation of the whole-type Hall theorem. Instead of testing all `2^k` unions of `k` types, it is enough to test the up-sets of the three-dimensional hardness poset.

It does **not** assert that every minimizer is an up-set; the theorem selects a maximum-cardinality minimizer.

## 7. Certificate form

A target-Hall failure may therefore be certified by

```text
(type table (q,c,P,n),
a hardness up-set S,
F(S)<0).
```

The type-level quotient flow of [`TYPE_LEVEL_MAXFLOW_COROLLARY.md`](TYPE_LEVEL_MAXFLOW_COROLLARY.md) remains an exact polynomial-time test. The new theorem is valuable because it adds order structure to the source side of a minimum cut and offers a more promising route to hand inequalities.

## 8. What remains open

The theorem does not prove that a minimum witness can be chosen as

- a one-dimensional prefix;
- a principal up-set generated by one type;
- a rectangle in `(q,c,P)` space;
- a staircase determined only by `(q,c)`;
- a single type class.

The one-dimensional prefix shortcut already has an explicit counterexample in the earlier orientation-flow work. The next empirical question is how many minimal generators are needed by the hardness up-sets which actually witness the current frontier exclusions.

## 9. Verification plan

[`verify_dominance_upset_hall.py`](verify_dominance_upset_hall.py) independently checks, on exhaustive small labelled profiles and a deterministic broad challenge suite:

1. the interval identity (1);
2. submodularity of the labelled Hall margin;
3. the exchange inequality (5) for every dominance pair and every allowed background set `T`;
4. existence of a maximum-cardinality global minimizer satisfying (10);
5. agreement between unrestricted minimum Hall margin and the minimum over hardness up-sets.

The verifier is an audit of the finite identities, not the basis of the hand proof.

## 10. Trust boundary

This theorem is exact for the directed target-capacity Hall relaxation once `(q,c,P)` and the canonical compatibility rule are accepted. Its Murty-Simon application still depends on the canonical graph-to-constraint bridge and on the validity of the target-capacity upper bounds `P`.

External review and novelty assessment remain open. The unrestricted Murty-Simon conjecture is not proved by this result.
