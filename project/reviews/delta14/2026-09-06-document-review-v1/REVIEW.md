# N=25: review of the complete Delta=14 candidate dossier

Review date: 6 September 2026. Review type: internal mathematical reading, source inspection and fresh arithmetic reproduction by ChatGPT/Codex. This is not external expert sign-off, formal verification or a promotion of the project theorem ledger.

**Finding: no blocking defect identified in the stated conditional argument. Both printed verifiers reproduce the complete reported arithmetic, including the recorded result hashes.** The conclusion under review is confined to the nonexistence of a 25-vertex diameter-2-critical graph with exactly 157 edges and maximum degree 14.

## Input and provenance

The reviewed attachment is `N25_Delta14_Complete_Workings_Candidate_v1(1).docx`, 91,667 bytes, SHA-256 `60639304c55dabb875ad485cc2711e99e1b1e1ad5438030094dc878bfc0fd3a3`. Its bytes match the original unnumbered filename recorded in the [repository distribution receipt](https://github.com/paullenz/MurtySimon25/blob/main/project/attacks/delta14/2026-09-06-all-active-v1/SHAREABLE_WORKINGS_v1.md). The filename suffix does not represent a different mathematical version.

The attachment was read locally. All sections and appendices, tables, equations and 14 source listings were examined. It renders to 39 pages; all pages were screened in rendered contact sheets, with no obvious clipping or overlap observed. This was a content review, not a new typesetting edition. Structural inspection found no tracked insertions, tracked deletions or comment parts.

All 1,137 printed Python source lines were recovered from the document XML by removing line-number gutters and joining visual continuation paragraphs. Every one of the 14 resulting files matches its printed SHA-256. The two final verifiers were inspected before execution. The new evidence bundle contains these recovered files and fresh outputs; it is not the original candidate ZIP or original sharing ZIP, and does not pretend to recover their missing historical payloads.

## Mathematical review

### External input and scope

The cited [Haynes–Henning–van der Merwe–Yeo paper](https://d-nb.info/1372516379/34) was consulted directly. Its Theorems 3.1 and 3.2 support the complement correspondence and the exceptional disjoint-two-cliques case; Observation 3.4 supplies the quasi-edge alternative. The exceptional complement makes the original graph complete bipartite, whose edge count cannot exceed 156 on 25 vertices. The complement here has minimum degree ten, so the isolated-complement concern does not arise.

The dossier also derives the needed quasi-edge observation directly: if adding a nonedge creates a total dominating pair and the nonedge's endpoints miss another vertex, an existing edge has the opposite endpoint as its unique undominated vertex. The derivation is sound under the stated hypotheses. Ordinary domination of vertices outside a pair and total domination of an adjacent pair are used consistently in the argument.

### Selected edges and the ledger (Section 2)

One A–B quasi-edge is selected for each missing unordered B-pair. A cross-edge fixes both its B endpoint and its unique supplement, making the assignment injective. Supplements of different selected edges at the same B endpoint are distinct. Thus selected cross-edges and existing B-edges together account for all 91 unordered B-pairs.

The count is 143 = 10 + e(C) + r + 91, giving e(C)+r=42 and e(F)=r+3. Minimum degree ten gives d_B(a) >= d_F(a), and hence Q >= r+6. No assumption that the complement has diameter two is needed.

### All B vertices have residual edges (Lemma 1)

For an inactive b, let S be its A-neighbours and T the remaining A vertices. Every b–S edge is selected. An F-edge crossing S and T would leave an A vertex undominated by one of these selected edges, which is impossible because its unique supplement is in B.

Each F-edge ac inside S forces two residual edges, c–w_a and a–w_c. They exist because the other selected edge must dominate the first edge's supplement. They are residual because each misses an A vertex. Their A endpoints and the injective supplement labels distinguish all 2e(F[S]) edges.

For an F-edge inside T, its endpoints miss b, so a quasi-edge must exist. Its auxiliary endpoint cannot be v, b or T. An auxiliary in S is adjacent to the exceptional T vertex because F has no S–T edge, so this is also impossible. The auxiliary therefore lies in B. Such cross-edges are residual and distinct because their A endpoints and unique exceptions identify the original F-edges. They have A endpoints in T, disjoint from the first family.

Consequently r >= 2e(F[S])+e(F[T]) = e(F)+e(F[S]), contradicting e(F)=r+3. This also handles S empty. The inference that all fourteen B vertices are residual-active, and therefore r >= 14, does not rely on a hidden supplement-activity assumption.

### Low and high k cases (Section 4)

For k >= 6, e(C) >= 5k gives r <= 12, contradicting r >= 14.

For k=0 or 1, a missing pair inside X misses x, forcing its quasi-edge auxiliary into Y or B. A B auxiliary gives a distinct residual cross-edge with A endpoint in X. If P contains m such edges, each B endpoint used by P forces an additional residual edge to x. The edge to x misses the original A supplement if treated as selected. Each B vertex not used by P has some residual edge by Lemma 1. The B endpoints distinguish all fourteen extra edges and keep them outside P. Thus 14 <= r-m.

For k=0 there are r-6 missing X-pairs and no Y auxiliary, so m=r-6, a contradiction. For k=1, writing s=e_C(y,X), there are r+s-13 missing X-pairs and at most s distinct quasi-edges with auxiliary y; hence m >= r-13, again a contradiction. Both counts and their injection directions check out.

### Residual inequalities and finite necessity (Sections 5–6)

The B-pair inequality d_a <= rho_b+rho_w charges each F-neighbour of a either to a residual edge at b or to a forced residual edge at w. The A-column inequality d_a <= rho_b+R_a uses the distinct supplements of the other selected edges at b to force distinct residual edges at a. In both arguments an allegedly selected forced edge would miss an A vertex. The closure bounds d_a <= rho_b+q_b-1 and rho_b+q_b <= 10 follow from the A-neighbourhood size.

The threshold lower bound subtracts an upper bound on residual incidences from the minimum required A degrees. Each remaining selected incidence consumes a distinct unordered B-pair. The relaxed matching calculation gives an upper bound on the number of labels a source can select, since reducing label requirements and enlarging supplier capacities can only help feasibility. The refined threshold calculation uses these source bounds in the necessary direction.

For the column lower bound, set s=d_a-R_a. If s>0, there must be at least s distinct selected sources at a, each having residual degree at least s. Therefore the residual-list statistic h is at least s and R_a >= max(0,d_a-h). Every labelled R vector meeting these bounds and the residual budget is enumerated, including distinct positions for equal-degree A vertices.

Finally, each supplement of a source with q selected labels has at least q-1 A-neighbours. Existing upper bounds on other sources therefore safely bound the eligible supplements. Both programs use the previous vector of bounds for the simultaneous refinement; neither substitutes an unjustified stronger value.

### Coverage and final hand argument (Sections 6–9)

The remaining domain is k=2,3,4,5 and 14 <= r <= 42-5k. The sorted A-degree list has length ten, maximum exactly 9-k, and sum 2r+6. The sorted positive B-residual list has length fourteen, entries at most ten, and sum r. Independent relabelling of A and B justifies sorting. Nongraphical lists are deliberately retained, making the domain a relaxation rather than an incomplete graph catalogue.

The two final patterns have ten light residual degrees equal to one, four equal to three, and exactly two residual units above R_a=d_a-3. A light source selecting any label would consume both spare units at that label; it can therefore select at most one label. The closure bound then rules even that out. All selected edges must come from the four heavy sources. The lower bound Q>=28 and upper bound seven per heavy source force seven selections each. Each needs seven distinct supplements with at least six A-neighbours, but only the other three heavy vertices qualify. This contradiction is valid and agrees with the final computational bound.

## Fresh arithmetic results

| Check | Result |
|---|---:|
| Outer degree/residual states | 59,264 |
| Parameter bands | 46 |
| Outer states reaching column enumeration | 31 |
| Labelled column vectors | 1,480 |
| Columns failing initial source-total bound | 1,370 |
| Columns requiring supplement refinement | 110 |
| Survivors in either implementation | 0 |
| Original unit/negative tests rerun | 12 passed |

The source files were rerun unchanged, using the commands below from the evidence directory:

```sh
python3 -I -B verify_primary.py --output results
python3 -I -B verify_independent.py --output results --reference results
python3 -I -B test_verifiers.py
python3 -I -B check_document.py input/N25_Delta14_Complete_Workings_Candidate_v1.docx
```

The last command additionally requires python-docx and lxml; the original arithmetic and unit tests use the Python standard library. Full command outputs and environment details are included. The historical runner is retained as recovered source, but its full original manifest input is not present in this reconstruction; it was not used to certify the original archive.

Both summary files, the primary compressed ledger and the primary column JSON match the hashes printed in Appendix D. The state-set hash and uncompressed ledger hash also match. All 46 printed parameter rows, all four k subtotals and the overall total, all 31 printed outer states, and all 31 printed column aggregate rows agree with fresh output.

The built-in cross-check compares the state-set hashes, per-band disposition counts and every final column/capacity record. It does not provide a second per-state rejection-witness ledger. Agreement of these implementations is computational corroboration, not independent authorship or a check of their common mathematical premises.

## Limits and project disposition

The appropriate retained status is **REPRODUCED arithmetic supporting a complete candidate proof for the stated Delta=14, 157-edge slice; no blocking defect found in this internal review**. This review does not alter the existing project certification status.

The optional graph regressions and exploratory programs were read and recovered with matching hashes. Their historical numerical outputs are described in the dossier but were not regenerated in this review. Their input/output archives are not contained in the attachment and are not treated as proof dependencies.

Independent mathematical scrutiny remains the next review step for this candidate. It need not depend on the older SAT/DRAT/LRAT or graph-catalogue pipeline, because this argument does not invoke them. Those older dependencies must still be assessed wherever they remain part of the whole-project proof chain.

Before claiming the full N=25 theorem, separately reconcile and audit the global reductions, the parked Delta=15 chain and the other maximum-degree cases. The 156-edge equality classification is a separate outstanding scope item. An exclusion at exactly 157 edges is not by itself a proof for every larger edge count; the reduction to that exact slice needs its own justification. No novelty or priority claim is made.

The new review bundle preserves the unchanged input document, all recovered source listings, fresh arithmetic outputs, this review, extraction/check records and a new manifest. The bundle has new provenance and must not be relabelled as either historical candidate archive.
