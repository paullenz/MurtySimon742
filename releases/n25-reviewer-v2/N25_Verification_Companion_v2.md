---
title: "Murty-Simon at n=25 - verification companion"
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

**Claim under review.** `e(G) <= 156, equality exactly K(12,13)`.

**Historical reviewer-v1 package.** `releases/n25-reviewer-v1/README.md` remains preserved.

---


\newpage

# Included source: `project/reviews/n25/2026-09-09-fan-free-v2/HISTORY.md`

# n=25 proof history for Fan-free edition 2

The canonical historical v1 proof remains unchanged at
`project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md`.

Its SHA-256 at v2 build time is `9f4daa246f794ab9e2de29fb968911ecdbb7b8698982dc6af234db6ba18b2aa9`.

Edition 2 changes only:

1. Fan's 1987 theorem is moved from logical dependency to historical attribution and replaced by `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md`;
2. the selected-edge convention now says explicitly that exactly one representative is designated per missing unordered B-pair, so reverse orientations cannot collide;
3. the Section 5 forced cross-edge is explicitly shown non-selected before being counted residual;
4. the final assembly sentence points to the Fan-free reduction.

No frozen v1 evidence, source, hash or theorem ledger entry is overwritten.


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

# Included source: `releases/n25-reviewer-v1/LITERATURE_AND_ATTRIBUTION.md`

# Literature and attribution check

Checked 6 September 2026. This is a targeted public-source check, not an exhaustive bibliographic review or a priority determination.

**Finding:** no published resolution of the complete order-25 case was located in the sources inspected. This does not establish novelty. The reviewer edition should be described as a candidate for examination, without a “39-year-old problem solved” announcement.

## Mathematical inputs

| Source | Exact use in the candidate | Check and limitation |
|---|---|---|
| Genghua Fan, *On diameter 2-critical graphs*, Discrete Mathematics 67 (1987), 235–240, [DOI](https://doi.org/10.1016/0012-365X(87)90174-9) | Strict numerical bound implies e(G)≤157 at n=25. | The formula was checked against the publisher abstract and Wang's primary manuscript, p.2. Fan's full publisher text was unavailable; no full-paper audit is claimed. |
| Tao Wang, *On Murty-Simon Conjecture*, [arXiv:1205.4397v1](https://arxiv.org/pdf/1205.4397v1), 2012 | Fan's exact formula; Theorem 2.1 covers the complement-diameter-three strict inequality at odd orders. | Primary manuscript consulted. It is cited as an arXiv manuscript; no unverified journal publication is asserted. |
| Haynes, Henning, van der Merwe and Yeo, *A maximum degree theorem for diameter-2-critical graphs*, 2014, [primary PDF](https://d-nb.info/1372516379/34) | Theorems 3.1, 3.2 and 3.6(a): complement correspondence, complete-bipartite exception and δ(H)≤0.3n bound. | The minimum-degree inequality points toward small δ. At n=25, δ≤7 gives e(H)≥145. Stars are handled separately. The odd-order diameter-three point is cross-checked using Wang. |
| Dailly, Foucaud and Hansberg, *Strengthening the Murty–Simon conjecture on diameter 2 critical graphs*, Discrete Mathematics 342 (2019), 3142–3159, [DOI](https://doi.org/10.1016/j.disc.2019.06.023), [primary manuscript](https://arxiv.org/pdf/1812.08420) | Theorem 4 excludes a dominating edge in a non-bipartite order-25 graph with 156 or 157 edges. | The bound is floor(n²/4)-2, with a six-vertex exception that cannot occur at order 25. |

## Recent and adjacent work inspected

- Kirchweger, Manrique and Szeider, *Formally Verified Graph Generation with SAT Modulo Symmetries and Lean*, IJCAR 2026, first online 24 July 2026. Section 5 explicitly reports formal confirmation through 13 vertices. It does not report an order-25 resolution. [Primary publisher text](https://link.springer.com/chapter/10.1007/978-3-032-32589-1_8)
- Kirchweger, Xia, Peitl and Szeider, *Smart Cubing for Graph Search: A Comparative Study*, arXiv:2501.17201, submitted January 2025 and subsequently appearing in CP 2026. Its diameter-critical-graph benchmarks and computational methodology are relevant background; it is not an input to this proof. [Primary manuscript](https://arxiv.org/html/2501.17201v1), [conference record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CP.2026.33)
- The 2016 manuscript *Improving the bound for maximum degree on Murty-Simon Conjecture* states a high-degree threshold of 0.6756n, which at order 25 only reaches integer degree 17. Its Theorem 2.6 reverses the minimum-degree inequality when restating the 2014 result. This candidate therefore cites the original 2014 text directly and does not depend on the 2016 manuscript. [Primary manuscript](https://arxiv.org/html/1610.00360v2)
- A 2025 publisher result on a restricted class of diameter-2-critical graphs was found in search, but the full abstract/text could not be retrieved. Its title is insufficient to establish coverage of all order-25 graphs, so it is not used as a novelty conclusion. [Publisher record](https://www.sciencedirect.com/science/article/abs/pii/S0166218X25003439)

The Erdős Problems page for 742 returned an access error during this check. Search results also surfaced recent experimental repositories and restricted symmetry exclusions; inaccessible repository pages and search snippets were not treated as proof of either a complete solution or the absence of one. No source here justifies declaring the general Murty–Simon conjecture solved.

Searches included the exact problem name with “25”, “n=25”, “proof”, “2025” and “2026”, followed by the primary papers and author pages. Before public submission, an expert should confirm the precise novelty claim and check Fan's original full paper and any more recent specialized results.

## Contribution and evidence disclosure

Paul Lenz initiated and directed this research project and supplied the earlier project material. ChatGPT/Codex produced substantial mathematical arguments, implementation code, internal audits and the assembled candidate text. Both arithmetic implementations and the separate certificate checker were produced with the same assistant; their agreement is a software cross-check, not independent mathematical authorship or review.

Published inputs remain attributed to their original authors. The frozen project dossier and new generalizations have separate, preserved provenance. This reviewer edition does not assign final scholarly authorship, assert independent expert endorsement, or claim Lean/formal-kernel verification. A publication byline and contribution statement should be settled explicitly before submission.

The original mathematical evidence remains byte-identical to the archived version. This edition adds typography, navigation, a top-level verification/replay wrapper, literature notes and review materials; it does not promote the governed theorem ledger.
