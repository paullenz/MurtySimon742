# N34 complete candidate: reviewer v2

12 September 2026. **Candidate e(G)<=289, equality exactly K(17,17).**
External specialist review, novelty assessment and external reproduction OPEN.

Reviewer v2 replaces the final large Farkas exclusion with a
[short hand theorem](../../project/reviews/n34/2026-09-12-heavy-independent-v1/HAND_PROOF.md).
The candidate conclusion is unchanged. The [whole-count audit](../../project/reviews/n34/2026-09-12-heavy-independent-v1/README.md)
also reconstructs every original model constraint separately and verifies a
translated exact certificate. Both historical certificates remain corroborating
evidence. The revised equality ledger is **6,709 hand/accounting exclusions
and 6,837 exact envelopes**, covering all 13,546 states.

## Proof assembly

Read the [original full N34 assembly](../../project/research/n34/2026-09-12-equality-v1/README.md),
retaining its degree reduction, upper layers and envelope exclusions. Replace
its last heavy-split Farkas step by the new hand theorem: for heavy label count
k and high-residual source count z, p<=4 on those sources implies `6k<=r+6z`.
The remaining state would require `78<=74`. No other proof step changes.

The new [v2 verification report](../../project/reviews/n34/2026-09-12-heavy-independent-v1/v2_verification.json)
has complete disjoint coverage and the same 3,018,781 local envelope checks.
No heavy model is built and no Farkas certificate is read in the v2 proof replay.
This removes the last large model from the proof-critical surface; it does
not remove the remaining finite envelope arithmetic.

## Replay

From the repository root, Python standard library only:

```sh
python project/research/n34/2026-09-12-frontier-v1/verify_upper_layers.py
python project/research/n34/2026-09-12-m290-v1/verify.py
python project/reviews/n34/2026-09-12-heavy-independent-v1/verify_hand.py
python project/reviews/n34/2026-09-12-heavy-independent-v1/verify_v2.py
python releases/n34-reviewer-v2/check_manifest.py
```

Optional corroborating normalization audit:

```sh
python project/reviews/n34/2026-09-12-heavy-independent-v1/compare_models.py
python project/reviews/n34/2026-09-12-heavy-independent-v1/verify_count_certificate.py
```

[MANIFEST.json](MANIFEST.json) pins the current artifacts and dependency
baseline. [VALIDATION.json](VALIDATION.json) records the clean replay and
navigation checks. The [historical v1 package](../n34-reviewer-v1/README.md)
remains available; its manifest applies to its original published snapshot.

The project now also has a [complete N35 candidate](../n35-reviewer-v1/README.md).
Neither result is externally accepted or an unrestricted all-order proof.
Paul Lenz directed the work; ChatGPT/Geeps supplied development and internal
checking. Separate internal programs are not external independent review.
