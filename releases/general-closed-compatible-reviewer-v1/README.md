# Closed compatible potential — reviewer v1

12 September 2026. Candidate general exact formula and finite applications.
External mathematical review, novelty and independent reproduction OPEN.

This package reviews the [preceding catalogue checkpoint](../general-compatible-catalogue-reviewer-v1/README.md)
and removes the remaining degree enumeration from its recurring potential.
The general formula needs at most **59 explicit candidate values per source
residual and sender class**, independently of graph order, and permits a
variable ordinary eligibility cutoff.

Read:

1. [Overview and exact scope](../../project/research/general_n/2026-09-12-closed-compatible-potential-v1/README.md).
2. [General hand derivation](../../project/research/general_n/2026-09-12-closed-compatible-potential-v1/CLOSED_POTENTIAL.md).
3. [Review of preceding work and audit of the continuation](../../project/research/general_n/2026-09-12-closed-compatible-potential-v1/AUDIT.md).
4. [Frozen experiment](../../project/research/general_n/2026-09-12-closed-compatible-potential-v1/EXPERIMENT.json), [full verification](../../project/research/general_n/2026-09-12-closed-compatible-potential-v1/verification.json), [local challenges](../../project/research/general_n/2026-09-12-closed-compatible-potential-v1/local_verification.json) and [failed shortcuts](../../project/research/general_n/2026-09-12-closed-compatible-potential-v1/shortcut_counterexamples.json).

The fixed cutoff-2 family excludes 708 cases over the full threshold search;
the variable-cutoff family excludes 832. **All were already handled by the
preceding combined record.** There are zero new exclusions, and the combined
frontier remains 994 exclusions and 4,584 survivors. The earlier qualified
707 count concerns the old recorded winning thresholds; one additional case
is found at a later threshold and was already excluded by another potential.

## Reproduction

From the repository root, using Python's standard library:

```sh
python releases/general-closed-compatible-reviewer-v1/check_manifest.py
python project/research/general_n/2026-09-12-closed-compatible-potential-v1/check_local.py
python project/research/general_n/2026-09-12-closed-compatible-potential-v1/verify.py
python project/research/general_n/2026-09-12-closed-compatible-potential-v1/check_shortcuts.py
```

The archived closed-form and full-enumeration outputs agree byte for byte.
The verifier checks coverage of all 5,578 states, 476,427 gaps and all 28,591
old recurring-potential gaps. The local challenge covers 39,902 parameter
tuples; the hand proof supplies the unbounded result. Same-assistant
implementations are not described as external independent review.

The [clean release validator](validate_release.py) also requires g++/C++17.
It regenerates both full result streams independently, checks their original
hashes, removes raw files, and verifies the preserved archives. It separately
reproduces the local challenges and invalid-shortcut examples. The [validation
report](VALIDATION.json) records the actual checks; original timings remain
preserved rather than replaced by fresh timings.

## Dependencies and scope

The candidate formula depends on the canonical graph bridge and the compatible
routing potential implication. Its hypotheses include a>=2, b>=a, rho>=1 and
h>=2. It is a constant-size local formula with explicit case distinctions,
not a single polynomial or a constant-time graph proof. Global source and
sender-count coverage remain necessary; local maxima need not coexist.

The [manifest](MANIFEST.json) pins this package, current navigation, direct
inputs, evidence and preceding current manifests. Its full baseline commit
pins unchanged transitive evidence. It excludes itself and the publication
receipt to avoid circular hashes. Five logical streams are preserved in four
unique stored streams because the independent outputs are byte-identical.
Their separate original logs and timings remain available.

The negative full-pool result is part of the deliverable. The next bounded
experiment should test whether allowed local capacities can coexist under an
actual assignment of arcs on a small survivor sample. No new fixed-order
theorem, improved 7/12 threshold or unrestricted proof is claimed. Paul handles
external review separately.
