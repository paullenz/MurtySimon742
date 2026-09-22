# Residual mass six: exact source-state exclusion of strict surplus

22 September 2026. Internal computer-assisted candidate theorem. This uses only the independently reconstructed selected/residual bridge and the exact finite screens saved here. It is not external verification and does not characterize equality at r=6.

## Claim

For every maximum-root construction and every legal selected assignment,

    r=6 implies t=f-r<=0.

Consequently a strict Murty-Simon counterexample has r>=7, and S<=8 proves the edge bound. Equality is still characterized here only through S<=5.

## Exhaustive reduction

R6_CORE_SCREEN.md proves at the declared necessary-relaxation level that t>0 with r=6 can occur only for residual partition (2,1,1,1,1), in one of four core-graph orbits under permutations of the unit columns. Every actual strict-surplus graph would map into one of these orbits: the screen optimistically removed N-slack and therefore can only add survivors.

For each of the four orbit representatives, screen_r6_sources.py enumerates all physical B-source states restricted to the five positive-residual columns. A state coordinate is:
- 0: adjacent crosspair;
- 1: selected missing crosspair;
- 2: residual missing crosspair.

It imposes the following necessary physical constraints:
1. exact residual column sums (2,1,1,1,1);
2. x_i>=d_i-R_i using the core degree, a lower bound on actual demand;
3. if a source is selected at i, every core neighbour of i is missing at that source;
4. the selected core neighbours of i are at most R_i, by the source-demand injection.

Every active state consumes at least one of the six residual pairs. Residual-free selected states are not silently discarded: the script asserts they cannot satisfy the local conditions. Indeed their selected labels would be a nonempty neighbourhood-closed set in a connected orbit, hence the entire core; the heavy or a unit label then violates its selected-neighbour capacity. Completely adjacent sources are irrelevant and may occur arbitrarily.

The recursion enumerates unordered multisets of active physical-source states, permits repeated states as distinct B-sources, exactly exhausts all six residual pairs, and checks every selected lower bound. The four orbits have respectively 65,61,56,52 allowed single-source states. They have:

    0, 0, 0, 0 surviving source multisets.

Therefore none of the optimistic strict-surplus cores can lift even to the necessary physical source layer. This is stronger than finding no actual graph: it is a finite obstruction before supplements, B-edges or deletion criticality.

## Consequences

Let D=floor(n^2/4)-b(n-b)>=0 and epsilon=m-floor(n^2/4). Since t=D+epsilon and S>=r+2t:
- a strict counterexample has epsilon>=1, hence r>=7 and S>=9+2D;
- therefore S<=8 implies m<=floor(n^2/4);
- the r=6 equality layer t=0 is not screened by this strict-surplus computation;
- balanced complete bipartite graphs remain the mandatory equality controls, and equality is proved exactly only through S<=5 in the current package.

The full live strip remains open. The next high-value step is to classify r=6 product-equality cores or move the strict screen to r=7 without promoting scalar/core feasibility to graph realizability.

## Reproduction

Run:
- python screen_r6_core.py > R6_CORE_SCREEN.json
- python screen_r6_sources.py > R6_SOURCE_SCREEN.json

SHA256:
55ba03b12979cf2e036f32ad7c70f829aaafdcf9e57589e986872cd94806759d  screen_r6_core.py
36756abb7551fb7a3c384de9eb7d6d5da222cd36868b2ece326a255c745a8dab  screen_r6_sources.py

Both outputs are deterministic JSON. The source screen reads the committed core output.
