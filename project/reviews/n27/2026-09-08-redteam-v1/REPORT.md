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
