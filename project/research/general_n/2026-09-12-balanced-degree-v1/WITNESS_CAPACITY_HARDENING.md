# Hardening of the all-order witness-capacity inequality

12 September 2026.

This note expands the short sentence leading to equation (4.1) in `BALANCED_DEGREE_THEOREM.md`. It introduces no new assumption; it makes the counting injection explicit so that the all-order theorem does not rely on the reader importing the N29/N31/N33 shorthand.

Use the odd-order notation from the theorem:

```text
n=2k+1,
L={x:epsilon_x>=2},  |L|=h,
O={x:epsilon_x=1},   |O|=o.
```

Every direct/two-step witness pair has deficit sum at least two.

Let `X=V\L`.

## 1. Edges incident with L

Let `E_L` be the number of actual graph edges having at least one endpoint in `L`. Write

```text
E_L = e(G[L]) + e_G(L,X).
```

These edges are counted directly.

## 2. Critical edges outside L whose witness meets L

Consider a critical edge `e` with both endpoints in `X`.

If a chosen witness pair for `e` meets `L`, that witness cannot be direct: a direct witness is the critical edge itself, which would then meet `L`. Hence it is a two-step witness pair, i.e. a **missing** pair `{u,v}` with unique common neighbour, with exactly one endpoint in `L` and the other in `X`.

For a fixed missing `L-X` pair, the unique common neighbour determines its two covered critical edges. Exactly one of those two can lie completely outside `L`; the other is incident with the `L` endpoint. Therefore each missing `L-X` pair accounts for at most **one** critical edge outside `L`.

Let `M_LX` be the number of missing `L-X` pairs. Then

```text
E_L + M_LX
 = e(G[L]) + e_G(L,X) + M_LX
 <= C(h,2) + h(n-h),
```

because

```text
e_G(L,X)+M_LX = h(n-h)
```

and `e(G[L])<=C(h,2)`.

Thus the direct count of edges incident with `L` and the one-edge capacities of missing `L-X` witnesses fit **inside the same** term

\[
{h\choose2}+h(n-h).
\]

There is no omitted extra `L-X` term and no double counting problem.

## 3. Witnesses disjoint from L

Now take a critical edge outside `L` whose chosen witness is disjoint from `L`. Every vertex outside `L` has deficit zero or one. Since every witness has deficit sum at least two, both witness endpoints must have deficit one. Hence the witness pair lies in `O-O`.

A direct `O-O` witness covers one critical edge. A two-step `O-O` witness has one unique common neighbour and covers at most the two edges of that length-two path. Therefore one unordered `O`-pair accounts for at most two critical edges, and all such witnesses together account for at most

\[
2{ o\choose2}=o(o-1)
\]

critical edges.

## 4. Combined inequality

Combining Sections 1-3 gives exactly

\[
\boxed{
 e(G)\le {h\choose2}+h(n-h)+o(o-1).
}
\]

For `n=2k+1` this is equation (4.1) of the balanced-degree theorem.

The argument is order-independent. It is the common combinatorial content behind the previously tabulated N29, N31 and N33 witness-deficit branches.