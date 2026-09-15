# Murty–Simon / Erdős #742 — live current state

> **Operational source of truth.** Read this file first after every timeout, new chat, takeover, or resumed session. `README.md` is the lower-frequency reviewer-facing summary and may lag routine WIP/status checkpoints. The complete pre-transaction-protocol handoff is preserved byte-for-byte at [`archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md`](archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md).

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `STATUS_ONLY` — clean post-rollout checkpoint for `STATUS_SYNC_POLICY_V2`.

**INSPECTED PREDECESSOR:** `7b67d1fbf8eb5fa0e0ef1ea334df28120a8ad8fd` on `main`. Remote verification confirmed the new transaction rules in `AGENTS.md`, the v2 synchronization guard in `scripts/check_status_sync.py`, and the byte-identical archived pre-protocol handoff.

**LAST VERIFIED RESULT:** mathematical status unchanged by the process rollout. The latest preserved mathematics remains [`project/research/general_n/2026-09-15-tight-label-equality-v1/`](project/research/general_n/2026-09-15-tight-label-equality-v1/): 25 internally verified whole-state certificates and 4,588/4,588 Python/C++ decision agreement. Together with the preceding disjoint strict-block family, 41 current states have internally verified certificates. These remain `NOT_PROMOTED`; external review remains open.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 canonical exclusions / 952 survivors / 3,632 whole-state closures**. The completed 170-candidate forced-core independent audit remains `AUDIT_COMPLETE_NOT_PROMOTED`. No process checkpoint promotes mathematics.

**ACTIVE / PENDING:** next mathematical route is the one-spare-receiver case `|M|=d+1`, starting from equality rigidity. Quantify each high source's omitted receiver and determine how many additional selected labels can survive; do not extend the equality theorem without a new proof. The earlier state 3349 q-enumeration timeout remains unresolved. Automatic workflow-completion reporting remains `NOT_IMPLEMENTED`.

**UNPRESERVED WORK:** `None`. The governing policy, live handoff, synchronization guard, and archived old handoff are durable on `main`.

**NEXT ACTION:** on resumption, first re-read this file on current `main` and record that head SHA. Run `python3 project/research/general_n/2026-09-15-tight-label-equality-v1/run_replay.py`; if clean, continue the hand mathematics for `|M|=d+1`. Checkpoint the first substantive result or failure before beginning another research unit.

**PROCESS RULE NOW IN FORCE:** never begin research unit N+1 while useful output from unit N exists only in session memory. Every active-line commit refreshes `CURRENT_STATE.md`; README is refreshed only for material reviewer-facing milestones or whenever README itself is edited. WIP/failure/status checkpoints are explicitly valid. Ten minutes is only a maximum backstop; substantive events trigger immediate checkpoints.
<!-- CURRENT-STATUS:END -->

## Recovery procedure

1. Read this file first and record current `main` SHA.
2. Inspect commits newer than `INSPECTED PREDECESSOR` plus only exact branches/runs/evidence named above.
3. If durable sources agree, execute `NEXT ACTION` directly; do not reconstruct the project from chat history.
4. After one substantive research unit, publish a new live checkpoint before beginning the next.

## Checkpoint invariant

A timeout may lose at most the single small in-memory research unit currently being attempted. Results, failures, counterexamples, changed attacks, and completed bounded computations are checkpoint events.
