# Forward-research session telemetry schema

Effective from the 21 September 2026 daily red-team audit. This file is a process/audit contract, not mathematical evidence.

## One scheduled trigger, one canonical finalized record

Every forward-research invocation must create exactly one canonical telemetry record under:

`project/research/session_logs/YYYY-MM-DD/`

The record filename must include a unique `run_instance_id`. A retry, delayed re-entry or duplicate invocation must identify the original `scheduled_trigger` and must not be counted as a second scheduled research window. If more than one invocation attaches to one trigger, all records remain visible and the latest audit must reconcile them explicitly.

## Mandatory fields

Each finalized record must state, with timezone:

- `scheduled_trigger`
- `run_instance_id`
- `actual_start`
- `next_scheduled_trigger`
- `mandatory_preservation_cutoff`
- `forward_research_stop`
- `preservation_start`
- `preservation_complete`
- `final_report_time`
- `wall_clock_span_to_preservation_complete`
- `available_research_window_span` (actual start to mandatory cutoff; never inferred from schedule if actual start is missing)
- `forward_research_span`
- `preservation_span`
- `substantive_unit_count`
- `timestamped_unit_ledger`
- `early_stop_check_time`
- `early_stop_check_result`
- `stop_reason`
- `target_50m_applies` (`YES` / `NO` / `UNVERIFIED`)
- `target_50m_met` (`YES` / `NO` / `N/A` / `UNVERIFIED`)
- `infrastructure_failure` (`NONE` or exact failure)
- `handoff_commit` (if preserved to GitHub before report)

## Compliance rules

1. Do **not** derive missing durations from commit timestamps, substantive-unit count, prose length, user-facing report time or the nominal schedule.
2. Any mandatory field left `PENDING`, missing or internally inconsistent at handoff makes that run **UNVERIFIED/NONCOMPLIANT** for utilisation accounting.
3. Historical missing timestamps are never backfilled unless an independent contemporaneous timestamp source actually records the event. A commit time may corroborate preservation timing but cannot stand in for `actual_start` or `forward_research_stop`.
4. The normal `>=50-minute` forward-research target applies only when at least 55 minutes were genuinely available from actual start to mandatory cutoff. If fewer than 55 minutes were available, mark the target `N/A`; the late start remains separately visible.
5. A run that starts late must record the lateness relative to `scheduled_trigger` and explain the cause if known. Never invent a cause.
6. Timestamped unit-ledger gaps may be described as unexplained idle only when telemetry evidence supports that inference. Absence of a unit timestamp alone is not proof of idleness.
7. Preservation-stage self-audit that uncovers a mathematical error may resume forward repair, but the resumption and revised forward stop must be timestamped.
8. The daily red-team audit must enumerate every scheduled forward window, reconcile duplicate/re-entry records, and compute aggregate utilisation from verified telemetry only.

## Minimal finalized example

```text
scheduled_trigger: 2026-09-21 14:00:38 BST
run_instance_id: 2026-09-21T14-00-42+01-00-a
actual_start: 2026-09-21 14:00:42 BST
next_scheduled_trigger: 2026-09-21 15:00:38 BST
mandatory_preservation_cutoff: 2026-09-21 14:55:38 BST
forward_research_stop: 2026-09-21 14:51:10 BST
preservation_start: 2026-09-21 14:51:10 BST
preservation_complete: 2026-09-21 14:53:00 BST
final_report_time: 2026-09-21 14:53:20 BST
wall_clock_span_to_preservation_complete: 52m18s
available_research_window_span: 54m56s
forward_research_span: 50m28s
preservation_span: 1m50s
substantive_unit_count: 6
early_stop_check_time: 2026-09-21 14:45:00 BST
early_stop_check_result: continue
target_50m_applies: NO
target_50m_met: N/A
infrastructure_failure: NONE
handoff_commit: <sha>
```

Numbers in the example are illustrative only and are not project telemetry.
