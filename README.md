# Murty–Simon / Erdős Problem #742

Candidate proofs and reproducible research. **Updated 9 September 2026. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.** Repository publication and internal replay are not external acceptance or a proof of the unrestricted conjecture.

**External reviewers:** please start with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md). The project actively welcomes hostile review, counterexamples, literature corrections and independent reproduction. GitHub Issues are the preferred place to report a suspected flaw.

## Public-review note

The repository intentionally preserves failed approaches and audit findings rather than silently rewriting them.

During the restarted hostile audit of the additional n=29 `Delta=16` cumulative-threshold verifier, a **real normalization bug** was found in its first version: a label-group multiplicity was counted twice. The v1 cumulative-threshold certificates are therefore **invalid as proof evidence** and the historical v1 source is retained only for auditability. The defect did not affect the original n=29 direct route or the separate fully fresh implementation.

A corrected `v2` model was then replayed cleanly and again produced zero survivors. The audit subsequently reduced the proof-critical `Delta=16` computation to a smaller trusted kernel, whose clean replay also produced zero survivors with every late exclusion rechecked by exact integer Farkas arithmetic. See the [public-release audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md) and [minimal-kernel report](project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json).

## Fixed-order candidate results

### n=25

**Candidate:** `e(G) <= 156`, equality only `K(12,13)`. [Reviewer release](releases/n25-reviewer-v1/README.md) · [frozen proof](project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md) · [8 September re-audit](project/reviews/n25/2026-09-08-reaudit-v1/README.md). The complete finite domain has now been replayed again in 16 disjoint clean-runner shards: 543,578 outer states, 3,442,212 labelled columns and 1,959 independently reconstructed final equality certificates. Independent specialist review remains open.

### n=27

**Candidate:** `e(G) <= 182`, equality only `K(13,14)`. [Reviewer release](releases/n27-reviewer-v1/README.md) · [proof](project/reviews/n27/2026-09-07-candidate-v1/PROOF.md) · [evidence release](releases/n27-candidate-v1/README.md) · [8 September red-team audit](project/reviews/n27/2026-09-08-redteam-v1/REPORT.md). The hardened replay checks 80,978,546 canonical columns and independently reconstructs all 35,435 terminal source-cap vectors. Independent review remains open.

### n=28

**Candidate:** `e(G) <= 196`, equality only `K(14,14)`. [Reviewer release](releases/n28-reviewer-v1/README.md) · [direct 197-edge exclusion](project/research/general_n/2026-09-07-direct-197-v8/README.md) · [red-team report](project/reviews/n28/2026-09-07-redteam-v1/REPORT.md). Independent review remains open.

### n=29 — complete candidate

**Candidate:**

```text
e(G) <= 210 = floor(29^2/4),
with equality exactly K(14,15).
```

[Reviewer release](releases/n29-reviewer-v1/README.md) · [full proof and replay guide](project/reviews/n29/2026-09-08-candidate-v1/README.md) · [candidate manuscript](project/reviews/n29/2026-09-08-candidate-v1/PROOF.md) · [standalone Delta=16 graph-to-model bridge](project/reviews/n29/2026-09-09-bridge-standalone-v1/GRAPH_TO_MODEL_BRIDGE.md) · [bridge hostile audit](project/reviews/n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md) · [restarted red-team audit](project/reviews/n29/2026-09-08-redteam-restart-v1/N29_RED_TEAM_RESTART.md) · [public-release audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md).

The proof does **not** depend on the later general profile-integral candidates. Fan's cited strict bound leaves only 211 edges to exclude. `Delta=15` is handled by a witness-deficit count, which also forces `K(14,15)` at 210. `Delta=17` is excluded by a short pointwise charging bound, `Delta=18..27` by the residual h-index inequality, and a universal vertex gives a star.

The difficult `Delta=16` case has several same-assistant computational routes. The preferred proof-critical route is now the **minimal trusted kernel**:

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

[Reviewer release](releases/n30-reviewer-v1/README.md) · [candidate package](project/reviews/n30/2026-09-09-candidate-v1/README.md) · [assembled proof](project/reviews/n30/2026-09-09-candidate-v1/PROOF.md) · [hostile assembly audit](project/reviews/n30/2026-09-09-candidate-v1/ASSEMBLY_AUDIT.md).

Fan's cited strict bound leaves only 226 edges as a possible upper-bound counterexample. The 225-edge `Delta=15` equality case is handled by a short witness-degree argument and forces `K(15,15)`. The `Delta=17` scopes close before residual-row enumeration: 250/250 charging-feasible profiles are threshold-rejected at 226 edges, while at 225 edges 1,137 profiles are rejected by threshold/source-count cuts and the remaining 18 by exact Hall duals. Clean replay `34292054922` verifies the committed duals exactly.

The `Delta=16` scopes use a genuine parameterisation of the stripped graph-to-demand kernel at `(a,b)=(13,16)`. Clean runs `34286806474`, `34287440190` and `34287739057` reduce the complete residual frontiers to 9 rows at 226 edges and 272 rows at 225 edges, then reject every final row by exact integer Farkas certificates. `Delta=18,...,28` have empty exact charging domains and `Delta=29` gives a star. The final assembly replay `34292557008` is green.

**Status: complete candidate; independent mathematical review OPEN.**

## General structural programme

### Strengthened profile-integral — 7/12 candidate

The current strongest reviewer-packaged maximum-degree candidate is

```text
n >= 6 and Delta(G) >= (7/12)n  ==>  e(G) < floor(n^2/4).
```

[Reviewer release](releases/general-7-12-reviewer-v1/README.md) · [standalone proof](project/research/general_n/2026-09-09-profile-integral-7-12-v1/PROOF.md) · [hostile audit](project/research/general_n/2026-09-09-profile-integral-7-12-v1/AUDIT.md) · [exact evidence](project/research/general_n/2026-09-09-profile-integral-7-12-v1/evidence/run-34355073705/RECEIPT.json).

The new scalar estimate strengthens the universal surplus bound to

```text
t < 5a^2/128 + a/8.
```

The improvement uses the actual substitution domain `u<=1/2` to obtain a sharper exact square-root minorant; the resulting scalar loss is `<5/64`. Two separately written standard-library checkers agree exactly on the scalar arithmetic, the eleven finite degree-assembly exceptions and their threshold certificates. The primary checker regressed 5,207,079 eligible degree pairs through `n=5000`; the separately structured audit regressed 1,874,246 pairs through `n=3000`. Those regressions are consistency checks, not proof by extrapolation. The main trust boundary remains the shared graph-to-demand/profile-integral lemmas inherited from the earlier profile-integral work.

A [strategic ceiling note](project/research/general_n/2026-09-09-profile-integral-7-12-v1/PROFILE_INTEGRAL_CEILING.md) shows that the current scalar-uniform profile-integral architecture has an asymptotic degree threshold near `0.582066`, so the clean `7/12 = 0.583333...` result is already fairly close to that route's intrinsic limit. Substantial further progress is therefore expected to require retaining more joint profile information.

**Status: complete candidate hand argument; internal exact audits green; independent mathematical review, novelty assessment and external reproduction OPEN.**

### Profile-integral 293/500 — retained predecessor

The [293/500 reviewer release](releases/general-293-500-reviewer-v1/README.md) and [profile-integral proof](project/research/general_n/2026-09-08-profile-integral-v1/PROOF.md) give the earlier candidate implication

```text
n >= 6 and Delta(G) >= (293/500)n  ==>  e(G) < floor(n^2/4).
```

It proves `t < a^2/24+a/8` by retaining the demand profile across thresholds. [Replay and audit](project/research/general_n/2026-09-08-profile-integral-v1/README.md). It remains preserved and reviewable, but is **superseded in threshold strength by the 7/12 candidate**. Neither profile-integral result is a dependency of the n=29 or n=30 fixed-order proofs.

### RX-Hall / pairwise-staircase continuation — research programme, not theorem

The active route below the profile-integral frontier is preserved under [`project/research/general_n/2026-09-09-rx-hall-v1/`](project/research/general_n/2026-09-09-rx-hall-v1/README.md). It is a **necessary-condition research programme**, not a new all-order theorem and not a dependency of the completed n=29 or n=30 candidate packages.

The incidence layer has now been reduced substantially. The [exact Hall projection](project/research/general_n/2026-09-09-rx-hall-v1/HALL_PROJECTION.md) removes the `Z` variables, the [neighbourhood-closure / staircase reduction](project/research/general_n/2026-09-09-rx-hall-v1/HALL_STAIRCASE_REDUCTION.md) identifies the finite staircase geometry, and the [finite monotone-coupling reduction](project/research/general_n/2026-09-09-rx-hall-v1/MONOTONE_COUPLING_REDUCTION.md) puts the remaining transport problem in the common coordinatewise order

```text
Y = (s, R+s, -(R+x)) <= X = (rho, rho+q-1, -(q+p)).
```

On the seven hardest preserved n=30 equality-frontier states, full 3D Hall geometry is not needed. The [pairwise staircase reduction](project/research/general_n/2026-09-09-rx-hall-v1/PAIRWISE_STAIRCASE_REDUCTION.md) reduces the obstruction to the two coupled 2D orders

```text
(d,-h) <= (alpha,-beta)
(s,-h) <= (rho,-beta),
```

where `d=R+s`, `h=R+x`, `alpha=rho+q-1`, `beta=q+p`. The first family alone closes six of seven states exactly; the second supplies the correction for the exceptional state. The [staircase-potential note](project/research/general_n/2026-09-09-rx-hall-v1/PAIRWISE_STAIRCASE_POTENTIAL.md) expresses their nonnegative weighted sums as a potential of the form

```text
Phi(s,d,h) = F(d,h) + G(s,h).
```

Several tempting simplifications have been falsified exactly: all first-moment dominance inequalities together close `0/7`; the natural diagonal-CDF subfamilies close `0/7`; and even all single-corner rectangle inequalities close only `2/7`. Thus genuine multistep staircase shape is doing mathematical work in this relaxation.

For the exceptional n=30 state, the exact certificate has been reduced from a large incidence LP to **6 BC staircases + 3 SH staircases**. An exhaustive subset test proves that the three SH corrections form the unique minimum rejecting subset within the generated SH family. The semantic exact dual then shows that only source threshold-transport rows `h=2,3` are used. Finally, all explicit density upper bounds `z<=1` have been eliminated exactly as redundant with group normalisation and nonnegativity: the [unit-bound-free checkpoint](project/research/general_n/2026-09-09-rx-hall-v1/checkpoints/N30_NO_UNIT_PAIRWISE_RUN_34357560084.json) retains the exact contradiction with RHS `-881` and nonnegative coefficients for every variable.

The finite n=30 obstruction has now been compressed further to a **single common exact 9-shape potential (6 BC + 3 SH) across all seven hard profiles**. A mixed-integer support search over the full generated dictionary of 262 BC + 4 SH shapes proved support cardinality 9 optimal for the stated shared-envelope model with zero MIP gap, and the selected support was then rebuilt and checked in exact integer arithmetic across all 2,775 envelope rows. See the [shared nine-shape note](project/research/general_n/2026-09-09-rx-hall-v1/SHARED_NINE_SHAPE_POTENTIAL.md) and [exact global checkpoint](project/research/general_n/2026-09-09-rx-hall-v1/checkpoints/N30_GLOBAL_NINE_EXACT_RUN_34362935743.json). A different six-BC basis also exactifies, so the compact mechanism is not tied to one brittle BC basis; the same three SH corrections persist.

The first cross-order falsification test is also encouraging. Keeping the **same nine staircase generator shapes** and allowing only continuous coefficients/envelopes to refit profile-by-profile on the independently regenerated n=29 `Delta=16` RX-Hall frontiers separates 94/94 `t=3` profiles and 838/902 `t=2` profiles: 932/996 overall (93.5743%). See the [n=29 transfer note](project/research/general_n/2026-09-09-rx-hall-v1/N29_NINE_SHAPE_TRANSFER.md). This is floating-point shape-transfer reconnaissance, not proof evidence; the remaining research frontier is the 64 n=29 `t=2` profiles not covered by the unchanged n=30 dictionary.

The present symbolic target is therefore to explain those 64 transfer survivors with the smallest parameter-dependent correction and then replace the finite `6+3` staircase architecture by parameterised pairwise-majorization potentials with universal label-side lower / source-side upper envelopes strong enough to push below the new `7/12` candidate frontier. No universal staircase theorem is claimed yet.

### Layer-sum 13/22 and earlier structural checkpoints

The [13/22 reviewer release](releases/general-13-22-reviewer-v1/README.md), [13/22 layer-sum proof](project/research/general_n/2026-09-08-layer-sum-v1/PROOF.md), and the preserved [v9](project/research/general_n/2026-09-07-stability-spare-sources-v9/README.md), [v10](project/research/general_n/2026-09-08-demand-tail-stability-v10/README.md), and [v11](project/research/general_n/2026-09-08-jensen-tail-v11/README.md) checkpoints document the preceding general-order programme. The local Lean slice checks ten scoped quasi-edge/edge-insertion lemmas; the complete universal theorems are not formally verified.

## Review-paper index

| Scope | Proof / paper | Evidence / review |
|---|---|---|
| n=25 | [Reviewer manuscript](releases/n25-reviewer-v1/N25_Reviewer_Manuscript_v1.pdf) | [Reviewer package](releases/n25-reviewer-v1/README.md) |
| n=27 | [Reviewer manuscript](releases/n27-reviewer-v1/N27_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/n27-reviewer-v1/N27_Verification_Companion_v1.pdf) |
| n=28 | [Mathematical manuscript](releases/n28-reviewer-v1/N28_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/n28-reviewer-v1/N28_Verification_Companion_v1.pdf) |
| n=29 | [Reviewer manuscript](releases/n29-reviewer-v1/N29_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/n29-reviewer-v1/N29_Verification_Companion_v1.pdf) |
| n=30 | [Reviewer manuscript](releases/n30-reviewer-v1/N30_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/n30-reviewer-v1/N30_Verification_Companion_v1.pdf) |
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
