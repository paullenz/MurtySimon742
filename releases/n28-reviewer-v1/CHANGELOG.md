# Reviewer release v1 — editorial and engineering changes

Baseline: `cd3c22411911280624a8223035e6de2343abbb7c`, inspected 7 September 2026.

The new main paper consolidates the direct order-28 candidate, restates its structural arguments and separates all density/degree cases. The companion records evidence identity, full checking instructions and review obligations. The two papers do not claim a new theorem beyond the existing candidate or independent acceptance.

`review_check.py` is a new default-full-check entry point. It hashes and extracts six immutable archives, runs the component checkers, compares the five exact handoffs, and requires the new guarded v8 helper in a derivative copy. The original manifest is deliberately not rewritten to pretend the derivative is original. `OVERLAY.json` records that single-file difference.

`check_rows_hardened.cpp` implements the documented RT-01 guard defect's correction: range, ordering, count, duplicate, truncation and trailing-input checks before output creation, plus output checks. It is a new implementation of the fix, not the exact prior audit-patch bytes. Enumeration and mathematical rejection loops are unchanged. All 13 malformed tests and the entire valid direct197 residual domain passed the comparison.

The successful full driver run is recorded in `validation/REVIEW_CHECK_REPORT.json`; all eight jobs passed. Two preliminary wrapper launches used incorrect handoff filenames and were stopped before the final validated run. Matching original payload hashes located the correct filenames. No proof, original archive or certificate was changed to correct those path errors. `validation/PRELIMINARY_TEST_NOTE.json` records them. A preliminary PDF rasteriser used the wrong row stride; corrected rasterisation was used for visual review. A preliminary companion build used an unsupported fancyvrb option; it was removed before the successful document builds. These are release-development issues, not new mathematical defects.

The earlier audit remains the unchanged historical record. No complete re-audit of its alternative degree-load-v7 binary, no independent external assessment, no novelty determination and no theorem-ledger promotion is asserted here.
