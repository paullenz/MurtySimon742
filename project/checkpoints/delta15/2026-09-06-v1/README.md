# Delta=15 parked checkpoint — 6 September 2026, v1

## Governing handover status

**Existing project-level Delta=15 elimination retained. Arithmetic reproduction recorded. Final written-proof reconciliation, paper/code coverage corrections, complete external-audit publication and independent mathematical review remain outstanding. Delta=15-specific audit work is parked in favour of Delta=14.**

No mathematical branch status is promoted or changed by this checkpoint. This note does not certify the complete proof. Shared lemmas needed for new Delta=14 work remain live dependencies and must be justified before use.

## Actual preserved archive

Filename: `N25_Delta15_Parked_Checkpoint_2026-09-06_v1.zip`

Size: **1,636,826 bytes**.

SHA-256:

```text
99b1c5ec7eed0d0bab98c9ea89bea4105ceef0e02d0539020947f61aa035bfd0
```

The complete archive is saved in the user's persistent file Library at:

```text
/N25_Checkpoints/Delta15/2026-09-06-v1/N25_Delta15_Parked_Checkpoint_2026-09-06_v1.zip
```

Library file ID: `file_00000000a920820a9ff6c4ae1692a1a1`.
Library object ID: `libfile_32c72516611c8191a539181efee0449c`.

The uploaded Library archive was retrieved again and compared byte-for-byte with the locally created ZIP: identical. The checksum file, verification report and README are also saved in that Library directory. A separate download was provided in the canonical chat; the user's off-platform backup is not yet confirmed.

**This GitHub entry is the handover/index, not the full ZIP or the manuscript/code payload. The complete ZIP has not been published to GitHub. The Library location is not a public external-audit download link.** A future external-audit release must publish the actual complete evidence in an auditor-accessible location.

## Contents and completed preservation checks

The ZIP has 40 file members: 39 manifest-listed files plus `MANIFEST.json`. Its manifest SHA-256 is:

```text
d34043f0eeeef1e1e7e728ce98e8dc2f5d1869efb27c533117cb1b76a831b13c
```

It contains nine unchanged manuscript files (v2, v3, v5 and fresh-audit PDF/DOCX pairs, plus comprehensive-audit DOCX); both original arithmetic verifier scripts and their historical outputs; the complete earlier readiness ZIP and uploaded phase-1 prototype ZIP; previous and new rerun records; file provenance; a separately authored integrity/replay wrapper and tests; and explicit checkpoint status, open tasks and resume instructions.

All nine manuscript files match their earlier recorded SHA-256 pins. All archived files were read back and matched to the source bytes. ZIP CRC passes. A fresh extraction passes all 39 file checks and reruns both arithmetic scripts with assertions enabled; both outputs exactly match their historical originals. Eleven preservation-checker regression tests pass, including missing/corrupted evidence, unsafe paths, optimization mode and rejection of an external-audit claim.

These checks establish preserved bytes and arithmetic reproducibility, not the correctness or completeness of the graph-theoretic proof. The original sources have not been edited or silently reconciled. The historical documents retain their dated, sometimes superseded, scope; their Delta=14 tables must not overwrite newer project progress.

## Deferred work retained explicitly

- D15-P01: close the full written dependency/case chain, including parameter bounds and published complement/quasi-edge assumptions.
- D15-P02: integrate the full earlier k=6 and k=5 arguments rather than relying on imported status labels.
- D15-P03: reconcile the paper's k=5 component-enumeration description with actual v3/v4 main-loop coverage.
- D15-P04: map every exceptional numerical claim to a check or hand argument; printed values and matching stdout alone are not independent validation.
- D15-P05: review the finite-domain/optimization necessity and hand-only arguments, especially k=0 and connected k=1, r=15..19.
- D15-P06: publish the complete, dependency-closed external-audit dossier with actual evidence bytes.
- D15-P07: obtain and resolve independent mathematical review and reproduction against exact versions.
- D15-P08: recover and compare the original Audit-v4 FINAL PDF/DOCX. These remain unlocated; the v5 inherited text is not claimed byte-identical to them.

The full details are in `OPEN_TASKS.md` inside the ZIP. The phase-1 ZIP is retained as prototype history, not as a complete Delta=15 proof-certificate corpus.

## Resume and extend

Retrieve the exact ZIP, compare its outer checksum, and extract into an empty directory. From the extracted root:

```bash
python3 tools/verify_checkpoint.py --manifest-sha256 d34043f0eeeef1e1e7e728ce98e8dc2f5d1869efb27c533117cb1b76a831b13c
python3 tools/verify_checkpoint.py --replay
```

Read `CHECKPOINT_STATUS.json`, `OPEN_TASKS.md` and `RESUME.md`. For Delta=14, reconcile the current ledger with later preserved packages before choosing the frontier, and check the precise shared lemmas needed. Reopen Delta=15 upon a shared-dependency concern or before a complete N=25 theorem claim.

Keep v1 unchanged. Newly found Audit-v4 originals, corrections and substantive additions belong in a dated v2 with a change log, not an overwritten v1. The repository baseline inspected for this preservation was `ca2b8f850448e3cda560cbb0dbb6f831d9d98bbd`.
