# Murty–Simon at n=29: reviewer-v3 candidate proof

11 September 2026. Research directed by Paul Lenz; mathematical development, implementation and internal checking by ChatGPT/Geeps. Hardened after a blind external-assistant red-team.

**Status: serious candidate proof; independent mathematical review, external computational reproduction and novelty assessment remain OPEN.** This edition reduces the computational dependency surface relative to the 9 September Fan-free v2 proof. It uses the minimal trusted Delta=16 kernel and new hand exclusions for the high Delta=16 upper range.

Historical editions remain preserved unchanged.

## 1. Statement

Let G be a simple diameter-two edge-critical graph on 29 vertices. The candidate statement is

\[
e(G)\le210=\left\lfloor\frac{29^2}{4}\right\rfloor,
\]

with equality if and only if

\[
G\cong K_{14,15}.
\]

A bipartite graph of diameter two is complete bipartite, so the bipartite case is immediate. Hence only the non-bipartite dense case needs analysis.

The published theorem of Dailly, Foucaud and Hansberg gives at most `floor(29^2/4)-2=208` edges for a non-bipartite diameter-two-critical graph with a dominating edge, apart from their order-six exception. Thus the dense cases below have no dominating edge.

A universal vertex forces a star and is therefore sparse.

## 2. Delta=15 witness argument and equality

A **direct witness** is an edge uv whose endpoints have no common neighbour. A **two-step witness** is a nonedge uv whose endpoints have exactly one common neighbour. Every critical edge is covered by one such witness: deleting the edge produces a pair whose every path of length at most two used that edge.

A direct witness covers one edge; a two-step witness covers at most the two edges of its unique length-two path.

Because there is no dominating edge, every witness pair uv satisfies

\[
d(u)+d(v)\le28. \tag{2.1}
\]

Assume `Delta=15`. Put

\[
\varepsilon_x=15-d(x),
\qquad L=\{x:\varepsilon_x\ge2\},
\qquad O=\{x:\varepsilon_x=1\}.
\]

Let `h=|L|`, `o=|O|`, and

\[
T=29\cdot15-2e(G).
\]

Every witness has deficit sum at least two, so

\[
2h+o\le T. \tag{2.2}
\]

Count all edges incident with L directly. An edge entirely outside L is witnessed either by an O-O witness, of capacity at most two, or by a missing L-X pair, of capacity at most one. This gives

\[
e(G)\le \binom h2+h(29-h)+o(o-1). \tag{2.3}
\]

No injective map from graph edges to witness pairs is assumed; only witness capacities are used.

At `e(G)=211`, `T=13`. The maximum right sides of (2.3) for `h=0,...,6` are

```text
156, 138, 127, 123, 126, 136, 153,
```

all below 211. Thus Delta=15 is impossible at 211 and therefore at every larger edge count as the deficit budget only shrinks.

At `e(G)=210`, `T=15`. The corresponding maxima are

```text
210, 184, 165, 153, 148, 150, 159, 175.
```

Equality forces `h=0,o=15`. All witnesses then lie inside O. Separating direct O-edges from two-step O-nonedges gives

\[
210\le e(G[O])+2\left(\binom{15}{2}-e(G[O])\right)
=210-e(G[O]),
\]

so O is independent. Its 15 vertices each have degree 14 and therefore meet all 14 vertices outside O. Those 210 cross edges exhaust the graph. Hence

\[
G=K_{15,14}.
\]

## 3. Self-contained Delta=16 bridge

For `Delta=16`, put `H=complement(G)`, choose a minimum-degree vertex v, and set

```text
A=N_H(v),          |A|=a=12,
B=V(H)\N_H[v],     |B|=b=16.
```

For every missing unordered B-pair choose exactly one cross quasi-edge representative `ui->w`, with exception w in B. Call these selected and all other A-B edges residual.

The complete graph-to-model proof is now isolated self-contained in

`project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md`.

Its necessary consequences include:

```text
e(F)=r+t,
S>=r+2t,
rho_u>=1 for every B-source when t>0,
s_i<=rho_u at every selected incidence,
r-b>=sum_i s_i(s_i-1)/(12-s_i),
sum_i s_i(13-2s_i)/(12-s_i)>=16+2t,
2W_h<=z_h^2-z_h+h(h+1),
delta(C)>=1,
d_i<=10,
r<=60-t,
```

together with the selected-edge, supplement and endpoint-load constraints needed by the late relaxation.

This v3 bridge expands the threshold-capacity proof in full rather than leaving it compressed in the main reviewer surface.

## 4. Delta=16 at m=210 and 211: minimal trusted kernel

The preferred proof-critical route is the minimal trusted kernel from the restarted hostile audit. It deliberately does **not** depend on the historical projected screen, joint propagator, old shared/typed/endpoint LP stack, or the old pair-capacity support formula.

Its sequence is:

```text
graph-to-model bridge
 -> exact charging demand domain
 -> exact threshold/source-count pruning
 -> exact source-capacity Hall dual pruning
 -> complete sorted residual-row enumeration
 -> monotone supplement-cap refinement
 -> corrected cumulative-threshold/source-q-flow relaxation
 -> exact integer Farkas verification.
```

### 4.1 m=211, t=3

The minimal preparation retains 72 demand profiles. Complete residual-row enumeration and necessary Hall/refinement cuts leave 126 rows. Every one of those 126 rows has an exact integer Farkas contradiction in the corrected late model.

```text
retained demands:   72
residual rows:     126
exact rejections: 126
final survivors:    0
```

### 4.2 m=210, t=2

The same independently specified kernel gives

```text
retained demands:  367
residual rows:     1467
exact rejections: 1467
final survivors:      0
```

The late model is the corrected v2 cumulative-threshold/source-q-flow relaxation. The historical v1 model contained a real label-group multiplicity normalization bug and is explicitly quarantined as invalid proof evidence.

Floating-point LP output is never accepted as a proof event. It is used only to propose multipliers. The checker accepts a Farkas contradiction only after exact integer recombination with nonnegative multipliers on inequalities, signed multipliers on equalities, nonnegative resulting variable coefficients, and a strictly negative combined right-hand side.

Therefore Delta=16 is impossible at both 211 and 210 edges.

## 5. Delta=16 upper range without Fan

For any positive-surplus Delta=16 scope the same bridge applies with

```text
t=m-208.
```

### 5.1 m=212, t=4

The exact trusted-kernel extension gives

```text
charging-feasible demand profiles: 2032
threshold rejects:                1706
source-count rejects:              258
exact early Hall-dual rejects:      65
open demand profiles:                3
residual numerical states:       19630
row survivors:                       2
exact late Farkas rejections:         2
final survivors:                      0
```

Thus m=212 is excluded.

### 5.2 m=213 and 214

At `m=213` (`t=5`), the complete charging domain has 586 profiles:

```text
576 threshold rejects,
  7 source-count rejects,
  3 exact Hall-dual rejects,
  0 survivors.
```

At `m=214` (`t=6`), all 79 charging-feasible profiles are threshold-rejected by exact integer arithmetic.

Thus both scopes are excluded before residual-row enumeration.

### 5.3 m=215 by hand

For every integer `0<=s<=11`,

\[
\frac{s(13-2s)}{12-s}\le\frac52, \tag{5.1}
\]

because

\[
\frac52-\frac{s(13-2s)}{12-s}
=\frac{(s-4)(4s-15)}{2(12-s)}\ge0. \tag{5.2}
\]

Equality occurs only at `s=4`.

At `m=215`, `t=7`, the bridge requires the sum of the twelve terms in (5.1) to be at least 30. Since 30 is also their maximum possible total, all twelve demands must equal four. Thus `S=48`.

The charging lower bound gives

\[
r-16\ge 12\frac{4\cdot3}{8}=18,
\]

so `r>=34`. But `S>=r+14` gives `r<=34`. Therefore `r=34`.

Let `z_4` be the number of residual rows of degree at least four. Residual activity gives

\[
34=r\ge16+3z_4,
\]

so `z_4<=6`. Threshold capacity gives

\[
96=2W_4\le z_4^2-z_4+20\le50,
\]

contradiction. Hence m=215 is impossible.

### 5.4 m>=216 by hand

Summing (5.1) over twelve labels gives a universal upper bound 30. The bridge requires

\[
16+2t\le30,
\]

so `t<=7`, i.e.

\[
m\le215.
\]

Therefore every Delta=16 scope with `m>=216` is excluded analytically. The historical generic outer scan over `m=216..232` is retained only as corroborating evidence and is no longer a logical dependency.

## 6. Delta=17 by a pointwise charging bound

For Delta=17, `a=11`. The bridge requires

\[
17+2t\le\sum_{i=1}^{11}\frac{s_i(12-2s_i)}{11-s_i}.
\]

For every integer `0<=s<=10`,

\[
\frac{s(12-2s)}{11-s}\le\frac{16}{7},
\]

because

\[
\frac{16}{7}-\frac{s(12-2s)}{11-s}
=\frac{2(s-4)(7s-22)}{7(11-s)}\ge0.
\]

Thus the right side is at most `176/7<29`. At 210 edges the required left side is already 29, and it only increases with m. Hence Delta=17 is impossible at every edge count relevant here.

## 7. Delta=18 through 27 by residual h-index

Let h be the largest integer for which at least h residual rows have degree at least h. A label of demand `s_i` needs `s_i` distinct selected sources with residual degree at least `s_i`, so `s_i<=h` and hence `S<=ah`.

Residual activity gives

\[
r\ge h^2+(b-h)=b+h(h-1).
\]

Combining with `S>=r+2t`,

\[
b+2t\le(a+1)h-h^2
\le\left\lfloor\frac{(a+1)^2}{4}\right\rfloor
=\left\lfloor\frac{(29-b)^2}{4}\right\rfloor. \tag{7.1}
\]

Every `b=18,...,27` violates (7.1) already at 210 edges, and increasing m only strengthens the contradiction. Delta=28 is the universal-vertex/star case.

## 8. Fan-free assembly

We can now exclude every `m>=211` without Fan's theorem.

For `m>=212`:

- `Delta<=14` is impossible by degree sum;
- `Delta=15` is excluded by the witness-deficit argument, monotone stronger above 211;
- `Delta=16` is excluded by exact finite arithmetic at `m=212,213,214`, by the hand threshold contradiction at `m=215`, and by the pointwise `5/2` cap for every `m>=216`;
- `Delta=17` is excluded by Section 6;
- `Delta=18,...,27` are excluded by Section 7;
- `Delta=28` gives a star.

At `m=211`, the same degree split leaves only Delta=16 after the hand cases, and the minimal trusted kernel excludes it.

Therefore

\[
e(G)\le210.
\]

At `m=210`, all non-Delta=15 cases are excluded by the minimal kernel or the hand degree arguments. Section 2 forces the unique equality graph

\[
K_{14,15}.
\]

This establishes the stated **candidate** order-29 result, subject to the review boundaries below.

## 9. Independent hostile evidence

A blind external-assistant red-team supplied on 11 September independently attacked the graph-to-model bridge, residual activity, threshold capacity, isolated-C, corrected LP normalization, exact Farkas semantics and the hand assembly, and reported no fatal defect.

It also independently obtained the complete charging-domain census

```text
t=2: 9251
t=3: 4867
t=4: 2032
t=5:  586
t=6:   79
t=7:    1
t=8:    0,
```

which the project independently regenerated again.

The blind reviewer also reported an exhaustive NetworkX graph-atlas bridge test through order seven. The project independently reproduced it:

```text
21 unlabeled diameter-two-edge-critical isomorphism types,
50 maximum-degree rooted cases,
58 admissible selection configurations,
0 bridge failures.
```

These small examples have only `t in {-3,-2,-1,0}`, so they do not independently test positive-surplus residual activity or charging. They are evidence for the base quasi-edge/selected/residual bridge only.

The preserved follow-up is

`project/reviews/n29/2026-09-11-blind-external-ai-redteam-v1/FOLLOWUP.md`.

## 10. Trust boundary

The current highest-value independent review targets are:

1. complement/quasi-edge construction and the one-representative-per-unordered-pair convention;
2. residual activity for `t>0`;
3. selected-source demand `s_i<=rho_u`;
4. threshold capacity;
5. isolated-C;
6. the actual-graph-to-averaged-variable embedding of the corrected late model;
7. exact Farkas checker semantics;
8. independent reproduction of the finite frontiers;
9. the cited Dailly-Foucaud-Hansberg dominating-edge theorem.

A counterexample to any universal bridge lemma overrides every green computation downstream. No unrestricted Murty–Simon theorem, order above the proved fixed-order frontier, external endorsement or novelty determination is asserted here.

## Key project dependencies

- Self-contained v3 bridge: `project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md`.
- Minimal-kernel report: `project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json`.
- Blind external red-team follow-up: `project/reviews/n29/2026-09-11-blind-external-ai-redteam-v1/FOLLOWUP.md`.
- Cross-order pointwise caps: `project/research/fan-free-fixed-orders/2026-09-11-pointwise-analytic-caps-v1/POINTWISE_CAPS.md`.
- Historical Fan-free v2 proof: `project/reviews/n29/2026-09-09-fan-free-v2/PROOF.md`.
