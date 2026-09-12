# Balanced-degree branch theorem

12 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate all-order structural theorem. Independent specialist review and novelty assessment remain OPEN.** This is not an unrestricted Murty-Simon proof. It isolates and closes the minimum-possible maximum-degree branch at the Turan edge level.

## 1. Statement

Let `G` be a finite simple diameter-two edge-critical graph on `n>=7` vertices. If

\[
\Delta(G)=\left\lceil\frac n2\right\rceil,
\]

then

\[
\boxed{e(G)\le \left\lfloor\frac{n^2}{4}\right\rfloor}.
\]

Moreover equality holds if and only if `G` is the balanced complete bipartite graph:

- `K_{k,k}` when `n=2k`;
- `K_{k,k+1}` when `n=2k+1`.

Consequently, any counterexample to the Murty-Simon bound must satisfy

\[
\boxed{\Delta(G)\ge \left\lceil\frac n2\right\rceil+1.}
\tag{1.1}
\]

The proof uses the standard direct/two-step witness lemma used in the fixed-order packages and the published Dailly-Foucaud-Hansberg dominating-edge theorem only to remove the dense non-bipartite dominating-edge case.

## 2. Even order

Let `n=2k` and `Delta=k`. Handshaking gives immediately

\[
e(G)\le \frac{2k\cdot k}{2}=k^2=\left\lfloor\frac{n^2}{4}\right\rfloor.
\]

Suppose equality holds. Then `G` is `k`-regular.

If `G` is bipartite, diameter two forces it to be complete bipartite, and regularity gives `K_{k,k}`.

Suppose instead that `G` is non-bipartite. At the Turan edge level the published dominating-edge theorem rules out a dominating edge. Hence every critical edge has a direct or two-step witness pair `xy` satisfying

\[
d(x)+d(y)\le n-1=2k-1.
\]

But regularity gives `d(x)+d(y)=2k`, a contradiction. Therefore equality is possible only for `K_{k,k}`.

This closes the even balanced-degree branch for every `n>=8` without any finite enumeration.

## 3. Odd order: setup

Let

\[
n=2k+1,\qquad \Delta=k+1,
\]

so the Turan number is

\[
M=k(k+1).
\]

The bipartite case is immediate: a bipartite diameter-two graph is complete bipartite, and maximum degree `k+1` forces the balanced partition `K_{k,k+1}`.

It remains to treat a non-bipartite graph with `m=e(G)>=M`. The published dominating-edge theorem rules out a dominating edge in this dense range. Therefore every direct/two-step witness pair `xy` satisfies

\[
d(x)+d(y)\le n-1=2k.
\tag{3.1}
\]

Define the degree deficit relative to `Delta=k+1` by

\[
\varepsilon_x=k+1-d(x).
\]

Put

\[
L=\{x:\varepsilon_x\ge2\},\qquad
O=\{x:\varepsilon_x=1\},
\]

and write

\[
h=|L|,\qquad o=|O|,
\qquad T=\sum_x\varepsilon_x=(2k+1)(k+1)-2m.
\tag{3.2}
\]

Equation (3.1) says every witness pair has total deficit at least two. Independently, from the definitions,

\[
2h+o\le T.
\tag{3.3}
\]

## 4. General witness-capacity inequality

Count every edge incident with `L` directly. This contributes at most

\[
{h\choose2}+h(2k+1-h).
\]

For an edge outside `L`, its direct/two-step witness either lies in `O-O`, where an unordered witness pair covers at most two critical edges, or is accounted for by the same missing-`L` injection used in the N29/N31/N33 witness proofs. Hence

\[
m\le {h\choose2}+h(2k+1-h)+o(o-1).
\tag{4.1}
\]

Since the last term is nondecreasing in integer `o>=0`, (3.3) gives the relaxation

\[
m\le F_T(h):={h\choose2}+h(2k+1-h)+(T-2h)(T-2h-1),
\tag{4.2}
\]

for

\[
0\le h\le \left\lfloor\frac T2\right\rfloor.
\]

Expanding,

\[
F_T(h)=T^2-T+\frac72h^2+\left(2k+\frac52-4T\right)h.
\tag{4.3}
\]

Thus `F_T(h)` is a **convex quadratic** in `h`. Its maximum on the allowed integer interval occurs at an endpoint.

This observation replaces the separate finite witness tables previously printed for N29, N31 and N33.

## 5. No graph above the Turan number

If `m>=M+1`, then from (3.2)

\[
T\le k-1.
\]

For fixed `h`, replacing `T` by `k-1` only enlarges the relaxed `o`-capacity relevant here, so it is enough to inspect `F_{k-1}`. By convexity the maximum occurs at

\[
h=0
\quad\hbox{or}\quad
h=\left\lfloor\frac{k-1}{2}\right\rfloor.
\]

At `h=0`,

\[
F_{k-1}(0)=(k-1)(k-2)<k(k+1)=M.
\]

At the other endpoint:

- if `k` is odd,
  \[
  F_{k-1}\left(\frac{k-1}{2}\right)
  =\frac{(k-1)(7k+3)}8
  =M-\frac{k^2+12k+3}{8}<M;
  \]
- if `k` is even,
  \[
  F_{k-1}\left(\frac{k-2}{2}\right)
  =\frac{(k-2)(7k+4)}8
  =M-\frac{k^2+18k+8}{8}<M.
  \]

Thus (4.1) would give `m<M`, contradicting `m>=M+1`. Hence

\[
m\le M.
\tag{5.1}
\]

## 6. Equality

Suppose `m=M`. Then (3.2) gives

\[
T=k+1.
\]

Again convexity leaves only the two endpoints.

At `h=0`,

\[
F_{k+1}(0)=k(k+1)=M.
\]

At the other endpoint:

- if `k` is odd,
  \[
  F_{k+1}\left(\frac{k+1}{2}\right)
  =M-\frac{(k-1)(k+1)}8<M;
  \]
- if `k` is even,
  \[
  F_{k+1}\left(\frac{k}{2}\right)
  =M-\frac{k(k+6)}8<M.
  \]

Therefore equality in the edge bound forces

\[
h=0,\qquad o=k+1.
\tag{6.1}
\]

All witness pairs must then lie inside `O`. Let `e_O=e(G[O])`. Splitting direct `O`-edge witnesses from two-step `O`-nonedge witnesses gives

\[
M\le e_O+2\left({k+1\choose2}-e_O\right)
   =M-e_O.
\]

Hence `e_O=0`: the `k+1` vertices of `O` are independent.

Every vertex of `O` has degree

\[
(k+1)-1=k,
\]

and exactly `k` vertices lie outside `O`. Thus every vertex of `O` is adjacent to every outside vertex. These `k(k+1)=M` cross edges exhaust the graph, so

\[
G\cong K_{k,k+1}.
\]

In the non-bipartite branch this is a contradiction; globally it identifies the unique equality graph.

## 7. Corollary for any prospective counterexample

At `m>=floor(n^2/4)`, average degree already forces

\[
\Delta\ge\left\lceil\frac n2\right\rceil.
\]

The theorem closes equality at that minimum possible maximum degree. Therefore every genuine counterexample must lie strictly above it, proving (1.1).

This is a genuine all-order reduction: the odd fixed-order witness tables at N29, N31 and N33 are instances of one convex endpoint calculation.

## 8. Trust boundary

The new algebra is elementary. The graph-theoretic inputs requiring independent review are:

1. every critical edge is covered by the direct/two-step witness mechanism used in the fixed-order papers;
2. in the no-dominating-edge case, every such witness pair satisfies `d(x)+d(y)<=n-1`;
3. the witness-capacity count (4.1);
4. the published dominating-edge theorem used to remove the dense non-bipartite dominating-edge case.

No computation is a logical premise of this theorem.