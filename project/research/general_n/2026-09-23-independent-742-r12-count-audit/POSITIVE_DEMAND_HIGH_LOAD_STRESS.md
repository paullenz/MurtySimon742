# Actual-D2C positive-demand/high-load stress

23 September 2026. Status: **FINITE_INTERNAL_DIAGNOSTIC**.

A fresh deterministic greedy deletion generator produced 990 distinct diameter-two-critical graphs on 7--16 vertices. Across 1,612 maximum-degree roots, 13,746 legal quasi-edge selections were checked (exhaustively for choice spaces at most 256, otherwise 32 deterministic samples). There were 1,677 positive-demand selections, 14 high-load selections, and no positive-surplus selection.

The strongest exhaustive witness is the n=15, seed=55, root=13 fixture saved first in the JSON output. It has a=b=7, S=2, H0=1 and two physical sources each co-selecting the two demand-positive labels. Their F-codegree is 2, exceeding a/5. Thus the purely local statement “D2C criticality forbids a high-codegree label pair with a common selected source” is false, even with a genuine high-load source.

This does **not** realize the plateau or threaten the edge bound: the witness has t=-21, only two selected-pair occurrences, and none of the run's fixtures has positive surplus. The useful conclusion is a route restriction: any successful closure must use positive density, surplus/near-extremality, or the full plateau endpoint hypotheses; it cannot exclude the local pair configuration by itself.

Scope: finite internally generated actual D2C graphs. Sampled selections are labelled in the JSON. Bounded nonappearance of positive surplus is not nonrealizability, and this is not external verification.
