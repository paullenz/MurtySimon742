# Source-price publication and replay audit

14 September 2026. Mathematical scope, publication and remote verification are separate.

## Initial publication and inspected checks

Research commit: `788819f813e92d32470ff23783a9dc9faf7a4ce1`.

| Check | Run / job | Observed outcome |
|---|---|---|
| Paired status synchronization | 34904353538 / 104177438850 | SUCCESS |
| README reviewer navigation | 34904353444 / 104177437535 | SUCCESS |
| N30 package integrity and portable replay | 34904353499 / 104177437671 | SUCCESS |
| q-layer threshold normal form | 34904353463 / 104177437839 | All steps SUCCESS, including verifier and frozen totals |
| Original source-price replay | 34904353492 / 104177437867 | FAILURE before mathematics: result-file byte hash mismatch |

The failed log identified actual SHA256 `0705a7da14d49e81bd02f5442464b81b5796791454d5a3de8cace333bc74596c` instead of original expected `1953c61d26c68dc2bcbb9aeddbe0d18336e05b118541f4d9ca3f9528c808caae` for ORIGINAL_SIX_RESULTS.json. Source and copied-input hashes preceding this check passed. Later computations were not reached.

## Diagnosis: changed data, not whitespace

The assistant introduced one trailing zero into original row338's low-q-weight best-price vector: 29 entries instead of 28. Appending exactly that zero to the original local frozen object reproduces the ENTIRE remote file's SHA256. Removing it and serializing sorted compact JSON plus its original newline restores the ENTIRE original expected hash. The local finite verifier and all 576 price evaluations were rerun and matched the original complete objects.

The later diagnosis in commit `7504cfa5f9899b9e2b088fc07142e4445ca049bc` that this was only format-sensitive hashing was incorrect. Canonical JSON hashing cannot repair an additional list entry. This correction preserves that attempted repair in Git history and restores run_replay.py to its exact original Git blob `54d461e9813b3ad230fa1720b0031b7add594837`. No mathematical expected hash is changed. The conditioned-source-pricing research and separate price/witness package from concurrent commits remain intact; this correction concerns only the original result transfer and replay diagnosis.

## Guarded restoration

The dedicated restoration script accepts only the known bad full-file hash, removes exactly the diagnosed zero and requires the ORIGINAL expected full-byte hash before writing. Already-correct data are accepted unchanged; unknown versions are rejected. Local tests checked exact restoration, idempotence and rejection of unknown data.

The workflow performs that deterministic transformation on main, runs the original UNCHANGED offline harness, and requires source hashes, canonical twelve-row input provenance, copied six-row equality and both complete replay outputs to pass. Only then may it publish the corrected RAW JSON, this receipt and BOTH current-status documents in one atomic commit. It runs the reviewer-navigation and paired-status guards and uses a non-forced push and remote-ref verification. No repeated-integer array is manually retranscribed. A concurrent conflicting update is not overwritten. No relational audit is duplicated or modified.

The original bad publication and failed run remain failures in history. A later successful restoration/replay is a separate event. Its dated receipt is appended only after the full replay succeeds; final publication must also be checked. The original readable JSON schema remains unchanged.

## Scope

The original experiment retains 9,043 incidence/demand configurations, 371 brute-force DP comparisons, three hostile/boundary checks and 576 price evaluations, with four weighted improvements and ZERO new profile exclusions. This replay does NOT verify the separate stronger price/witness or conditioned-source-pricing packages. Those newer packages and their row471/label-destination research target remain preserved. External review, canonical counts and promotion gates are unchanged.
