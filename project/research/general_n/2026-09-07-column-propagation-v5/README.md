# Column propagation v5: complete original checkpoint

7 September 2026. Repository publication after Paul uploaded the original ZIP.

**Candidate mathematics; creation-session exact arithmetic REPRODUCED; independent mathematical review OPEN.** No complete order 28, improved uniform coefficient, full shared-adjacency search, novelty determination or theorem-ledger promotion is claimed.

## Start here

Read the unchanged [original proof](PROOF.md), [exact results](RESULTS.json), and [review and handoff](REVIEW_AND_HANDOFF.md). These readable mirrors are byte-identical to their counterparts inside the [complete original ZIP](MurtySimon_GeneralN_ColumnPropagation_v5.zip). All 54 original payload files plus MANIFEST.json are in that archive, including code, input data, exact certificates, tests, historical reports, intermediate work and the final survivors. Nothing must be recovered from the earlier uncommitted multipart uploads.

The ZIP was uploaded to the repository root in commit `ff96063742208920e14526546d178b5c2cef4a6b`. This publication moves the same Git blob into this folder; it does not recompress or regenerate the archive.

| Archive property | Verified value |
|---|---|
| Bytes | 1,035,233 |
| SHA-256 | `79bdbdf02b23b9eef38e964b54eb300921b24d539014f07b476655d1575e63b6` |
| Git blob | `032bdf75157a8898f3e5381e18fdb42dd8e9ff02` |
| Contents | 54 manifested payload files plus the original manifest |

## Recover and replay

From this directory in a repository checkout, verify the ZIP and readable mirrors, then optionally extract into a NEW directory:

```sh
python3 -I -B verify_archive.py
python3 -I -B verify_archive.py --output /absolute/path/to/new-v5-extraction
cd /absolute/path/to/new-v5-extraction/MurtySimon_GeneralN_ColumnPropagation_v5
python3 -I -B replay.py --verify-only
python3 -I -B replay.py --check --output /absolute/path/to/new-v5-check
python3 -I -B replay.py --replay --output /absolute/path/to/new-v5-replay
```

Integrity verification and extraction use Python's standard library only. Full arithmetic checking additionally requires g++ with C++17 and Boost headers, but no optimisation solver or network. Keep assertions enabled: never use `-O`. The original replay wrapper writes to a fresh working copy and preserves historical evidence. `--check` runs the complete separate checking route; `--replay` also regenerates discovery outputs. The optional `--smoke` mode documented inside the ZIP checks only the first 100 rows plus other specified checks, not the entire row domain.

This publication verified the archive hash, CRCs, all 54 payload hashes, readable mirrors, extraction, and the original wrapper's `--verify-only` mode. It did NOT rerun the full mathematical computation. Creation-session full-check reports remain preserved unchanged and are distinguished from publication integrity checks.

## Scope and frontier

At **n=28, maximum degree 15, m=196**, the 13,196 v4 input rows reduce to 7,725 after joint column/matching/one-source tests, then to **6,918 rows in 830 demand patterns** after 663 activation-cost and 144 activation-cut certificates. The 47 short block certificates overlap these exclusions and are not counted again. The active frontier is `evidence/FINAL_SURVIVORS.json` inside the extracted package.

The general supplement-activation inequality gives the hand contradiction **78 > 57** for a specified retained row and excludes a specified infinite family of demand/residual patterns. These are profile exclusions, not completed orders. The uniform coefficient `(10-sqrt(2))/14` remains unchanged.

Different source rows may still have different witnessing full column assignments. The next target is one common assignment across multiple sources and shared neighbourhood constraints. The finite v5 calculation covers **196 edges only**; higher edge-count coverage remains OPEN. Surviving numerical rows are not constructed graphs.

## Preservation and review boundaries

The original README and provenance inside the ZIP are unchanged. Their historical statement that v5 had not been committed is superseded by this publication. Earlier partial blob uploads were not a completed checkpoint; this archive is now the complete evidence entry point. This README is a publication wrapper, not a replacement for the original mathematical record.

Both original implementations were written by ChatGPT/Geeps under Paul Lenz's direction; they are not independent external review. Actual-graph tests found no positive-surplus example and no positive activation-cost example in the saved sample. Universal lemma validity remains a mathematical review obligation.

The frozen n=25/n=27 candidates, previous research checkpoints and governed theorem ledger are not modified. The [commit-completion standing order](../../../REPO_SYNC_POLICY.md) remains in force. Publication preserves evidence; it does not certify mathematics.
