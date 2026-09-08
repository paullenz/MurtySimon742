# N=25 re-audit — completed partitioned replay

8 September 2026. This re-audits the frozen reviewer edition without invoking later general-degree results. **No blocking mathematical defect was found in the completed internal re-audit. Mathematical status remains CANDIDATE; independent specialist review OPEN.** Frozen sources, original evidence and the governed theorem ledger are unchanged.

The first hosted monolithic retry did **not** finish: run `34212897538`, job `102017807363`, received a runner shutdown signal and exited 143 after the original Delta14/157 replay had passed. That failed execution remains preserved in `history/INITIAL_RUN.json` and is not rewritten as a success.

The successful retry uses `band_replay.py` to run both original generators and classifiers unchanged in sixteen disjoint partitions, comparing complete state and column data immediately rather than retaining a large whole-scope JSON object. GitHub Actions run `34216192059` completed successfully. All sixteen band jobs, the separate assurance job and the aggregate job passed.

The aggregate covers exactly **543,578 outer states** and **3,442,212 labelled columns**:

| Scope | Outer states | Labelled columns |
|---|---:|---:|
| Delta14, 157 edges | 59,264 | 1,480 |
| Delta15, 157 edges | 108 | 0 |
| Delta15, 156 edges | 211 | 0 |
| Delta14, 156 edges, k=2..5 | 82,452 | 188,520 |
| Delta14, 156 edges, k=1 | 401,543 | 3,252,212 |
| **Total** | **543,578** | **3,442,212** |

Every shard matched both original generators/classifiers. The heavy k=1 domain is partitioned exhaustively by residual count and, for r=26..29, by `SHA256(state_key) mod 3`; aggregate totals are checked against the frozen complete domains.

The assurance job independently reran the prior red-team suite and passed. `terminal_reaudit.py`, which imports no frozen verifier, independently reconstructs source caps with a reachable-labelled-subset matching dynamic program and verifies all **1,959** final equality certificates: 171 in k=2..5 and 1,788 in k=1. The minimum strict subset-inequality slack is one in both scopes. Mutation tests reproduce the already known matching-helper defect outside production dimensions and identify declared trust boundaries in the modular final checker; altered inputs fail the frozen manifest and are rejected by the stricter new endpoint.

The successful partitioned replay is a complete replay of the original finite domains, but it is **not** the old monolithic wrapper completing successfully. `unpartitioned_original_wrapper_completed` remains false in the aggregate record. This distinction is intentional.

See [REPORT.md](REPORT.md), [evidence/REMOTE_REPLAY.json](evidence/REMOTE_REPLAY.json), and [evidence/AGGREGATE.json](evidence/AGGREGATE.json). The candidate statement remains `e(G)<=156` for every 25-vertex diameter-two edge-critical graph, equality exactly `K(12,13)`. This remains same-assistant internal assurance, not external peer review or full formal verification.
