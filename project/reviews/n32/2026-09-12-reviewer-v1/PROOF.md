# Murty-Simon at n=32: reviewer-v1 candidate proof

12 September 2026. Research direction: Paul Lenz. Mathematical development, implementation and internal checking: ChatGPT/Geeps.

**Status: complete candidate fixed-order proof. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.** The unrestricted Murty-Simon conjecture is not claimed.

## 1. Candidate statement

Let `G` be a finite simple diameter-two edge-critical graph on 32 vertices. The candidate theorem is

\[
e(G)\le256=\left\lfloor\frac{32^2}{4}\right\rfloor,
\]

with equality if and only if

\[
G\cong K_{16,16}.
\]

A bipartite diameter-two graph is complete bipartite, so the bipartite case is immediate. We therefore consider the non-bipartite dense range.

The Dailly-Foucaud-Hansberg dominating-edge theorem used elsewhere in this repository implies that a non-bipartite D2C graph with a dominating edge has at most `floor(n^2/4)-2=254` edges at order 32 (apart from its fixed order-six exception). Hence any non-bipartite graph relevant at 256 edges or above has no dominating edge.

At `e(G)>=256`, average degree is at least 16, so

\[
\Delta(G)\ge16.
\]

Put

\[
a=31-\Delta,
\qquad b=\Delta,
\qquad t=e(G)-b(32-b).
\]

We split by maximum degree.

## 2. Delta>=18

### 2.1 Delta=18

Here `(a,b)=(13,18)` and the complete-bipartite benchmark is

\[
18(32-18)=252.
\]

If `e(G)>=256`, then `t>=4`. The thirteen-label hand theorem gives

\[
Q\le21,
\]

while the canonical bridge gives

\[
Q\ge b+2t\ge18+8=26,
\]

impossible.

### 2.2 Delta>=19

For `19<=Delta<=30`, one has `a<=12`. The source-independent twelve-label theorem says that positive surplus over `b(32-b)` is impossible. But throughout this range

\[
b(32-b)\le19\cdot13=247<256.
\]

Hence no graph in the target range occurs.

If `Delta=31`, the graph has a universal vertex. A diameter-two edge-critical graph with a universal vertex is a star, so it is sparse.

Therefore every `Delta>=18` branch is excluded from 256 edges or above.

## 3. Delta=17: upper-bound levels above 256

Here

\[
(a,b)=(14,17),
\qquad b(32-b)=255,
\qquad t=e(G)-255.
\]

The fourteen-label hand theorem proves

\[
Q\le23.
\]

The bridge gives

\[
Q\ge17+2t.
\]

Thus `e(G)>=259` gives `t>=4` and `Q>=25`, impossible.

### 3.1 The 258-edge level

At `e(G)=258`, `t=3`, so `Q>=23`; equality is forced. The fourteen-label theorem classifies the three score-maximising demand profiles as

```text
3^14,
3,4^13,
4^14.
```

All three are excluded by hand in

- `project/research/n32/2026-09-11-hand-route-v1/`,

using the tight residual-tail ledger, supplement forcing, source indegree bounds and a core-pair counting contradiction. Hence `m=258` is impossible.

### 3.2 The 257-edge level

At `e(G)=257`, `t=2`. The exact score frontier has 71 demand profiles:

```text
Q=21 : 50
Q=22 : 18
Q=23 :  3.
```

The 70 positive-demand profiles expand, after every allowed residual-tail slack increment, to 154 `(s,rho)` states. A single fixed nine-term monotone BC rectangle potential excludes all 154 with exact integer acceptance:

\[
\begin{aligned}
F={}&4B_{2,0}+2B_{2,6}+B_{2,8}+B_{2,10}\\
&+B_{2,13}+B_{2,14}+B_{3,9}+B_{3,11}+B_{3,12}.
\end{aligned}
\]

The potential and exactifier are preserved at

- `project/research/n32/2026-09-12-t2-frontier-v1/N32_T2_RECTANGLE_POTENTIAL.md`,
- `project/research/n32/2026-09-12-t2-frontier-v1/n32_t2_nine_rectangle_exact.py`.

The sole zero-demand profile is

```text
0,3^13.
```

Its tail inequalities are all tight. The equality case of threshold capacity gives residual degrees `3^9,1^8`, forces at least 33 selected exceptions back into the nine high sources, while endpoint load and source forcing give at most two exceptions per high source, hence at most 18. Contradiction.

Therefore `e(G)=257` is impossible.

Combining Sections 3.1-3.2 with the scalar upper range gives

\[
\Delta=17\Longrightarrow e(G)\le256.
\]

## 4. Delta=17 at equality: m=256, t=1

This is the final difficult equality branch.

The fourteen-label theorem and bridge give

\[
19\le Q\le23.
\]

An independent exhaustive checker enumerates all 20,058,300 nondecreasing fourteen-demand multisets and finds exactly 381 frontier profiles:

```text
Q=19 : 206
Q=20 : 104
Q=21 :  50
Q=22 :  18
Q=23 :   3.
```

The frozen equality evidence is indexed at

- `project/research/n32/2026-09-12-equality-v1/README.md`,
- `project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md`.

### 4.1 Residual-tail completeness and one arithmetic impossibility

The lower bounds `z_h>=gamma_h(W_h)` must be made monotone because the residual tails satisfy

\[
z_1\ge z_2\ge\cdots.
\]

After monotone closure, one apparent `Q=19` profile is impossible before modelling:

```text
3^11,5^3.
```

It requires `r>=47`, whereas `S-2=46`.

Distributing every remaining admissible residual-tail slack unit gives an intentionally conservative finite domain of

```text
1,984 positive-demand states,
61 zero-demand states.
```

The positive domain over-enumerates actual all-positive graph images because in that sector the exact ledger gives `S=r+2`; the larger domain is safe and is the frozen certified domain.

### 4.2 Exact first-stage potential: 1,369 states

The natural `b=17` lift of the exact N30 `t=1` 3-D potential is fixed globally. Its BC `v` thresholds and diagonal `K` thresholds shift upward by one; the `s>=2` term is unchanged.

For each state only the scalar envelope coefficients are allowed to vary. Floating LP proposes them; acceptance is exact integer arithmetic after one-sided `ell/sigma` repair.

The exact replay gives

```text
positive states tested       : 1,984
exact potential exclusions   : 1,369
survivors                     :   615
exactification failures      :     0
```

Every accepted certificate uses denominator 10,000, with strict gap numerators between `-10003` and `-9827`.

Replay source:

- `project/research/n32/2026-09-12-equality-v1/n32_t1_lifted_potential_exact.py`.

### 4.3 Exact full RX/Hall replay: 614 of 615

The 615 survivors are passed to the preserved full positive-demand RX/Hall necessary-condition model. Each computational exclusion is accepted only when the generic exact integer Farkas verifier succeeds.

The completed exact ledger is

```text
input states       : 615
exact Farkas rejects: 614
primal survivors     :   1
unresolved            :   0.
```

The sharded replay is

- `project/research/n32/2026-09-12-equality-v1/n32_t1_full_rx_exact.py`.

### 4.4 The sole full-RX survivor is impossible by hand

The survivor is

```text
s   = 1^2,2^12,
rho = 1^10,2^7.
```

Let `Z={u:rho_u>=2}`, so `|Z|=7`. At threshold two,

\[
W_2=24=C_2(7).
\]

Thus every inequality in the threshold-capacity proof is equality. Writing `J={u in Z:ell_u>2}`, the capacity-gap identity forces `|J|=4` or `5`; consequently at least 18 heavy selected arcs have supplements back in `Z`, so

\[
\sum_{u\in Z}p_u\ge18.
\]

Equality also gives exactly 24 actual heavy incidences. Hence every demand-two label has `x_i=2`, and every source in `Z` is heavy-active. For a demand-two selected incidence from `u in Z`, positive demand gives `d_i=R_i+2`; endpoint load and source forcing give

\[
q_u+p_u\le R_i+2=d_i\le q_u+1,
\]

so `p_u<=1`. Therefore

\[
\sum_{u\in Z}p_u\le7,
\]

contradiction.

The full hand derivation is `project/research/n32/2026-09-12-equality-v1/HAND_EXCEPTION.md`.

### 4.5 Zero-demand states: 61 exact exclusions

For `s=0`, the compression `d=R+s` is unavailable. The zero-demand replay therefore keeps `d` and `R` separately and enforces

\[
s=\max(0,d-R),
\qquad \sum R_i=r,
\qquad \sum d_i=2(r+t).
\]

The isolated-C lemma applies parametrically: an isolated C-vertex would imply

\[
b\le a-1-t,
\]

which here reads `17<=12`, impossible. Hence `delta(C)>=1` and `d_i<=a-2=12`.

The strengthened exact model rejects

```text
61/61 zero-demand states
```

by exact integer Farkas verification, with zero unresolved rows. Replay source:

- `project/research/n32/2026-09-12-equality-v1/n32_t1_zero_exact.py`.

Therefore no non-bipartite `Delta=17` graph has 256 edges.

## 5. Delta=16 at equality

If `Delta=16`, the handshaking lemma alone gives

\[
e(G)\le\frac{32\cdot16}{2}=256.
\]

Assume equality. Then every vertex has degree 16, so `G` is 16-regular.

If `G` were non-bipartite, the dominating-edge theorem above shows it has no dominating edge at 256 edges. Every critical edge is covered by a direct or two-step witness pair. In a no-dominating-edge D2C graph every such witness pair `xy` satisfies

\[
d(x)+d(y)\le31.
\]

But regularity gives `d(x)+d(y)=32`, contradiction.

Hence an equality graph is bipartite. A bipartite diameter-two graph is complete bipartite, and with 32 vertices and 256 edges the only possibility is

\[
K_{16,16}.
\]

## 6. Assembly

At 256 edges or above, average degree gives `Delta>=16`.

- `Delta>=18`: excluded below 256 by the thirteen-/twelve-label hand bounds (or the universal-vertex star case).
- `Delta=17`: `m>=259` is scalar-impossible; `m=258` is hand-closed; `m=257` has an exact nine-rectangle closure plus one hand zero-demand contradiction; `m=256` is completely covered by the exact equality replay plus one hand tight-threshold contradiction.
- `Delta=16`: handshaking gives `m<=256`, and equality forces the bipartite graph `K_{16,16}`.

Therefore the candidate conclusion is

\[
\boxed{e(G)\le256,\qquad e(G)=256\iff G\cong K_{16,16}.}
\]

## 7. Replay and trust boundary

The equality replay can be regenerated with

```sh
bash project/research/n32/2026-09-12-equality-v1/run_replay.sh
```

No floating-point infeasibility is a proof event in the equality package. Floating solvers propose scalar/Farkas coefficients; accepted exclusions are checked exactly in rational/integer arithmetic.

The principal external-review trust boundary remains the universal selected/residual bridge and its threshold-capacity / endpoint-load consequences. The finite models are necessary-condition relaxations of that bridge; exact rejection is useful only if the graph-to-model implications are sound. Same-assistant hostile audits and replay are not external validation.
