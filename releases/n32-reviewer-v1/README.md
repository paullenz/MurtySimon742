# N32 reviewer-v1 package

12 September 2026.

**Candidate statement**

```text
e(G) <= 256 = floor(32^2/4),
with equality exactly K(16,16).
```

This is an AI-assisted candidate proof, not externally accepted mathematics. Independent specialist review, novelty assessment and independent computational reproduction remain OPEN.

## Start here

- [Complete proof source](../../project/reviews/n32/2026-09-12-reviewer-v1/PROOF.md)
- [Hostile internal audit](../../project/reviews/n32/2026-09-12-reviewer-v1/HOSTILE_AUDIT.md)
- [Reviewer index](../../project/reviews/n32/2026-09-12-reviewer-v1/README.md)
- [Equality certification ledger](../../project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md)
- [Equality replay directory](../../project/research/n32/2026-09-12-equality-v1/README.md)
- [257-edge exact nine-rectangle closure](../../project/research/n32/2026-09-12-t2-frontier-v1/N32_T2_RECTANGLE_POTENTIAL.md)

## Equality replay

From repository root:

```sh
bash project/research/n32/2026-09-12-equality-v1/run_replay.sh
```

The replay reconstructs the 381-profile t=1 score frontier, exactifies 1,369 lifted-potential exclusions, exact-certifies 614 of the 615 full-RX survivors, surfaces the one hand-closed state, and exact-certifies all 61 zero-demand states.

No saved floating dual vector is a proof premise.

## Highest-value review targets

1. selected/residual graph bridge;
2. threshold-capacity lemma and its equality case;
3. endpoint load and source-degree forcing;
4. completeness of the t=1 residual-tail expansion;
5. strengthened zero-demand finite model;
6. independent clean replay of the exact certificate stack.
