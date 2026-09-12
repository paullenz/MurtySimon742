# Compatible routing: bounded pilot and general envelope

12 September 2026. Candidate mathematics; external review and novelty OPEN.

The pilot succeeds at its stated gate: selected-degree destination eligibility
gives **16 additional exact exclusions beyond retaining selected degrees** in
a frozen sample of 29 states. These states came from the 5,578 survivors of
the preceding general-routing catalogue; their fixed-order candidate proofs
already had other certificates.

| Mode | Excluded sample states | Survivors |
|---|---:|---:|
| Catalogue-free optimization of the preceding heavy-only bound | 2 | 27 |
| Retain total selected degree q and its conservation | 3 | 26 |
| Add separate all-arc and forced-heavy destination-eligibility tails | 19 | 10 |
| Additionally couple the two traffic classes in mixed cuts | 19 | 10 |

The sets are nested. Of the 19 exclusions, two are attributable to extending
the multiplier search, one further exclusion to selected-degree information,
and sixteen further exclusions to destination eligibility. **Mixed cuts add
zero further whole-state exclusions in this sample.** These are bounded-model
comparisons, not claims of optimality over every routing model or potential.

The sample comprises 18 N34 m289 states, 10 N35 m306 states and the single
N35 m307 survivor. The final mode excludes 11, 7 and 1 respectively. All ten
sample survivors are listed in [verification.json](verification.json).
The sample was selected before any LP using first/middle/last state IDs in
each layer / historical method / zero-demand-presence stratum. It is not a
random sample, and its success rate must not be extrapolated to the full pool.

Read:

- [General compatible-routing inequalities and envelope](COMPATIBLE_ROUTING.md).
- [Compact hand exclusion of N34 state 4665](COMPACT_EXAMPLE.md): required 659,
  but source capacity is at most 636 or 628 for the only possible sender counts.
- [Audit and negative results](AUDIT.md).
- [Frozen pre-solver design](PLAN.md) and [full inputs](pilot_inputs.json).
- [Reviewer package](../../../../releases/general-compatible-routing-reviewer-v1/README.md).

The [independent verifier](independent_verify.py) reconstructs all 648 attempted
integer models from Cartesian domains and semantic row descriptions. It checks
321 integer certificates, 76,092 column inequalities and 275 capacity bypasses.
The [envelope extraction](extract_envelopes.py) removes LP normalization and
variable-bound rows. Its 321 positive envelopes are independently checked using
cardinality dynamic programming, again covering 76,092 source options. Minimum
integer envelope gap: 16. These counts include intermediate certificates and
multiple modes, not distinct excluded states.

The [routing check](check_routing.py) exhausts 15,756 light/heavy-coloured partial
orientations on one to four vertices, 94,536 residual-score/threshold settings,
and 3,090,516 mixed cuts. Its three invalid-extension examples are abstract
routings, not asserted D2C graphs. The compact proof's finite corroboration
checks 26,896 local options; its hand proof establishes the stated full scope.

## Reproduction

The exact verifiers require only Python's standard library:

```sh
python project/research/general_n/2026-09-12-compatible-routing-pilot-v1/verify_selection.py
python project/research/general_n/2026-09-12-compatible-routing-pilot-v1/independent_verify.py
python project/research/general_n/2026-09-12-compatible-routing-pilot-v1/verify_envelopes.py
python project/research/general_n/2026-09-12-compatible-routing-pilot-v1/check_routing.py
python project/research/general_n/2026-09-12-compatible-routing-pilot-v1/check_compact.py
```

Rediscovery needs NumPy/SciPy. Run `select_pilot.py`, then `probe.py`, then
`pack_evidence.py` before `extract_envelopes.py` and the exact checks. Packing
preserves a *new* discovery stream: use a separate checkout to retain the
original evidence. Readers prefer the encoded stream when its catalog exists.
The clean release validator instead compares a fresh discovery run with the
original while leaving the latter untouched.

Original solver statuses, objectives, vectors, rounding repairs and timings
are losslessly stored in `pilot_results.jsonl.gz.b64`, with hashes and byte
counts in [EVIDENCE_STORAGE.json](EVIDENCE_STORAGE.json). The original stdout
is [pilot.log](pilot.log); the exact environment and search limits are recorded
in [environment.json](environment.json). Original dual status 2 is a failure
to obtain a certificate, not a proof of graph or routing feasibility.

## Next decision and scope

The next justified step is to freeze a small catalogue of successful compatible
envelopes and test it, without an LP search on each case, against the complete
preserved pool. Prefer the simpler separate eligibility tails first; the mixed
cuts have no additional whole-state benefit demonstrated by this pilot.

That full-pool scan has **not** been run here. No new maximum-degree threshold,
new fixed-order result, actual graph construction or unrestricted proof is
claimed. Actual label/supplement compatibility involving label degrees and
residuals is still omitted. The established N34/N35 candidate ledgers and the
7/12 candidate remain unchanged.
