# Reviewer-v4 red-team hardening supplement

11 September 2026.

This supplement records **non-blocking self-containedness and presentation hardening** identified in the hostile reviewer-v4 audit. It changes no mathematical conclusion.

## 1. Complement / total-domination correspondence

Let `H=complement(G)`. A pair `{x,y}` is a two-vertex total dominating set of `H` exactly when:

1. `xy` is an H-edge, hence a G-nonedge; and
2. every vertex is adjacent in H to at least one of x,y, equivalently x and y have no common neighbour in G.

Thus a two-vertex total dominating set in H is the complement-language form of a G-pair at distance greater than two.

If `xy` is an edge of the D2C graph G, deleting it makes some pair have distance greater than two. Equivalently, after adding `xy` to H, a two-vertex total dominating set appears. Because the only changed adjacency is `xy`, every newly appearing pair must use x or y. This is the quasi-edge premise used in the selected/residual bridge.

## 2. Delta=15 witness-capacity count made explicit

Let L be the vertices of deficit at least two, O the vertices of deficit one. Write

```text
P_L = C(h,2)+h(29-h)
```

for the total number of unordered vertex pairs incident with L.

Partition these pairs into actual G-edges `E_L` and missing pairs `M_L`. Every graph edge outside L is covered either by:

- an O-O witness, with capacity at most two; or
- a missing L-X two-step witness, with capacity at most one on edges outside L.

Therefore

```text
e(G)
 = |E_L| + e_G(V\L)
 <= |E_L| + |M_L| + 2 C(o,2)
 = P_L + o(o-1),
```

which is the manuscript inequality (2.3).

## 3. Full 4->3 clipping endpoint table

In the hand threshold-tail proof, after `max s_i<=4`, let `k=N_4` and let `l` be the number of threes among the remaining entries.

For `k=9`, `d_4=1` and the level-three changes are:

```text
l      W_3 -> W'_3      g_3 -> g'_3      drop
0       36 -> 27          9 -> 7           2
1       39 -> 30          9 -> 8           1
2       42 -> 33          9 -> 8           1
3       45 -> 36         10 -> 9           1
```

For `k=10`, again `d_4=1`:

```text
l      W_3 -> W'_3      g_3 -> g'_3      drop
0       40 -> 30          9 -> 8           1
1       43 -> 33         10 -> 8           2
2       46 -> 36         10 -> 9           1
```

So the loss of `d_4=1` is always paid for.

For `k=11`, `d_4=2`. If the remaining entry is at most two,

```text
W_3: 44 -> 33,
g_3: 10 -> 8,
```

so the level-three gain is two. If the remaining entry is three, `(3,4^11)->(3^12)` gives one unit of gain at each of levels two and three.

For `k=12`, `(4^12)->(3^12)` likewise decreases each of `g_2,g_3` from 10 to 9, paying the two-unit loss of `d_4`.

## 4. Explicit parameterisation for Delta>=17

For the N29 degree split, set

```text
b = Delta(G),
a = 28-b,
t = m - b(29-b).
```

The selected/residual bridge is parameterised in `(a,b)`; its proofs of the exact ledger, residual activity, selected-incidence forcing, charging and residual h-index use no special numerical property of `(a,b)=(12,16)` until the final substitutions.

Thus:

- `Delta=17`: `a=11,b=17,t=m-204`;
- `Delta=18,...,27`: `a=28-b` and the same `t=m-b(29-b)`.

At `m=210`, `Delta=17` gives `t=6` and hence the charging lower bound `b+2t=29` used in reviewer-v4.

## 5. Dominating-edge citation

The cited result is:

Antoine Dailly, Florent Foucaud, Adriana Hansberg, **Strengthening the Murty-Simon conjecture on diameter 2 critical graphs**, *Discrete Mathematics* 342 (2019), 3142-3159. DOI: `10.1016/j.disc.2019.06.023`.

Their Theorem 4 states that a non-bipartite D2C graph with a dominating edge, other than the six-vertex graph H5, has at most

```text
floor(n^2/4)-2
```

edges. At n=29 this gives 208.

## 6. Independence wording

The exact programs in this project are **separately implemented internal regressions**, not independent external validation. Independent mathematical review and independent computational reproduction remain open.

## 7. Disposition

No mathematical correction to reviewer-v4 is made by this supplement. The hostile audit found no blocking flaw; these additions make the review surface easier to reconstruct without relying on implicit parameterisation or omitted tiny case tables.
