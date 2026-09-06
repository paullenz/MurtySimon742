# Murty–Simon n=25 / Erdős Problem #742

Private working repository for the n=25 Murty–Simon project.

## Governing status

The repository is preservation-first. The current governing audit is **Audit v5 (6 September 2026)**. It does **not** claim that n=25 is solved.

Current audited frontier recorded by Audit v5, together with the subsequently preserved project-certified Δ=16 and Δ=17 eliminations:

- any order-25 counterexample is reduced to `e(G)=157` and `Delta(G)=14`;
- `Delta=17` is **PROJECT-CERTIFIED impossible**;
- `Delta=16` is **PROJECT-CERTIFIED impossible**;
- `Delta=15` is PROJECT-CERTIFIED impossible;
- in `Delta=14`, `k=8`, `k=7`, `k=1`, and `k=0` are PROJECT-CERTIFIED impossible;
- `Delta=14, k=4, r=20,21,22` is PROJECT-CERTIFIED impossible;
- other computational eliminations retain exactly the status recorded in the theorem ledger and Audit v5 and must not be silently promoted.

Thus the surviving n=25 frontier is entirely within `Delta=14`, subject to the branch-level qualifications recorded in the theorem ledger.

## Repository layout

- `paper/` — current rendered paper/audit documents.
- `project/` — standing orders and project-level preservation policy.
- `repro-v1/` — browsable canonical reproducibility release.
- `releases/` — immutable release metadata and hashes.

The canonical machine-readable status is `repro-v1/ledger/theorem_ledger.json`.

## Preservation rule

A chat transcript must never be the sole record of material work. Code, inputs, outputs, certificates, hashes, commands, provenance, corrections, and paper dependencies must be preserved before a result is promoted.

**An UNSAT exit code is not a proof certificate.**
