# N30 equality frontier: hand classification of all 100 profiles

11 September 2026. Continuation from `d063c25445671c2588f5a619ecbc468e9698806d` in `paullenz/MurtySimon742`.

**Candidate hand classification with bounded arithmetic tables; exact audit REPRODUCED. Independent specialist review OPEN. No new reviewer edition or governed theorem-ledger promotion.**

The [written proof](HAND_CLASSIFICATION.md) derives precisely **70 profiles with maximum demand at most four, plus 30 containing fives**. A reverse-clipping argument excludes all profiles containing six or more. The 100-profile completeness conclusion is now supported by this candidate hand derivation, rather than only by the historical exhaustive demand sweep.

The proof uses explicit capacity tables and affine interval checks. It is not table-free: the [complete preimage arithmetic](PREIMAGE_ARITHMETIC.md) prints every interval, including rejected ones. The independent arithmetic methods in the checker agree on all 366 cap-five lifts and 225 cap-six lifts; it also checks the 365 entries underlying the cap-four classification and the clipping payment inequalities.

The [newly derived profiles](HAND_CLASSIFIED_PROFILES.txt) agree exactly with the historical list, but that file is not read during derivation. Their score distribution is `64 at Q=18`, `29 at Q=19`, `6 at Q=20`, and `1 at Q=21`.

Supplying this generated list to the existing [four-envelope checker](../2026-09-11-m225-resource-envelope-v1/verify_joint_certificates.py) reproduces all **211/211** tight-row contradictions, with four certificates and minimum exact gap one. See [ENDPOINT_REPLAY.json](ENDPOINT_REPLAY.json). The other 61 reconstructed rows remain excluded by the ledger identity.

## Read and reproduce

- [Hand classification](HAND_CLASSIFICATION.md).
- [Complete preimage arithmetic](PREIMAGE_ARITHMETIC.md).
- [Arithmetic audit](EXACT_AUDIT.json) and [checker](verify_hand_classification.py).
- [Internal review and its limits](INTERNAL_REVIEW.md).
- [Table-text/publication checks](PUBLICATION_CHECKS.json).
- [Handover and remaining obligations](HANDOVER.md).

From the repository root, using only Python's standard library:

```sh
python -I -B project/research/n30/2026-09-11-m225-hand-classification-v1/verify_hand_classification.py --profiles-output /tmp/n30-hand-profiles.txt
python -I -B project/research/n30/2026-09-11-m225-resource-envelope-v1/verify_joint_certificates.py --profiles /tmp/n30-hand-profiles.txt
```

The optional `--compare-historical` flag compares against the old list only after the new list has been derived. Neither the historical list, a solver, floating point, nor the original full multiset sweep is needed to derive these profiles.

## Next obligation

Review the full Delta=16 supplementary assembly, especially the bridge and all 211 explicit envelope evaluations, then account for the separate finite Delta=17 components before considering a replacement N30 reviewer edition. No complete hand-derived N30 replacement edition is claimed. The frozen N30 reviewer-v2 package remains the current review surface.
