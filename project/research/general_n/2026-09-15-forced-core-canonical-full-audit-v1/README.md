# Canonical forced-core full independent audit v1

Date: 15 September 2026.

This package freezes the completed forced-core discovery reconciliation and launches an exhaustive independent audit of every candidate whole-state closure. **It does not promote any canonical exclusion.** The canonical finite frontier remains **4,626 exclusions / 952 survivors / 3,632 whole-state closures** until a later reviewed promotion step.

## Completed discovery result

Authoritative discovery workflow: **34950746007**, commit `25fd9044e9d8ef52326d27f9a97732916aef5dc4`. The 256-way resumed exact enumeration and aggregate completed successfully with exact key coverage.

```text
promoted-relational survivors entering route: 952
stored witnesses already satisfying theorem: 646
states exhaustively rescanned:              306
rescanned survivors:                        136
candidate whole-state exclusions:           170
candidate N34 exclusions:                   170
candidate N35 exclusions:                     0
survivors of this forced-core route:         782
```

The 124 locally certified replacement witnesses in the predecessor audit package all reappear among the 136 exhaustive survivors. The remaining 12 survivors were found only by the full enumeration: `2454, 3145, 4453, 4618, 5163, 5672, 5972, 7664, 7851, 7927, 9014, 9849` (all N34).

The predecessor package's 24 independently audited whole-state closures are all members of the final 170-candidate set.

## Frozen audit inputs

- `DISCOVERY_AUDIT_INPUT_SUMMARY.json` records provenance and counts.
- `CANDIDATE_KEYS.tsv` and `RESCAN_SURVIVOR_KEYS.tsv` durably freeze the exact 170/136 classification.
- `prepare_audit.py` downloads the pinned run-34950746007 final and plan artifacts, checks their provenance and exact 306-key partition, verifies the 124+12 rescue reconciliation, and confirms the original 24 audit rows against the final primary counts.
- The same preparation step emits exact `AUDIT_INPUT.txt`, `PRIMARY_CANDIDATE_COUNTS.tsv`, `FULL_ENUMERATION_ONLY_RESCUES.tsv` and `RECONCILIATION.json` into the workflow artifact before any audit shard runs.

The discovery result is pinned to source relational SHA256 `2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970` and final workflow-artifact digest SHA256 `3a3b30ca8ba901f2687fc26370a9c684029c6340d73a7b7a6d485d961bee7fab`.

## Full independent audit

The workflow `.github/workflows/forced-core-canonical-full-audit.yml` reuses the independently structured type-multiplicity implementation from [`../2026-09-15-forced-core-canonical-audit-v1/scan_forced_core_types.cpp`](../2026-09-15-forced-core-canonical-audit-v1/scan_forced_core_types.cpp).

Each of the 170 candidates is recomputed from its original state data in a separate matrix job. For every state the comparator requires exact agreement on:

- `S`, `Emax`, and complete `profiles_tested`;
- every pair-capacity, incidence, pair-Hall, target-Hall, cost and forced-core pass/fail count;
- forced-core capacity/high-squeeze split;
- final `FORCED_CORE_EXCLUDED` status.

Wall-clock times and noncanonical “last rejected profile” diagnostics are deliberately not compared.

The aggregate requires exactly 170 unique keys, no missing/extra/duplicate rows and zero field mismatches. A mismatch is preserved as audit evidence and causes the aggregate to fail; it is never silently normalized away.

## Promotion gate

Even a completely green internal audit is **not** itself a canonical promotion and does not replace external mathematical review. A later reviewed step must reconcile the audited 170 keys against the current canonical ledgers, verify non-overlap/accounting, freeze the final artifacts/hashes, and only then decide whether to promote.

External specialist review remains OPEN.
