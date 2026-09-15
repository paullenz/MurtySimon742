# Murty–Simon / Erdős #742 — live current state

> **Operational source of truth.** Read this file first after every timeout, new chat, takeover, or resumed session. `README.md` is the lower-frequency reviewer-facing summary and may lag routine WIP/status checkpoints. The complete pre-transaction-protocol handoff is preserved byte-for-byte at [`archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md`](archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md).

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `POLICY` / `RESEARCH_EXECUTION_POLICY_V3` — protected execution modes fully enacted after bounded tooling reconciliation.

**WORK MODE:** `MATH` for the next research transaction. Requests such as “continue the maths”, “continue”, “carry on”, “proceed”, or “next” default to `MATH` unless the user explicitly asks for admin, audit, status, publication, or recovery work.

**INSPECTED PREDECESSOR:** `956e5633b8099d59ac20607a5e7f66817e9e7036` on `main`. The preceding checkpoint recorded the publication blocker. This commit completes the intended V3 standing-order update using the prepared policy tree; no mathematics changed.

**LAST VERIFIED RESULT:** mathematical status unchanged by the policy rollout. The latest preserved mathematics remains [`project/research/general_n/2026-09-15-tight-label-equality-v1/`](project/research/general_n/2026-09-15-tight-label-equality-v1/): 25 internally verified whole-state certificates and 4,588/4,588 Python/C++ decision agreement. Together with the preceding disjoint strict-block family, 41 current states have internally verified certificates. These remain `NOT_PROMOTED`; external review remains open.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 canonical exclusions / 952 survivors / 3,632 whole-state closures**. The completed 170-candidate forced-core independent audit remains `AUDIT_COMPLETE_NOT_PROMOTED`. No process checkpoint promotes mathematics.

**ACTIVE / PENDING:** mathematical next route remains the one-spare-receiver case `|M|=d+1`, starting from equality rigidity. Quantify each high source's omitted receiver and determine how many additional selected labels can survive; do not extend the equality theorem without a new proof. The earlier state 3349 q-enumeration timeout remains unresolved.

**UNPRESERVED WORK:** `None` after publication of this completed V3 policy checkpoint.

**DEFERRED ADMIN:** automatic workflow-completion reporting remains `NOT_IMPLEMENTED`; it is non-blocking and must not displace the next mathematical transaction. No other non-blocking admin issue should be repaired during `MATH` mode merely because it is noticed.

**NEXT ACTION:** remain in `MATH` mode. Run `python3 project/research/general_n/2026-09-15-tight-label-equality-v1/run_replay.py`; if clean, perform one bounded hand-mathematics unit on `|M|=d+1`. Preserve the first substantive result, failure, counterexample, or changed route immediately before beginning another unit. Do not poll CI or do unrelated repository maintenance during that transaction.

**PROCESS RULE NOW IN FORCE:** `RESEARCH_EXECUTION_POLICY_V3`. MATH mode is protected: exact-input reads → one bounded mathematical unit → immediate checkpoint → one publication verification → next unit. Routine CI is not awaited or repeatedly polled; unrelated admin is deferred; two consecutive connector/write failures trigger the tooling circuit breaker rather than a retry spiral. Recovery from a consistent handoff is narrow and does not reconstruct from chat history.
<!-- CURRENT-STATUS:END -->

## Recovery procedure

1. Read this file first and record current `main` SHA.
2. Read `AGENTS.md`; inspect only commits/evidence required by this handoff and the active work mode.
3. If durable sources agree, execute `NEXT ACTION` directly; do not reconstruct the project from chat history.
4. In `MATH` mode, do one bounded research unit and checkpoint it before beginning the next.

## Checkpoint invariant

A timeout may lose at most the single small in-memory research unit currently being attempted. Results, failures, counterexamples, changed attacks, and completed bounded computations are checkpoint events.

## Protected MATH-mode summary

- no unrelated README/reviewer-document maintenance;
- no broad repo archaeology or CI inventory;
- no repeated workflow polling;
- no piggybacked housekeeping/process fixes;
- maximum one sensible fallback after a preservation write failure;
- after two consecutive connector/write failures, checkpoint `BLOCKED_TOOLING` if possible and stop retrying;
- `UNPRESERVED WORK: None` before starting the next substantive unit;
- put non-blocking process work in `DEFERRED ADMIN:` instead of doing it immediately.