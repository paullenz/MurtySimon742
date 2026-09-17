# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has `D>=12`. Scope work now retains exact selected-incidence multiplicities, full capacitated Hall, and endpoint-tail restricted quadratic ledgers. In the mixed demand-4/5 near-Turán frontier at `(a,b,t)=(20,23,2)`, total selected excess `E=0,...,8` is internally excluded; any survivor in the established scope must have `E>=9`.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_SELECTED_EXCESS_BARRIER_E9_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Continued the exact-incidence scope attack without returning to the canonical survivor catalogue. After the E=4 closure, successively retained excess-threshold and endpoint-threshold quadratic incidence layers. This closes E=5,6,7,8 and exposes E=9 as the first genuine obstruction to the current affine support-potential hierarchy.

**INSPECTED PREDECESSOR:** `1ce8f16ed062acb4d779a528b223d871d84fd3d7` plus the preserved E=5/E=6/E=7/E=8 packages committed afterwards. All earlier E<=4 work, full selected-incidence Hall, quadratic endpoint results, common-margin/Hall hierarchy, staircase/heavy-load work and five-label `D>=12` theorem remain preserved.

**EXACT INCIDENCE LAYERS NOW AVAILABLE:** for every selected incidence `ui`,

`s_i<=rho_u`, `e_i>=g_u=max(0,p_u-rho_u+1)`, `C_i=R_i+x_i>=w_u=p_u+q_u`.

Besides the global quadratic endpoint inequality, one may sum endpoint load over any source threshold and dominate it by the corresponding compatible label threshold. In particular:

- `rho=4` sources -> `s=4` labels;
- `g>=h` sources -> `e>=h` labels;
- `w>=T` sources -> `C>=T` labels;
- intersections of these restrictions are valid as well.

Exact selected-label distinctness gives `q_u g_u<=E`. Full capacitated Hall remains available on the complete eligibility graph.

**E=5 CLOSURE:** `project/research/general_n/2026-09-17-e5-excess-restricted-v1/` gives one hand potential using

`12*(global)+2*(rho=4)+(g>=1)`.

Its source/label inequalities sum to the contradiction gap

`63+2k>0`

for every `k=0,...,20`. The checker has zero local violations.

**E=6 CLOSURE:** `project/research/general_n/2026-09-17-e6-endpoint-staircase-v1/` adds endpoint-tail weights

`psi_6(z)=3[z>=5]+3[z>=7]+2[z>=8]+[z>=9]+[z>=11]`.

With weights

`omega_B=3[rho=4]+[g>=1]+psi_6(w)`,
`omega_A=3[s=4]+[e>=1]+psi_6(C)`,

the exact local potentials sum to a **constant gap 12**, independent of `k`. The checker exhausts all allowed local source/label states.

**E=7 AND E=8 CLOSURE:** `project/research/general_n/2026-09-17-e7-e8-endpoint-staircase-v1/` records two further short endpoint staircases. At E=7 the summed gap is

`190-9k>=10`,

and at E=8 the gap is the **constant 4**. Exact local replay finds no violations.

**CURRENT BARRIER:** combining all preserved results gives

> **Any surviving mixed demand-4/5 near-Turán bridge in the established scope must have total selected excess `E>=9`.**

The E=3,...,8 closures themselves do not need the original `h>=5` assumption; the combined statement retains the scope hypotheses required by the E<=2 predecessor.

**E=9 METHOD OBSTRUCTION:** this is the first excess level where the affine support-potential programme fails in the middle demand-mixture range. A normalized continuous dual search allowed all endpoint thresholds `T=4,...,22`, excess thresholds `g/e>=1,2,3`, the demand-four restriction, and their demand/excess/endpoint intersections. It still finds no positive affine certificate for `k=5,...,18`. The same cone does certify `k=0,...,4` and `k=19,20`.

This is a **negative result about the projection**, not evidence that an actual bridge or graph exists at E=9. It says that simply adding more scalar threshold weights is no longer the right next move. The full selected-incidence Hall/transport structure has now become the natural next layer.

**AUDIT / PRESERVATION:** E5 theorem/checker are in `2026-09-17-e5-excess-restricted-v1/`; E6 theorem/checker in `2026-09-17-e6-endpoint-staircase-v1/`; E7/E8 theorem/checker in `2026-09-17-e7-e8-endpoint-staircase-v1/`. E4, E3, E<=2, full selected-incidence Hall, quadratic endpoint and all earlier failures/audits remain preserved. External mathematical review remains open.

**FIVE-LABEL STATUS:** every actual whole exact block `|T|=|H|=5` still satisfies `D>=12`, hence `W>=37` or `W>=57` with extras.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No canonical catalogue scan, q-enumeration or conjecture-level promotion.

**AUTOMATION STATUS:** the hourly Murty-Simon research automation was deliberately paused after 12:00 BST at the user's instruction. This handoff records the current manual continuation; other user alerts were not altered.

**UNPRESERVED WORK:** the E=9 dual-cone diagnostic itself should be frozen if it becomes proof-relevant. No E=9 feasibility or E>=10 claim is made.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: attack only the unresolved E=9 middle range `k=5,...,18` at the full selected-incidence level. Build/freeze an exact transport feasibility model with source rows `(rho,p,q)`, label columns `(s,R,e)`, simple-edge eligibility `s<=rho`, `e>=g`, `C>=w`, exact row/column selected degrees, and full capacitated Hall/max-flow. Preserve either the smallest incidence-level survivor or a complete finite infeasibility certificate. Do not broaden demand support before resolving whether E=9 is a true incidence obstruction or only an affine-potential obstruction.
<!-- CURRENT-STATUS:END -->
