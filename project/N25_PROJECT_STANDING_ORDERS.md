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

## GitHub standing order

The repository `paullenz/MurtySimon25` is the durable project home. Future material work should be preserved here (or in an explicitly hash-pinned external artifact referenced here) rather than left only in chat history.
