# Murty–Simon / Erdős Problem #742

Candidate proofs and reproducible research. **Updated 11 September 2026. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.** Repository publication and internal replay are not external acceptance or a proof of the unrestricted conjecture.

**External reviewers:** please start with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md). The project actively welcomes hostile review, counterexamples, literature corrections and independent reproduction. GitHub Issues are the preferred place to report a suspected flaw.

## Current headline status

| Scope | Current project status |
|---|---|
| `n=25` | Complete candidate: `e(G) <= 156`, equality exactly `K(12,13)`; Fan-free reviewer v2; complete partitioned replay and independent endpoint reconstruction green; external specialist review open |
| `n=27` | Complete candidate: `e(G) <= 182`, equality exactly `K(13,14)`; Fan-free reviewer v2; hardened replay green; external review open |
| `n=28` | Complete candidate: `e(G) <= 196`, equality exactly `K(14,14)`; Fan-free reviewer v2 plus 11 September analytic upper-range hardening; external review open |
| `n=29` | Complete candidate: `e(G) <= 210`, equality exactly `K(14,15)`; **reviewer-v4 package**; Delta=16 closed by a hand threshold-tail proof with no proof-critical computation; dedicated reviewer-v4 hostile audit found no blocking flaw and exact red-team CI passed; external review open |
| `n=30` | Complete candidate: `e(G) <= 225`, equality exactly `K(15,15)`; frozen Fan-free reviewer v2 plus candidate hand hardening; **all 100 Delta=16 equality demand profiles now have a hand classification with bounded tables, feeding four certificates for all 211 tight rows**; envelope/assembly audit, separate Delta=17 finite components and independent review remain open |
| General maximum-degree result | Candidate theorem: `n >= 6` and `Delta(G) >= (7/12)n` imply `e(G) < floor(n^2/4)`; complete candidate hand argument with internal exact audits green; external review and novelty assessment open |
| RX-Hall / 3-D potential programme | Active finite-to-symbolic research programme. Under the current fixed 3-D potentials the exact finite minimum scalar-template counts are `2` for `n=30,t=1`, `3` for `n=29,t=2`, and `4` for `n=29,t=3`. A non-circular exact audit now shows `J=2#{rho>=2}-#{s=1}` gives a common-template regime partition at `t=1,2`, while `(h_res,J)` does so at `t=3`. The suggestive `t+1` pattern remains a falsification target, **not a theorem** and not an unrestricted solution. |

The unrestricted Murty–Simon conjecture remains unsolved by this project.

## Public-review note

The repository intentionally preserves failed approaches and audit findings rather than silently rewriting them.

During the restarted hostile audit of the additional n=29 `Delta=16` cumulative-threshold verifier, a **real normalization bug** was found in its first version: a label-group multiplicity was counted twice. The v1 cumulative-threshold certificates are therefore **invalid as proof evidence** and the historical v1 source is retained only for auditability. The defect did not affect the original n=29 direct route or the separate fully fresh implementation.

A corrected `v2` model was replayed cleanly and again produced zero survivors. The audit subsequently reduced the proof-critical `Delta=16` computation to a smaller trusted kernel, whose clean replay also produced zero survivors with every late exclusion rechecked by exact integer Farkas arithmetic. See the [public-release audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md) and [minimal-kernel report](project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json).

On 11 September, a separate ChatGPT instance with no project background performed a hostile n=29 review supplied by the user. It independently attacked the graph-to-model bridge, residual activity, threshold capacity, isolated-C, corrected LP normalization, exact Farkas semantics and the hand assembly and reported **no fatal flaw**. It independently recovered the complete n=29 charging-domain counts and a NetworkX graph-atlas bridge regression through order 7; both were reproduced again inside this project. The review also found a new pointwise charging bound that removes substantial upper-range computation from the logical proof chain. See the [blind external red-team follow-up](project/reviews/n29/2026-09-11-blind-external-ai-redteam-v1/FOLLOWUP.md), the [reviewer-v4 proof](project/reviews/n29/2026-09-11-reviewer-v4/PROOF.md), the [reviewer-v4 release package](releases/n29-reviewer-v4/README.md), and the [cross-order analytic caps](project/research/fan-free-fixed-orders/2026-09-11-pointwise-analytic-caps-v1/POINTWISE_CAPS.md).

A separate proof-text audit also found a **non-blocking sign/order typo** in an intermediate explanatory sentence of the expanded threshold-capacity lemma. The corrected sign is exactly the direction needed to prove the already-used final inequality, so no numerical result or candidate status changed. The historical lemma records the correction explicitly; reviewer-v3 rewrites the proof self-contained.

A later recovery audit found a second **non-blocking display typo** in Section 5 of the frozen bridge: the source-degree identity omitted the selected cross-degree `q_u`. The correct identity is `d_H(u)=(rho_u+q_u)+(b-1-q_u-p_u)=rho_u+b-1-p_u`. It gives the same stated supplement bound, and the inspected N29/N30 models use that correct bound. The frozen appendix is preserved with a visible [source-degree erratum](project/reviews/cross-cutting/2026-09-11-source-degree-erratum-v1/ERRATUM.md); no candidate status changes.

Later on 11 September, the threshold-capacity family was summed over residual-degree tails to obtain a stronger demand-only inequality. A new hand clipping argument proves `Q(s)<=18`, while the bridge gives `Q(s)>=16+2t` for `Delta=16`, hence `t<=1`. Therefore the entire `n=29, Delta=16, m>=210` branch is now excluded without proof-critical computation. Reviewer-v4 is the current review surface; reviewer-v3 and its corrected minimal-kernel/Farkas route remain frozen as independent corroboration and audit history.

A dedicated hostile audit of reviewer-v4 subsequently reconstructed the full theorem chain without treating the old LP/Farkas route as proof support. It found **no blocking flaw**. A separately specified exact checker independently swept all 1,352,078 demand multisets, all clipping stages and the threshold-capacity integer parameter range; GitHub Actions run `34621982241` passed. The audit remains same-assistant internal evidence, not external validation. See the [reviewer-v4 hostile-audit report](project/reviews/n29/2026-09-11-reviewer-v4-redteam-v1/REPORT.md) and [hardening supplement](project/reviews/n29/2026-09-11-reviewer-v4/REDTEAM_HARDENING.md).

### Robustness milestone — Fan dependency removed from the current fixed-order proofs

A later external-AI critique raised three concrete objections: two possible collision/double-counting issues in the selected/residual construction, and the fact that the fixed-order papers used G. Fan's 1987 upper-density theorem to cap the edge search. The two local semantic objections did **not** survive re-audit: selection is one representative per missing **unordered** `B`-pair, and the forced cross-edges in the residual injection cannot themselves be selected because their endpoints miss an `A`-vertex. The current editions state those points explicitly. See the [cross-cutting feedback audit](project/reviews/cross-cutting/2026-09-09-external-ai-feedback-audit-v1/REPORT.md).

For the Fan point, the project deliberately went further than defending the citation. It constructed direct order-specific upper-range reductions for **all five current fixed-order candidates `n=25,27,28,29,30`**, so Fan's theorem is now **historical attribution only**, not a logical dependency of those proofs. Every historical reviewer-v1/proof source is retained unchanged. The current reviewer-facing PDF packages are Fan-free v2 at `n=25,27,28,30` and reviewer-v4 at `n=29`. The unified Fan-free replacement is documented in [`FAN_FREE_REDUCTION.md`](project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md), with later analytic simplifications in [`POINTWISE_CAPS.md`](project/research/fan-free-fixed-orders/2026-09-11-pointwise-analytic-caps-v1/POINTWISE_CAPS.md).

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

[**Fan-free reviewer v2**](releases/n28-reviewer-v2/README.md) · [current Fan-free proof](project/reviews/n28/2026-09-09-fan-free-v2/PROOF.tex) · [11 September analytic hardening](project/reviews/n28/2026-09-09-fan-free-v2/ANALYTIC_HARDENING_2026-09-11.md) · [historical reviewer v1](releases/n28-reviewer-v1/README.md) · [direct 197-edge exclusion](project/research/general_n/2026-09-07-direct-197-v8/README.md) · [red-team report](project/reviews/n28/2026-09-07-redteam-v1/REPORT.md).

The new hand cap shows every `Delta=15` scope with `m>=203` is analytically impossible, so the historical zero-domain computation over `m=203..210` is now corroborative rather than proof-critical.

**Independent review remains open.**

### n=29 — complete candidate

**Candidate:**

```text
e(G) <= 210 = floor(29^2/4),
with equality exactly K(14,15).
```

[**Current reviewer-v4 package**](releases/n29-reviewer-v4/README.md) · [reviewer-v4 manuscript PDF](releases/n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf) · [reviewer-v4 verification companion PDF](releases/n29-reviewer-v4/N29_Verification_Companion_v4.pdf) · [canonical reviewer-v4 proof](project/reviews/n29/2026-09-11-reviewer-v4/PROOF.md) · [hostile-audit report](project/reviews/n29/2026-09-11-reviewer-v4-redteam-v1/REPORT.md) · [red-team hardening](project/reviews/n29/2026-09-11-reviewer-v4/REDTEAM_HARDENING.md) · [threshold-tail hand proof](project/research/general_n/2026-09-11-threshold-tail-collapse-v1/N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md) · [frozen self-contained bridge](project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md) · [historical reviewer-v3 package](releases/n29-reviewer-v3/README.md).

The proof does **not** depend on Fan's density theorem or on the active general-N/RX-Hall research. `Delta=15` is handled by a witness-deficit count, which also forces `K(14,15)` at 210. `Delta=17` is excluded by a short pointwise charging bound, `Delta=18..27` by the residual h-index inequality, and a universal vertex gives a star.

The former difficult `Delta=16` branch is now hand-reduced completely. With `t=m-208`, the bridge gives residual activity, `S>=r+2t`, selected-incidence forcing and threshold capacity. Summing residual-degree tails gives a demand-only lower bound `Q(s)>=16+2t`. A hand monotone-clipping argument proves `Q(s)<=18`, so `t<=1`. Therefore **every `Delta=16` graph with `m>=210` is impossible**.

Accordingly, the historical demand enumeration, residual-row scan, Hall pruning, corrected cumulative-threshold/source-q-flow LP and exact Farkas certificates are no longer logical dependencies of the N29 theorem proof. The corrected minimal kernel remains preserved as independent corroboration: at 211 edges it rejected all 126 residual rows, and at 210 edges all 1,467 rows, by exact integer Farkas verification. The earlier v1 grouped-model normalization bug and its correction remain public audit history.

The hand tail lemma has two retained exact regressions: a small local-obligation checker and a full 1,352,078-demand-multiset audit; neither is a proof premise. A further dedicated reviewer-v4 hostile audit reconstructed the theorem chain, globally tested every clipping map, checked 1,472 threshold-capacity parameter triples, independently reproduced the `Delta=15` maxima and the higher-degree scalar contradictions, and found **no blocking flaw**. Its exact CI run `34621982241` passed. This remains internal hostile evidence; independent mathematical review is still open.

**Status: complete candidate; independent mathematical review OPEN.**

### n=30 — complete candidate

**Candidate:**

```text
e(G) <= 225 = floor(30^2/4),
with equality exactly K(15,15).
```

[**Fan-free reviewer v2**](releases/n30-reviewer-v2/README.md) · [current Fan-free proof](project/reviews/n30/2026-09-09-fan-free-v2/PROOF.md) · [11 September analytic hardening](project/reviews/n30/2026-09-09-fan-free-v2/ANALYTIC_HARDENING_2026-09-11.md) · [historical reviewer v1](releases/n30-reviewer-v1/README.md) · [historical candidate package](project/reviews/n30/2026-09-09-candidate-v1/README.md) · [hostile assembly audit](project/reviews/n30/2026-09-09-candidate-v1/ASSEMBLY_AUDIT.md).

Fan's density theorem is no longer used logically. The direct Fan-free upper-range reduction excludes every `m>=227`, leaving 226 edges as the sole upper-bound counterexample scope. The 225-edge `Delta=15` equality case is handled by a short witness-degree argument and forces `K(15,15)`. The `Delta=17` scopes close before residual-row enumeration: 250/250 charging-feasible profiles are threshold-rejected at 226 edges, while at 225 edges 1,137 profiles are rejected by threshold/source-count cuts and the remaining 18 by exact Hall duals.

The `Delta=16` scopes use a genuine parameterisation of the stripped graph-to-demand kernel at `(a,b)=(13,16)`. Clean runs reduce the complete residual frontiers to 9 rows at 226 edges and 272 rows at 225 edges, then reject every final row by exact integer Farkas certificates. `Delta=18,...,28` have empty exact charging domains and `Delta=29` gives a star. The final assembly replay is green.

The earlier 11 September hand caps show that every upper-range `Delta=17` scope with `m>=228` and every upper-range `Delta=16` scope with `m>=234` is analytically impossible. The later [threshold-tail hand reduction](project/research/n30/2026-09-11-threshold-tail-v1/README.md) is stronger at `Delta=16`: it proves `Q<=21`, excludes every `m>=227`, derives the seven `m=226` demand profiles and nine residual rows by hand, and excludes the endpoint rows using explicit selected-excess/Hall inequalities. This supplies a candidate hand route for the **entire `Delta=16,m>=226` upper-bound branch**, conditional on the universal bridge. The frozen reviewer-v2 package remains available with its original finite route.

At `m=225`, the same programme reconstructs the historical 272 residual rows from the 100 `Q>=18` profiles using at most three units of slack. Ledger equality excludes 61 rows. The [four-envelope continuation](project/research/n30/2026-09-11-m225-resource-envelope-v1/README.md) now excludes **all 211 tight rows**, including the four zero-demand rows, with four shared integer certificates and minimum assigned exact gap one. The new route retains the residual budget and joint source/label constraints, including the individual cap `x_i<=#{u:rho_u>=s_i}`; it needs only `d_F<=12`, rather than the stronger historical isolated-C cutoff. Its separate standard-library checker imports no solver or discovery program and verifies every formula on every tight row.

The subsequent [hand classification of the demand frontier](project/research/n30/2026-09-11-m225-hand-classification-v1/HAND_CLASSIFICATION.md) derives **70 profiles with demands at most four plus 30 containing fives**, and excludes all hidden preimages containing six or more. It supplies a candidate written completeness proof with explicit bounded arithmetic tables; the historical exhaustive profile list is no longer its premise. A separate replay feeds the newly derived list directly into the four-envelope checker and reproduces all 211 exclusions.

The earlier [57-row scalar reduction](project/research/n30/2026-09-11-m225-hall-continuation-v1/README.md) and its 150-row remainder are preserved as history. In the combined supplementary route, the historical demand sweep and final endpoint LP/Farkas models are replaced by the clipping classification and four explicit envelopes. **Review of the written arithmetic tables, all 211 envelope evaluations, the complete Delta=16 assembly and the separate Delta=17 finite pieces remains necessary.** No fully hand-derived N30 reviewer replacement or external acceptance is claimed. The next target is that assembly audit, followed by the Delta=17 dependencies.

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

#### 11 September: non-circular regime audit and tight boundary profiles

The adjacent `t=1,2,3` laboratories have now been re-audited without using pre-chosen assignment labels. Every preserved scalar template is evaluated on every profile first with exact `fractions.Fraction` arithmetic; only then are low-dimensional regime cells tested for a common valid template.

The exact finite result is:

```text
t=1: J alone suffices;
t=2: J alone suffices;
t=3: J alone fails, but (h_res,J) suffices,
```

where

```text
J = 2 #{u:rho_u>=2} - #{i:s_i=1}.
```

Thus every occupied `(h_res,J)` cell across the three current laboratories has a nonempty common-template intersection. This is a genuine sufficient finite regime partition, not merely a replay of labels generated from the same statistics.

The stronger statement is false: `(h_res,J)` does **not** determine the complete set of templates that work on a profile. Exact `t=3` collisions show that even the entire residual sequence can be held fixed while the validity mask changes, and conversely the entire demand sequence can be held fixed while the validity mask changes. Fine certificate geometry is therefore genuinely joint in `(s,rho)`. The corrected analysis and replay live under [`project/research/general_n/2026-09-11-regime-structure-v1/`](project/research/general_n/2026-09-11-regime-structure-v1/README.md).

An exact regime-margin census gives minimum assigned gaps

```text
t=1: 1/2
t=2: 367/30
t=3: 1
```

and at `t=3` the minimum gap `1` is attained by profiles `0,1,5,30,38`. Four of those five — `0,1,38,30` — are exactly the pairwise-incompatible four-profile clique proving that four templates are necessary. This makes the boundary profiles the current symbolic target: they simultaneously control the necessity and the tight end of sufficiency.

#### 11 September working hypothesis — `t+1` scalar regimes

The three current exact finite laboratories give

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

The first symbolic regime has now been completed: the [`t=3,(h_res,J)=(4,14)` A1 hand reduction](project/research/general_n/2026-09-11-regime-structure-v1/N29_T3_A1_COMPLETE_HAND_REDUCTION.md) removes the old 236,885-state histogram reduction from that regime's logical dependencies. Charging and Hall arguments dispose of the `D1=4` and `D1=2` branches; the remaining support conditions and an exact three-slack identity give `gap_A1>=1`. This is a scoped candidate hand certificate, not a general-N theorem. The next symbolic targets are the adjacent A530 cells `(4,16)` and `(4,18)`.

The broader proof-relevant target remains symbolic lower bounds for assigned template gaps on each `J` / `(h_res,J)` regime. The natural ingredients are cumulative demand/source tails, HC3 pointwise capacity `q_u <= #{i:s_i<=rho_u}`, and the joint Hall information forced by the tight profiles.

In parallel the same regime pair should be hostile-tested on fresh exact frontiers. Any universal promotion still depends on an independent red-team of the graph-to-profile/RX-Hall bridge and the 3-D monotone potential-certificate lemma. Only after these steps survive should a parameterized `t+1` regime lemma be attempted or combined with charging/demand bounds to push below the `7/12` maximum-degree frontier.

### Layer-sum 13/22 and earlier structural checkpoints

The [13/22 reviewer release](releases/general-13-22-reviewer-v1/README.md), [13/22 layer-sum proof](project/research/general_n/2026-09-08-layer-sum-v1/PROOF.md), and the preserved [v9](project/research/general_n/2026-09-07-stability-spare-sources-v9/README.md), [v10](project/research/general_n/2026-09-08-demand-tail-stability-v10/README.md), and [v11](project/research/general_n/2026-09-08-jensen-tail-v11/README.md) checkpoints document the preceding general-order programme. The local Lean slice checks ten scoped quasi-edge/edge-insertion lemmas; the complete universal theorems are not formally verified.

## Review-paper index

The fixed-order PDF rows below point to the **current reviewer packages**. Historical packages remain preserved in their release directories. `n=29` is reviewer-v4; the other fixed orders remain Fan-free reviewer-v2, with 11 September analytic hardening annotations at `n=28` and `n=30`.

| Scope | Proof / paper | Evidence / review |
|---|---|---|
| n=25 | [Reviewer manuscript v2](releases/n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf) | [Verification companion v2](releases/n25-reviewer-v2/N25_Verification_Companion_v2.pdf) |
| n=27 | [Reviewer manuscript v2](releases/n27-reviewer-v2/N27_Reviewer_Manuscript_v2.pdf) | [Verification companion v2](releases/n27-reviewer-v2/N27_Verification_Companion_v2.pdf) |
| n=28 | [Reviewer manuscript v2](releases/n28-reviewer-v2/N28_Reviewer_Manuscript_v2.pdf) | [Verification companion v2](releases/n28-reviewer-v2/N28_Verification_Companion_v2.pdf) |
| n=29 | [Reviewer manuscript v4](releases/n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf) | [Verification companion v4](releases/n29-reviewer-v4/N29_Verification_Companion_v4.pdf) |
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
