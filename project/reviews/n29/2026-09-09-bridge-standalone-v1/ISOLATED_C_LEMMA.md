# Parameteric isolated-C exclusion

9 September 2026. Research directed by Paul Lenz; mathematical development and hostile rederivation by ChatGPT/Geeps.

**Status: candidate hand lemma; independent expert review remains OPEN.** This file expands the previously compressed `delta(C)=0` step because it is used both in the n=29 and n=30 finite reductions.

## Statement

Use the standard complement/quasi-edge setup. Let

```text
H = complement(G),
A = N_H(v),                 |A|=a,
B = V(H) \ N_H[v],          |B|=b,
C = H[A],
F = complement(C) on A,
r = number of residual A-B edges,
t = m-b(n-b).
```

Assume `t>0`, so the residual-activity lemma gives at least one residual A-B edge incident with every vertex of `B`.

If `C` has an isolated vertex, then necessarily

```text
b <= a-1-t.                                      (I)
```

Consequently, whenever `b>a-1-t`, one has `delta(C)>=1`.

## 1. Choose the isolated vertex

Suppose `x in A` is isolated in `C=H[A]`. Put

```text
X=A\{x},        |X|=a-1.
```

Because x is C-isolated,

```text
e(C)=e(C[X]).
```

The exact ledger is

```text
e(C)+r = C(a,2)-t.
```

Hence the number P0 of missing H-edges inside X is

```text
P0 = C(a-1,2)-e(C[X])
   = C(a-1,2)-[C(a,2)-t-r]
   = r-(a-1-t).                                  (1)
```

In particular `P0>=0` for any realizable graph.

## 2. A missing X-pair forces a cross quasi-edge with B-auxiliary

Take a missing pair `ij` of `H[X]`. It is an edge of G. Add `ij` to H, corresponding to deleting that critical G-edge. The enlarged complement acquires a new adjacent total-dominating pair.

That new pair must use `i` or `j`, because no other adjacency changed.

It cannot be the pair `{i,j}` itself: x is nonadjacent in H to both i and j, since x is isolated in C, so `{i,j}` does not dominate x even after ij is added.

After interchanging i and j if necessary, write the new pair as `{i,z}`, where `iz` was already an H-edge. Before adding ij, the pair `{i,z}` covers every vertex except j; write

```text
iz -> j.                                         (2)
```

We claim `z in B`.

- `z` cannot equal `v`. The vertex v is already adjacent in H to every vertex of A, including j. Adding ij therefore cannot turn `{i,v}` from a non-total-dominating pair into a total-dominating pair: the only newly covered vertex by i is j, and v already covered j.
- `z` cannot lie in `A`. If `z in X`, then z is nonadjacent to x because x is C-isolated, while i is also nonadjacent to x; hence `{i,z}` cannot dominate x. If `z=x`, then `ix` is not an H-edge, so `{i,z}` is not an adjacent pair.

Therefore `z in B`.

Thus every missing H-edge inside X gives a cross quasi-edge `iz->j` with auxiliary z in B.

## 3. These cross quasi-edges are residual and distinct

The selected A-B edges used for missing pairs in `H[B]` have their unique undominated vertex in B.

The cross edge in (2) has its unique undominated vertex `j in X subset A`. Therefore it cannot be one of those selected edges; it is residual.

Distinct missing pairs inside X yield distinct residual cross-edges. Indeed, an existing cross-edge `iz` has a uniquely determined undominated vertex when it is a quasi-edge; it cannot simultaneously be `iz->j1` and `iz->j2` for two distinct exceptions.

Let `P` be this family. By (1),

```text
|P| = r-(a-1-t).                                 (3)
```

Every edge in P has its A-endpoint in X.

## 4. One additional residual edge for every B-vertex

Let Z be the set of B-endpoints used by edges of P.

### Used B-endpoints

Take `z in Z`, and choose one relation `iz->j` from P incident with z.

Because `x!=j`, the quasi-edge pair `{i,z}` must dominate x. Since i is nonadjacent to x, this forces

```text
xz in E(H).                                      (4)
```

Moreover xz is residual. Suppose instead that xz were selected for a missing B-pair. Then the selected pair `{x,z}` would have to dominate every A-vertex. Because x is isolated in C, x has no neighbours in X, so z would have to be adjacent in H to every vertex of X. But `iz->j` requires z to miss j: i misses j and `{i,z}` leaves j as its unique exception. Contradiction.

Thus each used endpoint `z in Z` supplies a residual edge xz outside P. These edges are distinct for distinct z.

### Unused B-endpoints

If `z in B\Z`, residual activity supplies at least one residual A-B edge incident with z. Such an edge is automatically outside P because no edge of P has B-endpoint z.

Therefore **every one of the b vertices of B supplies a distinct residual edge outside P**: xz for z in Z, and an arbitrary residual incidence for z outside Z.

Hence

```text
r >= |P|+b.                                      (5)
```

Substituting (3) into (5) gives

```text
r >= r-(a-1-t)+b,
```

and therefore

```text
b <= a-1-t.
```

This proves (I).

## 5. n=29 and n=30 specialisations

### n=29, Delta=16

Here `(a,b)=(12,16)` and `t in {3,2}`. The isolated-C inequality would require

```text
16 <= 11-t,
```

which is impossible. Hence `delta(C)>=1`, so `d_F(i)<=10`, `e(C)>=6`, and

```text
r<=C(12,2)-t-6=60-t.
```

### n=30, Delta=16

Here `(a,b)=(13,16)` and `t in {2,1}`. The isolated-C inequality would require

```text
16 <= 12-t,
```

i.e. `16<=10` or `16<=11`, both impossible. Hence `delta(C)>=1`, so

```text
d_F(i)<=11,
e(C)>=ceil(13/2)=7,
r<=C(13,2)-t-7.
```

Thus

```text
m=226, t=2: r<=69,
m=225, t=1: r<=70.
```

These are exactly the hard bounds used in the n=30 Delta=16 preparation.

## 6. Audit boundary

The proof depends only on:

1. the complement form of edge-criticality / quasi-edge creation;
2. uniqueness of the undominated exception for a chosen quasi-edge;
3. the selected/residual distinction by whether the exception lies in B or A;
4. the exact ledger;
5. residual activity for `t>0`.

No finite enumeration, LP model, projected screen or n=29-specific numerical constant is used.

A counterexample to any one of those ingredients would invalidate this lemma and the downstream `dmax`/row-total bounds. Until independent review occurs, the result remains candidate mathematics.
