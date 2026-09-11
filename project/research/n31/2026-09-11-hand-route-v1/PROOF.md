# Murty-Simon at n=31: first hand-route candidate proof

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: new candidate hand proof. Independent mathematical review and novelty assessment OPEN.** No large search, LP, Farkas certificate or proof-critical computation is used. The proof depends on the project's candidate canonical selected/residual bridge and the hand twelve- and thirteen-label tail lemmas, all still awaiting independent review.

## 1. Statement

Let `G` be a finite simple diameter-two edge-critical graph on 31 vertices. The candidate theorem is

\[
e(G)\le240=\left\lfloor\frac{31^2}{4}\right\rfloor,
\]

with equality if and only if

\[
G\cong K_{15,16}.
\]

If `G` is bipartite, diameter two forces it to be complete bipartite, so the statement is immediate. We therefore consider the non-bipartite case in the dense range.

Dailly-Foucaud-Hansberg prove that a non-bipartite D2C graph with a dominating edge has at most `floor(n^2/4)-2` edges, apart from their six-vertex graph `H_5`. At `n=31` this is at most 238. Hence any non-bipartite graph with at least 240 edges has no dominating edge.

Also, `2e(G)/31>=480/31>15` at 240 edges, so

\[
\Delta\ge16.
\]

The high-degree range will be handled directly by the source-independent twelve-label theorem, so the separate `7/12` maximum-degree theorem is not a dependency of this proof.

## 2. Every Delta>=18 branch

For `18<=Delta<=29`, put

\[
a=31-1-\Delta,
\qquad b=\Delta.
\]

Then `1<=a<=12` and `b>=18`. The source-independent twelve-label tail theorem says that no positive surplus over `b(n-b)` is possible, hence

\[
e(G)\le b(31-b).
\]

The quadratic decreases throughout `b>=18`, so its largest value in this range is

\[
18(31-18)=234<240.
\]

The remaining case `Delta=30` has a universal vertex; a diameter-two edge-critical graph with a universal vertex is a star and is sparse. Thus every `Delta>=18` branch is excluded from the target range by hand, with no appeal to the `7/12` theorem and no new enumeration.

## 3. Delta=17

Here `(a,b)=(13,17)` and the surplus relative to the complete-bipartite benchmark is

\[
t=e(G)-17\cdot14=e(G)-238.
\]

The thirteen-label hand lemma in

`project/research/general_n/2026-09-11-thirteen-label-tail-v1/THIRTEEN_LABEL_TAIL.md`

proves

\[
Q\le21,
\qquad Q\ge17+2t.
\]

Thus `e(G)>=241` gives `t>=3` and `Q>=23`, impossible.

At `e(G)=240`, `t=2`, so equality `Q=21` is forced. The same hand lemma proves that the unique equality demand vector is `3^13`, then uses the equality case of threshold capacity together with endpoint load to derive the incompatible bounds

\[
\sum_{u\in Z}p_u\ge33
\qquad\hbox{and}\qquad
\sum_{u\in Z}p_u\le18.
\]

Hence

\[
\Delta=17\Longrightarrow e(G)\le239.
\]

## 4. Delta=16: witness-deficit closure

This is the balanced odd-order branch. Because the graph has no dominating edge in the target range, every direct or two-step witness pair `xy` has

\[
d(x)+d(y)\le30.
\]

Put

\[
\varepsilon_x=16-d(x),
\qquad
L=\{x:\varepsilon_x\ge2\},
\qquad
O=\{x:\varepsilon_x=1\},
\]

and write `h=|L|`, `o=|O|`. Let

\[
T=31\cdot16-2e(G).
\]

Every witness has deficit sum at least two, so

\[
2h+o\le T.
\tag{4.1}
\]

Exactly as in the N29 witness argument, count all edges incident with `L` directly. An edge outside `L` is covered either by an `O-O` witness, of capacity at most two, or by a missing `L-X` witness, of capacity at most one. Therefore

\[
e(G)\le \binom h2+h(31-h)+o(o-1).
\tag{4.2}
\]

### 4.1 No graph above 240 edges

At `e(G)>=241`, one has `T<=14`. Maximising the right side of (4.2) under `2h+o<=14` gives, for `h=0,...,7`,

```text
182, 162, 149, 143, 144, 152, 167, 189.
```

Every value is below 241. Thus `Delta=16` is impossible above the Turan number.

### 4.2 Equality forces K(16,15)

At `e(G)=240`, `T=16`. The maxima of (4.2) for `h=0,...,8` are

```text
240, 212, 191, 177, 170, 170, 177, 191, 212.
```

Equality therefore forces

\[
h=0,\qquad o=16.
\]

All witnesses then lie inside `O`. Splitting direct `O`-edges from two-step `O`-nonedges gives

\[
240\le e(G[O])
 +2\left(\binom{16}{2}-e(G[O])\right)
=240-e(G[O]).
\]

Hence `O` is independent. Every vertex of `O` has deficit one and therefore degree 15. Since exactly 15 vertices lie outside `O`, each vertex of `O` is adjacent to every outside vertex. These `16*15=240` cross edges exhaust the graph, so

\[
G=K_{16,15}.
\]

## 5. Assembly

At 240 edges or above, average degree gives `Delta>=16`. The branches are:

- `Delta>=18`: at most 234 (or the elementary star at `Delta=30`) by the twelve-label hand theorem;
- `Delta=17`: at most 239 by the new thirteen-label hand theorem and equality contradiction;
- `Delta=16`: at most 240 by the witness-deficit count, with equality only `K_{16,15}`.

Therefore the candidate conclusion is

\[
\boxed{e(G)\le240,\qquad e(G)=240\iff G\cong K_{15,16}.}
\]

This is a hand-route candidate proof. The only finite tables are explicit small integer capacity/deficit tables. Independent specialist review of the canonical bridge, the thirteen-label clipping lemma, and the equality-chain argument remains essential before the result is treated as established.
