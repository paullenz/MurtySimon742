# N=25 re-audit after replay retry

8 September 2026. Requested by Paul Lenz. Internal audit by ChatGPT/Geeps, the same assistant involved in the earlier development. **Independent specialist mathematical review remains OPEN.**

## Verdict

The replay retry succeeded after replacing the interrupted monolithic execution with an exhaustive partitioned replay. **No blocking mathematical or computational defect was found in the completed re-audit.** The candidate remains:

> Every simple diameter-two edge-critical graph on 25 vertices has at most 156 edges, with equality exactly for K(12,13).

This is still a candidate proof, not an externally accepted theorem, PROJECT-CERTIFIED result or full formal verification. The later general-degree results were not used to rescue or replace any part of the original n=25 route.

## Replay outcome

The first hosted retry, run `34212897538`, did not complete. It received a runner shutdown signal and exited 143 after the original Delta14/157 replay and tests had passed. That attempt is preserved as a failed execution, not rewritten as success.

The second retry, run `34216192059` at commit `77dcf450c4b96ef1559d6bd3d362988e016322a8`, completed successfully. The original finite domains were divided into sixteen disjoint shards. Each shard regenerated its assigned states with **both original implementations unchanged** and compared complete state dispositions and labelled-column data immediately. The aggregate job required every shard and the separate assurance job to pass.

| Scope | Outer states | Labelled columns |
|---|---:|---:|
| Delta14, 157 edges | 59,264 | 1,480 |
| Delta15, 157 edges | 108 | 0 |
| Delta15, 156 edges | 211 | 0 |
| Delta14, 156 edges, k=2..5 | 82,452 | 188,520 |
| Delta14, 156 edges, k=1 | 401,543 | 3,252,212 |
| **Total** | **543,578** | **3,442,212** |

All totals match the frozen domains. For the heavy k=1 equality scope, residual levels 26 through 29 are further partitioned by `SHA256(state_key) mod 3`; this is an exhaustive disjoint partition, not sampling. Every shard reports exact agreement between the original primary and independent generators/classifiers. The aggregate record is `evidence/AGGREGATE.json`.

The old monolithic `review_package.py --replay` command itself did not complete in the first hosted attempt. The successful second run is therefore accurately described as a **complete partitioned replay of the original finite domains**, not as completion of that old monolithic process.

## Assurance checks

The assurance job also reran the complete earlier red-team suite. Its arithmetic and structural outputs remain PASS, including the previously audited 543,578 outer states, 3,442,212 labelled columns and 1,959 final equality certificates.

A new `terminal_reaudit.py` imports no frozen final verifier. It independently reconstructs source capacities using reachable subsets of labelled demands assigned to distinct suppliers, then applies the n=25 single simultaneous supplement refinement. It verifies every terminal equality column and every strict subset contradiction:

| Equality scope | Terminal certificates | Minimum strict slack |
|---|---:|---:|
| Delta14, 156 edges, k=2..5 | 171 | 1 |
| Delta14, 156 edges, k=1 | 1,788 | 1 |
| **Total** | **1,959** | — |

The new endpoint therefore removes the original final checker's declared reliance on ledger capacities as an unexamined premise at the terminal stage. It does not replace the whole-domain replay; the two checks are complementary.

## Mutation and robustness findings

The known primary matching-helper defect outside production dimensions was reproduced: in a synthetic `a=15,b=9` case the primary helper can overestimate capacity because Python `zip` truncates to the shorter input. A simple supplier-length guard repairs the synthetic case. The defect is unreachable in the production dimensions: the n=25 scans use `a=9,b=15` or `a=10,b=14`, where maximum trial loads are at most 8 or 9 and there are 14 or 13 suppliers. Its direction is an overestimate, not a false exclusion.

The mutation pass also clarifies the scope of the original modular final certificate checker. In isolation it can exit zero while explicitly recording an unresolved survivor, and it treats preceding ledger capacities as premises. Artificially modifying ledger and certificate capacities consistently can therefore fool that isolated stage. Numerically equal float tokens can also pass ordinary Python equality. These are **not** bypasses of the full frozen proof package: altered bytes fail the manifest, and the new endpoint independently derives capacities, requires integer tokens and requires zero unresolved survivors.

Ordinary malformed terminal certificates—missing, duplicated, wrong arithmetic, repeated/out-of-range subsets, bad totals and wrong input identity—were rejected. The mutation record intentionally distinguishes declared trust boundaries from true malformed-certificate rejection rather than labelling every test identically.

## Mathematical review retained from this re-audit

The structural audit found no missing degree range or equality case. The proof partition remains:

- maximum degree at most 12: degree sum;
- maximum degree 13: direct/two-step witness count, with equality forcing K(12,13);
- maximum degree 14: the complete finite residual route, including the essential k=1 equality domain;
- maximum degree 15: the replacement residual argument and finite checks, not the parked historical hand proof;
- maximum degree 16: residual-activity/small-k contradiction;
- maximum degree at least 17: the cited complement maximum-degree theorem, with star and bipartite exceptions handled separately.

The residual-activity lemma is used only where `t>0`; all production rows satisfy that premise. The low-k injection, selected-edge residual injections and subset-capacity inequality were rederived in the stated necessary direction. No positive-surplus actual critical graph was found in the finite structural samples, so those samples remain falsification tests rather than experimental proof of the dense case.

## Remaining limitations

The principal remaining uncertainty is mathematical rather than arithmetic: universal graph-theoretic lemmas are hand proofs, cited external theorems remain dependencies, and all development and auditing here were produced by the same assistant. The independent-looking implementations are computationally different implementations, not independent researchers. No full n=25 Lean formalisation or external referee verdict exists.

**Disposition:** retain the n=25 result as a complete candidate proof with internally reproduced computation and independent specialist review OPEN. Do not alter the governed theorem ledger on the strength of this internal re-audit. Frozen reviewer files and original evidence remain unchanged.

## Reproducibility record

- Frozen reviewer package SHA-256: `ff5a88f4202fb1e201f52e7e6ec0b50f88248cd43493eee78f120a3c1de15c3d`.
- Frozen candidate evidence SHA-256: `0588c85900762184040dfb313c89d36349f2a8183db5cbc91a1ee50915cb4e95`.
- Successful partitioned run: `34216192059`.
- Successful replay driver commit: `77dcf450c4b96ef1559d6bd3d362988e016322a8`.
- Complete-records artifact ID: `10052070289`, SHA-256 `8761ff3296c48d9c5f9b86b86e23f6015c812df3c660ce528938b596b51d2b55`.
- Failed first hosted attempt: run `34212897538`, exit 143; preserved in `history/INITIAL_RUN.json`.
