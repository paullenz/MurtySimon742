# Order-28 internal red-team audit — v1

7 September 2026. **No blocking defect found in the audited direct route. Independent mathematical review remains OPEN.**

Read the full [audit report](REPORT.md) and [exact summary](RESULTS.json). The audit follows the LocalIncidence-v7 equality route and direct197-v8 upper-bound route. The separate degree-load-v7 weak-core route was not computationally audited.

## Findings

The complete v3–v8 numerical sequence was replayed in fresh copies, all five equality-stage handoffs match byte-for-byte, and both density scopes finish with zero survivors. An additional integer arithmetic and branch checker verifies 8,983 certificate leaves and 833,923 cited constraint terms. It reuses the preserved model constructors, so it is not a third independent mathematical derivation. A fresh deterministic 107-graph regression finds no violation of the tested structural lemmas; none of those graphs has positive surplus.

One non-blocking defect was found in the standalone v8 C++ helper: an unsupported residual interval can return a successful empty report. The full Python proof driver rejects that input before invoking the helper. The additive guard patch rejects four malformed inputs and reproduces every result on the valid 8,216,928-row domain byte-for-byte. Frozen source and evidence are unchanged.

The direct order-28 statement remains a complete candidate argument, not an externally certified theorem. The original Fan proof, formal-kernel verification and independent researcher endorsement are not claimed.

## Recover the complete audit package

All 76 original audit payload files and their manifest are preserved losslessly in four hash-pinned text parts under `storage/`. These contain the full report, source, guard patch, exact fresh reports, graph inputs, command logs and portable replay driver. `STORAGE_MANIFEST.json` pins every part and the 44,624-byte tar.xz stream. This storage recovers the exact original payloads; it does not reconstruct the byte stream of the separately supplied distribution ZIP.

From this directory in a repository checkout:

```sh
python3 -I -B recover_audit.py
python3 -I -B recover_audit.py --output /absolute/path/to/new-audit-extraction
cd /absolute/path/to/new-audit-extraction/MurtySimon_N28_RedTeam_v1
python3 -I -B run_audit.py --verify-only
```

Recovery checks all storage hashes, safe archive paths, exact manifest membership, all 76 payload lengths and SHA-256 hashes, and the readable report/summary mirrors before writing. The output directory must be new. It uses Python's standard library only.

## Replay the audit

Obtain the six original proof ZIPs named and hash-pinned in the recovered `evidence/ARCHIVE_INTAKE.json`: v3, v4, v5, v6, LocalIncidence-v7 and v8. The v3/v4 repository guides recover their original ZIPs; v5–v8 have archive entries. Use those originals, not newly generated replacements.

```sh
python3 -I -B run_audit.py --check --archives-dir /absolute/path/to/original-zips --output /absolute/path/to/new-audit-run --jobs 3
```

Checking requires Python 3.10+, g++ with C++17 and Boost headers, but no optimisation solver or network. Keep assertions enabled. The complete combined driver was executed: all 13 jobs passed. The recovered README distinguishes that full execution from the final packaging integrity check and documents failed preliminary test-harness attempts rather than concealing them.

The original mathematical archives are dependencies, not duplicated inside this audit. Their [verified relocation receipt](../../../research/general_n/2026-09-07-v6-v7-intake/ARCHIVES_PUBLICATION_RECEIPT.json) records v6/v7/v8 publication. No frozen n25/n27 proof or governed theorem-ledger entry is altered by this audit.
