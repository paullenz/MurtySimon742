# A hand replacement and a parameterized heavy-label bound

12 September 2026. Candidate mathematics, internally checked. External
mathematical review and novelty assessment remain OPEN.

## Statement

Use the [canonical bridge](../../../research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).
Let I be the labels with demand s_i>=2, k=|I|, and let Z be the sources with
residual degree rho_u>=2, z=|Z|. Write r for the total residual cross degree.
If every u in Z has supplement indegree p_u<=4, then

**6k <= r+6z.**

This is a parameterized necessary condition on canonical graph data. It does
not assume a fixed order, all demands positive, or residual degrees at most
two. The p<=4 hypothesis is essential to this proof and must be checked.

## Proof

Let H_u count selected incidences from u to I. Such incidences have s_i<=rho_u,
so H_u=0 outside Z. The heavy-label supplement argument gives

`sum_Z H_u [H_u>2] <= sum_Z p_u`.                         (1)

Indeed, for a heavy selected arc from u with H_u>2, its supplement is adjacent
to the other H_u-1 heavy labels selected by u. If any of those cross edges is
selected, compatibility gives supplement residual degree at least two. If
all are residual, there are at least two residual edges. Thus the supplement
lies in Z. Distinct selected arcs have distinct oriented selected B-pairs,
and their incoming incidences are counted by p. See the
[source-capped threshold proof](../../../research/general_n/2026-09-12-source-capped-threshold-v1/SOURCE_CAPPED_THRESHOLD.md)
for the underlying forcing and pair uniqueness.

Define the decreasing load potential

`f(L)=[L<=2]+[L<=3]+[L<=4]+[L<=5]`.

For a heavy label, x_i>=s_i>=2 and L_i=R_i+x_i>=2. Hence

`2R_i+2x_i+x_i f(L_i) >= 12`.                            (2)

For 2<=L_i<=5, the left side is at least
`2L_i+2(6-L_i)=12`; for L_i>=6 its first two terms already give 12.

For integers H>=0 and 0<=p<=4, the following source inequality holds:

`2H+H f(H+p) <= 12+2(H[H>2]-p)`.                        (3)

Here is the complete hand case analysis. Move the correction term to the
left and write `g=2H+2p+H f(H+p)-2H[H>2]`.

| H | Bound on g |
|---|---|
| 0 | 2p<=8 |
| 1 | Values for p=0,1,2,3,4 are 6,8,9,10,11 |
| 2 | g=4+2p+2(4-p)=12 |
| H>=3 and H+p>=6 | g=2p<=8 |
| H>=3 and H+p<=5 | H=3,4,5 give 9-p, 8-2p, 5-3p, each at most 9 |

Since q_u>=H_u and f is decreasing, (3) also holds with f(q_u+p_u)
on the left. Each selected incidence u-i satisfies the endpoint load bound
`R_i+x_i>=q_u+p_u`. Therefore

`sum_I x_i f(R_i+x_i) <= sum_Z H_u f(q_u+p_u)`.

Sum (2), use `sum_I R_i<=r`, and count heavy incidences from both ends.
Then apply (3) and (1):

`12k <= 2r+sum_Z (2H_u+H_u f(q_u+p_u)) <= 2r+12z`.

Dividing by two proves the claim. Every inequality is on actual graph counts;
no grouping, linear-programming model or finite search is needed.

## N34 application

The final N34 equality state has

`s=(1^2,2^13)`, `rho=(1^10,2^8)`, `(a,b,t)=(15,18,1)`.

Thus k=13, z=8 and r=26. The canonical supplement bound on Z is
`p<=rho+b-a-1=2+18-15-1=4`. The theorem would require

`78=6*13 <= 26+6*8=74`,

a contradiction. This replaces the sole heavy-split Farkas exclusion in the
current N34 proof. The revised equality ledger is **6,709 hand/accounting
exclusions and 6,837 exact envelope exclusions**, covering all 13,546 states.
The other envelopes remain proof-critical finite arithmetic.

## Discovery and checking provenance

The independently reconstructed whole-count model first confirmed the original
normalization. A class-specific potential search then produced the preserved
23-term and 14-term coefficient records in `compact_heavy.json` and
`compact_simple.json`. A small integer search found the four-step potential
above; its script and results are preserved in `search_small_potential.py`
and `small_potential_search.json`. The hand argument supersedes these numerical
discoveries. `verify_hand.py` checks the finite local N34 domain as a regression;
the unbounded case analysis above proves the parameterized statement.

The old certificate, old relaxation's feasible point, all failed proposals,
the independent model reconstruction, and exact coefficient records remain
available. A feasible relaxation point was never a counterexample graph.
