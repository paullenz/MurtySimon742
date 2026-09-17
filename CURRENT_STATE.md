# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The live graph-theory problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. In parallel, two standalone-paper candidates are now explicit research priorities: stratified Hall/min-cut exactness first, and Boolean-flow/D2C stability second.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `STANDALONE_HALL_ABSTRACTION_AND_ALL_PRIVATE_STABILITY_NOT_PROMOTED`.

**WORK MODE:** `MATH + PAPER_EXTRACTION`. The project is deliberately separating reusable mathematics from the fate of the main conjecture attack.

**INSPECTED PREDECESSOR:** `9f7f8ea31d4af709b50fec48d8b463c22744cd66` on `main`, which created the two standalone paper skeletons.

## Priority 1 — stratified Hall/min-cut paper

The q-stratified minimum-cut theorem has been abstracted beyond its original q/c numerical compatibility relation.

For a layered directed Hall system with common integer source demand in each layer, receiver capacities `P_w`, and loopless compatibility `R`, assume **two-sided crossing dominance (TCD)**: for equal-layer `x,y` with `P_x<P_y`, they are mutually compatible and `y` dominates `x` in both incoming and outgoing compatibility away from the diagonal.

Then the hand proof gives

`min_S [U(S)-D(S)] = min_S [H(S)-D(S)]`,

where `H` is exact capped receiver capacity and `U` is the layerwise rearranged upper bound.

The proof now uses only:

1. layer-cake rearrangement;
2. TCD to force every positive crossing to have `x notin S`, `y in S`, and multiplicity gap exactly one;
3. submodularity/lattice of minimum Hall witnesses;
4. neutral deletion of the selected high endpoint;
5. finite crossing removal.

The original q/c target-Hall theorem is a corollary because fixed-q capacity monotonicity plus the numerical compatibility relation imply TCD.

**Standalone regression:** exhaustive four-vertex abstract checks found zero minimum-margin mismatches in both a one-layer regime (39,636 demand instances; 2,760 with pointwise gaps) and a two-layer regime (172,080 demand instances; 24,624 with pointwise gaps). This is evidence, not proof.

**Literature lead:** the 2026 Marmulla–Brandes Ferrers/threshold-digraph neighbourhood-inclusion paper is structurally close to TCD after diagonal deletion and must be compared carefully. No novelty claim is authorised.

## Priority 2 — Boolean-flow D2C paper / live all-private branch

The previous root-edge dichotomy remains:

- private foot, or
- disjoint-support antipode with residual payment.

The all-private branch now has a new quantitative theorem. Let `T` be the set of triangle-active vertices in `B`, `t=|T|`, `Q=e(G[B])`, and `delta=r-e(F)=b(n-b)-m`. If every vertex of `T` has a private A-foot, then distinct feet contribute `t(b-1)` missing A-B incidences. Maximum degree gives `e(F)<=Q+delta`, while all B-edges lie in `T`, so `Q<=binom(t,2)`. Therefore

`t(b-t) <= 2delta`.                                    (APG)

**Exact branch consequence:** if `Q>0` and `delta=0`, APG forces `t=b` and equality throughout. This rigidifies the graph to `B=K_b`, a `K_b` of private feet, and the natural matching between them (with any remaining A-vertices B-complete and F-isolated). Deleting a B-edge then leaves diameter at most two, contradicting D2C. Hence the non-bipartite all-private exact-defect branch does not exist.

**Near-exact consequence:** when `t=b` and `Q=binom(b,2)-s`, one has `s<=delta`; total A-side maximum-degree slack and additional cross-defect beyond the private feet are each at most `2(delta-s)<=2delta`.

**Atlas regression:** all D2C graph-atlas classes through order 7 give 9 maximum-degree triangle roots, 3 all-private roots, zero APG violations, and zero `delta=0` all-private roots.

## Preserved earlier core

The zero-residual Boolean-flow theorem and internal `n<=294` cutoff remain unchanged. The root-edge antipode/private-foot theorem and antipode inequality `(RSD)` remain unchanged. The 12-vertex obstruction remains a mandatory hostile control. Canonical fixed-order ledger remains **4,626 exclusions / 952 survivors / 3,632 whole-state closures**; no catalogue promotion changes.

## Paper programme

[`project/papers/README.md`](project/papers/README.md) is the paper index. The Hall paper is first priority because its central theorem is now independent of D2C notation. The Boolean-flow paper develops in parallel and has strengthened through APG/exact all-private exclusion.

**README SYNC:** pending one-time self-removing workflow in this transaction; it will add a prominent root-README paper banner and reviewer links without rewriting historical content.

## Trust boundary

Both new results are internal hand theorems with finite regression. External mathematical review and novelty assessment remain open. No eventual second-extremal theorem is claimed. The maximum-triangle-root scope issue remains open.

**UNPRESERVED WORK:** None after this checkpoint once the commit is published.

**NEXT ACTION:** First, audit TCD against Ferrers/threshold/minimum-deficiency literature and seek minimal counterexamples when individual TCD clauses are removed. In parallel on the D2C track, use the near-rigid all-private model to price each B-edge criticality witness against the at-most-`O(delta)` defect budget. Do not return to the closed mixed `{4,5}` ladder.
<!-- CURRENT-STATUS:END -->
