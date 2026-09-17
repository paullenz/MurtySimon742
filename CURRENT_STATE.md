# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has `D>=12`. Scope work now retains exact selected-incidence multiplicities, a full capacitated Hall theorem, and restricted quadratic endpoint potentials that rule out total selected excess `E=0,1,2,3,4` in the mixed demand-4/5 near-Turán frontier at `(a,b,t)=(20,23,2)`.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_E4_TWO_POTENTIAL_CLOSURE_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Continued from the uniform E=3 restricted-quadratic closure. Rather than enlarging a state census, kept the same exact global and demand-restricted incidence ledgers and searched for low-complexity linear support potentials at total selected excess four.

**INSPECTED PREDECESSOR:** `14a2e8380ca134a41d080223ead678c6163b5cf0`. Its uniform E=3 closure, corrected concurrent split-partition proof, full selected-incidence Hall theorem, E<=2 barrier, quadratic endpoint work, earlier Hall/common-margin/staircase/heavy-load packages and five-label `D>=12` theorem remain preserved.

**COMMON RESTRICTED QUADRATIC LEDGER:** as before,

`K_B=sum_u (6+[rho_u=4])q_u(p_u+q_u)`

and

`K_A=sum_i (6+[s_i=4])x_i C_i`

satisfy `K_B<=K_A`. This combines six copies of the global quadratic endpoint inequality with the restriction of that inequality to residual-degree-four sources, whose selected labels must have demand four.

**E=4 EXACT LOCAL CONSEQUENCE:** total selected excess `E=4` and distinct selected labels at every source imply

`q_u g_u<=4`, where `g_u=max(0,p_u-rho_u+1)`.

Two support-potential pairs for the same `(K_B,K_A)` suffice.

**POTENTIAL A:** every allowed source satisfies

`(6+[rho=4])q(p+q) >=70p+112q-98rho-112`,

and every allowed label satisfies

`(6+[s=4])xC <=112+28R+66[s=5]+189e`.

For demand four the label slack is exactly `7e(19-e-R)>=0`; for demand five it is `2(14-R)+e(129-6R-6e)>=0`. Summation gives the necessary gap

`140-10k<=0`,

which is impossible for `k=0,...,13`.

**POTENTIAL B:** every allowed source satisfies

`(6+[rho=4])q(p+q) >=60p+102q-79rho-108`,

and every allowed label satisfies

`(6+[s=4])xC <=112+30R+38[s=5]+182e`.

The demand-four label slack is `(2-7e)R+126e-7e^2>=0`; the demand-five slack is `e(122-6R-6e)>=0`. Summation gives the necessary gap

`15k-128<=0`,

which is impossible for `k=9,...,20`.

The two intervals overlap on `k=9,...,13` and cover all `k=0,...,20`. Therefore **no E=4 mixed demand-4/5 canonical bridge profile exists**.

**CURRENT BARRIER:** combining the preceding E<=3 results gives

> **Any surviving mixed demand-4/5 near-Turán bridge in the established scope must have total selected excess `E>=5`.**

The E=3 and E=4 proofs themselves do not require the earlier `h>=5` assumption; the combined barrier retains whatever scope hypotheses are required by the E<=2 predecessor.

**AUDIT:** `project/research/general_n/2026-09-17-e4-two-potential-v1/E4_TWO_POTENTIAL.md` contains the hand proof. `check_e4_two_potential.py` exhaustively checks every local source state allowed by the canonical caps plus `qg<=4`, every label state with `s in {4,5}`, `R+s<=19`, `e<=4`, and both global gap families. Independent replay found no local violations and confirms Potential A closes `k<=13` while Potential B closes `k>=9`; together all 21 k-values are covered. External mathematical review remains open.

**FULL SELECTED-INCIDENCE HALL:** remains available and unchanged. For eligibility `s_i<=rho_u`, `e_i>=g_u`, `C_i>=p_u+q_u`, the actual simple selected-incidence matrix has exact row degrees `q_u` and column degrees `x_i`, giving the full capacitated Hall family and the single-row requirement of `q_u` distinct compatible labels.

**STEP-BACK CONSEQUENCE:** the E=4 closure shows that a single restricted incidence ledger can support a **finite dual cover** of the mixture parameter rather than one globally optimal potential. This is more promising than treating excess values with bespoke enumeration. The next test is whether such small potential covers persist at E=5 and whether their coefficients reveal a parameterized family in E.

**FIVE-LABEL STATUS:** every actual whole exact block `|T|=|H|=5` still satisfies `D>=12`, hence `W>=37` or `W>=57` with extras.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No canonical catalogue scan, q-enumeration or conjecture-level promotion.

**PRESERVATION:** E4 theorem/checker are in `project/research/general_n/2026-09-17-e4-two-potential-v1/`; E3 restricted closure in `2026-09-17-e3-restricted-quadratic-v1/`; corrected split-partition work in `2026-09-17-e3-partition-reduction-v1/`; full selected-incidence Hall in `2026-09-17-full-selected-incidence-hall-v1/`; small-excess barrier in `2026-09-17-small-excess-quadratic-v1/`; all earlier structural/audit packages remain preserved.

**UNPRESERVED WORK:** exploratory E=5+ coefficient searches remain diagnostic until frozen; no `E>=6` claim yet.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: attack `E=5` using the same restricted quadratic ledger and exact local condition `q_ug_u<=5`. Search first for a small finite cover of `k=0,...,20` by integer source/label potentials; if successful, derive each potential algebraically and look for interpolation in E. If the dual cover fails, invoke full selected-incidence Hall on the uncovered k-range and preserve the smallest exact incidence-level obstruction rather than broadening demand support.
<!-- CURRENT-STATUS:END -->
