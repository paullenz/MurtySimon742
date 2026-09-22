# Research/monitor interruption correction — 22 September 2026

Observed reconciliation entry: 09:39:47 BST. Correction prepared: 09:41:24 BST.

The user correctly challenged the claimed recovery. The research task and health monitor both target conversation 6ab2352e-8664-83ed-9cd0-bb5b554b1e32. Both invocation messages were delivered into the active conversation. The assistant subsequently treated the monitor's read-only instruction as replacing the active research objective and ended the turn while the manual telemetry still said STARTED/IN_PROGRESS. This is a demonstrated continuation/finalization failure, not a diagnosis of the earlier overnight missed launches.

The last saved substantive work completed at 09:34:14 BST and was committed in 5c408fa8629af7211c08127ee29f1fb3509ce8ad. Three closed intervals total 670 seconds. All three useful research units were saved. No later mathematics or undocumented time is credited. The previous final report and final-preservation boundaries were not directly clocked: they remain UNVERIFIED. The manual record is now INTERRUPTED_CLOSED and NONCOMPLIANT_INTERRUPTED_UNVERIFIED_CLOSURE, with zero historical scheduled-slot or focused-session credit.

Both saved automation prompts were successfully updated:
- Health task 6ab236f04c78819188d2fe385270ce43 now explicitly scopes read-only restrictions to its monitoring subtask. During active research it must report briefly in commentary and resume the same authorized session rather than end the turn.
- Research task 6ab23822ccfc819180460a39e879b68a now explicitly preserves its session identity, deadlines and finalization across ancillary checks and status questions.
- Schedules, end dates, mathematical instructions, duration target and audit gates are unchanged. No extra task or immediate run was launched.

This is a prompt-level repair, not demonstrated platform isolation. The exposed update interface has no conversation-routing field. The original scheduler failure remains unexplained. The first prospective replacement trigger is 22 September 2026 at 10:00:38 BST; it was not due at reconciliation entry. Verify its remote STARTED record by 10:10:38, substantive checkpoints while active and final closure by 10:59:38. Only observed execution can validate recovery.

Mathematical status is unchanged. Resume the next audited action from CURRENT_STATE.md; do not replay saved units or fabricate missed sessions.
