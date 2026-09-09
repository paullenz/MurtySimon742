---
title: "Murty-Simon at n=27 - verification companion"
subtitle: "Reviewer edition 2 - Fan-free reduction, audit and history"
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
This companion records the Fan-free upper-range replacement, exact computational provenance, semantic clarifications prompted by external-AI feedback, and the preserved proof history. It does not convert same-assistant checking into external review.
\end{abstract}

**Claim under review.** `e(G) <= 182, equality exactly K(13,14)`.

**Historical reviewer-v1 package.** `releases/n27-reviewer-v1/README.md` remains preserved.

---


\newpage

# Included source: `project/reviews/n27/2026-09-09-fan-free-v2/HISTORY.md`

# n=27 proof history for Fan-free edition 2

The canonical historical v1 proof remains unchanged at
`project/reviews/n27/2026-09-07-candidate-v1/PROOF.md`.

Its SHA-256 at v2 build time is `97586723a7f85a0d6351e84ebfbeccdf2cb0a2817cb7977599190194779881b1`.

Edition 2 changes only:

1. Fan's 1987 theorem is moved from logical dependency to historical attribution and replaced by `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md`;
2. the selected-edge convention explicitly designates exactly one representative per missing unordered B-pair;
3. the Section 5 forced cross-edge is explicitly shown non-selected before being counted residual;
4. Equation (10.1)'s unordered-pair injection explicitly rules out reverse-orientation collisions;
5. the final assembly sentence points to the Fan-free reduction.

The 8 September red-team report and the later cross-cutting feedback audit remain preserved separately. No frozen v1 evidence, source, hash or theorem ledger entry is overwritten.


\newpage

# Included source: `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md`

# Fan-free upper-range reduction for the n=25 and n=27 candidate proofs

9 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate fixed-order proof component with exact finite arithmetic. Independent mathematical and computational review remains OPEN.**

## 1. Purpose and historical relation to Fan

The original n=25 and n=27 candidate manuscripts use G. Fan's 1987 theorem

> G. Fan, *On diameter 2-critical graphs*, Discrete Mathematics 67 (1987), 235-240, DOI 10.1016/0012-365X(87)90174-9,

as a convenient published reduction showing that only 157 edges at n=25 and 183 edges at n=27 need be examined above the conjectured extremal values.

This note removes **Fan's theorem as a logical dependency** of those two fixed-order candidate proofs. It does **not** claim to reproduce Fan's stronger all-order theorem. Instead it proves directly, using the project's already stated witness/quasi-edge/residual lemmas, that every edge count *above* the old Fan caps is impossible at these two orders.

The original Fan-based manuscripts remain frozen and preserved as historical versions. The reviewer-facing v2 assembly should cite Fan for attribution/history, but should use the argument below as the logical upper-range reduction.

## 2. Common ingredients

No new graph-theoretic hypothesis is introduced here. The finite verifier uses only necessary conditions already proved in the fixed-order manuscripts:

1. the complement/quasi-edge setup and the convention choosing **exactly one selected cross-edge for each missing unordered pair in B**;
2. the residual ledger

   ```text
   e(C)+r=L,
   e(F)=r+t,
   sum d_i = 2(r+t),
   sum rho_b = r;
   ```

3. residual activity `rho_b >= 1`, hence `r >= b`, whenever `t>0`;
4. the small-k necessary inequalities;
5. the selected-pair threshold inequality

   ```text
   ell_j <= #{ unordered {b,w} : rho_b+rho_w >= j };
   ```

6. source-cap and source-threshold upper bounds;
7. the residual-column h-index lower bound;
8. where necessary, the fixed residual-column source-cap refinement and strict subset-capacity inequality.

The enumeration deliberately retains nongraphical degree multisets. Therefore eliminating the enumerated relaxation is safe: every actual graph satisfying the bridge would appear in it, while many impossible numerical states are intentionally retained.

The selected-pair convention is important. Selection is indexed by the missing **unordered** B-pairs: one representative quasi-edge is chosen for each such pair. Opposite orientations of the same B-pair can never both be selected. Likewise, whenever the residual-injection proof forces an A-B edge whose two endpoints both miss an A-vertex, that edge cannot be selected for a B-B missing pair, because the unique exception of a selected edge belongs to B. These points are semantic consequences of the construction, not extra assumptions.

## 3. n=25 without Fan

Let `m=e(G)`.

### 3.1 Degree ranges outside Delta=14,15,16

If `Delta <= 12`, then the degree sum gives

```text
2m <= 25*12 = 300,
```

so `m <= 150`.

If `Delta >= 17`, the independent complement maximum-degree theorem already used in the frozen manuscript gives `m <= 155`; this step never depended on Fan.

For `Delta=13`, the witness-deficit inequality from Section 3 of the frozen n=25 proof is

```text
m <= C(h,2) + h(25-h) + o(o-1),
2h+o <= T := 325-2m.
```

For fixed `h`, the right-hand side is nondecreasing in the allowed integer `o>=0`. Hence, as `m` increases, `T` decreases and the witness upper bound cannot increase. The complete table at `m=157` already lies strictly below 157. Therefore the same argument excludes every `m>=157` at `Delta=13`.

Thus any graph with `m>=157` has `Delta in {14,15,16}`.

### 3.2 The edge count 157

The frozen n=25 candidate proof already excludes `m=157` in each of `Delta=14,15,16` by the residual finite argument. That part of the proof is retained unchanged.

### 3.3 Every larger edge count

For `m>=158`, the degree sum leaves only the finite ranges

```text
Delta=14: 158 <= m <= floor(25*14/2) = 175,
Delta=15: 158 <= m <= floor(25*15/2) = 187,
Delta=16: 158 <= m <= floor(25*16/2) = 200.
```

The exact Fan-free outer verifier scans **every integer edge count in all three ranges**. Its aggregate results are

| Delta | edge counts scanned | outer states | states surviving all outer necessary conditions |
|---:|---:|---:|---:|
| 14 | 158..175 | 128,666 | 0 |
| 15 | 158..187 | 88 | 0 |
| 16 | 158..200 | 0 | 0 |

Thus no graph with `m>=158` survives the necessary-condition relaxation.

Combining Sections 3.1-3.3 with the frozen exclusion of 157 gives, without Fan,

```text
e(G) <= 156.
```

The frozen equality argument at 156 is unchanged and forces `K(12,13)`.

## 4. n=27 without Fan

Again write `m=e(G)`.

### 4.1 Degree ranges outside Delta=15,16,17

If `Delta <= 13`, the degree sum gives

```text
2m <= 27*13 = 351,
```

hence `m <= 175`.

If `Delta >= 18`, the independent complement maximum-degree theorem already used in the frozen n=27 manuscript gives `m <= 181`; this step is independent of Fan.

For `Delta=14`, the witness-deficit inequality from Section 3 of the frozen n=27 proof is

```text
m <= C(h,2) + h(27-h) + o(o-1),
2h+o <= T := 378-2m.
```

As above, for fixed `h` the right-hand side is nondecreasing in `o`, while `T` decreases as `m` increases. The complete table at `m=183` lies strictly below 183, so the same witness argument excludes every `m>=183` at `Delta=14`.

Thus an above-target graph can only have `Delta in {15,16,17}`.

### 4.2 The edge count 183

The frozen n=27 candidate proof already excludes `m=183` for `Delta=15,16,17`. That proof component is retained unchanged.

### 4.3 Delta=16 and Delta=17 above 183

The Fan-free outer verifier scans every larger degree-sum-possible edge count:

| Delta | edge counts scanned | outer states | outer survivors |
|---:|---:|---:|---:|
| 16 | 184..216 | 8,880 | 0 |
| 17 | 184..229 | 0 | 0 |

Hence no larger graph occurs in these two degree bands.

### 4.4 Delta=15 above 183

For `Delta=15`, every integer `m=184,...,202` was scanned. The complete outer scan contains 2,858,079 states. Only 661 survive the outer necessary conditions:

```text
m=184: 772,670 outer states, 651 survivors;
m=185: 579,204 outer states, 10 survivors;
m>=186: zero outer survivors at every edge count through 202.
```

The 661 retained states were then passed through the same canonical residual-column and subset-capacity machinery used in the frozen n=27 proof.

At `m=184`:

```text
outer survivors:             651
canonical residual columns:  49,073
labelled orbit mass:          1,175,094
columns reaching subset flow:1
final column survivors:       0
```

At `m=185`:

```text
outer survivors:             10
canonical residual columns:  388
labelled orbit mass:          10,036
columns reaching subset flow:0
final column survivors:       0
```

The scan and replay modes agree exactly on the state count, canonical-column count, labelled orbit mass, survivor count and ordered per-column SHA-256 digest:

```text
m=184: 89e4e1d033ef0edd98aa557cb6df8d5fd2eea145b036c8604d0ac66c44f364be
m=185: 162403cef4b12375be6c442c91471fdd63aea9a2d3d04412ecc99f6ee723391f
```

The replay mode does not invoke max flow: it rederives the source caps and directly checks each recorded strict subset inequality.

Therefore every `m>=184` is impossible at `Delta=15`.

Combining Sections 4.1-4.4 with the frozen exclusion of 183 yields, without Fan,

```text
e(G) <= 182.
```

The frozen equality argument at 182 remains unchanged and forces `K(13,14)`.

## 5. Computational provenance

Primary Fan-free upper-range workflow:

```text
Fan-free n25/n27 upper-range scan
run 34393554788
head commit efe189ad911a3968e5b7d63a3de43a05c664bfb2
```

The six artifacts and their workflow-recorded SHA-256 digests are:

```text
fan-free-25-14  3f2e38c5d6cdf4895a77e3c9aaf2980ff2899a8565019af265264a7c18d9deb9
fan-free-25-15  17087194b6cb13720051e335847eb0c4819bdb171d4ece4f234ba3c776f32fba
fan-free-25-16  4e3c28d2a93798e8e307cffad14a0c02ab41b78f25e263481d8b9d20576e7c62
fan-free-27-15  03fbb10af9505fc4115a874cdba975e74eb8a8a5dbc5348c63919cf845aadf21
fan-free-27-16  96544a8f570cb54780e6496fac0411a035efc94e894e7abc4533d054f6d43178
fan-free-27-17  2130aca03ca9738531800698b6b5dfe34e30ff7e46c7a0f66d9b5dbc69b8f179
```

The only nonzero outer frontier, `n=27, Delta=15, m=184,185`, was closed by:

```text
Fan-free n27 delta15 column closure
run 34393710385
head commit 7cc1971604efdf8fea5ec11bbc3b8826868c55ff
```

Artifacts:

```text
fan-free-n27-d15-184  3cb20da5f70ece0990f665e4f6a35e13b5baaabdeb9b61cf37009af534ec63ac
fan-free-n27-d15-185  b9c2086cbc15f97ef61b494df340aaf9d04e543a123dfdd716d0c23ec76dbaa2
```

The source `fan_free_outer.cpp` is a count-only extraction of the already published fixed-order outer necessary conditions. The `m=184,185` closure deliberately reuses the frozen `survey.cpp` and `columns.cpp`, with `columns check` providing a second algorithmic route for the strict subset acceptance layer. All arithmetic is integer arithmetic.

## 6. Trust boundary and status

This removes Fan's 1987 theorem as a logical dependency of the **n=25 and n=27 fixed-order candidate proofs**. Fan remains cited because his theorem historically supplied the original reduction and is stronger than the order-specific replacement proved here.

This change does not remove the other published dependencies already disclosed in the fixed-order manuscripts, in particular the complement/total-domination reductions. Nor does it convert same-assistant computation into external review. The graph-to-residual lemmas remain hand mathematics and are still the main trust boundary.

The old Fan-based manuscripts, evidence packages and hashes remain preserved. Reviewer-facing v2 materials should identify this document as the replacement for the original Fan reduction and link the old versions as historical provenance.


\newpage

# Included source: `project/reviews/cross-cutting/2026-09-09-external-ai-feedback-audit-v1/REPORT.md`

# External-AI feedback audit: n=27 pair injection, residual injection, and Fan dependency

9 September 2026. Requested by Paul Lenz. Assessment performed by ChatGPT/Geeps. Same-assistant assessment is not external mathematical review.

**Disposition:** no blocking defect identified in the three allegations. Allegations 1 and 2 conflict with explicit definitions/arguments already present in the frozen n=27 proof and its 8 September hostile re-audit. Allegation 3 is a legitimate literature-provenance question, but the theorem statement used by the project matches the publisher/secondary literature checked here. Fan's full six-page proof has still not been independently re-proved by this project.

## Allegation 1: reverse-orientation collision in the unordered-pair injection

The criticism proposes two selected edges

```text
b1 i1 -> w1,
w1 i2 -> b1,
```

which would be distinct cross-edges but map to the same unordered B-pair `{b1,w1}`.

This configuration is **not permitted for two selected edges under the project's selection convention**.

Section 4 of the frozen n=27 proof does not designate every available quasi-edge as selected. Instead:

> for each missing unordered pair `bw` in `H[B]`, choose **one** cross-edge `bi -> w` (after interchanging the pair endpoints if necessary); call these chosen edges selected, and call every other A-B edge residual.

Thus selection is indexed by the missing **unordered** B-pairs. Exactly one cross-edge is chosen for each such pair. If both orientations/quasi-edges happen to exist in the graph, at most one is designated selected for `{b,w}`; the other is not selected.

Moreover, a selected cross-edge `bi -> w` recovers its indexing missing pair uniquely from its B-source `b` and its unique B-exception `w`. Hence the map

```text
selected edge  ->  {source, exception}
```

is injective by construction. Reverse orientation would correspond to the same indexing missing pair and cannot be a second selected edge.

This is exactly the point recorded in the 8 September n=27 red-team report: the quasi-edge selection chooses one cross-edge per missing unordered B-pair, and "one cannot silently allow both orientations of the same pair."

Therefore Equation (10.1) is not invalidated by the proposed directional collision. Its right side actually counts all unordered B-pairs satisfying the residual-sum threshold, not merely missing B-pairs, so it is an intentionally relaxed upper bound on the available selected-pair slots.

**Disposition: NOT A DEFECT.**

## Allegation 2: selected/residual double counting in Section 5

The criticism targets the Section 5 construction. If `ij` is an F-edge inside `S` and `bi -> w_i` is selected, the proof forces the cross-edge `j w_i` and declares it residual. The concern is that `j w_i` might itself be selected for some other missing B-B pair.

The residual conclusion is valid.

Because `ij` is an F-edge, `j` misses the A-vertex `i` in H. Because `bi -> w_i` has exception `w_i`, the edge `i w_i` is absent, so `w_i` also misses the same A-vertex `i`. Hence the endpoints of `j w_i` both fail to dominate `i`.

If `j w_i` were a selected edge for a missing B-B pair, its source would be the B-endpoint `w_i` and its unique selected exception would necessarily be another B-vertex. A selected edge must dominate every vertex except that B-exception. But `j` and `w_i` both miss the A-vertex `i`, a second non-dominated vertex which cannot be the selected B-exception. Contradiction.

Thus `j w_i` cannot be selected under the Section 4 convention. Since selected and residual A-B edges are disjoint by definition and all non-selected A-B edges are residual, `j w_i` is genuinely residual and cannot be counted in both `Q` and `r`.

The same reasoning is explicitly recorded in the 8 September n=27 red-team report: a forced cross-edge cannot itself be selected because both endpoints miss an A-vertex while the exception of a selected cross-edge belongs to B.

The analogous residual-activity argument in the n=25 proof uses the same convention and the same exclusion.

**Disposition: NOT A DEFECT.**

## Allegation 3: unaudited Fan dependency

This is the only allegation that identifies a real *trust boundary*, though not a discovered mathematical mismatch.

Both the n=25 and n=27 proofs use Fan's 1987 global numerical bound to restrict the above-target search to 157 and 183 edges respectively. The project has not independently re-proved Fan's six-page theorem.

However, the hypothesis used by the project matches the literature checked here:

1. Fan's publisher abstract defines a diameter-2-critical graph exactly as a graph of diameter 2 for which deleting any edge increases the diameter, and states its theorem for a diameter-2-critical graph on `n` vertices.
2. Tao Wang, *On Murty-Simon Conjecture* (2012), page 2, explicitly states that Fan proved

```text
|E(G)| < n^2/4 + (n^2 - 16.2 n + 56)/320
```

for `n >= 25`, in the context of an arbitrary diameter-2 edge-critical graph `G`.
3. Haynes, Henning and Yeo, *On a conjecture of Murty and Simon on diameter two critical graphs II*, Discrete Mathematics 312 (2012), likewise states the same bound for `n >= 25` without an extra maximum-degree, connectivity, bipartiteness, or other structural hypothesis.

I found no literature evidence for the suggested hidden preconditions. The n=25 and n=27 uses therefore match the published theorem statement as it is consistently reported.

The distinction should remain explicit:

- **theorem-statement/hypothesis match:** checked and currently supported;
- **independent re-proof of Fan's argument:** not done.

For journal-level hygiene it would still be worthwhile to archive/read the complete primary Fan paper and record a one-page hypothesis audit, but failure to re-prove a standard cited theorem is not itself a gap in a mathematical paper. If a genuine error in Fan's theorem were ever established, the current finite searches would indeed need their upper edge ranges widened; no such error is presently evidenced.

A minor robustness point: whether the displayed Fan inequality is printed as strict or non-strict would not affect the integral caps at n=25 or n=27, because the numerical right sides lie strictly between 157 and 158, and between 183 and 184, respectively.

**Disposition: VALID PROVENANCE/TRUST-BOUNDARY QUESTION; NO HYPOTHESIS MISMATCH FOUND.**

## Overall assessment

| Allegation | Assessment | Effect on current candidate status |
|---|---|---|
| reverse unordered-pair collision in (10.1) | ruled out by one-selected-edge-per-missing-unordered-pair convention | none |
| selected/residual double count in Section 5 | ruled out because forced edge misses an A-vertex and therefore cannot be selected for a B-B exception | none |
| Fan hidden hypotheses | no mismatch found in checked literature; full primary proof not independently rederived | retain explicit external-theorem trust boundary |

No theorem-ledger or candidate-status change is recommended from this feedback alone. The feedback is nevertheless valuable because it identifies exactly the sort of definitions that should be made visually unmistakable for external reviewers. A future editorial revision should emphasize in Section 4 that "selected" is a designation of exactly one quasi-edge **per missing unordered B-pair**, not a property shared by every possible quasi-edge, and should add the one-sentence contradiction showing why the Section 5 forced edges cannot be selected.

## Sources checked

- Frozen n=27 candidate: `project/reviews/n27/2026-09-07-candidate-v1/PROOF.md`.
- n=27 hostile re-audit: `project/reviews/n27/2026-09-08-redteam-v1/REPORT.md`.
- Frozen n=25 candidate: `project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md`.
- Genghua Fan, *On diameter 2-critical graphs*, Discrete Mathematics 67 (1987), 235-240, DOI 10.1016/0012-365X(87)90174-9.
- Tao Wang, *On Murty-Simon Conjecture*, arXiv:1205.4397 (2012).
- Teresa W. Haynes, Michael A. Henning and Anders Yeo, *On a conjecture of Murty and Simon on diameter two critical graphs II*, Discrete Mathematics 312 (2012), 315-323.


\newpage

# Included source: `project/reviews/n27/2026-09-08-redteam-v1/REPORT.md`

# N=27: red-team audit of the original candidate

8 September 2026. Requested by Paul Lenz. Audit performed by ChatGPT/Geeps, the same assistant responsible for the earlier development. **Independent specialist review remains OPEN.**

## Verdict

**No blocking mathematical defect was found in this internal audit of the original n=27 route.** The upper-bound and equality arguments survive the checks described below. Two real engineering issues were identified and addressed in a separate audit layer: a compression-dependent comparison failure and permissive parsing by the frozen C++ readers. Neither requires changing the graph-theoretic statement or the original evidence. The candidate is not promoted to PROJECT-CERTIFIED, externally accepted, or formally verified.

The statement under review is that a finite simple diameter-two edge-critical graph on 27 vertices has at most 182 edges, with equality exactly for K(13,14). The newer 13/22 and 293/500 general-degree results were deliberately not used to rescue or replace any part of this proof.

## 1. Scope and pinned evidence

The audit baseline is repository commit `7cd8a2ad562d69afe29634d1b888215750cb5e93`. The frozen manuscript is `project/reviews/n27/2026-09-07-candidate-v1/PROOF.md`, Git blob `83e09e02918adf461470bf7e70177bad275b57d9`. The original release archive has 71,778,093 bytes and SHA-256:

`8381ed450859b9efa54fa6ec3c76bda786ec3fc31ec52732637c5346224caf3c`.

The clean-runner workflow reassembles that exact archive, validates safe extraction and ZIP integrity, verifies all 115 manifest payloads, rebuilds the original programs, and repeats the entire original arithmetic. Locally, 108 of those payloads were transferred and hash-checked for source inspection and additional terminal-certificate tests; seven large ledger/column files were processed on the runner rather than represented as locally available. The final remote audit passed on commit `6114d4ec70afa779a3a8335b939c50b6ca5d9e92`, run `34209842203`, job `102007953539`: 59 complete data/source comparisons passed, all 13,596,058 rows in 13 guarded input files passed strict parsing, and all 115 original payloads were available to the final cap audit.

The audit read all thirteen manuscript sections, the distribution/replay instructions, the source and checking programs, domain and certificate records, adaptation notes, validation fixtures, and execution summaries. External results were checked for their stated hypotheses and their application here; this was not a new proof of every theorem in the cited literature. No novelty assessment is claimed.

## 2. External reductions and complete case coverage

Fan's strict inequality, as quoted on page 2 of Wang [1], gives the exact bound 146669/800=183.33625 at n=27. Thus an above-target graph has exactly 183 edges; the 182-edge equality case must and does receive a separate analysis. The proof does not delete arbitrary edges while assuming criticality is preserved.

Theorem 4 of Dailly, Foucaud and Hansberg [2] applies to non-bipartite diameter-two-critical graphs with a dominating edge. Its exception H5 has six vertices, so at n=27 it yields at most 180 edges. Bipartite graphs of diameter two are complete bipartite; a universal vertex forces an edge-critical graph to be a star. These cases are separated before using complement total domination.

For maximum degree at least 18 and no universal vertex, the complement has minimum degree between 1 and 8, hence at most 0.3 times 27. Theorem 3.6(a) of Haynes et al. [3] then gives more than 169 complement edges and at most 181 original edges. I checked a potentially important odd-order issue: the diameter-three result cited inside that theorem's proof has a historical even-order limitation. Wang's Theorem 2.1 explicitly covers odd orders and supplies the strict bound needed here. The n=27 manuscript already includes that dependency; it is not a repair imported from our later general-degree work. The stars excluded by the complement convention are handled directly.

The full partition is therefore:

| Maximum degree | Route at 183 edges | Route at 182 edges |
|---|---|---|
| At most 13 | Degree-sum contradiction | Degree-sum contradiction |
| 14 | Witness/deficit count | Witness equality forces K(13,14) |
| 15 | Complete outer and column certificates | Complete outer and column certificates |
| 16 | Pair-threshold enumeration | Pair-threshold enumeration |
| 17 | Residual activity and small-k bounds | Residual activity and small-k bounds |
| At least 18 | External complement bound; star handled separately | Same |

No maximum-degree interval is omitted. Fan's original 1987 full proof was not independently re-audited; its stated bound and exact substitution were checked through the explicit source in [1].

## 3. The degree-14 equality argument

Every critical edge either has no common neighbour at its endpoints, or lies on the unique length-two path of a nonadjacent pair. In the non-dominating-edge case every such witness pair has degree sum at most 26.

With deficits 14-d(u), let h count deficits at least two and o count deficits exactly one. The degree sum gives 2h+o<=T, where T=378-2m. The bound

`m <= binom(h,2)+h(27-h)+o(o-1)`

is sound: a cross-part witness can cover at most one edge wholly among the non-low vertices, while an O-O witness can cover at most two. Existing cross-part edges are subtracted from the possible cross nonedges, then cancel when edge classes are added. This does not assume a nonexistent one-to-one assignment of all witnesses.

At m=183 the complete h table lies strictly below 183. At m=182 only h=0,o=14 survives. Direct witnesses inside O cover one edge, not two, giving the sharper bound `182 <= 182-e(G[O])`. Hence O is independent. Its fourteen degree-13 vertices must each meet all thirteen remaining vertices; those 182 cross edges exhaust G. This proves the claimed equality structure, not merely an edge bound. Conversely K(13,14) is diameter-two edge-critical: deleting a cross edge makes its endpoints distance three.

## 4. Residual machinery: hypotheses, injections and small k

The quasi-edge selection chooses exactly one cross-edge for each missing unordered B-pair. Its source and unique exception recover that pair, so distinct chosen pairs cannot reuse a selected cross-edge. At a fixed source the supplements are distinct. These facts justify the later unordered-pair injections and supplement forcing; one cannot silently allow both orientations of the same pair.

The ledger was recomputed at both edge counts:

| m | Maximum degree | a | b | L | t=m-b(27-b) |
|---:|---:|---:|---:|---:|---:|
| 183 | 15 | 11 | 15 | 52 | 3 |
| 182 | 15 | 11 | 15 | 53 | 2 |
| 183 | 16 | 10 | 16 | 38 | 7 |
| 182 | 16 | 10 | 16 | 39 | 6 |
| 183 | 17 | 9 | 17 | 23 | 13 |
| 182 | 17 | 9 | 17 | 24 | 12 |

The residual-activity lemma requires t>0. **All six production rows, including equality rows, meet that condition.** I rechecked its disjoint charging families: 2e(F[S]) residual edges have A-endpoints in S, while e(F[T]) have endpoints in T; unique exceptions give injectivity. An inactive source would imply r>=e(F)>=r+t. The argument also handles empty S and does not smuggle in a diameter bound on the complement.

The small-k auxiliary-edge argument produces a family P and b additional residual edges outside P, one distinguished by each B-endpoint. The x-z edges for used endpoints are residual because a selected x-z edge would miss the original exceptional A-vertex. This verifies disjointness rather than just recounting the algebra. At degree 17 all k are excluded. At degree 16 the retained k range is 2..4. At degree 15 it is 1..6: **k=1 is correctly retained**, not incorrectly discarded by a non-strict inequality.

All four selected-edge inequalities in Section 7 were rederived. In particular, the forced cross-edge cannot itself be selected because both its endpoints miss an A-vertex whereas a selected cross-edge's unique exception belongs to B. The residual-column and supplement maps use distinct labels or exceptions exactly where injection is needed.

## 5. Enumeration and source-capacity soundness

The outer domain includes every sorted degree list with the required sum and exact maximum, and every sorted positive residual list with the correct sum. Independent relabellings of A and B justify the two sorts. Nongraphical sequences remain in the relaxation, so the search errs toward retaining impossible states rather than losing real graphs.

Residual columns are sorted **only within equal-degree label blocks**. Permuting labels inside such a block preserves all used predicates. The canonical count is separately checked by recurrence; labelled orbit weights are checked against a generating-function coefficient. Labelled orbit mass is not misrepresented as individual visits to every labelled column.

Source caps are upper bounds obtained from a relaxed matching problem. The search and replay use different matching calculations; trial loads are individually examined, so no unwarranted monotonic-feasibility shortcut is used. Synchronous supplement-cap refinement preserves the invariant actual q<=current cap: every true selected edge needs a distinct supplement with enough possible A-neighbours. Caps are nonnegative and decrease, guaranteeing termination. Subset-flow failures are replaced by explicit strict integer inequalities in the checker, which does not trust the flow solver's verdict.

A residual trust boundary remains: the full C++ column scan and replay share their enumeration routine. Separate domain recurrences, orbit weights, per-state digests and the existing fully labelled six-state cross-language check reduce that risk, but they are not a second independently authored full enumeration. This audit does not claim otherwise.

## 6. Independent reconstruction of all terminal columns

The additional `audit_n27.py` imports no original search or checker. It uses augmenting-path matching and synchronous fixed-point refinement to reconstruct source caps from d, rho and R for **every 35,435 column surviving the subset stage**. All cap vectors agree exactly with the frozen vectors. It then reconstructs the pair and forced-supplement contradictions directly.

| Scope | Terminal columns | Pair contradictions | Supplement contradictions |
|---|---:|---:|---:|
| m=183, degree 15 | 190 | 190 | 0 |
| m=182, degree 15 | 35,245 | 35,241 | 4 |

The ordered audit digest is `d85844f7555b1bbe28a247d97d97a5c5b6222a681ac0de530b067b367bf19a93`. The complete arrays and reconstructed final four certificates are preserved in `evidence/FINAL_SOURCE_CAP_AUDIT.json`.

For those last four columns, eight vertices have residual degree one and source cap zero. Every possible selected source has at least three selected labels: source closure supplies this at residual degree three, and forced labels supply it at the other sources. Each supplement therefore needs at least two A-neighbours; none of the eight zero-cap vertices can serve. Every selected pair lies among seven vertices, giving at most 21 unordered pairs. The four required counts are 39,39,37,37. The contradiction survives source/label relabelling checks. This is a genuine inequality, not an interpretation of four feasible relaxations as actual graphs.

## 7. Complete replay totals

The full original replay, rather than only `--verify-only`, rebuilds all programs and checks:

| Scope | Outer states | Canonical residual columns | Labelled orbit mass |
|---|---:|---:|---:|
| Degree 16, m=183 | 5,802 | 0 | 0 |
| Degree 16, m=182 | 8,970 | 0 | 0 |
| Degree 15, m=183 | 5,547,774 | 8,495,391 | 130,442,305 |
| Degree 15, m=182 | 7,047,851 | 72,483,155 | 1,320,569,120 |
| Total | 12,610,397 | 80,978,546 | 1,451,011,425 |

There are 782,933 strict subset certificates, followed by 35,431 pair certificates and four supplement certificates. Final survivor count is zero in both dense scopes. Per-state data, not just these totals, are compared in the new replay comparator. Counts and integer comparisons fit the stated types; the production column box has 16^11=2^44 labelled possibilities per unrestricted domain, below the unsigned 64-bit range.

The original actual-graph regression was also rerun. It includes the small labelled census, representative assignments and deterministic larger examples, but no positive-surplus actual graph. Therefore it cannot experimentally prove the dense residual contradiction. Its selected/source checks remain finite falsification tests. A complete replay in a clean environment is not an independent mathematical review.

## 8. Findings and their disposition

### F1 — Raw digit-scanner accepts malformed negative values

**Severity: verifier hardening; nonblocking for the hash-pinned original evidence.** The frozen C++ helper extracts digit runs rather than parsing JSON numbers. In the six-state validation fixture, changing a source cap from 2 to -2 still lets the standalone checker pass because the sign is discarded. This was reproduced with the actual compiled program, not just inferred from its source.

The published replay first verifies the frozen manifest, so changing such bytes invalidates the archive before the arithmetic is accepted. All original production input rows are nonnegative; this finding does not provide an accepted mathematical counterexample. Nevertheless standalone checking should reject malformed input. The new `check_raw_inputs.py` strictly parses JSON, rejects booleans, negatives, floats and oversized integers, and checks array shapes before executing the original C++ checker. The hardened workflow applies it to the original outer ledgers, frontiers, cuts and survivors. Frozen sources are not silently altered.

Seven other deliberate mutations were correctly rejected by the original checking programs: missing and duplicated pair certificates, a non-strict pair witness, a missing supplement certificate, a false subset mask, and missing and duplicated subset certificates. The negative-cap mutation is explicitly recorded as accepted by the frozen scanner and rejected by the new guard, not folded into an inaccurate “all mutations rejected” claim.

### F2 — First replay comparison failed on gzip timestamp metadata

**Severity: audit comparison bookkeeping, resolved without changing mathematical data.** Run 34208483684 completed the full original replay, then its added comparison step failed on `d15_182_supplement_certificates.json/input_sha256`. That field hashes a freshly compressed input. Inspection showed the old and fresh target files were both 152 bytes and differed only in gzip timestamp bytes; their decompressed SHA-256 was identical:

`358c90f4d10e9e2f9b81a503aec79ba804d001d79ed27e83d72195687c3483ec`.

Both certificate fields correctly hash their respective compressed target, and all other certificate content matches. The new comparator allows this one explicitly named normalization only after verifying both raw links and decompressed equality. It also compares nested degree-16 records omitted by the initial top-level-only comparison. The frozen `CLEAN_REPLAY_CHECK.json` already records the gzip-timestamp caveat; the failure was in this audit's initially over-literal comparator, not in the frozen proof. The first run remains recorded as an overall failure; its arithmetic completion is stated separately. `history/FIRST_RUN_RECONCILIATION.json` preserves the diagnosis.

## 9. Remaining uncertainty and status

No lemma failure, missing production case, false strict inequality, unsupported symmetry reduction or equality counterexample was found in this audit. The original n=27 candidate is materially better supported after a fresh full replay, input hardening and independent reconstruction of all terminal caps.

The remaining limitations are substantive: the universal graph lemmas are hand proofs; finite counterexample searches contain no positive-surplus actual graph; the full column generator is shared between scan and replay; and external theorems are dependencies rather than re-proved foundations. This work is by the same assistant, not a specialist referee. No full n=27 Lean formalisation or external endorsement is claimed.

**Disposition:** retain the n=27 statement as a complete candidate with internally REPRODUCED computation and independent review OPEN. Do not change the governed theorem ledger. The original manuscript, original archive and later general-degree work remain unchanged. Specialist scrutiny of the residual injections and the global enumeration-to-graph coverage remains the highest-value independent assurance step.

## Sources and replay record

[1] Tao Wang, *On Murty-Simon Conjecture*, arXiv:1205.4397v1. Page 2 quotes Fan's strict numerical bound; Theorem 2.1 on page 3 covers the odd-order diameter-three complement case. https://arxiv.org/pdf/1205.4397

[2] Antoine Dailly, Florent Foucaud and Adriana Hansberg, *Strengthening the Murty-Simon conjecture on diameter 2 critical graphs*, arXiv:1812.08420. Theorem 4, printed page 4; H5 has six vertices, printed page 18. https://arxiv.org/pdf/1812.08420

[3] Teresa W. Haynes, Michael A. Henning, Lucas C. van der Merwe and Anders Yeo, *A maximum degree theorem for diameter-2-critical graphs*. Theorems 3.1-3.3 and 3.6(a); DOI 10.2478/s11533-014-0449-3. https://d-nb.info/1372516379/34

[4] Original frozen n=27 proof, source, manifest and evidence archive at the pinned repository baseline above. New code commit: `6114d4ec70afa779a3a8335b939c50b6ca5d9e92`. The definitive execution statuses, complete comparison records and counts are in `evidence/REMOTE_REPLAY.json` and the neighbouring evidence files. Publication receipt separately records branch attachment and preservation checks.
