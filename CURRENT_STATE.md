# Murty–Simon / Erdős #742 — live current state

> **Operational source of truth.** Read this file first after every timeout, new chat, takeover, or resumed session. `README.md` is the lower-frequency reviewer-facing summary and may lag routine WIP/status checkpoints. The complete pre-transaction-protocol handoff is preserved byte-for-byte at [`archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md`](archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md).

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `STATUS_ONLY` / `CI_TRIGGER_PROBE` — verification checkpoint for cheap persistence.

**INSPECTED PREDECESSOR:** `e69bc22d5ac7718069b3343150da518f9bc7f608` on `main`. That commit path-scoped the only two legacy proof workflows found to wake on a status-only checkpoint.

**LAST VERIFIED RESULT:** mathematical status unchanged. Latest preserved mathematics remains the tight-label equality package: 25 internally verified whole-state certificates and 4,588/4,588 Python/C++ agreement; with the preceding disjoint strict-block family, 41 current states have internally verified certificates. These remain `NOT_PROMOTED`; external review remains open.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 canonical exclusions / 952 survivors / 3,632 whole-state closures**. The completed 170-candidate forced-core independent audit remains `AUDIT_COMPLETE_NOT_PROMOTED`.

**ACTIVE / PENDING:** inspect the GitHub Actions runs for this status-only commit. Success criterion: `Status synchronization` may run, but neither `Forced core receiver capacity` nor `Fresh forced core high squeeze` may be triggered. Mathematical next route remains the one-spare-receiver case `|M|=d+1`. State 3349 q-enumeration timeout remains unresolved. Automatic workflow-completion reporting remains `NOT_IMPLEMENTED`.

**UNPRESERVED WORK:** `None`.

**NEXT ACTION:** inspect Actions for this commit. If the cheap-checkpoint criterion passes, record that verification in one final status-only checkpoint and then run `python3 project/research/general_n/2026-09-15-tight-label-equality-v1/run_replay.py` before attacking `|M|=d+1`. Checkpoint the first substantive mathematical result or failure before another research unit.

**PROCESS RULE NOW IN FORCE:** never begin research unit N+1 while useful output from unit N exists only in session memory. Every active-line commit refreshes `CURRENT_STATE.md`; README is milestone-only unless itself edited. WIP/failure/status checkpoints are valid. Ten minutes is only a maximum backstop.
<!-- CURRENT-STATUS:END -->

## Recovery procedure

Read this file first; inspect only commits newer than `INSPECTED PREDECESSOR` plus exact named runs/evidence; then execute `NEXT ACTION`. Do not reconstruct the whole project unless durable sources disagree.
