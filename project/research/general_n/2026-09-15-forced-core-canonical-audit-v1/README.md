# Canonical forced-core audit checkpoint v1

Date: 15 September 2026.

This package preserves reconnaissance and independent-audit evidence obtained while the exact 306-state GitHub discovery scan remains in progress. **It does not promote any canonical closure.** The official finite frontier remains 4,626 exclusions / 952 survivors / 3,632 whole-state closures.

## Certified survival lower bound

The promoted-relational frontier has 952 survivors. The stored-witness screen proves 646 survive the forced-core theorem immediately. This package preserves **124 additional, pairwise distinct, explicit replacement `q` witnesses** that pass the pre-existing relational screens and the forced-core theorem. Therefore this route has at least

```text
646 + 124 = 770 definite survivors,
952 - 770 = 182 states at most still eligible to become new closures.
```

All three N35 survivors remain among the definite survivors; the unresolved closure candidates are N34-derived. `CERTIFIED_RESCUES.tsv` records one exact witness per rescued state. Candidate generation was heuristic in places, but certification was exact: a rescue is recorded only after the candidate passes every old relational acceptance stage and the new forced-core test.

## Independent closure audit

`scan_forced_core_types.cpp` is an independently structured implementation. It enumerates equal-`rho` classes by type multiplicities rather than the primary scanner's nondecreasing `q` vectors, uses closed type-count formulas for potential-pair degrees, and retains an independent flow implementation.

For **24 whole-state exclusions**, the independent implementation agrees with the primary implementation field-for-field on the complete profile count and every stage count. Those states are recorded in `INDEPENDENT_CLOSURE_MATCHES.tsv`. This is strong internal audit evidence, but these closures remain discovery/audit candidates until the full 306-state coverage, aggregate key check and reviewed promotion gate complete.

## Performance note

Most unresolved states are dominated by the `r=1,h=1` core. `scan_forced_core_h1fast.cpp` replaces the generic core-label partition DP by the exact one-dimensional specialization in that case and falls back to the generic routine otherwise. It reproduced the primary scanner's exact stage counts on regression closures before being used for local ranking. It is an optimization only; it does not alter the accepted condition.

## Search methods and scope

The preserved BFS and multi-jump scripts search for later relationally feasible `q` witnesses around or away from stored witnesses. Failure to find a witness is **never** treated as exclusion evidence. Only complete exact enumeration may close a state. The scripts are preserved because they revealed disconnected survivor components (for example state 2548) and materially reduced wasted exhaustive work.

## Active remote run

The authoritative discovery workflow is GitHub Actions run `34950746007` on commit `25fd9044e9d8ef52326d27f9a97732916aef5dc4`. The run is progressing in runner-limited waves; later matrix jobs remain queued while long exact shards execute. No restart or weakened acceptance criterion is used here.

External specialist review remains OPEN.
