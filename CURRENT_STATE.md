# Murty–Simon / Erdős #742 — live current state

> **Operational source of truth.** Read this file first after every timeout, new chat, takeover, or resumed session. `README.md` is the lower-frequency reviewer-facing summary and may lag routine WIP/status checkpoints. The complete pre-transaction-protocol handoff is preserved byte-for-byte at [`archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md`](archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md).

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `POLICY` / `CI_TRIGGER_FIX` — make status-only checkpoints genuinely cheap.

**INSPECTED PREDECESSOR:** `03a5e697754931e037af064a656c4c854c3aa23b` on `main`. Verification of that status-only checkpoint found two legacy proof workflows still had unconditional `push` triggers: `forced-core-capacity.yml` and `fresh-forced-core-high-squeeze.yml`.

**LAST VERIFIED RESULT:** mathematical status unchanged. The latest preserved mathematics remains [`project/research/general_n/2026-09-15-tight-label-equality-v1/`](project/research/general_n/2026-09-15-tight-label-equality-v1/): 25 internally verified whole-state certificates and 4,588/4,588 Python/C++ decision agreement. Together with the preceding disjoint strict-block family, 41 current states have internally verified certificates. These remain `NOT_PROMOTED`; external review remains open.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 canonical exclusions / 952 survivors / 3,632 whole-state closures**. The completed 170-candidate forced-core independent audit remains `AUDIT_COMPLETE_NOT_PROMOTED`. No process or CI-trigger commit promotes mathematics.

**ACTIVE / PENDING:** this commit path-scopes the two unconditional proof workflows to their own proof packages/workflow definitions. They may run once because their workflow files themselves changed. A following `CURRENT_STATE.md`-only checkpoint must be used to verify that future status-only saves trigger only the lightweight status synchronization workflow. Mathematical next route remains the one-spare-receiver case `|M|=d+1`. State 3349 q-enumeration timeout remains unresolved. Automatic workflow-completion reporting remains `NOT_IMPLEMENTED`.

**UNPRESERVED WORK:** `None` after publication of this checkpoint.

**NEXT ACTION:** publish one `CURRENT_STATE.md`-only verification checkpoint. Confirm its GitHub Actions runs include `Status synchronization` but not `Forced core receiver capacity` or `Fresh forced core high squeeze`. Then resume mathematics by running `python3 project/research/general_n/2026-09-15-tight-label-equality-v1/run_replay.py` and attack `|M|=d+1`, checkpointing the first substantive result/failure before another research unit.

**PROCESS RULE NOW IN FORCE:** never begin research unit N+1 while useful output from unit N exists only in session memory. Every active-line commit refreshes `CURRENT_STATE.md`; README is milestone-only unless itself edited. WIP/failure/status checkpoints are valid. Ten minutes is only a maximum backstop; substantive events trigger immediate checkpoints.
<!-- CURRENT-STATUS:END -->

## Recovery procedure

1. Read this file first and record current `main` SHA.
2. Inspect commits newer than `INSPECTED PREDECESSOR` plus only exact branches/runs/evidence named above.
3. If durable sources agree, execute `NEXT ACTION` directly.
4. After one substantive research unit, publish a new live checkpoint before beginning the next.
