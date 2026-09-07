# Direct 197-edge exclusion at order 28 — v8

7 September 2026. **Candidate mathematics; creation-session complete direct arithmetic REPRODUCED; independent mathematical review OPEN.**

Read [DIRECT_197_SUMMARY.md](DIRECT_197_SUMMARY.md), [RESULTS.json](RESULTS.json) and [EXACT_CHECK_REPORT.json](EXACT_CHECK_REPORT.json). Full proof, code and exact certificates are in the [complete original ZIP](MurtySimon_N28_197_Direct_v8.zip), now attached to this directory.

The fresh (n,Delta,m)=(28,15,197), t=2 calculation excludes every final row: 787 shared, 790 source-degree-type and seven endpoint-type certificates, with zero survivors. No integer branching, t=1 survivor-list transfer or weak-core density reduction is used. Other maximum degrees at 197 are covered explicitly; Fan's strict 197.2075 bound supplies the candidate upper bound 196. The separately preserved equality chain supplies the equality characterization K(14,14).

## Archive and replay

The unchanged archive uploaded by Paul in commit `9698513eb20817ebfa9556e79b11d5f538280065` contains 90 payload files plus MANIFEST.json. It is 5,677,524 bytes; SHA-256 `b753076ffc755066a0c57756be91cc5b265c163d869244d3aa65e3943799347b`; Git blob `45889e1b36f0bc395f9f39b9c18035b52ce74dbb`.

Publication intake checked CRCs, safe paths, exact manifest coverage and every payload length and SHA-256. Extract into a fresh directory and, inside `MurtySimon_N28_197_Direct_v8`, run:

```sh
python3 -I -B replay.py --verify-only
python3 -I -B replay.py --check --output /absolute/path/to/new-v8-replay
```

Integrity checking uses Python's standard library. Complete arithmetic checking also requires g++ with C++17 and Boost headers, no optimisation solver or network. Keep assertions enabled; do not use `-O`. No prior ZIP is needed for the new direct197 replay; the equality chain is a separate dependency.

## Provenance and review boundaries

The [previous directory guide](README_before_archive_publication.md), earlier PUBLICATION_RECEIPT.json and the original files inside the ZIP preserve the historical documentation-only state. Their statements that the binary archive was pending are superseded by this publication, not silently rewritten as historical successes.

The [v6 archive](../2026-09-07-shared-adjacency-v6/README.md) and [LocalIncidence-v7 archive](../2026-09-07-local-incidence-v7/README.md) are now attached too. They are distinct from the separate degree-load-v7 audit bundle, whose availability remains separately recorded.

A full direct197 check was recorded in the creation session, with fresh v6/v7 and Delta16 checks. A fresh full-chain red-team audit is being conducted separately; this publication does not pre-announce its outcome. Universal lemmas, graph-to-model lifting and upstream coverage remain mathematical review obligations. Both original implementations are by the same assistant, not independent researchers. Frozen n25/n27 proofs and the governed ledger are unchanged.
