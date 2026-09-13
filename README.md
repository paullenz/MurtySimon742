# Murty–Simon / Erdős Problem #742

Candidate proofs and reproducible research. **Updated 13 September 2026 through the N34 state-382 whole-state exclusion, the fifth quantified whole-state closure. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.** Repository publication, green replay and same-assistant hostile audit are not external acceptance and do not prove the unrestricted conjecture.

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

Examples include the [N29 normalization bug and audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md), the [general-foundations corrections](project/reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md), the [N34 failed relaxation and hand replacement](project/reviews/n34/2026-09-12-heavy-independent-v1/README.md), and the [alternative-attacks audit](project/research/general_n/2026-09-13-alternative-attacks-v1/AUDIT.md).

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
| Generalisation frontier | **999 exclusions / 4,579 survivors** after whole-state closures of N34 states 227, 279, 588, 526 and 382; these are scalar states in a frozen experiment, not surviving graphs |

The unrestricted Murty–Simon conjecture remains unsolved by this project.

## Fixed-order frontier through n=35

Canonical reviewer packages are indexed in [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). The fixed-order candidates have their own complete ledgers. The generalisation survivor counts below are **not** unresolved obligations in those fixed-order proofs.

## Current general structural results

Important candidate all-order or parameterized results include balanced-degree reduction; the `7/12` maximum-degree theorem candidate; heavy-load/routing families; joint routing and demand/tail projection; compatible-destination routing and Hall/flow criteria; containment spill and pair-overlap inequalities; shared residual budgets; selection-free candidate capacity; the selected-excess / threshold family; and the refined baseline-3/order-statistic lemma for positive-demand states with `s_i in {2,3}`.

For every selected positive-demand incidence,

```text
p_u-rho_u+1 <= e_i:=x_i-s_i.                         (1)
```

If `h_l=#{i:e_i>=l}`, then

```text
q_u>h_l => p_u<=rho_u+l-2.                            (2)
```

For the low-demand family, the new order-statistic refinement keeps the exact source score

```text
v_u=rho_u+q_u-1
```

at every selected incidence and retains the negative baseline contribution from zero-excess demand-two labels. See [`REFINED_BASELINE3_LEMMA.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/REFINED_BASELINE3_LEMMA.md).

## Quantifier pivot: five whole-state exclusions

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

Its unique coarse low-excess equality is removed by a source-availability/endpoint-budget contradiction. The relaxed `h_2` tail is positive on every `E=17,...,34`; its sole zero at `E=16` is already strictly excluded by the exact scan. Frontier: `997/4,581 -> 998/4,580`.

### N34 state 382

[`STATE_382_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_382_WHOLE_STATE.md) has

```text
s=2^2,3^13,
rho=1^6,2,3^11,
r=41, S=43.
```

The exact low-excess sweep through `E=17` is strictly positive throughout, so **no hand-rigidity exception is needed**. For the tail, let

```text
z_0=#{i:s_i=2,e_i=0}.
```

Retaining the negative baseline-three contribution of those labels gives the stronger necessary inequality

```text
T + 2 z_0 - P_+ <= 3(84+E).
```

The refined tail is strict for every `E=17,...,34`; its only non-strict layer is `E=16`, already strictly excluded by the exact replay. Incoming capacity excludes `E>=35`. Frontier: `998/4,580 -> 999/4,579`.

Replay: [`STATE_382_REPLAY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_382_REPLAY.md). No separate hand argument is required for this state.

The current frozen frontier is therefore

```text
999 exclusions / 4,579 survivors,
4,501 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

Survival in this catalogue is not graph feasibility.

## What the five closures suggest

The emerging reusable architecture is two-sided:

1. **High-excess scarcity:** threshold counts `h_l` restrict which large-p sources can also have large q.
2. **Low-excess availability:** zero/low-excess labels need sufficiently low-p sources; the incoming ledger may consume those cheap sources.
3. **Endpoint/order-statistic budget:** every selected source for label `i` bounds `d_i` by `rho_u+q_u-1`; the `x_i`-th eligible source score therefore bounds `C_i=d_i+e_i`.
4. **Negative baseline terms matter:** at baseline three, a demand-two label with `e_i=0` contributes at most `-2`, rather than zero. This is decisive in the state-382 tail.
5. **Triage before exact enumeration:** use the cheap refined threshold relaxation to rank states by non-strict excess layers, then exact-enumerate only exceptional layers and the low-excess boundary.

States 588, 526 and 382 demonstrate three complementary mechanisms: demand-three-only endpoint rigidity, source-availability rigidity, and a clean refined-baseline closure without any hand exception.

## How the preceding generalisation machinery reached this point

| Programme | Main recorded result | Limitation / role now |
|---|---|---|
| [General heavy load](releases/general-heavy-load-reviewer-v1/README.md) | All-threshold load/routing family; 595 alternative hand exclusions | Strong aggregate structure; does not by itself quantify all selected geometry |
| [Joint heavy routing](releases/general-joint-routing-reviewer-v1/README.md) | 729 further exact catalogue exclusions; 5,578 survivors | Frozen multiplier catalogue |
| [Compatible routing catalogue](releases/general-compatible-catalogue-reviewer-v1/README.md) | 994 retained full/pilot exclusions | Produced the 4,584-state frontier entering the quantifier programme |
| [Containment spill / pair overlap](project/research/general_n/2026-09-13-constraint-respecting-cross-v1/README.md) | Scalar spill witnesses for all 4,584; fixed-pattern failures | Exposed the quantifier gap |
| [Shared residual budgets](project/research/general_n/2026-09-13-shared-residual-budget-v1/README.md) | 4,487/4,584 stored patterns rejected | Very strong on fixed geometry; not a whole-state result by itself |
| [Alternative attacks](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md) | Selection-free/excess lemmas and whole-state closures of states 227, 279, 588, 526 and 382 | Current primary programme |

## Current refined-family scan

The files

- [`prepare_refined_h2_family_scan.py`](project/research/general_n/2026-09-13-alternative-attacks-v1/prepare_refined_h2_family_scan.py),
- [`scan_refined_h2_family.cpp`](project/research/general_n/2026-09-13-alternative-attacks-v1/scan_refined_h2_family.cpp), and
- [`.github/workflows/scan-refined-h2-adjacent-family.yml`](.github/workflows/scan-refined-h2-adjacent-family.yml)

implement an exact-integer triage of the structurally adjacent N34 low-demand family. Hash-verified preparation finds nine records in scope: the five already-closed regression states and four still-active companion states. The first workflow attempt is deliberately preserved as a tooling failure (`std::tie` applied to temporary `size()` values); the compile fix is committed. **No further frontier reduction is claimed here unless a later preserved checkpoint records it.**

## Independent maximum-cut route

For any cut `X|Y`, if `I` is the number of internal edges and `M` the number of missing cross-pairs,

```text
e(G)=|X||Y|+I-M.
```

Thus `I<=M` for some cut would prove Murty–Simon. A direct one-internal-edge/one-cross-nonedge matching proof is false and is preserved as a failed route.

## Current research priorities

1. **Complete refined threshold triage of the four active adjacent companions, then widen it.** Rank by non-strict excess layers and exact-enumerate only those exceptions.
2. **Extract a symbolic threshold/availability theorem.** Explain the shared five-state mechanism, now using the exact source-score order statistic and negative baseline term.
3. **Continue the selection-free raw candidate-capacity projection.** Proper source subsets and thresholded source/label classes remain promising.
4. **Maintain the maximum-cut route independently.** Do not retry the falsified direct matching.
5. **Return to shared residual/pair/exact-destination geometry after quantified pruning.**

## Trust boundary

The largest correlated mathematical risk is still the canonical bridge: its graph-to-quasi-edge implications, selected/residual ledger, forcing lemmas and endpoint consequences require independent specialist review. The whole-state arithmetic is exact, but independent computational reproduction and external checking of the hand-rigidity arguments remain open. The candidate `7/12` theorem and later general lemmas also require novelty assessment and external review.

No solver timeout, floating infeasibility status or unsuccessful search is used as proof.

For restart-level detail, read [`CURRENT_STATE.md`](CURRENT_STATE.md). For the latest quantified advance, read [`STATE_382_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_382_WHOLE_STATE.md) and [`REFINED_BASELINE3_LEMMA.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/REFINED_BASELINE3_LEMMA.md).
