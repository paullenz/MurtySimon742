# Murty–Simon / Erdős #742 — live current state

> **Operational source of truth.** Read this file first after every timeout, new chat, takeover, or resumed session. `README.md` is the lower-frequency reviewer-facing summary and may lag routine WIP/status checkpoints. The complete pre-transaction-protocol state is preserved byte-for-byte at [`archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md`](archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md).

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `POLICY` / `STATUS_ONLY` — transaction-style timeout-resilient research protocol enacted on 15 September 2026.

**INSPECTED PREDECESSOR:** `6b8e94eb7453259c4f4f849c5affb089bf496ff6` on `main`. No newer main commit existed when this checkpoint was prepared.

**LAST VERIFIED RESULT:** mathematical status unchanged by this policy checkpoint. The latest preserved mathematics remains [`project/research/general_n/2026-09-15-tight-label-equality-v1/`](project/research/general_n/2026-09-15-tight-label-equality-v1/): 25 internally verified whole-state certificates and 4,588/4,588 Python/C++ decision agreement. Together with the preceding disjoint strict-block family, 41 current states have internally verified certificates. These results remain `NOT_PROMOTED`; external review remains open.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 canonical exclusions / 952 survivors / 3,632 whole-state closures**. The completed 170-candidate forced-core independent audit remains `AUDIT_COMPLETE_NOT_PROMOTED`; this policy checkpoint promotes no mathematics.

**ACTIVE / PENDING:** next mathematical route is the one-spare-receiver case `|M|=d+1`, starting from equality rigidity. Quantify each high source's omitted receiver and determine how many additional selected labels can survive; do not extend the equality theorem without a new proof. The earlier state 3349 q-enumeration timeout remains unresolved. Automatic workflow-completion reporting remains `NOT_IMPLEMENTED`.

**UNPRESERVED WORK:** `None` after publication of this checkpoint. All prior live-state material is preserved in Git history and the archived pre-protocol snapshot. Future research must not begin a second substantive unit while the first unit is uncheckpointed.

**NEXT ACTION:** first re-read this file on current `main` and record that head SHA. Run `python3 project/research/general_n/2026-09-15-tight-label-equality-v1/run_replay.py`; if clean, continue the hand mathematics for the one-spare-receiver regime `|M|=d+1`. Checkpoint the first substantive result or failure before beginning another research unit.

**PROCESS RULE NOW IN FORCE:** `CURRENT_STATE.md` is refreshed on every active-line commit. README is refreshed only for material reviewer-facing milestones or whenever README itself is edited. WIP/failure/status checkpoints are explicitly permitted and should be small. The previous requirement to rewrite README for every commit is superseded by `STATUS_SYNC_POLICY_V2` in `AGENTS.md` and `CANONICAL_REPOSITORY.md`.
<!-- CURRENT-STATUS:END -->

## Recovery procedure

1. Read this file first and record current `main` SHA.
2. Compare current head with `INSPECTED PREDECESSOR` and inspect only newer commits plus exact branches/runs/evidence named above.
3. If durable sources agree, execute `NEXT ACTION` directly; do not reconstruct the whole project from chat history.
4. After one substantive research unit, publish a new live checkpoint before beginning the next.

## Checkpoint invariant

A timeout may lose at most the single small in-memory unit currently being attempted. Results, failures, counterexamples, changed attacks, and completed bounded computations are checkpoint events. Ten minutes is only a maximum backstop, not the normal cadence.

## Durable history

The previous full live handoff, including all historical status entries through tight-block equality rigidity, is preserved byte-for-byte at [`archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md`](archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md). Git history remains authoritative for earlier versions. Reviewer-facing cumulative history remains in `README.md`, `RESEARCH_EVIDENCE_INDEX.md`, package READMEs, and the archive.
