# Claim ledger — stratified Hall/min-cut paper

## A. Central candidate theorem

**SH1 — abstract minimum-margin exactness.** In every finite layered directed Hall system satisfying two-sided crossing dominance (`TCD`),

`min_S(H(S)-D(S)) = min_S(U(S)-D(S))`.

**Current basis:** fresh hand derivation in `ABSTRACT_CROSSING_DOMINANCE.md` plus standalone exhaustive regression. **Status:** internally proved candidate; external mathematical review OPEN; novelty review OPEN.

**SH1a — original q/c theorem as corollary.** The 14 September q-stratified target-Hall model satisfies TCD, so its minimum-cut exactness theorem follows from SH1.

## B. Supporting claims

**SH2. Rearrangement gap.** `U(S)>=H(S)` for every set, with strictness witnessed by a within-layer capacity/multiplicity crossing.

**SH3. Crossing orientation.** Under TCD, a positive crossing `P_x<P_y`, `y_x>y_y` forces `x notin S`, `y in S`, and `y_x=y_y+1`.

**SH4. Submodularity.** `F(S)=H(S)-D(S)` is submodular; its minimisers form a lattice.

**SH5. Neutral deletion.** If the low endpoint of a crossing lies outside the maximal minimiser, deleting the selected high endpoint preserves the minimum Hall margin.

**SH6. Crossing-removal termination.** Repeated neutral deletion reaches a crossing-free minimum witness.

**SH7. Pointwise exactness is false.** Preserve hostile positive-gap examples; they are conceptually necessary because SH1 is not pointwise rearrangement exactness.

## C. Regression status

Standalone exhaustive abstract verifier:

- one-layer four-vertex regime: 39,636 demand instances, 2,760 with pointwise gaps, zero minimum mismatches;
- two-layer four-vertex regime: 172,080 demand instances, 24,624 with pointwise gaps, zero minimum mismatches.

Finite testing is supporting evidence only.

## D. Claims not currently authorised

Do **not** claim without additional proof/review:

- novelty of SH1;
- that SH1 holds for arbitrary directed Hall systems without TCD or a replacement axiom;
- that TCD is necessary or best possible;
- that the system is exactly a standard Ferrers/threshold class;
- a polynomial-time improvement over standard min-cut/matching algorithms;
- weighted or real-capacity extensions;
- any new Murty–Simon consequence beyond the separately certified bridge applications.

## E. Promotion checklist

- [x] Re-derive the theorem from abstract axioms only.
- [x] Build a standalone abstract exhaustive verifier with pointwise-gap cases.
- [ ] Independent proof audit of crossing orientation and neutral deletion.
- [ ] Produce minimal counterexamples when each TCD component is removed, where possible.
- [ ] Dedicated Ferrers/threshold/minimum-deficiency literature comparison.
- [ ] Decide final terminology only after that comparison.
- [ ] External expert review.
