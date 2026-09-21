# Graph-level rigid realizability profile

Date: 2026-09-21

## Question

The conditional rigid branch needs a rooted A-cut `A=X⊔Y` built from code-pair classes, with `|X|>=3`, `Y≠∅`, complete X-Y adjacency, and then the appropriate Y→X certificate orientation.  The earlier bounded regression reported zero positive rigid cuts, but did not isolate **which stage first fails**.

This session separated the stages using an independent graph-level scanner.

## Corpus

- mandatory `X3` negative control, **all roots**;
- 40 deterministic greedy actual-D2C graphs for each `n=8,...,18`, **all roots**;
- total: 440 generated actual-D2C graphs plus X3;
- total roots tested: **5,732**.

A separate maximum-degree-root scan used 1,320 generated graphs and 2,078 roots; see `INTRINSIC_RIGID_CUT_SCAN_SUMMARY.json`.

## Stage profile

Across the 5,732-root all-root corpus:

- roots with at least one tight matched pair (`p>0`): **119**;
- roots with `|A|>=4` and `p>0`: **110**;
- roots with at least two active A code-pair classes: **1**;
- roots with `|A|>=4` and at least two active A code-pair classes: **0**.

The single root with at least two active classes is the cube root of **X3**: it has `|A|=3`, `p=4`, and three active code-pair classes.  Since `|A|=3`, it cannot have a nontrivial oriented cut with `|X|>=3` and `Y≠∅`.

Therefore the bounded corpus contains:

- candidate oriented code-pair cuts with `|X|>=3`, `Y≠∅`: **0**;
- complete such cuts: **0**;
- intrinsically Y→X-orientable rigid complete cuts: **0**.

## Interpretation

This materially sharpens the realizability diagnosis.  In the tested actual-D2C corpus, the rigid branch does **not** first fail because a complete code-pair cut lacks enough criticality witnesses.  It fails earlier: once `|A|>=4`, every tested root with a nontrivial tight-pair coordinate system has all A-vertices in a **single complementary code-pair class**.

That empirical fact suggests a much higher-value structural target than another downstream scalar inequality:

> **Multi-pair-class obstruction target.**  Prove, under a suitable large/near-extremal rooted hypothesis, that if `|A|>=4` and the root has tight matched fibres, then either all of A lies in one complementary Boolean code-pair class, or the rooted residual defect pays a definite positive cost.

A theorem of that form would attack the rigid complete-Hall-cut interface *before* the conditional source-tuple machinery is needed.  It would also explain the bounded regression rather than merely reporting no fixtures.

## Trust boundary

This is bounded computational evidence, not a theorem.  The greedy corpus is not exhaustive beyond the atlas range, and absence of a multi-class root does not prove nonexistence.  The important advance is the localization of the first empirical failure stage, not a universal claim.
