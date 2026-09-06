# Erdős Problem #742, n=25 — reproducibility scaffold v1

**Original release date:** 6 September 2026  
**Readiness review:** 6 September 2026  
**Status:** INCOMPLETE CHECKOUT — not yet an executable external-audit release.

This is **not** a claim that the n=25 case is solved. The current repository records mathematical status but still lacks much of the source evidence and several modules/manifests required by its advertised entry point. See [the canonical review](../project/CANONICAL_N25_REVIEW_2026-09-06.md) and [task backlog](../project/CANONICAL_TASKS.json).

## Intended command, after restoration

```bash
bash scripts/reproduce_all.sh --fast
```

At the reviewed baseline this command fails because `scripts/verify_artifacts.py` is missing; other required modules are also absent. Do not report reproduction as successful merely because the entry-point shell script exists.

The large checkpoint is expected under `external/`. The `--full` mode explicitly omits full proof replay, which requires a separate documented and tested command. `THIRD_PARTY_AUDIT.md` describes the intended audit protocol, not a claim that all its dependencies are currently present.

## Governing files

- `ledger/theorem_ledger.json` — recorded mathematical branch status.
- `ledger/proof_obligations.json` — original six-item obligation list, to be expanded against the canonical backlog.
- `ledger/paper_import_manifest.json` — expected but missing at baseline.
- `ledger/artifacts.lock.json` — expected but missing at baseline.
- `proof_migration/` — expected source/plan area, missing at baseline.

A completed external-audit package must distinguish mathematical status, internal certificate/replay status, actual artifact availability and independent external review.

**An UNSAT exit code is not a proof certificate.**
