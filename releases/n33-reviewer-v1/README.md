# N33 reviewer-v1 source package

12 September 2026.

**Candidate statement**

```text
e(G) <= 272 = floor(33^2/4),
with equality exactly K(16,17).
```

This is AI-assisted candidate mathematics, not externally accepted mathematics. Independent specialist review, novelty assessment and independent computational reproduction remain OPEN.

## Start here

- [Complete candidate proof](../../project/research/n33/2026-09-12-candidate-v1/PROOF.md)
- [Hostile internal audit](../../project/research/n33/2026-09-12-candidate-v1/HOSTILE_AUDIT.md)
- [Checkpoint/replay index](../../project/research/n33/2026-09-12-candidate-v1/README.md)
- [Frozen equality frontier](../../project/research/n33/2026-09-12-candidate-v1/N33_T2_FRONTIER.csv)
- [Independent frontier checker](../../project/research/n33/2026-09-12-candidate-v1/check_n33_t2_frontier.cpp)
- [Exact shifted-potential verifier](../../project/research/n33/2026-09-12-candidate-v1/n33_t2_shifted_potential_exact.py)

## Proof shape

The route is unusually compact:

- `Delta=17` is entirely hand-closed; equality forces `K(17,16)`.
- `Delta=18,m>=273` is scalar-impossible.
- `Delta=18,m=272` reduces to 21 demand profiles / 29 residual-tail states. A fixed nine-term potential excludes 25 exactly; four explicit profiles are excluded by hand.
- `Delta=19` is excluded by the thirteen-label theorem.
- `Delta>=20` is excluded by the twelve-label theorem (or the universal-vertex star case).

No full RX/Hall Farkas stage is proof-critical for N33.

## Replay

```sh
bash project/research/n33/2026-09-12-candidate-v1/run_replay.sh
```

Expected finite result:

```text
20,058,300 demand multisets checked
21 score-frontier profiles
29 expanded equality states
25 exact potential exclusions
4 hand states
0 exactification failures
```

Floating LP proposes scalar envelope coefficients only. Accepted finite exclusions are rechecked in integer arithmetic.

## Highest-value review targets

1. universal selected/residual bridge;
2. threshold-capacity proof and equality case;
3. endpoint load/source forcing;
4. the refined threshold count in the four hand profiles;
5. independent reproduction of the 21-profile / 29-state frontier and exact 25-state replay;
6. inherited twelve-, thirteen- and fourteen-label theorems.
