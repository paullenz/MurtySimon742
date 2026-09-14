# Canonical repository

Current project repository: `paullenz/MurtySimon742`

GitHub repository ID: `1359206057`

This supersedes older project repository names, including `paullenz/MurtySimon25`. Legacy `N25_*` filenames are historical paths, not repository identifiers.

## Mandatory restart order

For every project restart or context recovery:

1. confirm this repository identity;
2. read [`README.md`](README.md), [`CURRENT_STATE.md`](CURRENT_STATE.md), and [`AGENTS.md`](AGENTS.md);
3. inspect commits newer than the synchronization point recorded there;
4. reconcile any material newer result into both live status surfaces before treating the handoff as current.

## Standing synchronization order — every commit

**User instruction, 14 September 2026: the fixed-order and general-state summaries belong near the top of README.md, and current status must be reviewed and updated with EVERY commit.** This strengthens the earlier material-change-only rule; it does not replace preservation or review requirements.

Every new commit must contain an appropriate update to the `CURRENT-STATUS` blocks in BOTH `README.md` and `CURRENT_STATE.md`. Use one atomic, multi-file commit for research/code/evidence and its status update, rather than a later catch-up commit. This applies to documentation, verification, preservation and automation-generated commits as well as mathematical advances. If mathematical results are unchanged, explicitly say **mathematical status unchanged** and identify what this commit actually changes. Do not manufacture progress or merely change a date.

Each update must state the latest completed step, evidence/verification scope, unresolved limitations, and immediate next step. Use a descriptive checkpoint identifier and the inspected predecessor SHA or a known evidence commit. Never invent a self-referential final commit hash. Keep fixed-order results, general-theory candidates, canonical frontier counts, exploratory sample results and audit gates separate. Update the evidence index and reviewer index when their contents change.

For a research-state change, also reconcile canonical frontier/ledger counts; completion or failure of discovery, recovery and audit gates; theorem promotion, falsification or weakening; changes of attack; material negative results; and the handoff after a substantive research block. Historical observations must be dated and preserved rather than silently overwritten as though they were current observations.

Before publication: read latest main, preserve concurrent changes, check links and status consistency, commit all related files together, update the branch without force, then fetch the resulting branch/file to verify publication. A rejected/non-fast-forward update requires reconciliation, not overwriting newer work.

The lightweight `scripts/check_status_sync.py` and `Status synchronization` workflow detect commits missing either status-block update. They cannot determine whether mathematical prose is true and are not branch protection; substantive review remains mandatory. No historical backfill is demanded. An old branch must incorporate this rule before new work is published.

## Evidence, review and preservation

A state sync must preserve the distinction between discovery, internal verification, independently structured implementation, remote CI, external mathematical review and external reproduction. Queued workflows, timeouts, absent output and floating-point infeasibility are not proof. Preliminary scan output must never be promoted merely by rewriting a state file.

Preserve useful proofs, failed approaches, counterexamples, verifier code, exact inputs/outputs, audit challenges and prior reviewer editions. Keep the protected reviewer-navigation section in README.md and synchronize it with `releases/REVIEW_READY_INDEX.md` when editions change.

Do not duplicate or change the budgets/concurrency of relational audit 34854911792. Its 2,655 recovered candidates remain unpromoted until complete coverage, dual agreement, zero unresolved cases, successful aggregate and a separate reviewed ledger step. Fetch every job page or a complete diagnostic before asserting a live shard count.
