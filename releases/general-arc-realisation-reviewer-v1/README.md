# Fixed-neighbourhood routing flow — reviewer v1

12 September 2026. Candidate general conditional criterion and exploratory
evidence. External mathematical review, novelty and independent reproduction
remain OPEN.

For fixed selected/residual cross-neighbourhoods, the new argument identifies
exactly which labelled directed pairs are compatible with B-side quasi-edge
domination. Their labels and orientations are unique, so routing becomes an
integer flow problem. Failure has a checkable Hall obstruction for that fixed
cross pattern. This is not a criterion for a full diameter-two edge-critical
graph or an exclusion of every cross pattern with the same degree sequences.

Read:

1. [Overview and negative outcomes](../../project/research/general_n/2026-09-12-arc-realisation-pilot-v1/README.md).
2. [General proof and receiver-label conflict lemma](../../project/research/general_n/2026-09-12-arc-realisation-pilot-v1/FIXED_NEIGHBOURHOOD_FLOW.md).
3. [Audit, invalid shortcut and scope limits](../../project/research/general_n/2026-09-12-arc-realisation-pilot-v1/AUDIT.md).
4. [Exact model specification](../../project/research/general_n/2026-09-12-arc-realisation-pilot-v1/MODEL.md), [frozen inputs](../../project/research/general_n/2026-09-12-arc-realisation-pilot-v1/pilot_inputs.json), [original results](../../project/research/general_n/2026-09-12-arc-realisation-pilot-v1/runs/results.json), and [full verification](../../project/research/general_n/2026-09-12-arc-realisation-pilot-v1/verification.json).

All twelve solver attempts on six frozen survivors reached a time limit
without an incumbent. Twelve deterministic cross patterns have exact flow
obstructions, but all lack some compatible destinations and already violate
minimum endpoint loads. No added strength over the previous frontier bounds
is demonstrated. **Zero whole-state exclusions are added; 4,584 survivors
and the earlier 994 exclusions remain unchanged.**

## Reproduction

Python's standard library suffices for all preserved-evidence checks:

```sh
python releases/general-arc-realisation-reviewer-v1/check_manifest.py
python project/research/general_n/2026-09-12-arc-realisation-pilot-v1/check_flow.py
python project/research/general_n/2026-09-12-arc-realisation-pilot-v1/check_model.py
python project/research/general_n/2026-09-12-arc-realisation-pilot-v1/verify.py
```

The flow criterion agrees with every direct assignment on 729 tiny cross
patterns. An additional 5,024 compatible tiny patterns challenge its derived
constraints; 8,192 cases compare the linear row encoding with direct objects.
All twelve original models, totalling 109,035 rows, are rebuilt byte for byte.
No time-limited solver termination is treated as a certificate.

The [clean validator](validate_release.py) copies only tracked files to a
temporary directory and reproduces all deterministic checks and fixed-pattern
certificates. Its [report](VALIDATION.json) distinguishes this from fresh
solver execution. SciPy/NumPy are needed only for new solver attempts, for
which the research README supplies a separate output-directory command.

The [manifest](MANIFEST.json) pins this checkpoint, its current navigation,
direct graph-bridge and previous survivor inputs, and the preceding current
manifests. It excludes itself and the publication receipt to avoid circular
hashes. Original solver logs, exact encoded models and failed approaches are
part of the package. Historical theorem proofs, ledgers, forecasts and the
candidate 7/12 maximum-degree threshold are unchanged.
