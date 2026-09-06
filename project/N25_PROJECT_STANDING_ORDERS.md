# n=25 Project Standing Orders

This file records the preservation and evidence-first rules governing the Murty–Simon n=25 / Erdős #742 project.

## Core preservation rule

A chat transcript must never be the sole durable record of material mathematical or computational work. Every material result must be preserved with enough provenance for later reconstruction and audit.

## Evidence hierarchy

Use the exact hierarchy:

- PUBLISHED
- PROJECT-CERTIFIED
- REPRODUCED
- REPORTED ONLY
- OPEN

No lower-status claim may be silently upgraded.

## Computational work

Preserve code, exact parameters, inputs, survivor lists, outputs, environment information, hashes, commands, and certificates where applicable. Timeouts, interrupted jobs, partial sweeps, LP feasibility, and solver noncompletion never count as UNSAT. An UNSAT exit code is not a proof certificate.

## Audit scope

Audit the entire workstream, including hand arguments, finite arithmetic, experimental solvers, failed approaches, corrections, and superseded claims.

## Promotion rule

Only PROJECT-CERTIFIED material is safe to fold into the theorem chain. REPRODUCED computation may be reported as evidence but remains outside the proof until promoted by a complete audited argument or replayable proof evidence.

## GitHub standing order

The repository `paullenz/MurtySimon25` is the durable project home. Future material work should be preserved here (or in an explicitly hash-pinned external artifact referenced here) rather than left only in chat history.
