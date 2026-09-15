# Canonical repository

Current project repository: `paullenz/MurtySimon742`

GitHub repository ID: `1359206057`

This supersedes older project repository names, including `paullenz/MurtySimon25`. Legacy `N25_*` filenames are historical paths, not repository identifiers.

## Mandatory restart order

For every project restart or context recovery:

1. **FIRST ACTION: read the current [`CURRENT_STATE.md`](CURRENT_STATE.md) on `main` in `paullenz/MurtySimon742`, before substantive analysis, edits or computation.** Apply this after every timeout, new chat, context reset, takeover or resumed session; do not substitute memory or an earlier chat summary.
2. record the inspected main SHA, confirm this repository identity, and read [`AGENTS.md`](AGENTS.md), this file, [`README.md`](README.md) and [`RESEARCH_EVIDENCE_INDEX.md`](RESEARCH_EVIDENCE_INDEX.md);
3. inspect commits newer than the checkpoint and the exact active branches, workflow runs and evidence it names;
4. reconcile material newer results into both live status surfaces before treating the handoff as current or continuing research. If remote state is unavailable, identify the last durable checkpoint and explicitly leave current status unverified.

## Durable checkpoint cadence and timeout recovery

User standing order, 15 September 2026: checkpoint after every significant result, failure, correction or change of attack, **at least every ten minutes during sustained active work**, before the next long operation, and before a pause or handoff. The complete operational requirements are in [AGENTS.md — Mandatory first action and durable handoff](AGENTS.md#mandatory-first-action-and-durable-handoff).

A checkpoint must be published to main with paired CURRENT_STATE/README updates; branch-only and local-only status are insufficient. Preserve unfinished research on a durable branch when needed and link its exact commit from main. Include timestamp and inspected predecessor, last verified results and evidence, ledger/promotion scope, unresolved issues and failed attempts, exact branch/commit/file locations, active workflow/job/artifact IDs and observed states, and the precise next action or command with inputs and expected output. Use explicit pending/failure/review labels.

Long-running GitHub workflows must eventually have a verified completion handler that records their outcomes independently of the chat and updates both live status surfaces atomically. It must not promote mathematics or alter the canonical ledger automatically. **Recording this requirement does not install that handler: until implementation and verification are complete, keep it listed as pending and manually reconcile completed runs at each active checkpoint.**

Before reporting a checkpoint saved, re-read main, publish without force while preserving concurrent changes, then fetch the resulting commit and both files remotely. If publication fails, report the gap and preserve a remote recovery checkpoint where possible. An abrupt interruption cannot guarantee preservation of unfinished work; the durable checkpoint is the restart boundary.

## Standing synchronization order — every commit

**User instruction, 14 September 2026: the fixed-order and general-state summaries belong near the top of README.md, and current status must be reviewed and updated with EVERY commit.** This strengthens the earlier material-change-only rule; it does not replace preservation or review requirements.

Every new commit must contain an appropriate update to the `CURRENT-STATUS` blocks in BOTH `README.md` and `CURRENT_STATE.md`. Use one atomic, multi-file commit for research/code/evidence and its status update, rather than a later catch-up commit. This applies to documentation, verification, preservation and automation-generated commits as well as mathematical advances. If mathematical results are unchanged, explicitly say **mathematical status unchanged** and identify what this commit actually changes. Do not manufacture progress or merely change a date.

Each update must state the latest completed step, evidence/verification scope, unresolved limitations, and immediate next step. Use a descriptive checkpoint identifier and the inspected predecessor SHA or a known evidence commit. Never invent a self-referential final commit hash. Keep fixed-order results, general-theory candidates, canonical frontier counts, exploratory sample results and audit gates separate. Update the evidence index and reviewer index when their contents change.

For a research-state change, also reconcile canonical frontier/ledger counts; completion or failure of discovery, recovery and audit gates; theorem promotion, falsification or weakening; changes of attack; material negative results; and the handoff after a substantive research block. Historical observations must be dated and preserved rather than silently overwritten as though they were current observations.

## README preservation order

The root README is cumulative project memory and a reviewer-facing audit surface. Normal status rewrites must be **additive/reconciliatory**, not destructive. Do not remove or materially compress substantive prior content merely to make the README shorter. The marked `REDTEAM-HISTORY` and `REVIEW-MATERIALS` sections are protected content; hostile/red-team findings, actual defects, corrections, failed approaches, reviewer-triggered proof changes and their links must remain visible in the root README. If detailed material is archived, retain a meaningful root summary and direct navigation. Any intentional removal or material compression requires explicit user instruction. Before publishing, compare the proposed README with current `main` for dropped headings, links, failures and audit history; the automated guard is only a minimum backstop.

Before publication: read latest main, preserve concurrent changes, check links and status consistency, commit all related files together, update the branch without force, then fetch the resulting branch/file to verify publication. A rejected/non-fast-forward update requires reconciliation, not overwriting newer work.

The lightweight `scripts/check_status_sync.py` and `Status synchronization` workflow detect commits missing either status-block update. `tools/check_readme_review_materials.py` also protects the reviewer-navigation and hostile/red-team-history blocks. These guards cannot determine whether mathematical prose is true and are not branch protection; substantive review remains mandatory. No historical backfill is demanded.

## Evidence, review and preservation

A state sync must preserve the distinction between discovery, internal verification, independently structured implementation, remote CI, external mathematical review and external reproduction. Queued workflows, timeouts, absent output and floating-point infeasibility are not proof. Preliminary scan output must never be promoted merely by rewriting a state file.

Preserve useful proofs, failed approaches, counterexamples, verifier code, exact inputs/outputs, audit challenges and prior reviewer editions. Keep the protected reviewer-navigation section in README.md and synchronize it with `releases/REVIEW_READY_INDEX.md` when editions change.

Relational audit 34854911792 has completed and its 2,655 audited keys passed the separate reviewed-ledger promotion step on 14 September 2026. The promoted finite frontier is 4,626 exclusions / 952 survivors / 3,632 whole-state closures. Do not alter the historical audit budgets/concurrency or reinterpret this finite promotion as an unrestricted proof; external review of the canonical bridge remains separate.
