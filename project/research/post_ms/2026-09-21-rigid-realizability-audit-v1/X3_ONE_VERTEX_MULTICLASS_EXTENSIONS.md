# X3 one-vertex extensions: actual-D2C counterexamples to the naive single-pair-class obstruction

Date: 2026-09-21

## Purpose

The bounded random regressions suggested a tempting graph-level conjecture: perhaps every rooted D2C graph with `|A|>=4` and at least one tight matched pair has all A-vertices in a single complementary Boolean code-pair class.  Before promoting that conjecture, this session attacked it directly by extending the mandatory X3 negative control by one A-vertex.

## Exhaustive extension test at the X3 cube root

Start with X3 (`n=12,m=32`) at its cube root `r`.  The root has four tight matched pairs and three A-vertices (`a0,a1,a2`).  Add a new vertex `z` with:

- `zr` a nonedge, so `z∈A`;
- exactly one neighbour in each of the four tight matched pairs, giving all `2^4=16` possible Boolean codes;
- arbitrary adjacency to the three old A-vertices, giving `2^3=8` possibilities.

Thus **128** rooted extensions are checked exactly.  Of these, 89 retain diameter two and **five are actual diameter-2-critical graphs**.

All five D2C hits have the new vertex anticomplete to the old A-layer.  Their new-vertex codes and graph6 strings are:

| new code | graph6 |
|---|---|
| `0000` | `L?~muMwhKdOJBo` |
| `0011` | `L?~muMwhKdOJBK` |
| `0101` | `L?~muMwhKdOJAi` |
| `0110` | `L?~muMwhKdOJAU` |
| `1001` | `L?~muMwhKdOJ@h` |

For example, the first extension has A-codes

- `a0 : 0000`,
- `new : 0000`,
- `a1 : 0011`,
- `a2 : 0101`.

Hence `|A|=4`, `p=4`, and there are **three active complementary code-pair classes**.  The fourth and fifth hits similarly give multiple classes.  These are direct actual-D2C counterexamples to the naive single-pair-class obstruction.

## Why the rigid-cut regression still has no hit

The counterexamples do **not** realize the rigid complete Hall cut.  In all five hits the four A-vertices are independent: the added vertex is anticomplete to the old A-layer, and the old X3 face vertices are already independent.  Therefore every nontrivial A-cut has all crossing pairs missing, so Hall-cut completeness fails maximally.

This locates the graph-level obstruction more accurately:

- multiple A code-pair classes are genuinely realizable already at `n=13`;
- what remains absent is **dense/complete adjacency between different code-pair classes**;
- the correct structural target is therefore an **inter-class edge/defect price**, not a theorem forbidding multiple classes outright.

## Consequence for the next attack

Seek a raw graph-level lemma of the form

> if A contains multiple complementary code-pair classes, then edges between different classes are scarce, or every such edge consumes a rooted criticality/defect resource;

and feed that cost into `f=e(G[A])`, `r`, and `delta=r-f`.

This is better aligned with both X3 and its actual-D2C one-vertex extensions: they show that multi-class support itself is harmless, but it arrives with an independent A-layer and hence a large missing-cross-edge bill.

## Trust boundary

The extension enumeration is exact for the stated 128 one-vertex rooted extensions.  It does not classify all 13-vertex D2C graphs.  The negative conclusion is only that the naive single-class conjecture is false, while the five listed graph6 strings are explicit positive counterexamples.
