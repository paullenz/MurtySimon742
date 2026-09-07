# Direct 197-edge exclusion at order 28 — v8

7 September 2026. **Candidate mathematics; complete direct arithmetic reproduced; independent mathematical review OPEN.**

Read [DIRECT_197_SUMMARY.md](DIRECT_197_SUMMARY.md), [RESULTS.json](RESULTS.json), and [EXACT_CHECK_REPORT.json](EXACT_CHECK_REPORT.json). The new direct route generates the entire (n,Delta,m)=(28,15,197), t=2 domain. It excludes every final row with exact integer certificates: 787 shared, 790 source-degree-type and 7 actual-endpoint-type contradictions, with zero survivors. No integer branching, t=1 survivor-list transfer or weak-core density reduction is used.

Other maximum degrees at 197 are excluded by degree sum, a short Delta=16 charging inequality, the general residual h-index bound, and the universal-vertex/star case. Fan's strict 197.2075 bound then supplies the candidate upper bound 196. Together with the separately preserved complete 196-edge equality route, this gives a complete candidate order-28 chain with equality only K(14,14). It is not independent acceptance, formal verification, a new uniform coefficient or a solution of the all-order conjecture.

## Complete evidence package

The complete original package is **MurtySimon_N28_197_Direct_v8.zip**, supplied in the research chat. It contains 90 payload files plus MANIFEST.json, including all source, initial tuples and exact certificates, full handoffs, final certificates, tests, original review reports and proof texts. No prior ZIP is required to replay the *new direct197 calculation*. The equality-level ancestor chain is separate.

Archive bytes: **5,677,524**.

SHA-256: `b753076ffc755066a0c57756be91cc5b265c163d869244d3aa65e3943799347b`.

Git blob computed from those original bytes: `45889e1b36f0bc395f9f39b9c18035b52ce74dbb`.

**This documentation publication does not attach that binary archive.** The committed files are a readable summary and exact reports, not a substitute for the full code/certificate ZIP. Use the original supplied archive; no regeneration of missing historical certificates is intended. Binary attachment will require a separate verified publication.

From the extracted package:

```sh
python3 -I -B replay.py --verify-only
python3 -I -B replay.py --check --output /absolute/path/to/new-v8-replay
```

The first checks integrity only. The second re-generates and checks every direct197 domain and certificate in a fresh copy; it uses standard-library Python and g++ with C++17/Boost, no optimisation solver or network. Do not use `-O`. Full clean replay passed and left the checked original payloads unchanged. The report and final packaging checks are separate from graph-theoretic certification.

## Earlier archive intake

Both local originals, SharedAdjacency v6 and LocalIncidence v7, passed their 88 and 87 payload checksums, and both complete separate checking routes were rerun successfully in fresh copies. The v3 n28/Delta=16 equality scope also rechecked all 39 demand profiles and 604 residual rows. The [intake reconciliation](../2026-09-07-v6-v7-intake/README.md) explains why their reported GitHub uploads were not moved: the repository did not expose the ZIP files, and the v6 blob reference returned HTTP 422. This publication does not claim that issue has been resolved.

The separate repository degree-load-v7 proof uses a different 173/215 final-stage partition and a weak-core reduction. LocalIncidence-v7 uses 22/19/347 at 196; v8 supplies a fresh 197-edge scope for that latter route. Shared lemmas, methods and authorship mean that these are not independent researcher endorsements.

Frozen n=25/n=27 proofs, other research directories and the governed theorem ledger are unchanged. Both implementations are by the same assistant. The saved actual-graph regressions contain no positive-surplus graph. Independent review of the universal structural lemmas and graph-to-model lifting remains OPEN.
