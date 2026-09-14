# Durable evidence and historical exploration — 14 September 2026

This package repairs a preservation gap: several capped-spill and block-pressure exploratory scripts and numerical outputs existed only in the portable ZIPs, despite their conclusions being summarized in the research notes. The readable source files here match those original source bytes. Five block-pressure JSON outputs retain all original parsed values; whitespace and object-key order are normalized. `prior.py` is a convenience copy of the already committed capped-spill verifier; `baseline.py` matches the already committed localized verifier.

## Scientific status

The `exploration` directories are historical research, NOT canonical verification entry points. Their original local `/mnt/data/...` paths are intentionally preserved rather than silently rewritten. The dual experiment uses numerical optimization to search for candidate multipliers; its floating solver status is never a proof of infeasibility. The multiblock and weighted searches include zero/trivial inequalities and failed attempts. They do not imply optimality of the tested coefficient family. The proofs and separately written integer verifiers live in the linked main packages.

Start with:

- [canonical selected/residual bridge](../2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md);
- [localized excess](../2026-09-14-localized-excess-v1/README.md);
- [priced tails](../2026-09-14-q-tail-interval-budget-v1/PRICED_TAIL_BUDGET.md);
- [capped positive excess and all-source spill](../2026-09-14-capped-spill-v1/README.md);
- [block/source pressure](../2026-09-14-block-pressure-v1/README.md);
- [conditioned spill slack and the row-295 equality proof](../2026-09-14-conditioned-excess-v1/README.md).

## Large outputs and artifact dependency

The two large historical capped-spill outputs were regenerated locally and matched the originals BYTE FOR BYTE:

- `synthetic_results.json`: 120461 bytes, SHA256 `74ff677ed15b66eb57b8c20392de134bb8cb63307d37284115f45f2a967ee3bd`;
- `capped_results.json`: 137704 bytes, SHA256 `a2335c1292fe69e659e100626a2c9d35fbda1f6cfae523d7934e4edd456e3cc6`.

The corpus is the original 713-row stream, SHA256 `157db7e1f48261626eac8cb99bf875f4aec3b707d4c024f62989dd1bcec38572`. It is available in the completed combined replay artifact, not inferred from survivor IDs. A preservation helper and CI materialization step will copy hash-pinned raw evidence and regenerate these outputs into `durable/`; until a successful materialization record exists, do NOT claim those large files have been committed. The compact conditioned-result file already binds its entire deterministic replay by a canonical JSON SHA256, including unsuccessful branches.

The downloaded combined replay is run `34887492789`, artifact `10364839603`, archive SHA256 `08b3df5892c99c5fb8acc728052e1355ffe51a3af2d6d965c248d2003fe0e5a1`. Its capped and block actual/expected outputs were compared locally as complete parsed objects and agreed. Its complete audit snapshot at 2026-09-14 19:43:10 UTC contains 257 jobs: the successful plan, 128 successful audit shards and 128 queued shards. That is a timestamped snapshot, not a current full-audit success.

Raw evidence, deterministic reconstruction and manifest hashes are intended to remove dependence on temporary downloads. A workflow being queued is not materialization success. The original unsuccessful transfer attempts are documented in [TRANSFER_ERRATUM.md](TRANSFER_ERRATUM.md).

## Trust and coverage

This preservation pass covers the recent supplied localized/capped/block bundles and the new conditioned-excess checkpoint. It is not a fresh mathematical audit of every historical fixed-order manuscript or every repository file. The historical packages, reviewer index and canonical ledger remain untouched. Internal CI and same-assistant independently structured arithmetic remain distinct from external mathematical acceptance.

The 2655 relational candidates are not promoted by copying their audit evidence. Promotion still requires all candidates covered, exact agreement of both implementations, zero unresolved states, a successful aggregate and a separate reviewed ledger step.
