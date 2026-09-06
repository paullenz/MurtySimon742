# Erdős Problem #742, n=25 — reproducibility release v1

**Release date:** 6 September 2026  
**Scope:** canonical audit/reproduction scaffold for the current n=25 project, with Delta=14 evidence incorporated through the k=2 audit capsule.

This is **not** a claim that the n=25 case is solved. It is a trust-boundary release: the repository makes it mechanically difficult to confuse project-certified proofs with reproducible but uncertified solver exclusions.

## One command

```bash
bash scripts/reproduce_all.sh --fast
```

For the large proof checkpoint, place the pinned full archive under `external/` and use `--full`. See `THIRD_PARTY_AUDIT.md`.

## Governing files

- `ledger/theorem_ledger.json` — canonical branch status.
- `ledger/paper_import_manifest.json` — branches currently permitted as theorem dependencies.
- `ledger/proof_obligations.json` — every known promotion/open obligation.
- `ledger/artifacts.lock.json` — hashes for bundled and external evidence.
- `proof_migration/` — plan to replace solver trust with replayable LRAT.

The strongest rule is simple: **an UNSAT exit code is not a proof certificate.**
