# Exact strict r=9 closure

22 September 2026. Trust level: internally checked, computer-assisted necessary-condition exclusion. This remains inside the independent complement/residual/profile route. It is not external review and does not settle the full conjecture.

## Result

The finite core/source/supplement pipeline gives

`r=9 => t<=0`.

Therefore a strict counterprofile must have `r>=10`. With `t=D+epsilon>=1` and `S>=r+2t`, this extends the internal computer-assisted edge bound from `S<=10` to **`S<=11`**. Equality scope is unchanged.

## Support-eight completion

The support-seven checkpoint left only partition `(2,1,1,1,1,1,1,1)`; the all-unit support-nine partition is already excluded by the unit-column theorem.

A colour-preserving generator treats the distinguished residual-2 label as rooted and quotients the seven unit labels under all 5040 permutations. It independently obtains:

- 1044 unlabelled graphs on the seven unit labels;
- 79,264 rooted/coloured core orbits after quotienting the heavy-label neighbourhood under each unit graph's automorphism group;
- 69 optimistic strict-surplus core orbits after the audited ledger/capacity filters;
- 0 physical-source-feasible orbits after exact residual sums, selected lower bounds, neighbour containment and source-demand injection caps.

Thus support eight has no source-feasible strict core. Together with the saved support<=7 supplement closure and the unit-column theorem, all residual partitions of nine are closed.

## Reproducibility and limits

`enumerate_r9_support8_orbits.cpp` writes the 69 exact representatives in `R9_SUPPORT8_CORE_MASKS.txt`. `screen_r9_support8_sources.py` performs the independent physical-source DP and writes the zero-survivor result. The C++ mask order and Python edge order are both lexicographic `combinations(range(8),2)`.

The pipeline proves infeasibility of necessary profiles, not graph realizability of survivors. No survivor exists in the last source screen, but independent replay is still appropriate before promotion. The general theorem and live maximum-degree strip remain open.
