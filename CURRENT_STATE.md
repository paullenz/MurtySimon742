# Murty–Simon / Erdős #742 — live current state

> **Operational source of truth.** Read this file first after every timeout, new chat, takeover, or resumed session. `README.md` is the lower-frequency reviewer-facing summary and may lag routine WIP/status checkpoints. The complete pre-transaction-protocol handoff is preserved byte-for-byte at [`archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md`](archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md).

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `BLOCKED_TOOLING` / `RESEARCH_EXECUTION_POLICY_V3` — V3 policy tree prepared, but repeated contents-API writes prevented the intended ref-level publication path within this turn.

**WORK MODE:** `STATUS`. Do not begin new mathematical work until the next session re-reads this handoff and checks whether the prepared V3 policy commit has been fast-forwarded to `main`.

**INSPECTED PREDECESSOR:** `4289d3b3c28dff5173df5bd8f0c4cedafa5187bc` on `main`. Multiple contents-API status-only commits occurred while attempting to publish the prepared atomic V3 policy tree. No mathematics changed.

**LAST VERIFIED RESULT:** mathematical status unchanged. The latest preserved mathematics remains [`project/research/general_n/2026-09-15-tight-label-equality-v1/`](project/research/general_n/2026-09-15-tight-label-equality-v1/): 25 internally verified whole-state certificates and 4,588/4,588 Python/C++ decision agreement. Together with the preceding disjoint strict-block family, 41 current states have internally verified certificates. These remain `NOT_PROMOTED`; external review remains open.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 canonical exclusions / 952 survivors / 3,632 whole-state closures**.

**UNPRESERVED WORK:** the intended V3 policy modifications to `AGENTS.md`, `CANONICAL_REPOSITORY.md`, and `scripts/check_status_sync.py` exist in prepared Git object/commits but have not been verified as published on `main` in this turn.

**DEFERRED ADMIN:** complete one ref-level fast-forward of the prepared V3 policy commit, then verify remote head and live handoff once. Do not perform further contents-API retries.

**NEXT ACTION:** on resumption, first read this file and current `main`; inspect the prepared policy commit `db7145fb7b5ebe5cc8a2dfd421c350e59823cc20`. If `main` does not contain its V3 policy files, fast-forward by creating a child of current main with the prepared V3 tree and updating the branch ref once. Then switch back to `MATH` and resume `|M|=d+1`.

**PROCESS RULE:** tooling circuit breaker activated. Stop administrative retries in this turn rather than consuming more research time.
<!-- CURRENT-STATUS:END -->

## Recovery procedure

1. Read this file first and record current `main` SHA.
2. Resolve only the single prepared V3 policy publication described above.
3. Verify once, then return to mathematics; do not reconstruct the project from chat history.