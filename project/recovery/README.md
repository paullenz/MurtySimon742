# Evidence recovery records

Latest: [intake 02](2026-09-06-upload-02.md) and [machine-readable checks](2026-09-06-upload-02-check-results.json).

Intake 02 recovers every payload in the full Delta=14 k=5/k=6 checkpoint manifest: 773 matched, zero missing and zero mismatched. The received ZIP is a repackaged container, not the original hash-pinned release. The nested k=7 tools ZIP matches its original pin exactly. Eight original source/status files have been restored to the checkout; bulk evidence publication and fresh full RUP replay remain outstanding. Delta=15/v4 and the later connected-k=2 corpus are not recovered by this batch.

[Intake 01](2026-09-06-upload-01.md) is retained as the historical partial-recovery record. Its 755 missing payloads are supplied by intake 02; it must not be read as the latest completeness assessment. The canonical recovery manifest is a frozen baseline and is supplemented by these dated receipts. No theorem status has been promoted.

The checksums in `2026-09-06-upload-02-artifacts.sha256` pin files recovered/generated in the conversation workspace; they do not imply that those archive bytes have been uploaded to this repository.
