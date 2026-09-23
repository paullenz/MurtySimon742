# Demand-15/16 normal form for an H>=15 obstruction

23 September 2026. Status: **proved internal reduction at the exact graph-level certificate-assignment interface**. It does not strengthen the audited bridge into that interface.

Suppose the exact Hall envelope satisfies `H>=15`. By `HALL_ENVELOPE_EXACTNESS.md` there is a legal graph-level assignment of distinct physical certificate edges with total positive demand

`S=sum_i max(0,2x_i-h_i)=H>=15`.

Delete all assigned edges belonging to labels of zero demand. Then repeatedly delete one assigned physical certificate edge from a demand-positive label whenever the resulting total demand is still at least 15. This process terminates because the assignment is finite and deletion preserves legality.

## Lemma: irreducible total is 15 or 16

In the resulting deletion-minimal assignment,

`S in {15,16}`.

Proof. Removing one assigned edge from a positive label reduces its contribution by at most two: if its demand is at least three, the demand falls by exactly two; if its demand is one or two, that label becomes nonpositive and the total falls by one or two. Therefore if the current total were at least 17, deleting any assigned edge of any positive label would leave total at least 15, contradicting deletion-minimality. Since total remains at least 15, only 15 or 16 are possible. QED.

If `S=16`, no positive label can have demand one: deleting one of its assigned edges would remove that one unit and leave total 15. Hence every positive label in an irreducible `S=16` assignment has demand at least two, and there are at most eight positive labels. For `S=15` there are at most fifteen positive labels.

The assigned-witness graph construction survives deletion verbatim. Thus every hypothetical `H>=15` obstruction has a legal subassignment whose assigned-witness graph satisfies all of `ASSIGNED_WITNESS_OBSTRUCTION.md` and `STAR_CRITICALITY_SLACK.md`, but with bounded total left demand 15 or 16.

## Finite demand-pattern consequence

Up to permutation of labels, there are only 176 integer partitions of total demand 15. There are 231 partitions of 16, and only 55 of them have no part equal to one; these 55 are the only deletion-minimal 16-patterns. A 15-pattern uses at most 15 labels; an irreducible 16-pattern uses at most 8.

For a label of demand `d_i=2x_i-h_i>0`, simplicity gives `x_i<=h_i`, hence `x_i>=d_i`. Therefore the quadratic star-slack theorem supplies at least

`binom(x_i,2) >= binom(d_i,2)`

units of pair-deficit slack before overlap between different labels is considered. In particular every irreducible 16-pattern has at least eight units of per-centre star slack when summed labelwise (the minimum occurs at eight demand-2 labels). This sum cannot yet be charged injectively to global `D`, so it is a diagnostic lower bound rather than a theorem-level global deficit bound.

## Why this matters

The residual proof no longer needs to reason about arbitrarily large total Hall demand. To contradict a strict counterexample it is enough to exclude two bounded demand totals, 15 and 16, under the actual graph-realizability constraints. Large individual certificate counts can still occur because a small demand may sit on a large `h_i`, so the problem is not finite merely from this reduction; however the number of demand-positive labels and their demand composition are now absolutely bounded.

This is compatible with both parity equality controls: balanced complete bipartite graphs have no positive obstruction demand at this interface.

## Next target

Retain the 15/16 normal form while combining the quadratic star-slack inequalities for multiple labels. The principal unresolved issue is multiplicity: the same endpoint deficit `delta_t` can enter the slack inequalities of several labels. Either bound that reuse using assigned physical-edge/source geometry, or preserve an actual D2C negative control showing high multiplicity. Do not expand back to arbitrary total `H` unless a proof step genuinely requires it.
