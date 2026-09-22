# Residual mass seven: exact source-state exclusion of strict surplus

22 September 2026. Internal computer-assisted candidate theorem, pending adversarial and external review.

The optimistic core screen reduces every hypothetical r=7 strict-surplus profile to 15 residual-core orbits across partitions (3,1,1,1,1), (2,2,1,1,1), and (2,1,1,1,1,1).

screen_r7_sources.py independently enumerates all physical B-source state multisets over each core. It imposes exact residual column sums, core selected-demand lower bounds, the selected-source missing-neighbour rule and selected-neighbour injection capacity. Repeated source states are allowed. Residual-free selected states are asserted unable to meet any P-label demand and are omitted only on that basis; arbitrary fully adjacent sources remain allowed.

The 15 core orbits have between 52 and 157 allowed active single-source patterns. Every orbit has exactly zero source-multiset survivors. Thus no optimistic r=7 strict-surplus core lifts to the necessary physical source layer; supplements and graph realization need not be invoked.

Combining the exact core and source screens gives the internal computer-assisted statement:

    r=7 implies t=f-r<=0.

Together with the r<=6 work, a strict Murty-Simon counterexample must have r>=8. Since t=D+epsilon>=D+1 and S>=r+2t, it must satisfy

    S >= 10+2D.

Therefore S<=9 proves the edge bound. Equality remains characterized only through S<=6; this strict screen says nothing about t=0 at r=7.

This is not a full-strip theorem. It depends on deterministic finite enumeration over an explicitly proved necessary relaxation. Exact evidence: R7_CORE_SCREEN.json, R7_SOURCE_SCREEN.json and their scripts. The next step is an independent replay/hostile audit, then either r=7 equality or r=8 strict classification.
