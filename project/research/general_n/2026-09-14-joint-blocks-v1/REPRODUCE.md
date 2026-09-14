# Reproduce shared-slack research and its negative experiments

Run from a checkout of `paullenz/MurtySimon742` with Python 3 and a C++17 compiler named `g++`. Python code uses only the standard library. No live Actions artifact download, optimizer, private token or network request is required.

```sh
python3 project/research/general_n/2026-09-14-joint-blocks-v1/run_replay.py \
  --outdir /tmp/shared-slack-replay
```

The command can be launched from another working directory; `--repo` optionally names the checkout explicitly. Do not use Python `-O`: assertions are verification checks. All generated files go to the specified output directory. The script neither writes to the canonical ledger nor promotes a profile or state.

## What is checked

The replay first checks seven exact source Git blobs. It reruns the PARENT conditioned verifier and compares its entire canonical JSON both to the pinned hash and to the durable parent output. It then runs the new arbitrary-block/incidence/brute-force verifier and checks every value of the committed shared-slack result. This prevents an inherited rejected branch from being treated as proof solely because a previous summary listed its ID.

Next it regenerates the fresh seed using the original hash-pinned generator/scanner and verifies the entire raw corpus and generator totals. The fresh-corpus replay must match every value in the committed fresh output, including all seven non-rejected arrays and all three new complete branch certificates. Finally it reproduces the unsuccessful multiblock experiment and checks its ENTIRE output digest, not merely its headline counts.

Canonical JSON means UTF-8 `json.dumps(value,sort_keys=True,separators=(',',':'))`, with no trailing newline before hashing:

| Output | Canonical SHA256 |
|---|---|
| Parent conditioned replay | `7a29e4b93739f676fe2f11701235d0982d621b85b1086de7ece057723221455e` |
| `SHARED_SLACK_FULL.json` | `35d4c3c05595102b2a568d986d8bab753059da4a2c59b31689a550aaddb23ce6` |
| `FRESH_RECHECK_FULL.json` | `754774a0d4fdb23c8403efe4c5e41f2df950ebf933f903ca7e3d335d6ce370f9` |
| `MULTIBLOCK_FULL.json` | `d979d53bad1239b65442265b477594cffa05ec67750d8be6b3123add2b2b5127` |

The fresh raw TSV SHA256 is `f0e32e99a66d51027d1ad89d9f3874a8d50b3d4d215e8e1dd0d816786504dc2e`; its seed is 74220260919. It is a different row namespace from the original 713-profile corpus, hash `157db7e1f48261626eac8cb99bf875f4aec3b707d4c024f62989dd1bcec38572`.

## Actual test and transfer status

The new shared-slack verifier, portable fresh replay, portable multiblock explorer and fresh regeneration helper were executed locally. Their outputs reproduce the complete frozen values. Repository source blobs and both committed complete result blobs were fetched and matched to those locally executed/source-result bytes.

The combined `run_replay.py` harness additionally reruns the parent proof; its whole end-to-end invocation is a SEPARATE new CI gate, not something to infer merely from the completed component tests. Workflow `.github/workflows/verify-shared-slack.yml`, run34898768799, was queued when first inspected. Read its latest job and all frozen-value checks before claiming remote PASS. This is new-scope verification, not a retry or duplication of the 256-shard relational audit.

The compiler reports an inherited warning that the renamed original scanner main reaches the end of a non-void function. The synthetic generator supplies its own main and does not call that renamed entry point. The original bytes are hash-pinned and were not silently edited; compilation and the exact corpus check completed.

## Data preservation and coverage

`SHARED_SLACK_FULL.json` and `FRESH_RECHECK_FULL.json` are complete committed result objects, not excerpts. The original six non-rejected arrays remain addressable in the committed parent twelve-profile input. The seven fresh non-rejections are included in the fresh result. The earlier original corpus, scanner, 812 diagnostic, parent full output and provenance manifest are in the committed evidence-preservation durable directory.

The larger multiblock output and the fresh full raw TSV are reconstructed deterministically by the committed code from committed inputs and bound by the hashes above. They are also retained in the portable session bundle and uploaded by the new CI. They are NOT claimed to be raw files already committed in this directory. The multiblock output includes all 454 retained tuples; no further profile exclusion resulted from that experiment.

The old sample changes from704/713 to707/713 via three new profile exclusions; the fresh sample has708/715 rejected after all preceding/new screens. Both are necessary-condition reconnaissance, not complete scalar-state scans or actual graphs. The new local random incidence checks are a separate domain and need not satisfy the positive-surplus graph ledger.

## Audit and review boundary

No failed hash or frozen-value comparison may be weakened. A failure requires classification and preservation. The canonical frontier remains1971 exclusions /3607 survivors /977 whole-state closures, and the2655 recovered relational candidates remain unpromoted until their separate full-coverage, dual-agreement, zero-unresolved, aggregate and reviewed-ledger gate passes.

Same-assistant independent implementation, successful local or remote arithmetic, durable data publication, specialist mathematical acceptance and third-party reproduction remain distinct.
