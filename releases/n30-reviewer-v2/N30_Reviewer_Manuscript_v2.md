---
title: "Murty-Simon at n=30: Fan-free candidate proof"
subtitle: "Reviewer edition 2 - hostile-audited dependency replacement"
author: "Paul Lenz research project; mathematical development and drafting with ChatGPT/Geeps"
date: "9 September 2026"
documentclass: article
fontsize: 11pt
geometry: [a4paper, margin=25mm]
colorlinks: true
linkcolor: "black"
urlcolor: "blue"
---

\begin{abstract}
This reviewer edition replaces the historical use of G. Fan's 1987 upper-density theorem by a direct order-specific exclusion of every larger edge count. Fan remains cited for attribution. The historical reviewer-v1 proof surface is preserved unchanged. The Fan-free assembly has passed an internal hostile coverage/integrity audit; independent mathematical and computational review remain open.
\end{abstract}

**Canonical claim.** `e(G) <= 225, equality exactly K(15,15)`.

**Logical source.** `project/reviews/n30/2026-09-09-fan-free-v2/PROOF.md`.

---

# Murty–Simon at n=30: Fan-free complete candidate proof, edition 2

9 September 2026. Fan-free edition 2, built from the frozen candidate proof. Research directed by Paul Lenz; mathematical development, implementation and internal audit by ChatGPT/Geeps.

**Status: complete candidate proof. Independent expert mathematical review, external computational reproduction and novelty assessment remain OPEN. Fan's 1987 theorem is cited historically but is not a logical dependency of this edition. Frozen source SHA-256: `6a03ea7ce46d8f7e26921fcb03e2bcf58005d628b9763e481b647d10768be7da`. Fan-free upper-range component: `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md`.** This is not a proof of the unrestricted Murty–Simon conjecture.

## 1. Candidate statement

Let `G` be a finite simple diameter-two edge-critical graph on 30 vertices. The candidate statement is

```text
e(G) <= 225 = floor(30^2/4),
```

with equality if and only if

```text
G ~= K(15,15).
```

Deleting an edge is understood to increase the diameter, with disconnected pairs assigned infinite distance.

## 2. Fan-free upper reduction

Historically, edition 1 used G. Fan's 1987 strict density estimate to reduce a possible counterexample to `m=226`. Fan remains cited for attribution, but **his theorem is not a logical dependency of edition 2**.

The replacement is `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md`. It directly excludes every `m>=227`: degree sum forces `Delta>=16`; exact trusted-kernel calculations cover `Delta=16` through its degree-sum ceiling `m=240`; a complete explicit early-kernel scan covers `Delta=17,m=227..255`; for `Delta=18..28` the charging domain was already empty at the lower dense scopes and only becomes harder as `t` increases; and `Delta=29` is the star case. Hence any upper-bound counterexample has exactly `m=226`, which is excluded below. Equality at `m=225` is treated separately.

The historical Fan-based proof remains preserved at `project/reviews/n30/2026-09-09-candidate-v1/PROOF.md`.

A bipartite diameter-two graph is complete bipartite: a missing cross-part pair would have odd distance at least three. Hence any bipartite graph in the class has at most 225 edges, and equality on 30 vertices forces `K(15,15)`.

It remains to treat non-bipartite graphs at `m=226` and `m=225`.

## 3. Degree entry points

At `m=226`, the degree sum is 452, so

```text
Delta >= 16.
```

At `m=225`, the degree sum is 450, so

```text
Delta >= 15.
```

A universal vertex (`Delta=29`) forces an edge-critical graph to be a star: any edge among the remaining vertices could otherwise be deleted while every pair remained within distance two. Thus `Delta=29` is sparse.

The proof now separates the degree values `15`, `16`, `17`, and `18,...,28`.

## 4. Equality degree Delta=15

This degree occurs only at `m=225`, because `30*15/2=225`. Thus every vertex is degree 15.

Assume first that `G` is non-bipartite. At this density, the published dominating-edge result of Dailly, Foucaud and Hansberg used elsewhere in the project excludes a dominating edge (their non-bipartite dominating-edge upper bound is below 225, apart from the order-six exception).

Every critical edge has a direct or two-step witness. Briefly: delete a critical edge `xy` and choose a pair whose distance becomes greater than two. In the original graph, every path of length at most two between that pair uses `xy`. If the witness pair is adjacent it is a direct witness with no common neighbour; if nonadjacent it has exactly one common neighbour and its unique two-edge path uses `xy`.

For either witness type in a 30-vertex graph with no dominating edge,

```text
d(u)+d(v) <= 29.
```

For a two-step witness, the two neighbourhoods have intersection one and their union lies among the other 28 vertices, giving degree sum at most 29. For a direct witness, the neighbourhoods are disjoint; degree sum 30 would make their union all vertices and the witness edge dominating.

But in a 15-regular graph every pair has degree sum 30. Hence no witness can exist, contradicting edge-criticality.

Therefore the `Delta=15, m=225` graph cannot be non-bipartite. The bipartite observation from Section 2 then forces

```text
G = K(15,15).
```

Conversely, `K(15,15)` is diameter-two edge-critical: deleting a cross edge makes its endpoints distance three.

Thus the equality graph is uniquely determined once the `Delta>=16` equality scopes are excluded.

## 5. Common graph-to-demand bridge for Delta=16 and 17

For the remaining dense scopes put `H=complement(G)`, choose a minimum-degree vertex `v` in `H`, and set

```text
A=N_H(v),
B=V(H)\N_H[v],
a=|A|=n-1-Delta,
b=|B|=Delta.
```

Let `C=H[A]`, `F=complement(C)` on `A`, and define the selected/residual cross-edge system as follows.

For every missing unordered pair `uw` of `H[B]`, adding `uw` corresponds to deleting a critical G-edge. The enlarged complement acquires a new adjacent total-dominating pair. It cannot be `{u,w}`, because both miss `v`; therefore, after interchanging `u,w` if necessary, there is an existing cross-edge `ui` with `i in A` such that

```text
N_H(u) union N_H(i) = V(H)\{w}.
```

Write `ui -> w`. Selection is indexed by missing **unordered** B-pairs: designate exactly one such cross-edge for each unordered pair, never one per orientation, and call all other existing A-B edges residual. The source and unique exception recover the missing unordered B-pair, so the selected assignment is injective and opposite orientations cannot collide.

Let `rho_u,R_i` be residual row/column degrees, `r=sum rho=sum R`, `d_i=deg_F(i)`, and

```text
s_i=max(0,d_i-R_i),
S=sum_i s_i,
t=m-b(n-b).
```

The exact ledger and minimum-complement-degree condition give

```text
e(F)=r+t,
S>=r+2t.
```

For `t>0`, every B-source is residual-active: `rho_u>=1`.

For a selected source of label `i`, the selected-edge forcing gives

```text
s_i <= rho_u.
```

Charging chosen selected incidences then yields the universal necessary inequality

```text
r-b >= sum_i s_i(s_i-1)/(a-s_i),
```

and hence

```text
sum_i s_i(a+1-2s_i)/(a-s_i) >= b+2t.     (5.1)
```

For thresholds `h>=1`, define

```text
I_h={i:s_i>=h},
W_h=sum_{i in I_h}s_i,
Z_h={u:rho_u>=h},
z_h=|Z_h|.
```

The exact source/supplement capacity argument gives

```text
2W_h <= z_h^2-z_h+h(h+1).                (5.2)
```

The complete standalone derivations are preserved in the n=29 bridge package, especially `GRAPH_TO_MODEL_BRIDGE.md` and `THRESHOLD_CAPACITY_LEMMA.md`. The n=30 parameterization audits check that no n=29-specific constant is retained when these statements are instantiated below.

## 6. Delta=17 closes before residual-row enumeration

Here

```text
a=12,
b=17.
```

The two dense scopes have

```text
m=226 -> t=5,
m=225 -> t=4.
```

### 6.1 m=226

Complete enumeration of the nondecreasing integer demand profiles satisfying (5.1) gives exactly 250 profiles.

For each profile, charging gives an exact upper bound `rmax`. Residual activity then implies

```text
z_h <= floor((rmax-b)/(h-1))
```

for `h>=2`. Substitution into (5.2) rejects every one of the 250 profiles by exact integer arithmetic. The smallest strict threshold margin is 2.

Thus `Delta=17, m=226` is impossible.

### 6.2 m=225

The complete charging domain has 1,155 profiles.

Exact threshold/source-count inequalities reject

```text
1,070 by threshold capacity,
   67 by source count,
```

leaving 18 profiles.

For the `k` largest demands, let `D_k` be their total. A residual-degree-j source has at most `a-j` selected slots and can serve only demands at most `j`, so its contribution to that prefix is at most

```text
A[k,j]=min(a-j, #{top-k labels with demand<=j}).
```

Every graph-realizable source-count vector `n_j` satisfies

```text
D_k <= sum_j A[k,j] n_j,
sum_j n_j = 17,
sum_j (j-1)n_j <= rmax-17.
```

All 18 remaining profiles have exact integer dual contradictions to this necessary Hall system. The weakest exact dual margin is 3.

The clean replay `34292054922` completed successfully: the complete demand frontier was regenerated, the same 18 post-threshold profiles were recovered, and both regenerated and committed dual certificates were verified by a standard-library exact checker.

Hence `Delta=17, m=225` is impossible.

## 7. Delta=16: parameterized trusted kernel

Here

```text
a=13,
b=16,
```

and

```text
m=226 -> t=2,
m=225 -> t=1.
```

Both have `t>0`, so residual activity applies.

### 7.1 Isolated-C exclusion

The parameteric isolated-`C` lemma says that if `C=H[A]` has an isolated vertex then necessarily

```text
b <= a-1-t.                              (7.1)
```

Its expanded proof is preserved as `ISOLATED_C_PARAMETERIC_LEMMA.md` in the n=30 reconnaissance directory. At `(a,b)=(13,16)`, (7.1) would require

```text
16<=10  at t=2,
16<=11  at t=1,
```

both impossible. Therefore

```text
delta(C)>=1,
d_i<=11,
e(C)>=7.
```

Using `e(C)+r=C(13,2)-t`, the safe residual-total bounds are

```text
r<=69 at m=226,
r<=70 at m=225.
```

No order-specific graph lemma beyond the parameterized bridge is added.

### 7.2 Demand preparation and residual rows

The exact strengthened preparation uses only charging, residual activity, (7.1), threshold capacity, and exact source-capacity Hall dual lower bounds on `r`.

At `m=226`:

```text
48,046 charging-domain profiles
 -> 2,590 retained demand profiles.
```

At `m=225`:

```text
67,050 charging-domain profiles
 -> 5,379 retained demand profiles.
```

The clean residual-row scanner enumerates every sorted length-16 residual row in the certified total interval and uses only necessary largest-demand-prefix Hall bounds and monotone supplement-cap refinement.

Clean workflow run `34286806474` gives:

| m | raw residual states | initial Hall rejects | refinement rejects | row survivors |
|---:|---:|---:|---:|---:|
| 226 | 50,690,620 | 50,561,364 | 93,726 | 35,530 |
| 225 | 158,314,695 | 157,894,303 | 269,496 | 150,896 |

These are arithmetic necessary-condition states, not graphs.

### 7.3 Exact row-threshold screen

Once a concrete residual row is known, (5.2) can use the exact value

```text
z_h=|{u:rho_u>=h}|.
```

The exact row-threshold workflow `34287440190` reduces the frontiers to

```text
m=226: 9 rows,
m=225: 272 rows.
```

### 7.4 Fresh corrected cumulative-threshold/source-flow model

The remaining 281 rows are tested by a fresh n=30 implementation specialized directly to `(a,b)=(13,16)`. It does not import the historical n=29 threshold builders.

The grouped normalization uses the corrected per-label identity

```text
sum_k n_k Z = sum_h T_h,
```

with no extra label-group multiplicity. The same-group ordered-pair capacity is deliberately relaxed, not strengthened, so it can create false survivors but not false exclusions.

A numerical LP result is never itself an exclusion. HiGHS is used only to propose a Farkas ray; integer multipliers are then reconstructed and accepted only if direct exact arithmetic verifies coefficientwise nonnegativity and a strictly negative combined right-hand side.

Clean final workflow `34287739057` completed both jobs successfully:

```text
m=226: 9/9 exact Farkas rejections, zero survivors,
m=225: 272/272 exact Farkas rejections, zero survivors.
```

Thus both `Delta=16` dense scopes are impossible within the audited bridge framework.

## 8. Delta=18,...,28

For every `Delta=18,...,28` at both `m=225` and `m=226`, instantiate (5.1) with

```text
a=29-Delta,
b=Delta,
t=m-Delta(30-Delta).
```

The complete nondecreasing integer demand domain is empty in every scope: there is no profile `0<=s_i<=a-1` satisfying the charging inequality.

This is reproduced by the standard-library checker `check_outer.py` in this candidate directory.

Hence every `Delta=18,...,28` scope is impossible. `Delta=29` is the universal-vertex/star case already excluded as sparse.

## 9. Assembly

At `m=226`:

- `Delta<=15` is impossible by degree sum;
- `Delta=16` is excluded by the parameterized trusted kernel;
- `Delta=17` is excluded by threshold capacity;
- `Delta=18,...,28` are excluded by charging;
- `Delta=29` gives a star.

The Fan-free upper-range reduction already excludes every `m>=227`. Since the 226-edge scope has now also been excluded,

```text
e(G)<=225.
```

At `m=225`:

- `Delta<=14` is impossible by degree sum;
- `Delta=15` forces the unique equality graph `K(15,15)`;
- `Delta=16` is excluded by the parameterized trusted kernel;
- `Delta=17` is excluded by threshold/source-count plus 18 exact Hall duals;
- `Delta=18,...,28` are excluded by charging;
- `Delta=29` gives a star.

Thus the complete candidate statement is

```text
e(G)<=225,
with equality exactly K(15,15).
```

## 10. Trust boundary

This remains a candidate theorem. The principal remaining risk is the correctness of the universal graph-to-demand bridge, not the arithmetic replay.

Highest-value external review targets are:

1. complement/quasi-edge construction and selected-edge injection;
2. residual activity for `t>0`;
3. selected-source demand `s_i<=rho_u`;
4. charging inequality;
5. threshold-capacity lemma;
6. the parameteric isolated-`C` lemma;
7. the n=30 Delta=16 grouped LP normalization and graph-to-relaxation embedding;
8. exact Farkas checker semantics;
9. the use and exact hypotheses of the cited published dominating-edge reduction. Fan is historical attribution only in edition 2.

Any counterexample to a universal bridge lemma overrides every green workflow.