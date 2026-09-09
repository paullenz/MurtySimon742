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
