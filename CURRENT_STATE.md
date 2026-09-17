# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has `D>=12`. Scope work now retains the complete selected-incidence matrix and has reduced the mixed demand-4/5 near-Turán `E=3` problem to one sharply defined case: a single label carrying all three units of selected excess.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_E3_REDUCED_TO_UNIQUE_TRIPLE_EXCESS_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Reassessed the `E=3` problem after the full selected-incidence Hall theorem rather than launching the unfinished transport screen. Splitting the three excess partitions exposed a compact coefficient change that eliminates two partitions by hand.

**INSPECTED PREDECESSOR:** `ff4553d8c3c77da0d9f1343a34d6f8b565815bb3`, whose full selected-incidence Hall theorem and strictness example remain preserved. The `E<=2` small-excess barrier, quadratic endpoint ledger, common-margin/Hall hierarchy, staircase/heavy-load work and five-label `D>=12` theorem remain unchanged.

**NEW HAND RESULT — E=3 PARTITION REDUCTION:** at total selected excess `E=3`, the possible positive excess multisets are `(3)`, `(2,1)`, `(1,1,1)`. For the split partitions `(2,1)` and `(1,1,1)`, every source satisfies the new support inequality

`12p_u+15q_u-q_u(p_u+q_u) <= 12rho_u+24`.

The proof uses exact selected-incidence multiplicity: with `(1,1,1)`, a positive excess requirement has `g=1` and `q<=3`; with `(2,1)`, `g=1` gives `q<=2` and `g=2` gives `q<=1`. For `g=0`, the usual `p<=rho-1`, `q<=20-rho` bounds suffice.

Summing over the 23 sources gives

`sum_u q_u(p_u+q_u) >= 27Q-12r-24b = 777+15k`,

where `k` is the number of demand-five labels, `r=76+k`, and `Q=83+k`.

The zero-excess label ceiling remains

`U_0(k)=624+13k+min(14k,76+k)`.

At `E=3`, partition `(1,1,1)` raises the label side by at most `75`, while `(2,1)` raises it by at most `77`. Even against the larger ceiling `U_0(k)+77`, the new source lower bound has strict gap for every `k=0,...,20`: for `k<=5` the gap is `76-12k>=16`, and for `k>=6` it is exactly `k>=6`. Therefore both split partitions are impossible.

**IMPORTANT CORRECTION / PRESERVED FAILURE:** the first attempt in this research unit tried to reuse the older `10p+15q` inequality for `(1,1,1)`. That is false: `(rho,p,q,g)=(5,5,3,1)` gives `71>70`. The failed coefficient choice is preserved in the proof/checker. Replacing coefficient 10 by 12 fixes the local theorem cleanly and removes the former `rho=4` bonus term entirely.

**SOLE REMAINING E=3 CASE:** any surviving `E=3` bridge must have exactly one excess-positive label `i_*` with `e_*=3`, hence `x_*=s_*+3 in {7,8}`. This case genuinely escapes the new 12/15 support inequality: `(rho,p,q,g)=(4,6,1,3)` gives `80>72`, and `(5,7,1,3)` gives `91>84`. Every such `g=3` source must use the same unique label `i_*`, and eligibility requires `s_*<=rho_u` and `C_*>=rho_u+3`. Thus the remaining obstruction is a single-column row-packing / endpoint-tail problem.

**FULL SELECTED-INCIDENCE HALL REMAINS AVAILABLE:** for every source subset `S`,

`sum_{u in S} q_u <= sum_i min(x_i, |{u in S: s_i<=rho_u, e_i>=g_u, C_i>=p_u+q_u}|)`.

This is now the natural tool for the unique `(3)` partition rather than another broad scalar census.

**AUDIT:** `project/research/general_n/2026-09-17-e3-partition-reduction-v1/E3_PARTITION_REDUCTION.md` contains the corrected hand proof and explicitly records the failed first coefficient attempt. `check_e3_partition_reduction.py` exhaustively checks every local state for both closed partitions across `k=0..20`, `rho=1..20`, verifies all global gaps, and confirms the surviving `(3)` local obstruction. Local replay returned `PASS_E3_PARTITION_REDUCTION`. External mathematical review remains open.

**SMALL-EXCESS STATUS:** the earlier theorem `E>=3` remains valid. The new result strengthens it conditionally: if `E=3`, then necessarily `(e_i)^+=(3)`.

**E=3 DIAGNOSTIC:** the earlier exploratory integer transport model reportedly rejected tested patterns for all three partitions at difficult `k=9,10,12,13,14`, but that screen remains unfrozen and is not used as a theorem here. The two split partitions are now closed independently by hand; only the unique triple-excess partition remains to justify.

**FIVE-LABEL STATUS:** every actual whole exact block `|T|=|H|=5` still satisfies `D>=12`, hence `W>=37` or `W>=57` with extras.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No canonical catalogue scan, q-enumeration or conjecture-level promotion.

**PRESERVATION:** corrected E=3 partition reduction/checker are in `project/research/general_n/2026-09-17-e3-partition-reduction-v1/`; full selected-incidence Hall theorem/checker remain in `2026-09-17-full-selected-incidence-hall-v1/`; small-excess barrier remains in `2026-09-17-small-excess-quadratic-v1/`; all earlier structural and audit packages remain preserved.

**UNPRESERVED WORK:** the exploratory integer transport screen for complete `E=3` closure has not yet been frozen as a proof package; do not claim `E>=4` from it.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: step back again, then attack only the unique `(3)` partition. Couple the exceptional `g=3` sources to the single excess-three label's exact column capacity `x_*=7 or 8` and endpoint mass `C_*`, using full row-packing/Hall and the demand-four endpoint tail. Seek a compact hand inequality bounding the total support bonus from `p=rho+2,q=1`; if such a hand bound fails, freeze the smallest true incidence-level survivor rather than returning to a broad histogram scan. Do not move to `E>=4` until this final `E=3` partition is resolved.
<!-- CURRENT-STATUS:END -->
