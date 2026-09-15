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

## Protected execution modes

`RESEARCH_EXECUTION_POLICY_V3`

The purpose of this policy is to stop mathematically modest work from being swallowed by repository, connector, CI, or recovery overhead.

Every live handoff must state `WORK MODE:` and `DEFERRED ADMIN:`. Allowed work modes are `MATH`, `ADMIN`, `AUDIT`, `STATUS`, and `RECOVERY`.

### MATH mode is the default for research-continuation requests

When the user says **continue the maths**, **continue**, **carry on**, **proceed**, **next**, or equivalent in an active research thread, enter `MATH` mode unless the user explicitly asks for repository maintenance, CI work, audit work, publication work, or a status-only task.

In `MATH` mode:

1. Read `CURRENT_STATE.md` first and record the current `main` SHA.
2. Read only the mathematical inputs needed for the exact `NEXT ACTION`; do not perform broad repository archaeology when durable sources agree.
3. Perform **one bounded substantive research unit**.
4. Immediately preserve its result, failure, counterexample, changed route, or useful partial output in one checkpoint, preferably an atomic commit containing the changed artifact(s) and `CURRENT_STATE.md`.
5. Verify publication **once** by confirming the resulting remote head and live handoff. A successful non-forced publication plus one remote confirmation is enough for durability; do not recursively re-verify the same checkpoint.
6. Only after `UNPRESERVED WORK: None` may the next research unit begin.

### Hard exclusions while in MATH mode

Unless they directly block or invalidate the current mathematical unit, **do not** spend the research turn on:

- README maintenance or reviewer-facing prose;
- broad commit-history or repository sweeps;
- unrelated audit reconciliation;
- CI/workflow inventory or repeated workflow polling;
- workflow-trigger cleanup, repository housekeeping, issue cleanup, or cosmetic refactors;
- re-checking already verified status evidence merely because it is available.

Record such items under `DEFERRED ADMIN:` and continue the mathematics. Do not piggyback an unrelated administrative repair onto a mathematical transaction.

### CI discipline

- Routine research checkpoints do **not** wait for CI completion.
- If a workflow is launched, record its run ID if materially relevant and continue with an independent bounded unit when possible.
- Poll a workflow only when its result is necessary to interpret the current mathematical claim. Avoid repeated polling loops; one targeted observation is the default, followed by either useful independent work or a checkpoint stating that the claim is pending.
- CI success is verification evidence, not permission to promote a claim; existing audit/promotion gates remain separate.

### Administrative-call budget and circuit breaker

- After the mandatory live-handoff read, do not allow a chain of repository-administration operations to displace the maths. As a default, **no more than four consecutive administration/connector operations** (workflow polling, status reconciliation, maintenance writes, branch/history checks) may occur in `MATH` mode before either returning to the mathematical unit or checkpointing a genuine blocker. Mathematical source-file reads needed for the stated lemma/computation do not count toward this budget.
- On the first recoverable GitHub/connector write failure, make at most **one sensible fallback attempt**.
- After **two consecutive connector/write failures affecting preservation**, stop the retry spiral. If possible, publish a `BLOCKED_TOOLING` handoff describing the exact unsaved work and failure. If GitHub itself is unavailable, state explicitly in the user-visible response what remains unpreserved and do not claim it was saved.
- Do not turn a connector quirk into a multi-step repository reconstruction unless the durable state is genuinely inconsistent.

### Recovery ceiling

On timeout/new-chat recovery, if `CURRENT_STATE.md`, current `main`, and the exact named evidence agree, recovery is complete after reading those sources. **Do not reconstruct the project from the chat transcript or perform a repo-wide forensic review.** Broader recovery is permitted only when durable sources conflict, are missing, or explicitly say reconciliation is required.

### ADMIN, AUDIT, STATUS and RECOVERY modes

These modes may do the work their names imply, but remain transaction-bounded and must checkpoint useful results. When an administrative issue is discovered during `MATH` mode and is not blocking mathematics, defer it rather than silently switching modes. A mode switch should be explicit in `CURRENT_STATE.md`.

### Required live-checkpoint contents

Every `CURRENT-STATUS` block in `CURRENT_STATE.md` must contain:

- `CHECKPOINT CLASS:`
- `WORK MODE:`
- `INSPECTED PREDECESSOR:`
- `LAST VERIFIED RESULT:` (or explicit mathematical status unchanged)
- relevant canonical/promoted counts and trust boundary
- unresolved questions, failures, blockers, evidence paths, and active run/job/artifact IDs when relevant
- `UNPRESERVED WORK:` — normally `None`; if not, state exactly what remains outside GitHub and preserve it before beginning another substantive unit
- `DEFERRED ADMIN:` — `None` or a concise list of non-blocking repository/CI/process work intentionally postponed
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

- **Verify publication before saying work is saved.** Re-read main before writing; publish without force; preserve concurrent changes; then fetch the resulting commit and `CURRENT_STATE.md` remotely once.
- Before pausing, ending a research turn, or handing off, publish and verify the latest checkpoint. An abrupt interruption can occur before checkpointing; never imply unsaved work was preserved.
- On recovery: read current `CURRENT_STATE.md` first, inspect commits newer than its recorded predecessor and exact named runs/branches, reconcile only discrepancies, then execute `NEXT ACTION`. Do not do a repo-wide forensic reassessment unless durable sources disagree.

After the mandatory first read, consult `CANONICAL_REPOSITORY.md`, `README.md`, `RESEARCH_EVIDENCE_INDEX.md`, and package-specific instructions only as needed for the active mode and exact next action. Existing audit and promotion gates remain in force.

Keep the README cumulative and reviewer-facing. Preserve protected reviewer navigation, `REDTEAM-HISTORY`, `REVIEW-MATERIALS`, failures/corrections, counterexamples, hostile-audit findings, proof-hardening consequences, and direct links. Removal or material compression requires explicit user instruction.

The user authorizes sensible research commits and handoff updates without asking again. Re-read the branch before writing, preserve concurrent work, use non-forced fast-forward publication, and verify the result remotely. `scripts/check_status_sync.py` is a process guard, not a mathematical validator.

Keep audit 34854911792 and its promotion gate unchanged unless separately authorized. Full details: `CANONICAL_REPOSITORY.md`.