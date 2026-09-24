# Canonical repository

**24 September 2026: research cadence paused by the user.** Repository restart/recovery instructions below mean recover context, not restart mathematical execution. Follow [CURRENT_STATE.md](CURRENT_STATE.md); a new explicit user instruction is required to resume research.

Current project repository: `paullenz/MurtySimon742`

GitHub repository ID: `1359206057`

This supersedes older project repository names, including `paullenz/MurtySimon25`. Legacy `N25_*` filenames are historical paths, not repository identifiers.

## Mandatory restart order

For every project restart or context recovery:

1. **FIRST ACTION: read the current [`CURRENT_STATE.md`](CURRENT_STATE.md) on `main` before substantive analysis, edits, or computation.** Apply this after every timeout, new chat, context reset, takeover, or resumed session.
2. Record the inspected main SHA and read [`AGENTS.md`](AGENTS.md). Consult this file, [`README.md`](README.md), [`RESEARCH_EVIDENCE_INDEX.md`](RESEARCH_EVIDENCE_INDEX.md), and package-specific instructions only as required by the active work mode and exact next action.
3. Inspect commits newer than the predecessor named by the live handoff and the exact active branches, workflow runs, and evidence it names.
4. Reconcile only genuinely newer or conflicting evidence before continuing. If remote state is unavailable, identify the last durable checkpoint and explicitly leave current status unverified.

`CURRENT_STATE.md` is the high-frequency operational source of truth. README is a lower-frequency reviewer-facing summary and need not mirror routine WIP/status checkpoints.

## Transaction-style checkpoint cadence and timeout recovery

`STATUS_SYNC_POLICY_V2`

User standing order, 15 September 2026: **never allow more than one substantive research unit to exist solely in session memory.** A unit may be a lemma/proof attempt, computational screen, verifier change, counterexample search, evidence reconciliation, or similarly bounded piece of work.

Checkpoint immediately after each substantive result, failure, correction, counterexample, change of attack, or completed bounded computation; before starting another long operation; after a long operation returns a material result; and before pausing or handing off. The ten-minute rule remains a maximum elapsed-time backstop only.

WIP commits are explicitly valid and encouraged. Preserve partial proofs, failed routes, exact inputs/outputs, scripts, and negative evidence with status labels such as `WIP_UNVERIFIED`, `FAILED_ROUTE`, `IN_PROGRESS`, `VERIFIED_INTERNAL_NOT_PROMOTED`, or `AUDIT_COMPLETE_NOT_PROMOTED`. Do not wait for polished exposition before making useful work durable.

A live checkpoint is normally a small `CURRENT_STATE.md` update plus any artifact that actually changed. It must record `CHECKPOINT CLASS:`, `WORK MODE:`, `INSPECTED PREDECESSOR:`, `LAST VERIFIED RESULT:`, `UNPRESERVED WORK:`, `DEFERRED ADMIN:`, and `NEXT ACTION:` together with relevant counts, trust boundaries, failures, evidence paths, and run/job/artifact IDs.

Before reporting a checkpoint saved, re-read main, publish without force while preserving concurrent changes, then fetch the resulting commit and `CURRENT_STATE.md` remotely. An abrupt interruption cannot guarantee preservation of the current in-memory unit; the last published handoff is the deterministic restart boundary.

## Protected execution modes and turn-budget discipline

`RESEARCH_EXECUTION_POLICY_V3`

The default work mode for requests such as **continue the maths**, **continue**, **carry on**, **proceed**, or **next** in an active research thread is `MATH`. `ADMIN`, `AUDIT`, `STATUS`, and `RECOVERY` are explicit alternative modes.

In `MATH` mode, perform the mandatory handoff read, obtain only the mathematical inputs needed for the recorded `NEXT ACTION`, complete one bounded research unit, checkpoint it immediately, verify publication once, and only then begin the next unit. Do not use the mathematics turn for unrelated README work, broad repository archaeology, CI inventories, repeated workflow polling, housekeeping, cosmetic refactors, or non-blocking process fixes. Put those under `DEFERRED ADMIN:` instead.

Routine checkpoints do not wait for CI. Record materially relevant run IDs and continue independent work when possible. Poll only when a workflow result is required to interpret the current mathematical claim, avoiding repeated polling loops.

As a default, after the mandatory read there may be no more than four consecutive repository-administration/connector operations in `MATH` mode before returning to mathematics or checkpointing a genuine blocker. Necessary mathematical source-file reads do not count toward that budget.

On a recoverable publication/tooling failure, make at most one sensible fallback attempt. After two consecutive connector/write failures affecting preservation, stop the retry spiral: checkpoint `BLOCKED_TOOLING` if possible; if GitHub is unavailable, state exactly what remains unpreserved and do not claim it was saved.

If current `CURRENT_STATE.md`, `main`, and named evidence agree after a timeout, recovery is complete; do not reconstruct from chat history or perform a broad forensic sweep. A broader recovery is justified only by contradictory, missing, or explicitly unresolved durable evidence.

These limits exist to protect research throughput. An unrelated administrative defect discovered during `MATH` mode is normally deferred, not repaired immediately.

## Standing synchronization order — live handoff every commit

**Every active-line commit must update the `CURRENT-STATUS` block in `CURRENT_STATE.md`.** If mathematics is unchanged, explicitly say so and identify the actual operational change.

The former rule requiring `README.md` and `CURRENT_STATE.md` status blocks to change together on every commit is superseded. README is now a reviewer-facing milestone surface. Update its `CURRENT-STATUS` block when reviewer-facing mathematical state materially changes: theorem/proof status, canonical ledger counts, promotions/demotions, completed audits that alter reviewer interpretation, reviewer-package releases, or comparable substantive milestones. Routine status-only, WIP, failure-preservation, launch-recording, and timeout-recovery commits need not touch README. Whenever README itself is edited, its `CURRENT-STATUS` block must be refreshed in that same commit.

This separation is deliberate: cheap durable checkpoints should stay cheap. Most proof workflows are path-scoped, so a `CURRENT_STATE.md`-only commit should not trigger expensive mathematical jobs. If research code/evidence changes, preserve it with the checkpoint and allow relevant path-scoped verification to run; durability takes priority over waiting for a polished batch.

The lightweight `scripts/check_status_sync.py` and `Status synchronization` workflow enforce the live-handoff rule, the V3 mode/deferred-admin fields, and a refreshed README status block whenever README itself changes. They are process guards, not mathematical validators or branch protection.

## README preservation order

The root README is cumulative project memory and a reviewer-facing audit surface. Normal rewrites must be additive/reconciliatory, not destructive. Do not remove or materially compress protected `REDTEAM-HISTORY`, `REVIEW-MATERIALS`, failures/corrections, hostile-audit findings, or proof-hardening consequences without explicit user instruction. If detailed material moves to an archive, retain a meaningful root summary and direct link.

## Evidence, review and preservation

Preserve the distinction between discovery, internal verification, independently structured implementation, remote CI, external mathematical review, and external reproduction. Queued workflows, timeouts, absent output, and floating-point infeasibility are not proof.

Relational audit 34854911792 completed and its 2,655 audited keys passed the separate reviewed-ledger promotion step on 14 September 2026. The promoted finite frontier remains **4,626 exclusions / 952 survivors / 3,632 whole-state closures** unless and until a separately reviewed promotion changes it. Do not reinterpret this finite promotion as an unrestricted proof; external review of the canonical bridge remains separate.