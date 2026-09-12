# N34 equality: internal audit

12 September 2026. Same-assistant review by ChatGPT/Geeps.
**No blocking flaw found in this pass; external review OPEN.**

## Mathematical checks

- **Proof scope and coverage.** The prior bound handles m>=290. The original
  degree reduction applies at m=289 and leaves Delta=17,18. This package
  covers every one of the 13,546 Delta=18 states; the balanced-degree theorem
  closes Delta=17. Attainment and edge criticality of K(17,17) are explicit.
  No branch is inferred closed from average degree alone.
- **Exact mass.** All-positive demands give r=S-2. Multiple zero demands
  are allowed in the envelope only when their total nonnegative deficit is
  zero, forcing each deficit to zero. The five two-zero states entering the
  envelope satisfy this condition. Cases with one zero label use d=R-E.
- **Source-capped threshold.** The capacity c_u counts distinct compatible
  heavy labels and also respects q_u<=a-rho_u. The bound outside J is L-jh,
  because every member of J has capacity greater than h. The sum over J
  is bounded both by the j largest capacities and by the number of incident
  unordered pairs. Taking their minimum and maximizing over j is a safe
  relaxation; it does not assume that the maximizing choices are realizable.
- **Envelope implication.** All potential basis functions are monotone in
  s,d,-load. Exact balances justify the three free multipliers; transport
  and potential weights remain nonnegative. The verifier checks the full
  admissible local domain independently of the numerical builder and checks
  every strict gap after one-sided integer repair.
- **Heavy-degree split.** H counts actual heavy selected incidences, not
  total q. The additional routing inequality follows from the same unique
  exception argument as canonical threshold capacity. The normalized W, L,
  P and Z graph images have the displayed exact balances. Source group and
  label group multiplicities appear once in the appropriate incidence sums.
  The identity `n_k(n_l-[k=l])=n_l(n_k-[k=l])` validates the two orientations
  of P normalization. Self-pairs are excluded. Unit upper bounds are valid
  for all these fractions, which justifies rounding repair in the Farkas stage.
- **Final certificate.** Reconstructing the heavy model gives 12,570
  variables, 12,985 inequalities and 690 equalities. Every inequality
  multiplier is nonnegative, every resulting variable coefficient is
  nonnegative, and the integer right-hand side is -998,530. Numerical
  infeasibility is not used as proof evidence.

## Implementation and preservation checks

The verifier matches every saved state ID to the independently generated
frontier vectors, rejects duplicate coverage, and requires each stage's
input set to equal the preceding unresolved set. Its complete report contains
3,018,781 local envelope checks and zero unresolved states. All 620 zero-demand
states are separately accounted for.

The fixed and adaptive sweeps preserve every unsuccessful proposal status.
The numerical feasible point from the older RX/Hall model is also retained,
together with the code and exact input that produced it. That point is labelled
as a relaxation point rather than a graph or a counterexample.

Lossless storage records the original hashes and decodes back to the original
JSONL bytes. Clean-copy replay uses the stored streams without the raw scratch
files. The reviewer release records its actual replay and link-check results.
The original exhaustive demand enumeration is reused unchanged from the
previous byte-for-byte reproduction; it was not rerun as new evidence here.

The envelope verifier is separately implemented. The heavy-stage verifier
uses the same pure-integer model specification as discovery and independently
checks its integer linear combination. That shared specification remains a
review dependency, not a second independent implementation of the graph model.

## External review priorities

Review the canonical bridge and the source-capped/heavy-routing implications,
then the normalized graph image in `HEAVY_SPLIT.md`, and reproduce the complete
saved certificate streams and the original frontier independently. The existing
dominating-edge literature dependency remains required through the prior
bound/reduction package. No new literature theorem or novelty claim is added.
Internal exact replay and repository publication are not external acceptance.
