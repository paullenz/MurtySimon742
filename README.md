# Murty–Simon / Erdős Problem #742

Candidate proofs and reproducible research. **Updated 11 September 2026. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.** Repository publication and internal replay are not external acceptance or a proof of the unrestricted conjecture.

**External reviewers:** please start with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md). The project actively welcomes hostile review, counterexamples, literature corrections and independent reproduction. GitHub Issues are the preferred place to report a suspected flaw.

## Current headline status

| Scope | Current project status |
|---|---|
| `n=25` | Complete candidate: `e(G) <= 156`, equality exactly `K(12,13)`; Fan-free reviewer v2; complete partitioned replay and independent endpoint reconstruction green; external specialist review open |
| `n=27` | Complete candidate: `e(G) <= 182`, equality exactly `K(13,14)`; Fan-free reviewer v2; hardened replay green; external review open |
| `n=28` | Complete candidate: `e(G) <= 196`, equality exactly `K(14,14)`; Fan-free reviewer v2; direct 197-edge exclusion and red-team package preserved; external review open |
| `n=29` | Complete candidate: `e(G) <= 210`, equality exactly `K(14,15)`; Fan-free reviewer v2; minimal trusted `Delta=16` kernel and exact Farkas endpoint; external review open |
| `n=30` | Complete candidate: `e(G) <= 225`, equality exactly `K(15,15)`; Fan-free reviewer v2; exact finite endpoint certificates and assembly replay green; external review open |
| General maximum-degree result | Candidate theorem: `n >= 6` and `Delta(G) >= (7/12)n` imply `e(G) < floor(n^2/4)`; complete candidate hand argument with internal exact audits green; external review and novelty assessment open |
| RX-Hall / 3-D potential programme | Active finite-to-symbolic research programme. Under the current fixed 3-D potentials the exact finite minimum scalar-template counts are `2` for `n=30,t=1`, `3` for `n=29,t=2`, and `4` for `n=29,t=3`. The suggestive `t+1` pattern is an active falsification target, **not a theorem** and not an unrestricted solution. |

The unrestricted Murty–Simon conjecture remains unsolved by this project.

## Public-review note

The repository intentionally preserves failed approaches and audit findings rather than silently rewriting them.

During the restarted hostile audit of the additional n=29 `Delta=16` cumulative-threshold verifier, a **real normalization bug** was found in its first version: a label-group multiplicity was counted twice. The v1 cumulative-threshold certificates are therefore **invalid as proof evidence** and the historical v1 source is retained only for auditability. The defect did not affect the original n=29 direct route or the separate fully fresh implementation.

A corrected `v2` model was replayed cleanly and again produced zero survivors. The audit subsequently reduced the proof-critical `Delta=16` computation to a smaller trusted kernel, whose clean replay also produced zero survivors with every late exclusion rechecked by exact integer Farkas arithmetic. See the [public-release audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md) and [minimal-kernel report](project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json).

### Robustness milestone — Fan dependency removed from the current fixed-order proofs

A later external-AI critique raised three concrete objections: two possible collision/double-counting issues in the selected/residual construction, and the fact that the fixed-order papers used G. Fan's 1987 upper-density theorem to cap the edge search. The two local semantic objections did **not** survive re-audit: selection is one representative per missing **unordered** `B`-pair, and the forced cross-edges in the residual injection cannot themselves be selected because their endpoints miss an `A`-vertex. The current editions state those points explicitly. See the [cross-cutting feedback audit](project/reviews/cross-cutting/2026-09-09-external-ai-feedback-audit-v1/REPORT.md).

For the Fan point, the project deliberately went further than defending the citation. It constructed direct order-specific upper-range reductions for **all five current fixed-order candidates `n=25,27,28,29,30`**, so Fan's theorem is now **historical attribution only**, not a logical dependency of those proofs. Every historical reviewer-v1/proof source is retained unchanged; the current reviewer-facing surfaces are **Fan-free v2** editions. The unified replacement is documented in [`FAN_FREE_REDUCTION.md`](project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md).

The assembled replacement passed a fresh [hostile coverage/integrity audit](project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md): the required upper edge ranges are complete, every proof-event checkpoint has zero survivors under exact acceptance, the v2 proof surfaces contain no residual logical invocation of Fan, and the frozen historical source hashes still match their recorded v2 provenance. This is **internal** robustness evidence, not external acceptance; the graph-to-residual lemmas and short hand monotonicity arguments remain important review targets.

## Fixed-order candidate results

### n=25

**Candidate:** `e(G) <= 156`, equality only `K(12,13)`.

[**Fan-free reviewer v2**](releases/n25-reviewer-v2/README.md) · [current Fan-free proof](project/reviews/n25/2026-09-09-fan-free-v2/PROOF.md) · [historical reviewer v1](releases/n25-reviewer-v1/README.md) · [8 September re-audit](project/reviews/n25/2026-09-08-reaudit-v1/README.md).

The complete finite domain has been replayed again in **16 disjoint clean-runner shards**: 543,578 outer states, 3,442,212 labelled columns and 1,959 independently reconstructed final equality certificates. The new terminal re-audit imports no frozen verifier and reconstructs the source-cap endpoint independently. No blocking mathematical defect was found in the completed internal re-audit.

This is the project's candidate resolution of the conspicuous order-25 gap between Fan's published `n<=24` and `n=26` results. **Independent specialist review and independent novelty confirmation remain open.**

### n=27

**Candidate:** `e(G) <= 182`, equality only `K(13,14)`.

[**Fan-free reviewer v2**](releases/n27-reviewer-v2/README.md) · [current Fan-free proof](project/reviews/n27/2026-09-09-fan-free-v2/PROOF.md) · [historical reviewer v1](releases/n27-reviewer-v1/README.md) · [evidence release](releases/n27-candidate-v1/README.md) · [8 September red-team audit](project/reviews/n27/2026-09-08-redteam-v1/REPORT.md).

The hardened replay checks 80,978,546 canonical columns and independently reconstructs all 35,435 terminal source-cap vectors. **Independent review remains open.**

### n=28

**Candidate:** `e(G) <= 196`, equality only `K(14,14)`.

[**Fan-free reviewer v2**](releases/n28-reviewer-v2/README.md) · [current Fan-free proof](project/reviews/n28/2026-09-09-fan-free-v2/PROOF.tex) · [historical reviewer v1](releases/n28-reviewer-v1/README.md) · [direct 197-edge exclusion](project/research/general_n/2026-09-07-direct-197-v8/README.md) · [red-team report](project/reviews/n28/2026-09-07-redteam-v1/REPORT.md).

**Independent review remains open.**

### n=29 — complete candidate

**Candidate:**

```text
e(G) <= 210 = floor(29^2/4),
with equality exactly K(14,15).
```

[**Fan-free reviewer v2**](releases/n29-reviewer-v2/README.md) · [current Fan-free proof](project/reviews/n29/2026-09-09-fan-free-v2/PROOF.md) · [historical reviewer v1](releases/n29-reviewer-v1/README.md) · [historical proof/replay guide](project/reviews/n29/2026-09-08-candidate-v1/README.md) · [standalone Delta=16 graph-to-model bridge](project/reviews/n29/2026-09-09-bridge-standalone-v1/GRAPH_TO_MODEL_BRIDGE.md) · [bridge hostile audit](project/reviews/n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md) · [restarted red-team audit](project/reviews/n29/2026-09-08-redteam-restart-v1/N29_RED_TEAM_RESTART.md) · [public-release audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md).

The proof does **not** depend on the later general profile-integral candidates or on Fan's density theorem. The direct Fan-free upper-range reduction excludes every `m>=212`, leaving 211 edges as the sole upper-bound counterexample scope. `Delta=15` is handled by a witness-deficit count, which also forces `K(14,15)` at 210. `Delta=17` is excluded by a short pointwise charging bound, `Delta=18..27` by the residual h-index inequality, and a universal vertex gives a star.

The difficult `Delta=16` case has several same-assistant computational routes. The preferred proof-critical route is the **minimal trusted kernel**:

```text
quasi-edge / selected-residual construction
  -> residual activity
  -> charging and threshold-capacity inequalities
  -> exact source-capacity dual pruning
  -> simple residual-row Hall/refinement scan
  -> corrected cumulative-threshold/source-q-flow LP
  -> exact integer Farkas verification
```

Its clean replay retains 72 demand profiles and 126 residual rows at 211 edges, and 367 demand profiles and 1,467 residual rows at 210 edges. All 1,593 late residual rows receive exact Farkas contradictions and final survivors are zero. This route does **not** use the old projected screen, joint propagator, shared LP, typed LP, old endpoint LP or older pair-capacity support formula.

**Status: complete candidate; independent mathematical review OPEN.**

### n=30 — complete candidate

**Candidate:**

```text
e(G) <= 225 = floor(30^2/4),
with equality exactly K(15,15).
```

[**Fan-free reviewer v2**](releases/n30-reviewer-v2/README.md) · [current Fan-free proof](project/reviews/n30/2026-09-09-fan-free-v2/PROOF.md) · [historical reviewer v1](releases/n30-reviewer-v1/README.md) · [historical candidate package](project/reviews/n30/2026-09-09-candidate-v1/README.md) · [hostile assembly audit](project/reviews/n30/2026-09-09-candidate-v1/ASSEMBLY_AUDIT.md).

Fan's density theorem is no longer used logically. The direct Fan-free upper-range reduction excludes every `m>=227`, leaving 226 edges as the sole upper-bound counterexample scope. The 225-edge `Delta=15` equality case is handled by a short witness-degree argument and forces `K(15,15)`. The `Delta=17` scopes close before residual-row enumeration: 250/250 charging-feasible profiles are threshold-rejected at 226 edges, while at 225 edges 1,137 profiles are rejected by threshold/source-count cuts and the remaining 18 by exact Hall duals.

The `Delta=16` scopes use a genuine parameterisation of the stripped graph-to-demand kernel at `(a,b)=(13,16)`. Clean runs reduce the complete residual frontiers to 9 rows at 226 edges and 272 rows at 225 edges, then reject every final row by exact integer Farkas certificates. `Delta=18,...,28` have empty exact charging domains and `Delta=29` gives a star. The final assembly replay is green.

**Status: complete candidate; independent mathematical review OPEN.**

## General structural programme

### Strengthened profile-integral — 7/12 candidate

The current strongest reviewer-packaged maximum-degree candidate is

```text
n >= 6 and Delta(G) >= (7/12)n  ==>  e(G) < floor(n^2/4).
```

[Reviewer release](releases/general-7-12-reviewer-v1/README.md) · [standalone proof](project/research/general_n/2026-09-09-profile-integral-7-12-v1/PROOF.md) · [hostile audit](project/research/general_n/2026-09-09-profile-integral-7-12-v1/AUDIT.md) · [exact evidence](project/research/general_n/2026-09-09-profile-integral-7-12-v1/evidence/run-34355073705/RECEIPT.json).

The scalar estimate gives the universal surplus bound

```text
t < 5a^2/128 + a/8.
```

Two separately written standard-library checkers agree exactly on the scalar arithmetic, the eleven finite degree-assembly exceptions and their threshold certificates. The primary checker regressed 5,207,079 eligible degree pairs through `n=5000`; the separately structured audit regressed 1,874,246 pairs through `n=3000`. Those regressions are consistency checks, **not proof by extrapolation**. The main trust boundary remains the shared graph-to-demand/profile-integral lemmas.

A [strategic ceiling note](project/research/general_n/2026-09-09-profile-integral-7-12-v1/PROFILE_INTEGRAL_CEILING.md) shows that the current scalar-uniform profile-integral architecture has an asymptotic degree threshold near `0.582066`, so the clean `7/12 = 0.583333...` result is already close to that route's intrinsic limit. Substantial further progress is therefore expected to require retaining more joint profile information.

**Status: complete candidate hand argument; internal exact audits green; independent mathematical review, novelty assessment and external reproduction OPEN.**

### Profile-integral 293/500 — retained predecessor

The [293/500 reviewer release](releases/general-293-500-reviewer-v1/README.md) and [profile-integral proof](project/research/general_n/2026-09-08-profile-integral-v1/PROOF.md) give the earlier candidate implication

```text
n >= 6 and Delta(G) >= (293/500)n  ==>  e(G) < floor(n^2/4).
```

It proves `t < a^2/24+a/8` by retaining the demand profile across thresholds. [Replay and audit](project/research/general_n/2026-09-08-profile-integral-v1/README.md). It remains preserved and reviewable, but is **superseded in threshold strength by the 7/12 candidate**. Neither profile-integral result is a dependency of the n=29 or n=30 fixed-order proofs.

### RX-Hall / 3-D potential continuation — research programme, not theorem

The active route below the profile-integral frontier is preserved under [`project/research/general_n/2026-09-09-rx-hall-v1/`](project/research/general_n/2026-09-09-rx-hall-v1/README.md). It is a **necessary-condition research programme**, not a new all-order theorem and not a dependency of any current fixed-order candidate package.

The incidence layer has been reduced from the original large endpoint LP to monotone Hall/transport geometry. In the current 3-D formulation, a selected incidence obeys a coordinatewise relation of the schematic form

```text
(s, d, v) <= (rho, alpha, w),
```

which permits exact inequalities from coordinatewise nondecreasing potentials. The universal trust boundary remains the derivation of these profile/RX-Hall constraints from an actual diameter-2-critical graph and the 3-D potential-certificate lemma.

#### Exact t=3 analytic compression

For the complete regenerated n=29 `t=3` frontier (94 hard profiles), a single exact rational potential using only nine analytic min-hinges

```text
H_{D,V}(d,v) = min((d-D)_+, (v-V)_+)
```

works across all 94 profiles. The nine breakpoints are

```text
(0,0), (0,2),
(1,7), (1,8), (1,9), (1,10), (1,11),
(2,0), (4,0).
```

See the [analytic min-hinge reduction](project/research/general_n/2026-09-09-rx-hall-v1/MIN_HINGE_ANALYTIC_REDUCTION.md) and [exact checkpoint](project/research/general_n/2026-09-09-rx-hall-v1/checkpoints/N29_T3_MIN_HINGE_EXACT_RUN_34384549422.json). This is exact **finite** evidence conditional on the RX-Hall bridge/frontier preparation, not an unrestricted theorem.

Separately, a simpler fixed 3-D potential

```text
F = 6 B(3,0) + 4 B(3,5) + 3 B(3,9)
```

admits an exact four-template cover of the same 94-profile `t=3` frontier. Profiles 0, 1, 38 and 30 form a four-vertex pairwise incompatibility clique for a single scalar template, with every pair excluded by an exact rational Farkas certificate. Hence **within this fixed-potential model the minimum scalar-template count is exactly four**. See [`n29_t3_four_template_lower_bound_exact.py`](project/research/general_n/2026-09-09-rx-hall-v1/n29_t3_four_template_lower_bound_exact.py) and [`n29_t3_count_tree_four_templates_exact.py`](project/research/general_n/2026-09-09-rx-hall-v1/n29_t3_count_tree_four_templates_exact.py).

#### 10 September: n=30, t=1 falsification laboratory

A naive parameter-derived BC/diagonal architecture failed one of the seven preserved `n=30,t=1` hard profiles, even after a deliberately generous BC enlargement. Restoring the first Hall coordinate with the single threshold `1[s>=2]` repaired the obstruction.

The resulting [exact n=30 t=1 3-D potential](project/research/general_n/2026-09-09-rx-hall-v1/N30_T1_TWO_TEMPLATE_POTENTIAL.md) has **13 primitive nonnegative generators** and just **two rational scalar templates** covering all seven hard profiles, with minimum exact strict gap `1/2`. Its acceptance checker uses only Python's standard library and `fractions.Fraction`: no LP/MIP solver, floating point or saved dual vector participates in final acceptance.

An exact rational Farkas certificate additionally proves that hard profiles 0 and 2 cannot share one nonnegative scalar template even when the required common gap is weakened to `>=0`. Combined with the exact two-template cover, **within this fixed-potential model the minimum scalar-template count is exactly two**. See [`n30_t1_two_template_lower_bound_exact.py`](project/research/general_n/2026-09-09-rx-hall-v1/n30_t1_two_template_lower_bound_exact.py).

This was a useful falsification result: it shows that the first monotone-coupling coordinate contains genuine information, but the repair needed in this laboratory is extremely small.

#### 10 September: n=29, t=2 exact three-template compression

The full regenerated `n=29, Delta=16, t=2` frontier contains 902 profiles. The current exact 3-D compression uses one fixed **11-term primitive potential** consisting of a compact `D3` staircase, two diagonal thresholds and the first-coordinate threshold `SH3 = 1[s>=3]`.

[**Exact three-template certificate**](project/research/general_n/2026-09-09-rx-hall-v1/N29_T2_3D_THREE_TEMPLATE_EXACT.md): three fixed rational scalar templates cover **902/902** profiles with exact `Fraction` arithmetic. Moreover profiles 0, 3 and 77 form an exact pairwise incompatibility triangle for one scalar template under this fixed potential. Three sparse rational Farkas certificates prove that no two templates can cover all three even at zero gap. Therefore, **within this fixed-potential model, the minimum scalar-template count is exactly three**.

This is a finite certificate-compression theorem inside the RX-Hall model. It is **not** an unrestricted Murty–Simon theorem and does not replace the fixed-order n=29 reviewer proof chain.

#### 11 September working hypothesis — `t+1` scalar regimes

The three current exact finite laboratories now give

```text
n=30, t=1: minimum 2 scalar templates;
n=29, t=2: minimum 3 scalar templates;
n=29, t=3: minimum 4 scalar templates.
```

This makes

```text
minimum regime count = t+1
```

a natural **falsification target**. It is not presently a theorem: the three results use different finite frontiers and different fixed 3-D potentials, and no extrapolation to general `(n,t)` is claimed.

The immediate research priority is to characterize the exact scalar regimes by elementary statistics of the demand/source profiles `(s,rho)`, test whether the resulting regime boundaries can be generated from parameters rather than profile IDs, and then attack the proposed `t+1` rule on fresh finite domains. Only after surviving those tests would it be appropriate to seek a symbolic regime lemma and combine it with charging/demand bounds to push below the `7/12` maximum-degree frontier.

### Layer-sum 13/22 and earlier structural checkpoints

The [13/22 reviewer release](releases/general-13-22-reviewer-v1/README.md), [13/22 layer-sum proof](project/research/general_n/2026-09-08-layer-sum-v1/PROOF.md), and the preserved [v9](project/research/general_n/2026-09-07-stability-spare-sources-v9/README.md), [v10](project/research/general_n/2026-09-08-demand-tail-stability-v10/README.md), and [v11](project/research/general_n/2026-09-08-jensen-tail-v11/README.md) checkpoints document the preceding general-order programme. The local Lean slice checks ten scoped quasi-edge/edge-insertion lemmas; the complete universal theorems are not formally verified.

## Review-paper index

The fixed-order rows below point to the **current Fan-free v2 reviewer editions**. Historical v1 packages remain preserved in their release directories.

| Scope | Proof / paper | Evidence / review |
|---|---|---|
| n=25 | [Reviewer manuscript v2](releases/n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf) | [Verification companion v2](releases/n25-reviewer-v2/N25_Verification_Companion_v2.pdf) |
| n=27 | [Reviewer manuscript v2](releases/n27-reviewer-v2/N27_Reviewer_Manuscript_v2.pdf) | [Verification companion v2](releases/n27-reviewer-v2/N27_Verification_Companion_v2.pdf) |
| n=28 | [Reviewer manuscript v2](releases/n28-reviewer-v2/N28_Reviewer_Manuscript_v2.pdf) | [Verification companion v2](releases/n28-reviewer-v2/N28_Verification_Companion_v2.pdf) |
| n=29 | [Reviewer manuscript v2](releases/n29-reviewer-v2/N29_Reviewer_Manuscript_v2.pdf) | [Verification companion v2](releases/n29-reviewer-v2/N29_Verification_Companion_v2.pdf) |
| n=30 | [Reviewer manuscript v2](releases/n30-reviewer-v2/N30_Reviewer_Manuscript_v2.pdf) | [Verification companion v2](releases/n30-reviewer-v2/N30_Verification_Companion_v2.pdf) |
| **General 7/12** | [Reviewer manuscript](releases/general-7-12-reviewer-v1/General_7_12_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/general-7-12-reviewer-v1/General_7_12_Verification_Companion_v1.pdf) |
| General 293/500 | [Reviewer manuscript](releases/general-293-500-reviewer-v1/General_293_500_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/general-293-500-reviewer-v1/General_293_500_Verification_Companion_v1.pdf) |
| General 13/22 | [Reviewer manuscript](releases/general-13-22-reviewer-v1/General_13_22_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/general-13-22-reviewer-v1/General_13_22_Verification_Companion_v1.pdf) |

## Governance and limits

**No complete order above 30, proof through n=1,000, unrestricted all-order solution, novelty determination, full formal verification or external endorsement is claimed.** Numerical states are necessary-condition systems, not graphs. Saved actual-graph regressions contain no positive-surplus graph, so universal correctness depends on the written structural proofs, not extrapolation from samples.

Paul Lenz directed the project; ChatGPT/Geeps supplied mathematical development, software, manuscripts and internal checks. Same-assistant independent implementations are explicitly **not** described as external independent review. Frozen fixed-order proofs, original archives and the governed theorem ledger remain preserved.

The README immediately preceding the n=29 publication is preserved verbatim at `project/reviews/history/README_before_n29_candidate_2026-09-08.md`. See [standing orders](project/N25_PROJECT_STANDING_ORDERS.md), [repository sync policy](project/REPO_SYNC_POLICY.md), and the [theorem ledger](repro-v1/ledger/theorem_ledger.json).

## Review and corrections

Please use the [reviewer starting point](START_HERE_FOR_REVIEWERS.md) and open a GitHub Issue for suspected errors. The repository includes a mathematical-review issue template. Corrections should preserve the original failure evidence and state clearly which downstream claims are affected.

## Licence

MIT — see [`LICENSE`](LICENSE).
