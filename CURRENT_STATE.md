# Murty–Simon / Erdős #742 — live current state

> **Operational source of truth.** Read this file first after every timeout, new chat, takeover, or resumed session. `README.md` is the lower-frequency reviewer-facing summary and may lag routine WIP/status checkpoints. The complete pre-transaction-protocol handoff is preserved byte-for-byte at [`archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md`](archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md).

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `BLOCKED_TOOLING` / `RESEARCH_EXECUTION_POLICY_V3` — prepared V3 policy commit exists but ref-level publication could not be completed within this turn.

**WORK MODE:** `STATUS`.

**INSPECTED PREDECESSOR:** `68162b8f7f998a280ccb69447022713eeba11a62` on `main`.

**LAST VERIFIED RESULT:** mathematics unchanged. Latest preserved mathematics remains the tight-label-equality package with 25 internally verified whole-state certificates and 4,588/4,588 Python/C++ agreement; combined with the preceding strict-block family, 41 current states have internally verified certificates. These remain `NOT_PROMOTED`; external review remains open.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 canonical exclusions / 952 survivors / 3,632 whole-state closures**.

**UNPRESERVED WORK:** V3 standing-order changes are prepared in commit `f0d409fcc1b6514e978577642048978019a04887`, but this turn did not successfully place that commit on `main`.

**DEFERRED ADMIN:** fast-forward `main` to a child containing the prepared V3 policy tree; do not make further contents-API publication retries in this turn.

**NEXT ACTION:** on resumption, read this file first, inspect prepared commit `f0d409fcc1b6514e978577642048978019a04887`, and complete exactly one ref-level fast-forward if still needed. Then switch to `MATH` and resume `|M|=d+1`.

**PROCESS RULE:** tooling circuit breaker active; stop administrative retries now.
<!-- CURRENT-STATUS:END -->
