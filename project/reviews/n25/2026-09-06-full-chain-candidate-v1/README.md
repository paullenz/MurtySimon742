# Repository archive assembly

The complete evidence ZIP is stored here in two byte-contiguous parts. Download both, concatenate part1 followed by part2, and verify the SHA256 in ARCHIVE_RECEIPT.json. For example:

```sh
cat N25_Full_Chain_Candidate_Evidence_2026-09-06_v1.zip.part1 N25_Full_Chain_Candidate_Evidence_2026-09-06_v1.zip.part2 > N25_Full_Chain_Candidate_Evidence_2026-09-06_v1.zip
```

Then extract the ZIP and run the commands below from its N25_Full_Chain_Candidate_2026-09-06_v1 directory. The proof and source files are also exposed separately here for convenient reading. The joined ZIP is byte-identical to the saved single-file deliverable.

# N=25 complete candidate proof: reproducible audit package

Start with **PROOF.md**, then **RESULTS.md** and **RECONCILIATION.md**. The candidate conclusion is e(G)≤156 for every 25-vertex diameter-2-critical graph, with equality exactly for K_{12,13}. Internal mathematical reading and exact computational checks support the complete chain; external mathematical review remains outstanding.

## Contents

- `PROOF.md`: published inputs, all new hand arguments, necessary finite tests and theorem assembly.
- `RESULTS.md`: complete new parameter-band tables, state hashes and result counts.
- `RECONCILIATION.md`: relationship to the earlier canonical review and parked Delta=15 evidence.
- `general_primary.py`, `general_independent.py`: generalized versions of the separately written frozen Delta=14 arithmetic verifiers. They import no code from one another.
- `column_hall.py`, `check_column_certificates.py`: subset-capacity rejection search and a separate certificate/coverage checker.
- `compare_runs.py`: complete comparison of saved primary columns against the second implementation's canonical fingerprint.
- `reconstruct_columns.py`: byte-exact recovery of the redundant pretty-printed column JSON from the compressed ledger.
- `d15_157`, `d15_156`, `d14_156`, `d14_156_k1`: fresh summaries, complete compressed state/rejection/column ledgers and equality certificates.
- `d14_156_k1_independent`: independently generated boundary-case summary.
- `logs`: complete fresh execution logs and standard errors.
- `historical`: the prior Delta=14 review/replay bundle, original Delta=15 parked archive and its fresh preservation/arithmetic replay result.
- `chain_arithmetic.json`, `environment.json`, `MANIFEST.json`: exact hand-arithmetic tables, execution environment and integrity inventory.

All primary column records are preserved inside the compressed ledgers. The standalone, redundant pretty-printed column JSON files are omitted to avoid several gigabytes of duplicate output. `column_reconstruction.json` verifies that the included reconstruction script recreates their original bytes exactly. This is lossless preservation, not a removal of final states or capacities.

## Checking and replay

Python 3.10 or later and its standard library suffice for the new arithmetic. The recorded interpreter is in environment.json. No SAT solver, graph catalogue, floating-point optimizer or third-party graph library is needed.

From an extracted package:

```sh
python3 -I -B reproduce.py --verify-only
python3 -I -B reproduce.py --replay --output /absolute/path/to/new-replay
```

Verification checks the manifest and all equality rejection certificates. A full replay regenerates both arithmetic scans for all new scopes, compares all states and columns, and checks the newly regenerated equality certificates against their preserved hashes. It writes into a new directory and leaves the evidence untouched. The k=1 replay is the largest part: 3,252,212 labelled columns, several gigabytes of transient memory/output and several minutes of computation on the recorded environment. The compressed ledger is about 15 MB.

The unchanged Delta=14/e157 verifiers and their original tests are in the nested historical review ZIP, together with the exact input document, fresh logs and a separate manifest. Its review gives the commands to rerun that original domain. The parked Delta=15 ZIP likewise includes its own integrity/replay tools; that old proof is not a premise of the new route.

To inspect just the new equality certificates without rerunning enumeration:

```sh
python3 -I -B check_column_certificates.py d14_156/primary_ledger.jsonl.gz d14_156/hall_certificates.json
python3 -I -B check_column_certificates.py d14_156_k1/primary_ledger.jsonl.gz d14_156_k1/hall_certificates.json
```

For a byte-exact reconstruction of the omitted redundant output:

```sh
python3 -I -B reconstruct_columns.py d14_156_k1/primary_ledger.jsonl.gz --output /absolute/path/to/primary_column_cases.json
```

Computational agreement checks the stated finite inequalities. It does not independently establish their graph-theoretic premises or constitute external expert approval.
