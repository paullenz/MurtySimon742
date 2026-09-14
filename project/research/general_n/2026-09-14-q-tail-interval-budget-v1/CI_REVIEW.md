# Live CI review and failure classification

Checked during the 14 September 2026 interval-budget restart. These are observations at inspection, not guarantees of later run state.

| Run | Observed evidence | Classification / consequence |
|---|---|---|
| 34854911792 | Run not globally completed; plan and visible initial shards green; job audit (255), ID 104025296865, still queued; jobs API total 257 and no aggregate job yet | 2,655 candidates remain UNPROMOTED; first-page success is not full coverage |
| 34875592126 | verify job 104081860854 queued on repeated inspection | Frozen-ledger CI not yet promoted to green |
| 34871045562 | verify job 104066716372 completed successfully, including frozen totals and artifact upload | q-layer threshold CI green |
| 34868771056 | verifier execution passed; frozen-output diff failed only on compact versus multiline JSON arrays; no different value or assertion failure in full job log | Workflow serialization/evidence-comparison failure, NOT mathematical counterexample or verifier failure |
| 34859094097 | Completed artifact 10356424619 downloaded and replayed; frozen output records all 205,919 Hall failures with C_q=0 | Finite 15-state reconnaissance, not a universal zero-crossing theorem |

The historical mincut failure remains preserved in its run logs. Commit `81560e92698d07992df4a53976ee1ea8efaaeb4d` fixes the comparison by canonicalizing both JSON documents and diffing every resulting value and array entry; artifact upload now uses `if: always()`. No frozen mathematical count was changed.

The root README and restart file must keep the promoted frontier at 1,971 exclusions / 3,607 survivors and 977 whole-state closures. Promotion of the independent relational candidates still requires coverage of all 2,655 inputs, state-by-state agreement of both implementations, zero unresolved states, successful aggregate and a separate ledger-promotion step.

Local interval replay and its independent arithmetic audit are separate from both the original 256-shard audit and the new small identity-verifier CI. Green status for one does not imply completion of another.
