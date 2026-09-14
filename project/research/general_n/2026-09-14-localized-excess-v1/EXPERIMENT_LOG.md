# Experiment and audit log — 14 September 2026

This is a same-assistant research checkpoint, not external acceptance. The local finite verifier completed; the instrumented wider scan did not. These evidence classes must remain separate.

## Repository synchronization

The requested restart commit was `0e6546e8947b43896d0c8f5eebde8335b8d95f11`. The first live head was `81560e92698d07992df4a53976ee1ea8efaaeb4d`, five commits ahead. These newer commits added a q-tail scanner/pilot, summed-tail pressure and the mincut JSON-comparison fix. During this session further work arrived concurrently: `94cbfd966f6fd913ad9f96bdc4b0ba835c530dbb` (selected-excess tail losses), `de82393062163dc2ffab10b90ba68ce4a0f7a741` and `d1e20da87e8d8dcda3633e550b8b5556b6e7c9ee` (interval budgets and verification), then `d6c818440c736367dae68bd425ce7e6df7fa0bed` (replay instrumentation and hostile searches). They were read and retained. The localized-cap theorem is an additional strengthening, not a replacement or reattribution of those identities.

## Completed local checks

The independent standard-library verifier completed all 133,586 exhaustive incidence configurations, 6,880 integer optimization cases, 3,000 seeded incidence mutations, all three standing hostile examples, both old surviving profile witnesses, and the full 812-row frozen diagnostic. Results are frozen in `LOCALIZED_EXCESS_VERIFICATION.json`.

Frozen input provenance:

- q-stratified pilot run `34859094097`, artifact `10356424619`, name `q-stratified-receiver-reach-pilot`; archive SHA256 `b91c48268fb6b2b3c6545b28ced230d4ab8ad71b371b49205af1b6166c2a63f4`;
- difficult-profile diagnostic run `34850187436`, artifact `10351372086`, name `layered-receiver-exception-diagnostic`; archive SHA256 `d856c6987acedfc824a85ddd2826ca05d35a4a724b5417c866a235deba17fe4e`;
- extracted diagnostic `LAYER_EXCEPTION_DIAGNOSTIC.tsv`: SHA256 `c4f859f97bed726f6e4799473906bd1673520aa2501d755fc5136a1c3cb46885`;
- extracted pilot input `Q_STRATIFIED_RECEIVER_REACH_PILOT_INPUT.txt`: SHA256 `6a2391d22d5a04734f340461545feecdcec78cf9d498af5091583bb2f3f20240`.

Replay:

```sh
python3 verify_localized_excess.py \
  --exceptions /path/to/LAYER_EXCEPTION_DIAGNOSTIC.tsv \
  --pilot-input /path/to/Q_STRATIFIED_RECEIVER_REACH_PILOT_INPUT.txt \
  > replay.json
```

Compare parsed JSON objects, not whitespace. Without the optional inputs the script runs all non-frozen tests, but that is not an 812-profile replay. The CI explicitly downloads both inputs and requires equality of the complete parsed output, including both hashes.

## Bounded C++ instrumented pilot — INCOMPLETE

A copy of the scanner from artifact 10356424619 was instrumented by `make_localized_excess_scanner.py`, compiled, and run against the original 15-state pilot input with a 240-second process limit. The experiment exited with timeout code 124. The output TSV remained empty because buffered output was not flushed before termination. The retained stderr line was:

```text
state 226 RELATIONAL_EXCLUDED E=-1 profiles=18086360 pairpass=135810 incpass=135810 sec=22.9833
```

This one progress line is NOT a complete durable audit table. No complete replay, new whole-state exclusion or frontier change is claimed from it. The two independently checked witness-profile exclusions stand separately and do not depend on this interrupted run.

The instrumentation preserves the source enumerator but inserts a new necessary cap before downstream tests. Existing `paircap_fail/pass` counters consequently include the localized-excess test and must not be compared as unchanged mathematical categories. Stronger caps can remove a former early-stopping witness and substantially increase the remaining search. A future full scan needs bounded/checkpointed per-state work and an independently implemented replay before promotion.

## Rejected shortcuts retained

1. **The two-defect identity plus the old cap/incidence relaxation cannot force a deficient tail on every relaxed profile.** The two explicit witnesses in the README have old target flow equal to Q and feasible selected incidence. The concurrent interval package also preserves broader synthetic target-Hall passes. The new localized inequality uses additional joint endpoint forcing to reject the two witnesses.

2. **Uniform weights do not explain all 812 profiles.** Old caps detect 476; localized caps detect 773, still leaving 39 uniform-weight misses. Exact/adaptive tails remain necessary for the current evidence. The exact old-cap fixed-weight obstruction is retained in the interval package and is not automatically transferable to new capacities.

3. **Two separate compatibility marginals are not generally exact.** For a tail T, write n_w=|T|-1_{w in T}, U_w=#{u in T:q_u>c_w+1}, V_w=#{u in T:c_u<q_w}. These deletion sets are disjoint. The upper bound min(P_w,n_w-U_w,n_w-V_w) exceeds exact capacity min(P_w,n_w-U_w-V_w) by

```text
min(U_w,V_w,(P_w-y_w)_+).
```

A preserved cap-formula-only counterexample has a=10,b=15,Esel=26,z=0,

```text
q=[1,0,4,0,5,1,0,0,4,0,4,2,8,0,8]
rho=[1,10,5,2,5,2,9,6,5,10,1,6,2,9,1]
P=[5,14,8,6,6,6,13,10,8,14,5,10,1,13,1].
```

At tau=1 the marginal gap at zero-based target 10 is 1. This example does NOT satisfy a positive-surplus scalar ledger (Q<r), and no demand/residual realization is claimed. It refutes unrestricted marginal exactness only. The verifier checks the exact gap identity on every frozen threshold. The concurrent interval package separately retains stronger frozen-domain examples of strict one-sided interval gaps.

## CI rechecks and classification

Statuses below are observations during this session, not promises of later completion.

| Run | Observed evidence | Consequence |
|---|---|---|
| `34854911792` relational cross-audit | Plan and first visible 29 audit shards succeeded. A later paginated read returned 257 jobs total and `audit (255)` still queued. No successful aggregate/full-coverage result. | 2,655 candidates remain unpromoted; frontier unchanged. |
| `34875592126` frozen ledger | Initially queued, then rechecked: verifier, combined survivor coverage and upload steps completed successfully. | Frozen-ledger CI is green. |
| `34871045562` q-layer threshold | Independent verifier and frozen-total checks completed successfully. | Threshold CI is green. |
| `34868771056` mincut exactness | Replay step succeeded; raw `diff -u` failed. Full job 104059179591 logs showed only list formatting changes in P_values, q_values, rho_values and final_witness. | Workflow JSON-serialization comparison problem; not mathematical disagreement or a verifier counterexample. |
| `34878019517` repaired mincut | Job 104089980265 still queued at recheck. Repair commit 81560e92698d07992df4a53976ee1ea8efaaeb4d compares parsed JSON without weakening value checks. | Repair exists; successful repaired CI is not yet claimed. |
| `34859094097` q-stratified pilot | Completed artifact retrieved and inspected: 201,493,148 generated profiles, 205,919 Hall failures, all 205,919 q-stratified detections and zero positive C_q. | Finite reconnaissance, not a universal crossing or tail theorem. |

The promoted frontier remains 1,971 exclusions / 3,607 survivors and 977 whole-state closures. External bridge review, novel-cap review, complete relational audit and separate ledger promotion remain distinct obligations.
