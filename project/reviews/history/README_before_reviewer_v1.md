# Murty–Simon n=25 / Erdős Problem #742

Private working repository for the n=25 Murty–Simon project.

## Canonical coordination and review

The user designated the 6 September 2026 chat opened with “make this now the canonical chat for N=25” as the canonical coordination chat. GitHub remains the durable record.

- [Canonical review and consolidated branch status](project/CANONICAL_N25_REVIEW_2026-09-06.md)
- [Canonical 40-task backlog](project/CANONICAL_TASKS.json)
- [Evidence-recovery manifest](project/EVIDENCE_RECOVERY_MANIFEST.json)
- [Inspected baseline inventory](project/BASELINE_REPOSITORY_INVENTORY_2026-09-06.json)

## Governing mathematical status

The existing project mathematical baseline is **Audit v5 (6 September 2026)** plus the preserved Delta=16 and Delta=17 notes. It does **not** claim that n=25 is solved.

The current theorem ledger records:

- any order-25 counterexample is reduced to `e(G)=157` and `Delta(G)=14`;
- `Delta=17`, `Delta=16` and `Delta=15` are PROJECT_CERTIFIED impossible;
- in `Delta=14`, `k=8`, `k=7`, `k=1`, and `k=0` are PROJECT_CERTIFIED impossible;
- `Delta=14, k=4, r=20,21,22` is PROJECT_CERTIFIED impossible;
- the remaining branch-level statuses, including partial k=2 and k=5 results and reproduced k=6, are exactly those in `repro-v1/ledger/theorem_ledger.json`.

Later reported connected-k=2 certificate completion is recorded in the canonical review as pending evidence reconciliation. It has not been silently promoted in the theorem ledger.

## External-audit readiness: NOT YET COMPLETE

The baseline review found 23 named, hash-pinned original artifacts absent from the repository, as well as unlocated Delta=15/v4 and later k=2 certification packages. In particular, the Delta=15 status currently refers to an Audit-v5 PDF whose bytes are not yet present. The mathematical status is retained, but the repository alone does not yet substantiate every claimed closure.

The current `repro-v1/scripts/reproduce_all.sh` cannot run from a clean checkout: required modules and manifests are missing. Its `--full` mode also deliberately excludes full proof replay. Follow the canonical backlog; do not describe this checkout as a completed external-audit release.

## Repository layout

- `project/` — standing orders, canonical review, tasks and recovery inventories.
- `repro-v1/` — reproducibility scaffold and currently preserved hand proofs; evidence restoration is outstanding.
- `releases/` — expected release metadata and hashes; no complete binary release was present at the reviewed baseline.
- `paper/` — planned location for the current manuscript and rendered documents; not yet populated at the reviewed baseline.

The canonical machine-readable **mathematical status** is `repro-v1/ledger/theorem_ledger.json`; the canonical **work backlog** is `project/CANONICAL_TASKS.json`.

## Preservation rule

A chat transcript must never be the sole record of material work. Code, inputs, outputs, certificates, hashes, commands, provenance, corrections, and paper dependencies must be preserved before a result is promoted.

Keep mathematical status, certificate completion, available evidence bytes and independent external review distinct. A hash or an LFS configuration is not an uploaded proof package.

**An UNSAT exit code is not a proof certificate.**
