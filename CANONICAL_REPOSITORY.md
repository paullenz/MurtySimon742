# Canonical repository

Current project repository: `paullenz/MurtySimon742`

GitHub repository ID: `1359206057`

## Timeout-resilient research protocol

`STATUS_SYNC_POLICY_V2`

Read `CURRENT_STATE.md` first on every restart. Never allow more than one substantive research unit to exist solely in session memory. Checkpoint every substantive result, failure, correction, counterexample, completed bounded computation, before any long-running operation, after material long-run output, and before pause/handoff. Ten minutes is only a maximum backstop.

WIP commits are explicitly valid. Preserve failures and partial work. `CURRENT_STATE.md` is the high-frequency operational source of truth; README is lower-frequency reviewer-facing history and is refreshed for material reviewer-facing milestones or whenever README itself is edited.

Every active-line commit must refresh the `CURRENT-STATUS` block in `CURRENT_STATE.md`. The live block must include `CHECKPOINT CLASS:`, `INSPECTED PREDECESSOR:`, `LAST VERIFIED RESULT:`, `UNPRESERVED WORK:`, and `NEXT ACTION:`. Cheap `CURRENT_STATE.md`-only checkpoints are preferred when no research artifact changed.

On recovery, read current state, inspect only newer commits and exact named branches/runs/evidence, then execute `NEXT ACTION`; do not reconstruct the full project unless durable sources conflict.

Canonical mathematical status remains **4,626 exclusions / 952 survivors / 3,632 whole-state closures** unless a separately reviewed promotion changes it. Audit and external-review gates remain separate from internal checks and CI.
