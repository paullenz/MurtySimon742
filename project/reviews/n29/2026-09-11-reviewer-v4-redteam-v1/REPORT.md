# Hostile audit of N29 reviewer-v4

11 September 2026. Research direction: Paul Lenz. Hostile same-assistant audit: ChatGPT/Geeps.

**Audited release:** reviewer-v4 package published from commit `8378a381c09b4f9d9576d6b220cb649816d1a2f3`, with later audit tooling added on `main`.

**Verdict: NO BLOCKING FLAW FOUND.**  
This is internal hostile review, not independent mathematical validation. A counterexample to any universal bridge lemma still overrides every downstream conclusion.

## 1. Audit policy

The audit did not treat green historical computation as protection for reviewer-v4. It reconstructed the logical route now claimed by the manuscript:

```text
D2C graph
 -> no dense dominating-edge non-bipartite case
 -> degree split
 -> Delta=15 witness/equality argument
 -> Delta=16 selected/residual bridge
 -> residual activity + selected-incidence forcing
 -> threshold capacity
 -> demand-only threshold tails
 -> hand bound Q(s)<=18
 -> Delta=17 pointwise charging
 -> Delta=18..27 residual h-index
 -> assembly.
```

The old residual-row / LP / Farkas route was treated only as corroborating history.

## 2. Dominating-edge citation

The published Dailly-Foucaud-Hansberg result was checked against the paper itself:

Antoine Dailly, Florent Foucaud, Adriana Hansberg, *Strengthening the Murty-Simon conjecture on diameter 2 critical graphs*, Discrete Mathematics 342 (2019), 3142-3159, DOI 10.1016/j.disc.2019.06.023.

Their Theorem 4 states that a non-bipartite D2C graph with a dominating edge, other than the six-vertex graph H5, has at most

```text
floor(n^2/4)-2
```

edges. At n=29 this is 208. The reviewer-v4 use of the theorem is therefore correct.

**Verdict:** survives.

## 3. Delta=15 witness argument

The edge-critical witness dichotomy was reconstructed directly:

- if deletion of an edge destroys the distance-one path between its own endpoints, those endpoints are an adjacent direct witness with no common neighbour;
- otherwise the destroyed distance-two connection is a nonedge with exactly one common neighbour, and its unique two-edge path contains the critical edge.

A direct witness covers only its own edge; a two-step witness covers at most the two path edges.

For maximum degree 15 and no dominating edge, every witness pair has degree sum at most 28, hence deficit sum at least two.

The manuscript's inequality

```text
e(G) <= C(h,2)+h(29-h)+o(o-1)
```

was rederived by partitioning all unordered pairs incident with L into actual edges and missing L-X pairs. Each missing L-X witness can cover at most one graph edge outside L; O-O witness pairs contribute capacity at most two each.

The displayed maxima were independently regenerated exactly:

```text
T=13: 156, 138, 127, 123, 126, 136, 153
T=15: 210, 184, 165, 153, 148, 150, 159, 175.
```

At 210 edges equality forces h=0,o=15. Then every witness lies in O, and the capacity inequality

```text
210 <= e(G[O]) + 2(C(15,2)-e(G[O]))
```

forces O independent. Every O-vertex has degree 14 and therefore meets all 14 vertices outside O, yielding K(15,14).

**Verdict:** survives.

## 4. Delta=16 bridge

The following proof-critical consequences were rederived from the graph definitions rather than accepted from the late-model code:

### 4.1 Complement/quasi-edge construction

For a missing unordered B-pair {u,w}, adding uw to H corresponds to deleting the critical edge uw from G. The resulting new two-vertex total-dominating pair must use u or w; it cannot be {u,w} because both miss v. Thus, after orientation, one obtains a cross edge ui with unique exception w. The auxiliary i must lie in A because u misses v.

One selected representative is chosen per missing unordered B-pair. A selected cross edge recovers its B-source and unique exception, so the selection is injective on unordered B-pairs.

**Verdict:** survives.

### 4.2 Exact ledger and demand

Direct edge counting gives

```text
e(F)=r+t,
S>=r+2t.
```

No approximation is involved.

**Verdict:** survives.

### 4.3 Selected-incidence forcing

For selected ui->w and every F-neighbour j of i, the forced cross edge from the standard injection is residual: if it were selected, its endpoints would jointly miss an A-vertex, impossible for a selected edge whose unique exception lies in B. The injections are collision-free because distinct selected labels at a source have distinct supplements.

Hence

```text
d_i<=rho_u+R_i,
s_i<=rho_u
```

at every selected incidence.

**Verdict:** survives.

### 4.4 Residual activity

Assume rho_u=0 and put U=N_A(u), T=A\U. Then F(U,T) is empty. F[U] ordered endpoints inject into two residual cross-edge families, while F[T] edges inject into a disjoint residual family with A-endpoint in T. Therefore

```text
r>=2e(F[U])+e(F[T])>=e(F)=r+t,
```

contradicting t>0.

The collision and possible-hidden-selected-edge cases were rechecked explicitly.

**Verdict:** survives.

## 5. Threshold-capacity lemma

For each h, heavy selected arcs from a source with more than h heavy labels have supplements inside Z_h. One selected orientation per missing unordered B-pair therefore bounds the heavy arcs from the high-load source set J by the number of unordered Z_h-pairs incident with J.

The key algebra was independently checked over all finite integer parameter values in scope:

```text
[h z + C(z-h,2)]
 - [(z-j)h + jz - j(j+1)/2]
 = (z-h-j)(z-h-j-1)/2 >= 0.
```

The separate exact audit checked 1,472 integer (h,z,j) parameter combinations with zero failures.

Thus

```text
2W_h <= z_h^2-z_h+h(h+1)
```

survives the hostile rederivation.

**Verdict:** survives.

## 6. Hand threshold-tail lemma

This was attacked both algebraically and by a separately specified exhaustive program that imports no project verifier.

### 6.1 Full domain

Every nondecreasing 12-tuple

```text
0<=s_1<=...<=s_12<=11
```

was enumerated independently. Results:

```text
total multisets:          1,352,078
threshold-compatible:     1,352,011
threshold-incompatible:          67
max Q(s):                         18
number of maximisers:              4
```

The four maximisers are exactly

```text
(2,3^11),
(3^12),
(3,4^11),
(4^12).
```

### 6.2 Clipping monotonicity

The red-team checker tested the clipping maps globally, not merely at the manuscript's exceptional endpoints:

```text
>6 -> 6 : 1,352,011 compatible source states, 0 counterexamples
 6 -> 5 :    18,564 compatible source states, 0 counterexamples
 5 -> 4 :     6,188 compatible source states, 0 counterexamples
 4 -> 3 :     1,820 compatible source states, 0 counterexamples
```

Thus every clipping direction used by the hand proof is correct over its full compatible stage domain.

### 6.3 Final two-level inequalities

The three polynomial ranges in y were checked independently. Their signs are correct at every integer point in the stated ranges.

**Verdict:** survives strongly.

## 7. Delta=17 and Delta=18..27

For Delta=17, the exact pointwise maximum of

```text
s(12-2s)/(11-s),  0<=s<=10 integer,
```

is 16/7, uniquely at s=4. Eleven labels therefore contribute at most 176/7<29, while the bridge requires 29 already at m=210.

For Delta=18,...,27, the h-index scalar contradiction was recomputed at m=210. In every case

```text
b+2t > floor((a+1)^2/4).
```

The margins are large; increasing m only strengthens the contradiction.

**Verdict:** survives.

## 8. Exact audit workflow

The separately specified audit is

```text
independent_exact_redteam.py
```

and imports no project verifier. GitHub Actions run

```text
34621982241
```

completed successfully. Its artifact records exact integer/rational arithmetic only, no solver and no floating point.

## 9. Package/PDF inspection

The published reviewer-v4 package was downloaded from the successful package workflow and rendered page-by-page.

```text
manuscript:              19 pages
verification companion:  4 pages
```

PDF preflight found both files openable, unencrypted and text-based. Full-page render contact sheets showed no clipping, overlap, black boxes or broken page geometry.

Three non-blocking reviewer-facing weaknesses were identified:

1. **Compressed 4->3 endpoint presentation.** The main manuscript says that the small cases were checked but does not print the tiny table. The detailed hand-proof source does give the drop sequence. Recommendation: include it in the main proof.
2. **Parameterisation is implicit above Delta=16.** The Delta=17 and h-index branches correctly reuse the general bridge, but the reviewer proof should explicitly state `b=Delta`, `a=28-b`, `t=m-b(29-b)` before those branches.
3. **Typesetting/epistemic wording.** Several prose quantities appear as programmer-style `N_h`, `g_h`, `<=` rather than inline mathematics, and phrases such as "independent exact regressions" could be read as external independence. Prefer "separately implemented internal exact regressions".

These are presentation/self-containedness issues, not discovered mathematical defects.

## 10. Remaining risk

The current proof is substantially less correlated with implementation than reviewer-v3. The remaining genuinely high-value independent targets are now:

1. complement-D2C / total-domination quasi-edge correspondence;
2. selected/residual injection and residual activity;
3. threshold-capacity combinatorics;
4. the hand clipping proof;
5. the Delta=15 witness-capacity argument.

The scalar arithmetic is no longer the main risk.

## 11. Overall assessment

Reviewer-v4 survived this hostile pass without a fatal implication failure. In particular, the new hand Delta=16 route is consistent with:

- a fresh first-principles bridge audit;
- a full independently specified 1,352,078-multiset threshold-tail check;
- global clipping monotonicity sweeps;
- exact threshold-capacity algebra;
- independent witness-budget arithmetic;
- exact Delta=17 and h-index arithmetic;
- the published dominating-edge theorem.

**Candidate status is unchanged.** Independent expert mathematical review is still required before theorem-level acceptance.
