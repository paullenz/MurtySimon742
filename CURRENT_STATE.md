# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has `D>=12`. Scope work now retains exact selected-incidence multiplicities, has a general weighted endpoint/excess ledger, and rules out the entire mixed demand-4/5 near-Turán `h>=5` band at `(a,b,t)=(20,23,2)` whenever total selected excess is `E<=2`.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_SMALL_SELECTED_EXCESS_BARRIER_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Continued the positive-selected-excess attack from the quadratic endpoint checkpoint. Rather than enumerating positive-excess histograms, retained the global excess budget on the actual selected incidence matrix.

**INSPECTED PREDECESSOR:** `41ff4233d8054a0b7090f58d902826701ce85cb7`, whose quadratic endpoint lemma, zero-excess mixed 4/5 closure, selected-witness Hall theorem, common-margin/excess-aware endpoint results, staircase/heavy-load theory, five-label `D>=12` theorem and canonical counts remain preserved.

**GENERAL LAST RESULT:** on every selected incidence `ui`, retain

`C_i=R_i+x_i >= p_u+q_u`

and

`e_i=x_i-s_i >= g_u:=max(0,p_u-rho_u+1)`.

Because the actual selected incidence matrix has row degrees exactly `q_u` and column degrees exactly `x_i`, for every real `lambda>=0`,

`sum_i x_i(C_i+lambda e_i) >= sum_u q_u(p_u+q_u+lambda g_u)`.

This is the weighted endpoint/excess ledger. It charges the excess condition on **every** selected incidence, not merely once per active source.

**SMALL-EXCESS CLOSURE:** fix `(a,b,t)=(20,23,2)`, all twenty demands in `{4,5}`, let `k` be the number of demand-five labels, and assume at least five residual sources have `rho>=5`. Write total selected excess

`E=sum_i(x_i-s_i)`.

Then `r=76+k` and `Q=80+k+E`. Since positive demand gives `d_i=R_i+s_i<=19`, the zero-excess label side sharpens to

`U_0(k)=624+13k+min(14k,76+k)`.

For `E<=2`, adding excess raises `sum x_iC_i` by at most `24E+E^2`.

On the source side, distinct selected labels at a source and the excess condition give

`q_u max(0,p_u-rho_u+1) <= E`.

For `E<=2` this leaves only the exceptional active possibilities `(p,q)=(rho,1),(rho,2),(rho+1,1)` beyond the old `p<=rho-1` regime; direct substitution shows the previous local support inequality remains valid unchanged:

`10p_u+15q_u-q_u(p_u+q_u) <= 10rho_u+20+delta_k[rho_u=4]`,

with `delta_k=6` for `k<=14`, `5` at `k=15`, `2` at `k=16`, and `0` for `k>=17`.

After summation and the residual-mass bound on `c_4=#{rho=4}`, the zero-excess source-minus-label gaps over `k=0,...,20` are

`90,78,66,48,36,24,8,9,10,5,6,7,2,3,4,15,64,97,98,99,100`.

Thus `E=0,1` are immediately impossible. For `E=2` every `k!=12` remains strict. At the sole arithmetic boundary `k=12,E=2`, equality would force `rho=(5^5,4^15,1^3)`. If every local source bound were tight, the incoming total would be at most

`3*3+15*3+5*7=89`,

but the exact orientation ledger requires `sum p=Q=94`. Hence that boundary is also impossible.

Therefore:

> **Any canonical bridge profile in this mixed `{4,5}`, `h>=5` scope must have total selected excess `E>=3`.**

This strictly extends the preceding zero-excess closure and does not use a broad survivor census.

**AUDIT:** `project/research/general_n/2026-09-17-small-excess-quadratic-v1/SMALL_EXCESS_BARRIER.md` contains the hand proof and weighted general lemma. `check_small_excess_barrier.py` enumerates every local integer source state used for `E=0,1,2`, checks all 21 arithmetic gaps and the unique `k=12,E=2` boundary. Independent replay in the working environment returned `PASS_SMALL_EXCESS_BARRIER`; exact tight states were `rho=1:(p,q)=(3,0)`, `rho=4:(3,6)`, `rho=5:(4,5),(4,6),(7,0)`. External mathematical review remains open.

**STEP-BACK CONSEQUENCE:** positive excess is no longer merely the next unanalysed coordinate: the first two units are structurally impossible. The next obstruction, if any, begins at `E=3`. At that point new source states first appear (notably `g=3,q=1` and `g=1,q=3`), so the right next theorem is to use excess-level selected-incidence capacities rather than weaken back to a one-source envelope.

A necessary threshold family available directly from the incidence system is

`sum_{u:g_u>=h} q_u <= sum_{i:e_i>=h} x_i` for every `h>=1`.

This should be combined with the weighted ledger and the exact total excess budget before any bounded enumeration.

**FIVE-LABEL STATUS:** every actual whole exact block `|T|=|H|=5` still satisfies `D>=12`, hence `W>=37` or `W>=57` with extras.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No canonical catalogue scan, q-enumeration or theorem promotion.

**PRESERVATION:** small-excess theorem/checker are in `project/research/general_n/2026-09-17-small-excess-quadratic-v1/`; quadratic endpoint theorem/application/checker remain in `2026-09-17-quadratic-endpoint-v1/`; selected-witness Hall, excess-aware endpoint, common-margin, uniform-band and all earlier proofs/obstructions remain preserved.

**UNPRESERVED WORK:** None for the `E<=2` theorem after remote preservation and local replay.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: attack `E=3` first, using the threshold selected-incidence excess capacities `sum_{g_u>=h}q_u <= sum_{e_i>=h}x_i` together with the weighted endpoint/excess ledger. Characterize the genuinely new exceptional source states at `E=3`, derive a hand correction/transport inequality if possible, and preserve either an `E>=4` barrier or the smallest exact bridge-level obstruction. Reassess before broadening to larger excess or demands outside `{4,5}`.
<!-- CURRENT-STATUS:END -->
