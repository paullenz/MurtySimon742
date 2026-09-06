# N=25 candidate: adversarial audit of lemmas, assumptions and computation

6 September 2026. Prepared by ChatGPT/Codex for Paul Lenz.

**Verdict: no blocking failure identified in this audit. The result remains a candidate awaiting independent mathematical review.**

This pass attempted to falsify the argument, including its implicit dependencies and computational bounds. It found one implementation defect outside the parameter range used in the proof, and explicit counterexamples to weakened versions of several lemmas. The candidate states the hypotheses that exclude those counterexamples. A third arithmetic checker independently recalculated every stored state disposition, every labelled-column capacity, and every final certificate.

This is another check by the same assistant that helped construct the argument. It is not an external assessment, formal verification, or a guarantee that no mathematical error remains.

## 1. Exact object audited

- Reviewer edition 1 at commit `448e4bc3c5f0493b1f553343a4484fd232cb202e`.
- PDF SHA256: `3ae32e4be90e9516b685fa66f4353d8b6294449eef34903f478a7290a37bccd8`.
- Reviewer ZIP SHA256: `ff5a88f4202fb1e201f52e7e6ec0b50f88248cd43493eee78f120a3c1de15c3d`.
- Frozen candidate evidence ZIP SHA256: `0588c85900762184040dfb313c89d36349f2a8183db5cbc91a1ee50915cb4e95`.

The mathematical statements were checked against the frozen proof and its editorial PDF. `AUDIT_INPUTS.json` pins the 15 data/source files consumed by the new executable checks. The frozen manuscript, sources, evidence, and governed theorem ledger have not been changed.

## 2. Findings and their impact

| Finding | Evidence | Impact on the candidate |
|---|---|---|
| A primary matching helper silently truncates comparisons when there are fewer suppliers than labels. | A synthetic a=15, b=9 instance returns capacity 14 with only 8 possible suppliers; the second implementation returns 8. A proposed length guard fixes this example. | Outside every proof dimension. It overestimates capacity and cannot by itself cause a false rejection. No audited result is affected. |
| Several hypotheses are essential, not interchangeable conveniences. | Actual critical graphs violate weakened statements if the minimum-degree base, strict positive surplus, all-active premise, or no-dominating-edge premise is dropped. | These premises are present in the candidate. They should be repeated in explicit lemma statements to prevent misuse. |
| The original final-certificate checker treats recorded source caps as premises. | It compares certificate caps with ledger caps and verifies the subset inequality, but does not derive the caps from scratch. | This is a declared trust boundary, not a discovered contradiction. The new checker rederives all 3,442,212 recorded column-cap vectors and all final certificate caps. |
| Published dependencies remain dependencies. | The relevant theorem statements and numerical applications were checked; Fan's full original paper was not retrieved. | No hypothesis mismatch was found. This audit does not claim to have re-proved every cited result. |

### 2.1 Matching-helper boundary defect

`general_primary.py: matches()` uses `zip(reversed(labels), suppliers)` without checking the lengths. Python stops at the shorter input. With a=15, b=9, fifteen zero degree labels and nine residual degrees equal to one, the primary source helper accepts q=14 even though only b-1=8 distinct suppliers exist. `helper_boundary_attack.py` reproduces this and tests a length guard.

In the actual scans a is 9 or 10, b is 15 or 14, and residual degrees are positive. Therefore q≤a-1≤9 while b-1≥13. The defective boundary cannot be reached. The structurally handled a=8 case is also outside that boundary. Moreover, the defect makes the capacity bound too generous, so its direction does not create an invalid exclusion. This is a reuse/robustness defect, not a counterexample to the n=25 proof.

The exact proposed guard is in `PROPOSED_CLARIFICATIONS.md`. It has not been applied to a frozen source file.

### 2.2 Concrete negative controls for the hypotheses

The following are counterexamples to weakened statements, not to the stated candidate.

1. **Strict positive surplus.** The six-vertex critical graph with edges 01, 02, 04, 05, 13, 15, 23, 24 admits a decomposition with t=0 and r=0. B-vertices are inactive. Thus “t≥0 implies all B-vertices are active” is false. The candidate uses t>0, and all six dense parameter rows satisfy it.
2. **All-active premise in the low-k count.** The same example has a=1, b=4, k=0, r=m=0. The conclusion b≤r-m would read 4≤0. The missing premise is precisely that all B-vertices have a residual edge; Section 6 obtains it from Section 5 in the candidate's positive-surplus regime.
3. **Minimum-degree base.** For the six-vertex critical graph with edges 03, 04, 05, 12, 14, 15, 23, choosing vertex 2 as the complement base gives an A-vertex with F-degree 2 but B-degree 1. The inequality d_B(i)≥d_F(i) fails because that base does not have minimum complement degree. The candidate explicitly chooses a minimum-degree base.
4. **No dominating edge.** In K12,13 every edge is a direct witness with endpoint degree sum 25. The Section 3 bound 24 therefore fails without the no-dominating-edge hypothesis. The candidate first handles the complete bipartite case and then applies the published non-bipartite dominating-edge bound.

Full labelled graphs, base vertices and selected-edge choices are recorded in `structural_results.json`.

## 3. Structural arguments: attempted failure modes

### Witness counting, Section 3

An edge's deletion can only destroy a previously available distance-one or distance-two connection. For nonadjacent endpoints, two distinct length-two paths cannot both contain the same deleted edge, so a witness of this kind has one common neighbour. The direct-witness and two-step-witness classes therefore cover every critical edge.

Under the no-dominating-edge hypothesis, both classes have endpoint degree sum at most n-1. At n=25 and maximum degree 13 this forces every witness contained in R to have both endpoints in O. An L–L witness contributes no R–R edge; an L–R witness contributes at most one; an O–O witness contributes at most two. The subtraction of the existing L–R edges counts only missing cross pairs. No injective assignment across different witness classes is required because this is an upper bound on a union of covered edges.

The deficit table was recomputed with exact integers. At 156 edges it forces h=0 and o=13. The sharpened count then forces O independent; degree 12 forces every cross edge, and the edge total leaves no additional edges. No equality case was found to be omitted.

### Selection and residual ledger, Section 4

A missing B-pair misses v. Adding it must produce an adjacent total dominating pair using an endpoint of the added edge; the original pair itself cannot dominate v. The other endpoint of the resulting existing edge must lie in A. Its sole undominated vertex in H is the opposite endpoint of the missing pair.

A cross-edge with B-endpoint b and unique exception w identifies exactly one unordered B-pair {b,w}. Thus choices for different missing B-pairs cannot reuse a cross-edge. Exactly one choice per pair also makes supplements at a fixed B-source distinct. Both properties are used later and were tested with every allowed selection on the small representatives.

The ledger is an exact partition of edges. The inequality d_B(i)≥d_F(i) additionally uses the minimum-degree choice; it is not a consequence of quasi-edge uniqueness alone.

### All-active lemma, Section 5

For an inactive source, selected edges force F to have no S–T edge. An F-edge inside S produces two residual edges whose identities are fixed by the A-endpoint and the distinct supplement label. An F-edge inside T has its quasi-edge auxiliary in B: an auxiliary in S would be adjacent to the supposed exception, and the other possible locations fail domination or adjacency.

The T-family edges are distinct because their A-endpoint and unique exception identify the missing F-edge. The S- and T-families have disjoint A-endpoint sets. Hence r≥2e(F[S])+e(F[T])=e(F)+e(F[S]). This contradicts e(F)=r+t only when t>0. The proof accommodates S empty; no unstated complement-diameter-two assumption was needed.

### Low-k injection, Section 6

Each selected quasi-edge for a missing X-pair with B-auxiliary z forces xz. The edge xz misses that pair's exceptional X-vertex and therefore cannot be one of the selected edges whose unique exception lies in B. It is residual and lies outside P. Distinct used B-endpoints give distinct extra edges; unused B-endpoints contribute residual edges under the all-active premise. This justifies the b extra edges without double counting.

For k=1, at most s=e_C(y,X) missing X-pairs can use auxiliary y, because each such y–X edge has a unique exception. Cancelling s yields the stated bound. The numerical band calculation confirms that k=1 must remain in the Delta14/156-edge search; applying the 157-edge exclusion to it would be invalid, and the candidate does not do so.

### Source, column and subset inequalities, Sections 7–9

Each charge in the pair-residual and column-residual arguments can be identified by its A-endpoint or distinct supplement. A cross-edge missing an A-vertex cannot be selected for a B-pair. This supplies the residual classification needed by both charges.

The h-index lower bound uses distinct selected B-sources at one A-vertex. The supplement refinement uses the old capacity bounds simultaneously, avoiding circular use of newly reduced bounds. The subset inequality counts at least the required selected incidences on the left and an upper bound from every source on the right. Simplicity of the graph gives at most one selected edge per source/label pair.

No invalid reversal of a necessary inequality was identified. Independently sorting A-degrees and B-residual degrees is legitimate because A and B can be relabelled separately. The R-vector remains labelled, including positions with equal A-degree.

## 4. Published hypotheses checked

**Fan.** Wang's primary manuscript, page 2, gives the strict bound for n≥25 used in the candidate. At n=25 its value is exactly 12569/80=157.1125, giving e(G)≤157 by integrality. Fan's original full paper was not retrieved. Wang describes Fan's small-order result as the first, upper-bound part of the conjecture; the candidate uses only that part. [Wang manuscript](https://arxiv.org/pdf/1205.4397)

**Dominating edges.** Dailly–Foucaud–Hansberg Theorem 4 requires a non-bipartite diameter-2-critical graph with a dominating edge and excludes H5. The paper identifies H5 as a six-vertex graph. Thus the application to the dense non-bipartite order-25 case is appropriate. [Primary paper](https://arxiv.org/pdf/1812.08420)

**High degree and complements.** Haynes–Henning–van der Merwe–Yeo Theorems 3.1–3.2 require the star/isolated-complement exception to be handled, as the candidate does. Theorem 3.6(a) has delta(H)≤0.3n, with delta(H)≥1. At n=25, delta(H)≤7 yields e(H)>144. The degree conversion uses n-1-Delta(G); it is therefore Delta(G)≥17, even though the paper's conveniently stated Theorem 2.1 has a weaker sufficient threshold. Wang's Theorem 2.1 explicitly includes odd orders in the complement-diameter-three case. [2014 primary paper](https://d-nb.info/1372516379/34), [Wang primary manuscript](https://arxiv.org/pdf/1205.4397)

`PROPOSED_CLARIFICATIONS.md` also gives a direct alternative for Delta≥17 from the candidate's residual ledger and all-active lemma. It is a further internal derivation, not a change to the frozen proof or a replacement for external review.

## 5. Actual-graph falsification tests

The new structural test imports no proof-verifier code and uses only the Python standard library. It generates all 33,864 labelled simple graphs of orders 3–6, checks diameter-two criticality by actual edge deletion, and finds 608 labelled critical graphs. These reduce to 11 isomorphism representatives. All base vertices and all eligible selected-edge assignments are checked on the non-bipartite small representatives.

It also checks 180 seeded examples obtained by edge minimization at orders 7,8,9,10,12,14,16,20,25, and five explicit C5 blowups. The larger examples use minimum-degree bases and sampled selections.

The run performed 2,643 assignment checks, 6,960 checks of each principal selected-edge bound, and 51,374 subset inequalities using actual selected degrees. These are check counts, not claims of distinct graphs or distinct random assignments. Inactive-source checks included 80 forced S-family residual-edge occurrences and 60 T-family occurrences.

**Coverage limit:** no positive-surplus actual graph occurred in this sample. The nonvacuous test is of the inactive-source inequality that precedes the t>0 contradiction, not a search over every hypothetical dense n=25 graph. The largest actual selected source degree encountered was 4. Universal validity still rests on the structural argument. The negative controls show that the tests can detect invalid weakened statements.

## 6. Third audit of the complete stored computation

`arithmetic_attack.py` imports neither original scanner nor the final certificate checker. It uses a different way to count domains and calculate source capacities.

For a proposed matching of q labels to distinct suppliers, every threshold t gives the necessary bound

\[
q\le \#\{\text{eligible labels with requirement}<t\}
   +\#\{\text{suppliers with capacity}\ge t\}.
\]

Matched labels below t cannot exceed the first count; the remaining matched labels require distinct suppliers counted by the second. The checker uses these threshold cuts, together with the number of eligible labels, to bound each trial q. It reproduced every stored capacity. Its threshold-matching calculation was additionally checked against exhaustive injection search on 4,900 small instances.

For outer domains, it computes generating-function coefficients for bounded multisets. Every recorded key must satisfy the full domain conditions and be unique; matching the independently calculated cardinality then establishes coverage of that finite domain. For labelled columns it uses coefficients of products of bounded ordinary polynomials, and again checks membership, uniqueness and exact cardinality. This also tests whether repeated-degree labels were incorrectly identified.

| Scope | Outer states checked | Labelled columns checked | Final certificates checked |
|---|---:|---:|---:|
| Delta14, 157 edges | 59,264 | 1,480 | 0 |
| Delta15, 157 edges | 108 | 0 | 0 |
| Delta15, 156 edges | 211 | 0 | 0 |
| Delta14, 156 edges, k=2–5 | 82,452 | 188,520 | 171 |
| Delta14, 156 edges, k=1 | 401,543 | 3,252,212 | 1,788 |
| **Total** | **543,578** | **3,442,212** | **1,959** |

Every recorded pruning inequality was recalculated. All 137 recorded bands matched independently calculated domain sizes, and the six dense parameter cases matched the algebraically derived k-r coverage. Every column capacity and refinement was recalculated; final certificate caps were compared against these newly derived values. Every strict subset contradiction passed, with no unaccounted surviving column. The full arithmetic pass took about 72 seconds on this environment; that timing is not a hardware-independent promise.

This strengthens the computational evidence substantially. It remains conditional on the mathematical necessity of the structural reductions and bounds.

## 7. Recommended disposition

Retain the status **candidate proof, independent mathematical review OPEN**. Give an external reviewer this report alongside edition 1. Ask them to challenge the structural injections and source bounds in particular, with the essential hypotheses explicitly in view.

For a future edition, consolidate the hypothesis statements and include the helper length guard before any broader computational reuse. The direct high-degree alternative is available for consideration. Preserve edition 1 and record any adopted changes in a new dated version.

This audit found no reason to withdraw the candidate. It does not establish that an independent expert will accept it, and it does not confirm novelty or priority.
