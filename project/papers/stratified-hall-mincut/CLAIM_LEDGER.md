# Claim ledger — stratified Hall/min-cut paper

## A. Central candidate theorem

**Claim SH1.** In the monotone directed Hall model of `MANUSCRIPT.md`,

`min_S(H(S)-D(S)) = min_S(U_q(S)-D(S))`.

**Current basis:** hand proof via crossing removal in the 14 September 2026 research checkpoint; finite exhaustive/random verifier also preserved.

**Status:** internally proved candidate; external mathematical review OPEN; novelty review OPEN.

## B. Supporting claims

**SH2. Crossing-gap identity.** `U_q(S)-H(S)=C_q(S)` for every source set.

**SH3. Submodularity.** `F(S)=H(S)-D(S)` is submodular; its minimisers form a lattice.

**SH4. Neutral deletion.** Under equal-q ordered endpoints and positive receiver slack, deletion of the selected high endpoint preserves the minimum Hall margin.

**SH5. Crossing-removal termination.** Repeated neutral deletion reaches a crossing-free minimum witness.

**SH6. Pointwise exactness is false.** Preserve the hostile small counterexample in the final paper; it is conceptually important because it shows SH1 is not a trivial corollary of a stronger pointwise statement.

## C. Claims not currently authorised

Do **not** claim without additional proof/review:

- novelty of SH1;
- that SH1 holds for arbitrary directed Hall systems;
- that fixed-q capacity monotonicity is necessary or best possible;
- a polynomial-time improvement over standard min-cut algorithms;
- a general Monge/Ferrers theorem unless equivalence is proved;
- any Murty–Simon consequence beyond those separately certified in the canonical research ledger.

## D. Promotion checklist

- [ ] Re-derive SH1 independently from the abstract axioms only.
- [ ] Have another checker/prover verify every containment and marginal-capacity identity in the neutral-deletion lemma.
- [ ] Freeze standalone definitions; remove hidden dependence on Murty-specific identities.
- [ ] Produce minimal counterexamples when each main hypothesis is removed, where possible.
- [ ] Dedicated literature search and comparison table.
- [ ] Rebuild standalone verifier and archive exact output.
- [ ] External expert review.
