# n=25 Project Standing Orders

This file records the preservation and evidence-first rules governing the Murty–Simon n=25 / Erdős #742 project.

## Canonical coordination

On 6 September 2026 the user designated the chat opened with “make this now the canonical chat for N=25” as the canonical coordination chat. Consolidate future mathematical progress, decisions, corrections, certificate status, paper dependencies and GitHub preservation there. The repository remains the durable project record; this is not a background synchronization process.

The consolidation baseline is `project/CANONICAL_N25_REVIEW_2026-09-06.md`. The canonical work backlog is `project/CANONICAL_TASKS.json`; recovery evidence is tracked in `project/EVIDENCE_RECOVERY_MANIFEST.json`. The mathematical branch-status record remains `repro-v1/ledger/theorem_ledger.json`.

Account explicitly for the earlier Delta=15 certification and final-audit work, not only the active Delta=14 frontier. Merge later results from other chats only with dated provenance and an explicit reconciliation against the existing ledger. Do not discard later reported progress merely because the repository lags, and do not promote it without the required evidence.

## Core preservation rule

A chat transcript must never be the sole durable record of material mathematical or computational work. Every material result must be preserved with enough provenance for later reconstruction and audit.

## Evidence hierarchy

Use the exact hierarchy:

- PUBLISHED
- PROJECT-CERTIFIED
- REPRODUCED
- REPORTED ONLY
- OPEN

No lower-status claim may be silently upgraded. Elementary exclusions may additionally be labelled INADMISSIBLE under the theorem-ledger schema.

Keep mathematical status, internal certificate completion/replay, availability of actual evidence bytes in the repository or pinned storage, and independent external review distinct. Missing uploads do not automatically invalidate a mathematical argument, but a status label or hash alone does not make it externally auditable.

## Computational work

Preserve code, exact parameters, inputs, survivor lists, outputs, environment information, hashes, commands, and certificates where applicable. Timeouts, interrupted jobs, partial sweeps, LP feasibility, and solver noncompletion never count as UNSAT. An UNSAT exit code is not a proof certificate.

## Audit scope

Audit the entire workstream, including hand arguments, finite arithmetic, experimental solvers, failed approaches, corrections, and superseded claims. Record inaccessible original work as a recovery obligation; any reconstruction must carry new provenance rather than fabricated historical filenames, hashes or logs.

## Promotion rule

Only PROJECT-CERTIFIED material is safe to fold into the theorem chain. REPRODUCED computation may be reported as evidence but remains outside the proof until promoted by a complete audited argument or replayable proof evidence. An external-audit release additionally requires available and checked supporting artifacts and closed dependencies.

## README frontier-synchronisation standing order

The repository README must keep pace with the effective research frontier. README synchronisation is a required follow-up whenever material progress changes what an informed reviewer should regard as the current state of the project.

Update the README when any of the following occurs:

- a new theorem-level candidate proof or fixed-order result is added;
- a reviewer-ready manuscript, release, verification companion or audit package is created;
- a result is materially promoted, weakened, falsified, corrected or superseded;
- a new canonical checkpoint becomes important to understanding the current frontier;
- the active general-order research programme changes direction materially;
- a dependency or non-dependency relationship changes in a way reviewers should know.

The README must remain a concise current map rather than an exhaustive changelog. It should link to canonical proof/reviewer packages, distinguish theorem-level candidate results from exploratory/reconnaissance work, state material limitations and open review boundaries, and preserve visible corrections where they affect trust. Experimental checkpoints should be linked only when they are important for understanding the active frontier and must never be presented as theorem status.

Before treating a major research checkpoint or reviewer package as fully preserved, check whether the README needs a corresponding update. If it does, update it in the same repository-writing pass whenever practicable.

### Protected papers/review-material navigation standing order — 13 September 2026

The root `README.md` must permanently retain a visible reviewer-facing **Papers and review materials** section delimited by the exact markers

```text
<!-- REVIEW-MATERIALS:START -->
<!-- REVIEW-MATERIALS:END -->
```

This section is a protected navigation surface, not disposable prose. It must continue to expose the current fixed-order reviewer packages, principal general-theory reviewer packages, `START_HERE_FOR_REVIEWERS.md`, `releases/REVIEW_READY_INDEX.md`, the canonical bridge, material audits and material errata/corrections.

A full-file README rewrite must preserve the protected section. Before committing such a rewrite, compare the protected section against the current default-branch version and ensure that no current package, paper, verification companion, audit or erratum has silently disappeared. When a reviewer version is superseded, replace the current-version link deliberately and preserve the superseded package in history/indexes; do not remove the navigation surface itself.

Whenever a new current reviewer-facing paper/package is created or promoted, add it to the protected README section in the same publication pass unless there is a documented reason not to. The canonical detailed source remains `releases/REVIEW_READY_INDEX.md`; the README is intentionally a duplicated human navigation layer so reviewers cannot lose the papers through a status rewrite.

Run `python3 tools/check_readme_review_materials.py` after relevant README/release changes. The workflow `.github/workflows/check-readme-review-materials.yml` is a standing CI guard. A guard failure means the reviewer-facing publication pass is incomplete and must be corrected before the checkpoint is treated as fully preserved.

### Reviewer-version and link consistency standing order

Whenever any reviewer package, manuscript, verification companion, proof surface, audit release, or other canonical reviewer-facing artifact is created, superseded, renamed, or promoted, perform a repository-facing consistency sweep in the same update pass.

At minimum, verify all of the following before the update is considered complete:

- the README headline/status table names the current reviewer version;
- the fixed-order/current-result section points to the same current version;
- the Review-paper index points to the same current manuscript and verification companion;
- `START_HERE_FOR_REVIEWERS.md` and any other reviewer entry point do not direct reviewers to a superseded package as current;
- links resolve to files that actually exist on the default branch;
- superseded packages remain clearly labelled historical rather than silently deleted;
- version numbers, filenames, labels such as “current”, and prose descriptions agree across all reviewer-facing surfaces.

A reviewer release is **not fully published/preserved** until this consistency sweep has been completed. When practical, re-open the README after the commit and verify the rendered/current paths rather than assuming the write succeeded.

## GitHub standing order

The repository `paullenz/MurtySimon742` is the durable project home. Future material work should be preserved here (or in an explicitly hash-pinned external artifact referenced here) rather than left only in chat history.

## Standing authorization for GitHub commits and pushes — 12 September 2026

Paul explicitly instructed: “Great - you don't need to ask my permission to commit to GitHub in future”.

This is continuing user authorization to commit and push routine Murty–Simon research, code, proofs, audit evidence, documentation and corrections to the public repository `paullenz/MurtySimon742`, including its `main` branch. Complete these updates without requesting fresh user permission for each checkpoint. Continue the existing preservation, README/link consistency, non-forced update and publication verification requirements.

If a platform approval or access-control block occurs, report the actual block and preserve the prepared work. Do not misdescribe it as missing user authorization, and do not bypass the control.
