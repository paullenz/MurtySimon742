# Hourly research recovery — 22 September 2026

Status: **CONFIGURATION_REPAIRED; EXECUTION_NOT_YET_VERIFIED**.

This is an operational checkpoint, not a mathematical result. The user asked to fix the missed sessions. The inspected repository head was `7499d32d03eee71d985ca6faf30bb590563bca1d`.

## Evidence

The last verified completed forward session is the 21 September 20:00 BST session. The midnight audit exists. The latest pre-recovery commit, at 22 September 01:32:50 BST, changed logging rules. No 22 September session-log directory was present during inspection. The eleven historical gaps are listed in `GAPS.json`; all remain unverified, with unknown durations rather than invented zero-work claims. The 09:00 slot was still current and was not added to the historical gap count.

The research task was enabled and returned a last-run timestamp of 22 September 08:56:15 BST. This is not proof of useful execution. The automation interface exposes no detailed run-history/error retrieval. An immediate run was requested successfully on the predecessor during recovery but no STARTED checkpoint appeared during subsequent checks. The predecessor has now been disabled and replaced in this fresh recovery conversation. A manual recovery request on the replacement is planned after durable publication; no completion is claimed. Disabling a schedule does not prove that a previously queued invocation was cancelled. Duplicate-writer safeguards remain necessary. The browser was not signed in, so no run history was read through that route.

## Changes made

- Disable the stalled research task and create its replacement in the fresh recovery conversation with the same hourly boundaries, excluding midnight, from 22 September 10:00:38 BST through 27 September 23:00:38 BST. The recurrence uses COUNT=129 to preserve the exact existing end date without relying on normalized UNTIL timezone text.
- Keep the independent #742 research objective, 24-session gate, fifty-minute target and midnight adversarial audit.
- Require a remote STARTED record before mathematics, a CURRENT-STATUS update with every checkpoint, and immediate preservation after each substantive unit with a ten-minute backstop.
- Resolve the contradiction between first reading CURRENT_STATE and creating a record before any repository read. Observing the clock precedes reading; the first repository read remains CURRENT_STATE; durable startup publication follows the required policy/schema reads.
- Distinguish manual recovery from scheduled sessions; prohibit fabricated backdated credit.
- Add a separate hourly read-only execution health check at :15, from today 09:15 through 27 September 23:15 (135 checks), reporting missing starts, stale checkpoints, incomplete or short sessions, and source-access failures. It never launches additional research writers.
- Retarget the health check to the replacement. Update the existing 28 September 00:05 stop task to include the replacement and health check, while requiring both retired predecessors to remain disabled. Unrelated automations are untouched.

The saved prior settings are in `BEFORE.json`. Exact new prompts and schedules are in `AFTER.json`. Tool acknowledgements establish configuration changes and run-request acceptance, not completion.

## Verification and limits

Connector reads succeeded. The local process guard and recurrence checks are recorded in `VALIDATION.json`. Publication must be verified once after the atomic non-forced commit.

A successful repair still requires a new canonical record with a substantive checkpoint and then a correctly closed scheduled session. A monitor is also a scheduled task: configuring it is not proof it will run, and it is not a guarantee against a shared scheduler outage. No root cause of the historical execution gap is asserted. Repeated requests, new clocks, and administrative commits cannot be used to manufacture recovery evidence.

## Mathematical handoff

independently reconstruct the complete selected-quasi-edge/profile lemma from raw D2C criticality in a standalone note, then build an actual-graph regression of every bridge inequality under multiple legal selections. Freeze `250/429` on any source/supplement reuse or choice-dependence gap. Only after that gate, attack the corrected high-codegree cluster and separately preserve the zero-demand balanced complete-bipartite equality branch.

The last verified focused-session count remains 1/24. The `250/429` threshold remains internally reviewed candidate mathematics with the same graph-to-profile dependence and equality caveats as the daily audit.
