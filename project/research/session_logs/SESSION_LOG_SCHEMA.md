# Forward-research session telemetry schema

Effective prospectively from 22 September 2026. This is a process/audit contract, not mathematical evidence.

## Core accounting rule: one scheduled trigger = one session

The unique accounting identity of an hourly research session is its **scheduled trigger timestamp in Europe/London**, not the invocation, retry, context, compaction, re-entry, preservation continuation, or final report.

For each scheduled trigger there must be exactly one canonical telemetry record:

`project/research/session_logs/YYYY-MM-DD/<scheduled-trigger>-canonical.json`

Example:

`project/research/session_logs/2026-09-22/2026-09-22T14-00-38+01-00-canonical.json`

Historical fragment files must never be deleted. If multiple files/invocations belong to the same scheduled trigger, preserve them as evidence, reconcile them into the canonical record, and mark them as superseded by that canonical record for utilisation accounting.

## Canonical record structure

Each canonical record must contain at minimum:

- `session_id`: exactly the scheduled trigger timestamp
- `scheduled_trigger`
- `next_scheduled_trigger`
- `research_cutoff`
- `hard_close_deadline`
- `earliest_actual_start`
- `lateness_vs_trigger`
- `segments`: ordered array of every invocation/re-entry/reconciliation segment
- `forward_research_intervals`: closed timestamp intervals only
- `forward_research_stop`
- `preservation_start`
- `preservation_complete`
- `final_report_time`
- `wall_clock_span_to_preservation_complete`
- `verified_forward_research_span`: union of evidenced non-overlapping forward-research intervals
- `preservation_span`
- `substantive_unit_count`
- `timestamped_unit_ledger`
- `early_stop_check_time`
- `early_stop_check_result`
- `stop_reason`
- `target_50m_applies`: YES / NO / UNVERIFIED
- `target_50m_met`: YES / NO / N/A / UNVERIFIED
- `compliance_status`
- `infrastructure_failures`
- `commit_shas`
- `live_unfinished_line`
- `historical_fragments`: paths of any older split files reconciled into this session

Each element of `segments` must state:

- `segment_id`
- `actual_start`
- `actual_stop` if evidenced
- `role`: `forward_research`, `preservation`, `reconciliation`, or `late_no_research`
- `notes`
- any missing boundary as `UNVERIFIED`, never guessed

## Timing and anti-overlap rule

For hourly forward sessions:

- `research_cutoff = next_scheduled_trigger - 7 minutes`
- `hard_close_deadline = next_scheduled_trigger - 1 minute`

Forward research must stop by `research_cutoff`. Preservation, CURRENT_STATE synchronization, telemetry finalization and report preparation must finish by `hard_close_deadline`.

Do not perform optional cleanup or reconciliation past the hard-close deadline. Leave unfinished reconciliation to the audit rather than consuming the next trigger.

If prior-session cleanup nevertheless crosses the next trigger, it remains attached to the prior session. The new trigger still has its own distinct canonical session identity and must not be silently lost.

## Start-of-session rule

Before repository reading or mathematics:

1. obtain an authoritative Europe/London current timestamp;
2. identify the scheduled trigger to which this invocation belongs;
3. open or update that trigger's canonical record;
4. append the new segment;
5. record actual start, next trigger, cutoff, and lateness.

A context reset or re-entry **does not create a new session** and does not reset the target or clock.

## Research-interval rule

Every period claimed as forward research must be represented by an evidenced closed interval `[start, stop]`.

- On context handoff or compaction, close the current interval if the stop boundary is actually known.
- On re-entry, append a new interval to the same canonical record.
- If a boundary cannot be evidenced, mark it `UNVERIFIED`; do not infer it from commits, prose, unit count, user-report time, or nominal schedule.
- Timestamp substantive units as they complete. Unit timestamps support continuity but are not substitutes for interval boundaries.

The canonical verified forward-research span is the union of the closed non-overlapping intervals only.

## 50-minute target

If at least 50 minutes were genuinely available from the earliest actual session start to the research cutoff, the >=50-minute target applies.

- At least 50 **verified** minutes of forward research are required.
- Less than 50 verified minutes is NONCOMPLIANT unless all reasonable mathematical, audit, repair, regression, hostile-example, derivation, and checker avenues were genuinely blocked by unavailable information/capability.
- Completing a theorem, reaching a clean checkpoint, context compaction, tool failure, GitHub write, or report readiness is not by itself an exception.
- If fewer than 50 minutes were available from earliest actual start to research cutoff because the first invocation was late, mark target applicability N/A and preserve the lateness.

## Early-stop check

Before beginning final preservation, obtain a fresh timestamp.

If more than 5 minutes remain before research cutoff and any sensible next mathematical/audit step exists, continue forward research. Record the check and result.

## No-lost-hour rule

Late cleanup from one trigger remains attached to that trigger.

If preservation or reconciliation crosses into the next scheduled hour:

- it does **not** redefine or consume the next session identity;
- when the next trigger fires, the next canonical record must begin independently;
- if infrastructure/overlap actually prevents that new session from running, the missed/late session must be recorded explicitly rather than silently disappearing.

No scheduled trigger may be omitted from the daily audit.

## Finalisation

Before the user-facing report, finalize the canonical record.

Any mandatory field left `PENDING`, missing, contradictory, or internally inconsistent makes that session **UNVERIFIED/NONCOMPLIANT** for utilisation accounting.

Do not fabricate historical timestamps to repair a record.

`CURRENT_STATE.md` must contain a compact mirror of the latest canonical record:
scheduled trigger, earliest actual start, verified forward intervals, verified forward span, cutoff, preservation completion, substantive-unit count, stop reason, target result, compliance status, and canonical record path.

## Daily audit reconciliation

The daily red-team audit must enumerate **every scheduled trigger** in the audited window and classify it as one of:

- COMPLIANT
- SHORT/NONCOMPLIANT
- LATE-START / target N/A
- MISSED / NO FORWARD RESEARCH
- UNVERIFIED / MISSING TELEMETRY

For each trigger, reconcile all fragment files and re-entries into the single canonical session identity.

Aggregate utilisation must be computed only from evidenced closed intervals. Separately report partial verified forward minutes as a lower bound where full-session telemetry is incomplete.

Historical records from before this schema remain evidence but are not to be rewritten with invented times.
