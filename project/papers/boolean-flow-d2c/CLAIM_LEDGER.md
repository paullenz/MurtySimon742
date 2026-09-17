# Claim ledger — Boolean-flow D2C paper

## A. Core exact-boundary claims

**BF1. One-coordinate coding.** In `t=0, F=empty, r=0`, every `B`-edge changes exactly one A-neighbourhood coordinate.

**BF2. Unique coordinate flow.** Each zero coordinate has exactly one outgoing edge flipping it under canonical orientation.

**BF3. Factorial path inequality.** A code with `z` zero coordinates satisfies `z! <= b lambda^z`, `lambda=2b-n`.

**BF4. Large-zero root consequence.** Root criticality forces some `z>=ceil(a/2)` in the non-bipartite exact boundary.

**BF5. Order cutoff.** Under `m>=floor((n-1)^2/4)+1`, BF3+BF4 give the internal cutoff `n<=294` after exact finite arithmetic.

**Status BF1–BF5:** internal candidate theorem package; external mathematical and novelty review OPEN.

## B. Model family

**BF6. Hypercube-face family.** `X_k` is D2C for all `k>=3`, with `n=2^k+k+1`, `m=(k+1)2^k`.

**BF7. Density self-dilution.** For `k>=4`, `X_k` lies below the second-extremal comparison threshold.

No novelty or authoritative `X_3`/published-graph identity claim is authorised.

## C. Perturbative stability

**BF8. Root-edge antipode-or-private-foot.** Every triangle-active root neighbour has either a private A-foot or an antipodal B-partner with only the root as common neighbour.

**BF9. Private-foot charge.** Private-supported triangle-active sources inject into nonisolated vertices of `F`, hence are at most `2e(F)`.

**BF10. Antipode defect payment.** In the antipode branch, `Q+r>=a`, hence `2r+b(2b-n)>=a`, equivalently `2delta+2e(F)+b(2b-n)>=a`.

**BF11. All-private edge bound.** If every triangle-active source is private-supported, `Q<=binom(min(b,2e(F)),2)`.

**BF12. All-private gap theorem.** Let `t` be the number of triangle-active `B` vertices. In the all-private branch,

`t(b-t)<=2delta`.

This follows from private-foot cross-deficit mass, the maximum-degree bound on `F`, and `Q<=binom(t,2)`.

**BF13. Exact all-private exclusion.** If `Q>0` and `delta=0`, the all-private maximum-root branch cannot be D2C. Equality in BF12's proof forces a rigid `B=K_b` / private-foot `K_b` structure; deleting a `B`-edge then leaves diameter at most two.

**BF14. Near-exact rigidity when `t=b`.** Writing `Q=binom(b,2)-s`, one has `s<=delta`, total A-side maximum-degree slack at most `2(delta-s)`, and at most `2(delta-s)` additional missing A-B incidences beyond the private feet.

**Status BF8–BF14:** internal hand theorem package. Atlas regression through order 7 supports BF12–BF13 but is not proof.

## D. Claims not authorised

Do not claim:

- an eventual second-extremal theorem or classification;
- a general order bound outside stated hypotheses;
- novelty of the Boolean coding or hypercube family;
- authoritative identity of `X_3` with the published Figure-1 graph;
- that every triangle-containing D2C graph has a maximum-degree root in a triangle;
- optimality/significance of the constant 294 beyond this mechanism;
- that BF14 already forces a contradiction for positive `delta`.

## E. Promotion checklist

- [ ] Independent proof audit of BF1–BF5 and repeated-code path counting.
- [ ] Independent proof audit of BF8–BF14.
- [x] Graph-atlas regression of BF12–BF13 through order 7.
- [ ] Price B-edge criticality witnesses against the `O(delta)` defects in BF14.
- [ ] Resolve or quarantine maximum-triangle-root scope.
- [ ] Authoritative 12-vertex adjacency/isomorphism check if needed.
- [ ] Full construction/Boolean-cube novelty search.
- [ ] Compare against 2024 primitive-D2C and 2025 C5-free results.
- [ ] External graph-theory review.
