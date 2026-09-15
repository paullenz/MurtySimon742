# Research-agent standing orders

Canonical repository: `paullenz/MurtySimon742` (ID 1359206057).

## Mandatory first action and durable live handoff

`STATUS_SYNC_POLICY_V2`

**User standing order — 15 September 2026: whenever work is picked up again, the FIRST action must be to read the current `CURRENT_STATE.md` on `main`.** This applies after a timeout, new chat, context reset, takeover, or any resumed research session. Do this before substantive analysis, editing, or computation. Record the inspected main SHA, then inspect only the exact newer commits, branches, runs, and evidence named by the live handoff unless durable sources disagree.

`CURRENT_STATE.md` is the **high-frequency operational source of truth**. `README.md` is the lower-frequency reviewer-facing summary and may legitimately lag routine WIP/status checkpoints.

### Transaction-style research invariant

- **Never start substantive research unit N+1 while useful output from unit N exists only in session memory.** A unit is one bounded lemma/proof attempt, counterexample search, computation, verifier change, evidence reconciliation, or comparable step.
- **Checkpoint immediately after every substantive result, failure, correction, counterexample, change of attack, or completed bounded computation.** Ten minutes is only a maximum elapsed-time backstop, not the normal cadence.
- **Before launching a long-running operation, publish useful completed work and record the launch/run ID.** When the run yields a material result, checkpoint that result before starting another research unit.
- **WIP commits are encouraged.** Do not wait for polish. Use explicit labels such as `WIP_UNVERIFIED`, `FAILED_ROUTE`, `IN_PROGRESS`, `VERIFIED_INTERNAL_NOT_PROMOTED`, and `AUDIT_COMPLETE_NOT_PROMOTED`. Negative results are research progress and must be preserved.
- **Bound timeout loss to at most one small research unit.** If more than one meaningful step has happened since the last durable checkpoint, stop and checkpoint before continuing.

### Required live-checkpoint contents

Every `CURRENT-STATUS` block in `CURRENT_STATE.md` must contain:

- `CHECKPOINT CLASS:`
- `INSPECTED PREDECESSOR:`
- `LAST VERIFIED RESULT:` (or explicit mathematical status unchanged)
- relevant canonical/promoted counts and trust boundary
- unresolved questions, failures, blockers, evidence paths, and active run/job/artifact IDs when relevant
- `UNPRESERVED WORK:` — normally `None`; if not, state exactly what remains outside GitHub and preserve it before beginning another substantive unit
- `NEXT ACTION:` — one concrete next step or command with expected interpretation

The current durable head is the `main` commit containing the handoff. A self-referential final SHA is not required inside that same commit; the handoff records its inspected predecessor.

### Commit and README synchronization policy

**Every active-line commit must update the `CURRENT-STATUS` block in `CURRENT_STATE.md`.** This includes research, code, evidence, documentation, maintenance, policy, and automation commits. If mathematics is unchanged, say so explicitly and describe the actual non-mathematical change.

**README is no longer a per-commit handoff surface.** Refresh its `CURRENT-STATUS` block when reviewer-facing mathematical state materially changes: theorem/proof status, canonical ledger counts, promotions/demotions, completed audits that alter reviewer interpretation, reviewer-package releases, or comparable substantive milestones. Routine `STATUS_ONLY`, WIP, failure-preservation, launch-recording, and timeout-recovery checkpoints do not require a README edit. If a commit edits `README.md` for any reason, refresh its `CURRENT-STATUS` block in that commit.

This supersedes the former rule requiring paired README/CURRENT_STATE edits on every commit. Historical commits and archived snapshots are preserved and are not rewritten.

### Cheap durable checkpoints

- Prefer a `CURRENT_STATE.md`-only commit when no research artifact itself changed.
- Most mathematical workflows are path-scoped, so status-only checkpoints should not launch expensive proof jobs.
- If code/evidence changed and is worth preserving, commit it with the live handoff; do not keep it local merely to avoid CI.
- Do not manufacture code/file touches solely to trigger CI. Verification and preservation are separate concerns.
- Never promote a mathematical claim merely because a WIP checkpoint or CI run exists.

### Publication and recovery

- **Verify publication before saying work is saved.** Re-read main before writing; publish without force; preserve concurrent changes; then fetch the resulting commit and `CURRENT_STATE.md` remotely.
- Before pausing, ending a research turn, or handing off, publish and verify the latest checkpoint. An abrupt interruption can occur before checkpointing; never imply unsaved work was preserved.
- On recovery: read current `CURRENT_STATE.md` first, inspect commits newer than its recorded predecessor and exact named runs/branches, reconcile only discrepancies, then execute `NEXT ACTION`. Do not do a repo-wide forensic reassessment unless durable sources disagree.

After the mandatory first read, consult `CANONICAL_REPOSITORY.md`, `README.md`, `RESEARCH_EVIDENCE_INDEX.md`, and package-specific instructions as needed. Existing audit and promotion gates remain in force.

Keep the README cumulative and reviewer-facing. Preserve protected reviewer navigation, `REDTEAM-HISTORY`, `REVIEW-MATERIALS`, failures/corrections, counterexamples, hostile-audit findings, proof-hardening consequences, and direct links. Removal or material compression requires explicit user instruction.

The user authorizes sensible research commits and handoff updates without asking again. Re-read the branch before writing, preserve concurrent work, use non-forced fast-forward publication, and verify the result remotely. `scripts/check_status_sync.py` is a process guard, not a mathematical validator.

Keep audit 34854911792 and its promotion gate unchanged unless separately authorized. Full details: `CANONICAL_REPOSITORY.md`.
