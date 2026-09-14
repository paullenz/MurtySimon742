# Murty–Simon / Erdős Problem #742

Candidate proofs and reproducible research. **Updated 14 September 2026 through the audited post-pair relational recovery promotion: 977 quantified whole-state closures, frontier 1,955/3,623. Independent mathematical review, novelty assessment and genuinely independent third-party computational reproduction remain OPEN.** Repository publication, green replay and same-assistant hostile audit are not external acceptance and do not prove the unrestricted conjecture.

**External reviewers:** start with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md). Canonical theorem-level packages are indexed in [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). The project welcomes hostile review, counterexamples, literature corrections and genuinely independent reproduction; GitHub Issues are the preferred place to report a suspected flaw.

**Research restarts:** read [`CURRENT_STATE.md`](CURRENT_STATE.md), then inspect commits newer than its reconciliation point. The repository, not any chat transcript, is the durable source of truth.

## How this research develops general theory

The aim is to extract structural principles explaining why a diameter-two edge-critical graph cannot be too dense. Specific graph orders are used as manageable laboratories in which to develop those principles, expose false shortcuts and identify hypotheses needed by broader theorems. Progress at finitely many orders does not by itself establish an all-order result.

The [canonical bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md) translates graph structure into demands, residual budgets, selected quasi-edge representatives and source/destination loads. We organise these constraints by

```text
a=n-1-Delta,
b=Delta,
t=e(G)-b(a+1).
```

The working cycle is structural reduction, exact finite closure, simplification to hand arguments where possible, explicit generalisation, and—critically—quantification over alternative selected geometry.

## Failures, audit challenges and corrections are part of the record

**Failed approaches, counterexamples to proposed lemmas, incomplete computations, audit challenges, discovered bugs, corrections and unresolved proof obligations are preserved alongside successful results.** The [preservation standing orders](project/N25_PROJECT_STANDING_ORDERS.md) require enough provenance for reconstruction and audit.

Examples include the [N29 normalization bug and audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md), the [general-foundations corrections](project/reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md), the [N34 failed relaxation and hand replacement](project/reviews/n34/2026-09-12-heavy-independent-v1/README.md), the first failed refined-family compile, and the [alternative-attacks audit](project/research/general_n/2026-09-13-alternative-attacks-v1/AUDIT.md).

Exact replay, internal audit, repository publication and external mathematical acceptance are distinct statuses.

## Current headline status

| Scope | Current project status |
|---|---|
| `n=25` | Complete candidate: `e(G)<=156`, equality exactly `K(12,13)`; reviewer-v2; external specialist review open |
| `n=27` | Complete candidate: `e(G)<=182`, equality exactly `K(13,14)`; reviewer-v2; external review open |
| `n=28` | Complete candidate: `e(G)<=196`, equality exactly `K(14,14)`; reviewer-v2 plus analytic hardening; external review open |
| `n=29` | Complete candidate: `e(G)<=210`, equality exactly `K(14,15)`; reviewer-v4; difficult `Delta=16` branch hand-closed; external review open |
| `n=30` | Complete candidate: `e(G)<=225`, equality exactly `K(15,15)`; reviewer-v3; external review open |
| `n=31` | Complete candidate: `e(G)<=240`, equality exactly `K(15,16)`; source-first reviewer-v1; external review open |
| `n=32` | Complete candidate: `e(G)<=256`, equality exactly `K(16,16)`; source-first reviewer-v1; external review open |
| `n=33` | Complete candidate: `e(G)<=272`, equality exactly `K(16,17)`; source-first reviewer-v1; external review open |
| `n=34` | Complete candidate: `e(G)<=289`, equality exactly `K(17,17)`; reviewer-v2; final heavy certificate replaced by a short hand proof; external review open |
| `n=35` | Complete candidate: `e(G)<=306`, equality exactly `K(17,18)`; reviewer-v1; external review open |
| General maximum-degree result | Candidate theorem: for `n>=6`, `Delta(G)>=(7/12)n` implies `e(G)<floor(n^2/4)`; internal exact audits green; external review and novelty assessment open |
| Generalisation frontier | **1,971 exclusions / 3,607 survivors** from the canonical quantified whole-state ledger; `3,529` are N34 equality-derived and `78` are N35 `m=306`-derived; these are scalar states in a frozen experiment, not surviving graphs |

The unrestricted Murty–Simon conjecture remains unsolved by this project.

## Fixed-order frontier through n=35

<!-- REVIEW-MATERIALS:START -->
## Papers and review materials

This reviewer-facing index is intentionally duplicated here as a protected navigation surface. The detailed canonical status remains [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md), and new editions must update both surfaces rather than deleting this section.

### Fixed-order papers and packages

- [`n=25 reviewer-v2`](releases/n25-reviewer-v2/README.md) — [manuscript PDF](releases/n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n25-reviewer-v2/N25_Verification_Companion_v2.pdf).
- [`n=27 reviewer-v2`](releases/n27-reviewer-v2/README.md) — [manuscript PDF](releases/n27-reviewer-v2/N27_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n27-reviewer-v2/N27_Verification_Companion_v2.pdf).
- [`n=28 reviewer-v2`](releases/n28-reviewer-v2/README.md) — [manuscript PDF](releases/n28-reviewer-v2/N28_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n28-reviewer-v2/N28_Verification_Companion_v2.pdf).
- [`n=29 reviewer-v4`](releases/n29-reviewer-v4/README.md) — [manuscript PDF](releases/n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf) and [verification companion PDF](releases/n29-reviewer-v4/N29_Verification_Companion_v4.pdf).
- [`n=30 reviewer-v3`](releases/n30-reviewer-v3/README.md) — [manuscript PDF](releases/n30-reviewer-v3/N30_Reviewer_Manuscript_v3.pdf) and [verification companion PDF](releases/n30-reviewer-v3/N30_Verification_Companion_v3.pdf).
- [`n=31 reviewer-v1`](releases/n31-reviewer-v1/README.md) — source-first proof/review package; [hostile audit](project/research/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md).
- [`n=32 reviewer-v1`](releases/n32-reviewer-v1/README.md) — source-first proof/review package; [exact equality ledger](project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md).
- [`n=33 reviewer-v1`](releases/n33-reviewer-v1/README.md) — source-first proof/review package; [hostile audit](project/research/n33/2026-09-12-candidate-v1/HOSTILE_AUDIT.md).
- [`n=34 reviewer-v2`](releases/n34-reviewer-v2/README.md) — complete candidate package; [normalization audit and hand replacement](project/reviews/n34/2026-09-12-heavy-independent-v1/README.md).
- [`n=35 reviewer-v1`](releases/n35-reviewer-v1/README.md) — complete candidate package; [internal audit](project/research/n35/2026-09-12-candidate-v1/AUDIT.md).

### General-theory papers and reviewer packages

- [`7/12` maximum-degree reviewer-v1](releases/general-7-12-reviewer-v1/README.md) — [manuscript PDF](releases/general-7-12-reviewer-v1/General_7_12_Reviewer_Manuscript_v1.pdf) and [verification companion PDF](releases/general-7-12-reviewer-v1/General_7_12_Verification_Companion_v1.pdf).
- [`13/22` retained maximum-degree reviewer-v1](releases/general-13-22-reviewer-v1/README.md) — [manuscript PDF](releases/general-13-22-reviewer-v1/General_13_22_Reviewer_Manuscript_v1.pdf) and [verification companion PDF](releases/general-13-22-reviewer-v1/General_13_22_Verification_Companion_v1.pdf).
- [`293/500` retained maximum-degree reviewer-v1](releases/general-293-500-reviewer-v1/README.md) — [manuscript PDF](releases/general-293-500-reviewer-v1/General_293_500_Reviewer_Manuscript_v1.pdf) and [verification companion PDF](releases/general-293-500-reviewer-v1/General_293_500_Verification_Companion_v1.pdf).
- [General step-back structural package](releases/general-stepback-v1/README.md) — balanced-degree theorem candidate, `a=14`, fifteen-label and sixteen-label results.
- [Joint-clipping reviewer-v1](releases/general-joint-clipping-reviewer-v1/README.md) — sharp scalar tail bounds and tight-threshold obstruction.
- [Heavy-load / routing reviewer-v1](releases/general-heavy-load-reviewer-v1/README.md).
- [Joint heavy routing](releases/general-joint-routing-reviewer-v1/README.md).
- [Demand/tail projection reviewer-v1](releases/general-routing-tail-reviewer-v1/README.md).
- [Compatible-destination routing reviewer-v1](releases/general-compatible-routing-reviewer-v1/README.md).
- [Compatible-routing full-catalogue reviewer-v1](releases/general-compatible-catalogue-reviewer-v1/README.md).
- [Closed-compatible-potential reviewer-v1](releases/general-closed-compatible-reviewer-v1/README.md).
- [Fixed-neighbourhood / arc-realisation reviewer-v1](releases/general-arc-realisation-reviewer-v1/README.md).

### Reviewer entry points, audits and corrections

- [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) — reviewer orientation and high-value review targets.
- [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md) — canonical theorem-level manuscript/package index.
- [Canonical graph-to-constraint bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).
- [General-foundations audit](project/reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md).
- [N29 public-release / normalization audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md).
- [Source-degree display erratum](project/reviews/cross-cutting/2026-09-11-source-degree-erratum-v1/ERRATUM.md).
- [Alternative-attacks audit](project/research/general_n/2026-09-13-alternative-attacks-v1/AUDIT.md).

Superseded reviewer editions and failed/corrected research remain preserved in Git history and the linked package histories; they are not silently deleted.
<!-- REVIEW-MATERIALS:END -->

The fixed-order candidates have their own complete ledgers. The generalisation survivor counts below are **not** unresolved obligations in those fixed-order proofs.

## Current general structural results

Important candidate all-order or parameterized results include balanced-degree reduction; the `7/12` maximum-degree theorem candidate; heavy-load/routing families; joint routing and demand/tail projection; compatible-destination routing and Hall/flow criteria; containment spill and pair-overlap inequalities; shared residual budgets; selection-free candidate capacity; the selected-excess / threshold family; the refined baseline-3/order-statistic lemma; the zero-excess endpoint-order lemma; exact low-demand incidence-capacity; mixed-class joint Hall; and the orientation target-capacity lemma for missing-edge orientations.

For every selected positive-demand incidence,

```text
p_u-rho_u+1 <= e_i:=x_i-s_i.                         (1)
```

If `h_l=#{i:e_i>=l}`, then

```text
q_u>h_l => p_u<=rho_u+l-2.                            (2)
```

For low-demand states, [`REFINED_BASELINE3_LEMMA.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/REFINED_BASELINE3_LEMMA.md) keeps the exact selected-source score

```text
v_u=rho_u+q_u-1
```

and the negative baseline contribution from zero-excess demand-two labels.

The newer [`ZERO_EXCESS_ENDPOINT_ORDER.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/ZERO_EXCESS_ENDPOINT_ORDER.md) adds the opposite-side order statistic: a zero-excess demand-`d` label needs `d` active selected sources with `rho_u>=d` and `p_u<=rho_u-1`, and its endpoint `C_i` is at least the `d`-th smallest eligible `q_u+p_u`.

[`ORIENTATION_TARGET_CAPACITY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/ORIENTATION_TARGET_CAPACITY.md) links those source/label constraints back to the missing-edge graph. If a missing `B`-edge is oriented `u->w`, then

```text
q_u - 1 <= q_w + rho_w,
```

so every threshold `k` satisfies

```text
sum_{w:q_w+rho_w<=k} p_w <= sum_{u:q_u<=k+1} q_u.
```

This one-sided Hall-type cut closes the entire `E=0` q-frontier for states 77 and 60 with a six-incidence margin even in the closest profiles.

## Quantifier pivot: 16 whole-state exclusions

The [alternative-attacks package](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md) was created because the shared-residual continuation had become extremely strong on one stored selected geometry—4,487 of 4,584 stored patterns were rejected—but that did not quantify alternative selections, q-vectors or `x>s`.

### N34 state 227

[`STATE_227_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_227_WHOLE_STATE.md) combines exact integer enumeration through `E=20`, two hand rigidity exclusions, a relaxed `h_2` tail for `E=21,...,34`, and the incoming-capacity ceiling. Frontier: `994/4,584 -> 995/4,583`.

### N34 state 279

[`STATE_279_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_279_WHOLE_STATE.md) uses exact low-excess enumeration through `E=15`, three hand-rigidity cases, and an `h_2` tail strict throughout `E=16,...,34`. Frontier: `995/4,583 -> 996/4,582`.

### N34 state 588

[`STATE_588_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_588_WHOLE_STATE.md) has `s=3^15` and `rho=1^5,2,3^12`. Its unique low-excess equality is removed by an endpoint-budget contradiction `sum C_i>=106>97`. The cheap `h_2` tail leaves only `E=16` and `E=24`, both closed by exact replay. Frontier: `996/4,582 -> 997/4,581`.

### N34 state 526

[`STATE_526_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_526_WHOLE_STATE.md) has

```text
s=2,3^14,
rho=1^5,2^2,3^11,
r=42, S=44.
```

Its unique coarse low-excess equality is removed by a source-availability/endpoint-budget contradiction. The relaxed `h_2` tail is positive on every `E=17,...,34`. Frontier: `997/4,581 -> 998/4,580`.

### N34 state 382

[`STATE_382_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_382_WHOLE_STATE.md) has

```text
s=2^2,3^13,
rho=1^6,2,3^11,
r=41, S=43.
```

The exact low-excess sweep through `E=17` is strictly positive throughout. Retaining the negative baseline-three contribution of zero-excess demand-two labels makes the refined tail strict through `E=34`. Frontier: `998/4,580 -> 999/4,579`.

### N34 state 519

[`STATE_519_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_519_WHOLE_STATE.md) has

```text
s=2,3^14,
rho=1^6,3^12,
r=42, S=44.
```

A generic refined-family scan ranked 519 as the best active companion. Exact profile replay through `E=24` left only three coarse exceptional layers, `E=6,8,9`. A new source-availability replay retains the two low-p selected sources required by the zero-excess demand-two label and their endpoint loads jointly; the three minimum gaps become `2,4,2`. The refined tail is strict for every `E=25,...,34`, and `E>=35` is impossible by incoming capacity. GitHub Actions run `34773463128` completed green. Frontier: `999/4,579 -> 1,000/4,578`.

Replay: [`STATE_519_REPLAY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_519_REPLAY.md). Machine summary: [`STATE_519_WHOLE_STATE_VERIFICATION.json`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_519_WHOLE_STATE_VERIFICATION.json).

### N34 state 153

[`STATE_153_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_153_WHOLE_STATE.md) has

```text
s=2^5,3^10,
rho=1^7,2^2,3^9,
r=38, S=40.
```

The audited low-demand extension logic is strict on **every** admissible excess layer `E=0,...,34`; the minimum gap is `+1` and there are no nonpositive layers. The basic incoming cap is `7*3+2*4+9*5=74`, while `sum p_u=40+E`, so `E<=34`. Thus the scan covers the whole state without a separate equality-profile hand argument. GitHub Actions run `34780310971`, job `103786002313`, completed green. The exact layer table and hashes are preserved in [`LOW_DEMAND_EXTENSION_153.tsv`](project/research/general_n/2026-09-13-alternative-attacks-v1/LOW_DEMAND_EXTENSION_153.tsv) and [`STATE_153_WHOLE_STATE_VERIFICATION.json`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_153_WHOLE_STATE_VERIFICATION.json). Frontier: `1,000/4,578 -> 1,001/4,577`.

<!-- N34-WHOLE-STATE-LEDGER:START -->
### Canonical N34 whole-state ledger

The canonical [`WHOLE_STATE_LEDGER.tsv`](project/research/general_n/2026-09-13-alternative-attacks-v1/WHOLE_STATE_LEDGER.tsv) now records **961 distinct quantified whole-state exclusions**. Eighteen were established on the earlier individual/family lines; a further **943 N34-derived scalar states** are excluded by the audited potential-pair capacity family.

The large promotion is documented in [`PAIR_CAPACITY_FRONTIER_AUDIT.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/PAIR_CAPACITY_FRONTIER_AUDIT.md), with the exact promoted state certificate in [`PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv`](project/research/general_n/2026-09-13-alternative-attacks-v1/PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv). Two structurally different full-frontier implementations agree exactly on the 943-state excluded set and, for every excluded state, on exhaustive profile counts and best capacity deficits.

The durability checker [`tools/check_n34_whole_state_ledger.py`](tools/check_n34_whole_state_ledger.py) protects the 18 earlier closures plus the hash-pinned 943-state family and verifies their ledger provenance.

The current frozen frontier is therefore

```text
1,971 exclusions / 3,607 survivors,
3,529 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

Survival in this catalogue is not graph feasibility. The unrestricted Murty–Simon conjecture remains unproved by this project.
<!-- N34-WHOLE-STATE-LEDGER:END -->

## What the quantified closures suggest

The emerging reusable architecture is two-sided:

1. **High-excess scarcity:** threshold counts `h_l` restrict which large-p sources can also have large q.
2. **Low-excess availability:** exact-demand labels need sufficiently many low-p selected sources.
3. **Endpoint upper order statistics:** selected-source scores `rho_u+q_u-1` bound `C_i=d_i+e_i` from above.
4. **Endpoint lower order statistics:** eligible-source loads `q_u+p_u` bound zero-excess `C_i` from below.
5. **Negative baseline terms matter:** demand-two labels at zero excess contribute negatively in baseline three and should not be thrown away.
6. **Triage before exact enumeration:** cheap refined relaxations identify the few layers worth exact profile work.
7. **Reusable exact machinery is beginning to close states directly:** state 153 is strict across its entire admissible excess range, without bespoke rigidity.
8. **Missing-edge orientation is itself capacitated:** a large-`q` source cannot send an oriented missing edge into a target with insufficient cross-degree. This supplies a second Hall/flow system on the same margins and reconnects the selected-label machinery to the graph-level missing-edge geometry.

State 519 is theoretically useful because it converts the earlier qualitative source-availability idea into the explicit reusable endpoint-order lemma. State 153 is useful operationally because it demonstrates that the strengthened exact machinery can itself constitute the whole finite closure. States 77 and 60 are especially useful structurally because the final obstruction is a general orientation-capacity condition rather than a state-specific selected geometry.

## How the preceding generalisation machinery reached this point

| Programme | Main recorded result | Limitation / role now |
|---|---|---|
| [General heavy load](releases/general-heavy-load-reviewer-v1/README.md) | All-threshold load/routing family; 595 alternative hand exclusions | Strong aggregate structure; does not by itself quantify all selected geometry |
| [Joint heavy routing](releases/general-joint-routing-reviewer-v1/README.md) | 729 further exact catalogue exclusions; 5,578 survivors | Frozen multiplier catalogue |
| [Compatible routing catalogue](releases/general-compatible-catalogue-reviewer-v1/README.md) | 994 retained full/pilot exclusions | Produced the 4,584-state frontier entering the quantifier programme |
| [Containment spill / pair overlap](project/research/general_n/2026-09-13-constraint-respecting-cross-v1/README.md) | Scalar spill witnesses for all 4,584; fixed-pattern failures | Exposed the quantifier gap |
| [Shared residual budgets](project/research/general_n/2026-09-13-shared-residual-budget-v1/README.md) | 4,487/4,584 stored patterns rejected | Very strong on fixed geometry; not a whole-state result by itself |
| [Alternative attacks](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md) | Selection-free/excess/Hall/orientation/potential-pair lemmas and 977 quantified whole-state closures | Current primary programme; potential-pair capacity removed 943 further N34-derived scalar states; symbolic generalisation and the 3,623-state residual frontier are now primary |

## Current low-demand programmes

The older narrow [`REFINED_H2_FAMILY_SCAN.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/REFINED_H2_FAMILY_SCAN.md) and the seven-state extension matrix are now **historical triage surfaces**, not live target lists. Every state they highlighted has since been whole-state closed.

The preserved extension history is:

| State | original/earlier minimum gap | current status |
|---:|---:|---|
| 153 | `+1` | whole-state closed |
| 283 | `-2` at `E=7` | subsequently whole-state closed |
| 122 | `-3` at `E=0` | subsequently whole-state closed |
| 154 | `-3` at `E=0,6,7` | subsequently whole-state closed |
| 231 | `-7` at `E=6,...,10` | subsequently whole-state closed |
| 77 | `-7` across historical weak layers | subsequently whole-state closed by joint Hall + orientation capacity |
| 60 | `-11` across historical weak layers | subsequently whole-state closed by joint Hall + orientation capacity |

Similarly, the formerly active adjacent-family states `230,282,385,519` are all closed. Their older gaps remain preserved because failed/intermediate frontiers are part of the audit record, but none is a live research obligation now.

The older local target lists are obsolete. The current residual experiment contains **3,623 frozen scalar survivors**; the next targets should be chosen by combining potential-pair capacity, orientation Hall/flow, selected-incidence Hall and excess-budget machinery on that reduced frontier.

## Independent maximum-cut route

For any cut `X|Y`, if `I` is the number of internal edges and `M` the number of missing cross-pairs,

```text
e(G)=|X||Y|+I-M.
```

Thus `I<=M` for some cut would prove Murty–Simon. A direct one-internal-edge/one-cross-nonedge matching proof is false and is preserved as a failed route.

## Current research priorities

1. **Generalise the potential-pair obstruction symbolically.** The strongest compact new consequence is the low-`c`/high-`q` product bound `Q + ell_r u_r <= binom(b,2)` for every threshold `r`. Optimise the `(q,c)` distributions under this family, `q+rho<=a`, demand forcing and incoming caps, seeking an all-order theorem rather than further finite accumulation.
2. **Rescan the remaining 3,623 scalar survivors with the stronger relational systems.** Apply exact pair-choice Hall, target-capacity Hall, selected-incidence Hall and the excess-budget min-cost coupling only after the cheap potential-pair screen; use the new survivor structure to rank genuinely hard branches.
3. **Understand the 78 N35-derived survivors separately.** The potential-pair family closes 943 N34-derived states but none of the 78 N35-derived states, so this residual class is a valuable diagnostic of what the current theorem still misses.
4. **Strengthen independent audit/reproduction.** Prioritise external checking of the canonical bridge, directed compatibility, total-excess source cap and potential-pair theorem. The two internal implementations and green CI are strong replay evidence, not external acceptance.
5. **Continue genuinely independent routes.** Preserve and develop maximum-cut/stability, selection-free and other structurally different approaches; use failures to test whether the orientation/pair picture is genuinely central rather than merely effective on the frozen catalogue.
6. **Return to exact shared-residual/destination geometry only after quantified pruning.** The cheaper reusable theory should first identify where pair capacity and Hall/flow stop; bespoke geometry belongs on that residual set, not on already excluded states.
## Trust boundary

The largest correlated mathematical risk is still the canonical bridge: its graph-to-quasi-edge implications, selected/residual ledger, forcing lemmas and endpoint consequences require independent specialist review. The whole-state arithmetic is exact, but independent computational reproduction and external checking of structural arguments remain open. The candidate `7/12` theorem, mixed-class Hall projection and orientation target-capacity lemma also require novelty assessment and external review.

No solver timeout, floating infeasibility status or unsuccessful search is used as proof.

For restart-level detail, read [`CURRENT_STATE.md`](CURRENT_STATE.md). For the latest quantified advance, read [`POTENTIAL_PAIR_CAPACITY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/POTENTIAL_PAIR_CAPACITY.md), [`PAIR_CAPACITY_FRONTIER_AUDIT.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/PAIR_CAPACITY_FRONTIER_AUDIT.md), [`LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md), and [`ORIENTATION_FLOW_HALL.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/ORIENTATION_FLOW_HALL.md).

## 14 September 2026 relational recovery checkpoint

Sixteen further N34-derived scalar states have been promoted after a fresh state-by-state post-pair relational replay and exact agreement between two implementations with different q-profile representations and potential-pair calculations. See [`POST_PAIR_RELATIONAL_RECOVERY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/POST_PAIR_RELATIONAL_RECOVERY.md). Aggregate certificate SHA-256: `c1ce4e645edf9dcc3e2f39ef42bd85030449b161549978877eb2e15ab2abe832`. The canonical frozen frontier is now **1,971 exclusions / 3,607 survivors**. These are quantified scalar exclusions inside the generalisation experiment, not an unrestricted proof of Murty-Simon.
