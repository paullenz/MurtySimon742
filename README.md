# Murty–Simon / Erdős Problem #742

Candidate proofs and reproducible research. **Updated 13 September 2026 through the N34 state-588 whole-state exclusion. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.** Repository publication, green replay and same-assistant hostile audit are not external acceptance and do not prove the unrestricted conjecture.

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

The working cycle is:

1. **Reduce structurally.** Prove necessary inequalities and identify a complete remaining domain with assumptions and dependencies explicit.
2. **Use computation for discovery and finite closure.** Accept a computational exclusion only after exact verification and coverage checks; a solver timeout or floating-point infeasibility status is never proof.
3. **Extract simpler explanations.** Replace large computational objects with hand arguments where possible.
4. **Generalise with explicit hypotheses.** Formulate parameterized lemmas and test their reach against preserved hard cases and failures.
5. **Quantify alternative geometry.** A strong inequality on one representative system does not exclude the graph/state unless every admissible alternative geometry is controlled.

That fifth step is now central and has produced three whole-state frontier exclusions.

## Failures, audit challenges and corrections are part of the record

**Failed approaches, counterexamples to proposed lemmas, incomplete computations, audit challenges, discovered bugs, corrections and unresolved proof obligations are preserved alongside successful results.** The [preservation standing orders](project/N25_PROJECT_STANDING_ORDERS.md) require enough provenance for reconstruction and audit: code, parameters, inputs, outputs, survivor lists, certificates and review findings as applicable.

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
| General maximum-degree result | Candidate theorem: for `n>=6`, `Delta(G)>=(7/12)n` implies `e(G)<floor(n^2/4)`; complete candidate hand argument with internal exact audits green; external review and novelty assessment open |
| Generalisation frontier | **997 exclusions / 4,581 survivors** after whole-state closures of N34 states 227, 279 and 588; these are scalar states in a frozen experiment, not surviving graphs |

The unrestricted Murty–Simon conjecture remains unsolved by this project.

## Fixed-order frontier through n=35

Canonical reviewer packages are linked from [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). The fixed-order candidates have their own complete ledgers. The generalisation survivor counts below are **not** unresolved obligations in those fixed-order proofs.

## Current general structural results

Important candidate all-order or parameterized results include:

- balanced-degree reduction and fixed-`a`/tail families;
- the `7/12` maximum-degree theorem candidate;
- all-threshold heavy-load/routing inequalities with incoming-degree penalties and demand-only consequences;
- joint heavy routing, demand/tail projection and equality rigidity;
- compatible-destination routing, closed compatible potential and fixed-neighbourhood exact Hall/flow routing;
- co-singleton trace hierarchy and receiver-containment spill;
- pair-overlap/residual-cover inequalities;
- shared residual budgets and a balance-or-concentration alternative;
- selection-free raw candidate-capacity subsets;
- selected-excess inequality and the threshold excess-cap family.

### Selected excess and threshold capacity

For every selected positive-demand incidence, the [selection-free/excess package](project/research/general_n/2026-09-13-alternative-attacks-v1/SELECTION_FREE.md) gives the candidate inequality

```text
p_u-rho_u+1 <= x_i-s_i.                              (1)
```

Put

```text
e_i=x_i-s_i,
h_l=#{i:e_i>=l}.
```

Then

```text
q_u>h_l => p_u<=rho_u+l-2.                            (2)
```

This threshold family is a principal mechanism in the quantified whole-state programme.

## Quantifier pivot: three whole-state exclusions

The [alternative-attacks package](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md) was created because the shared-residual continuation had become extremely strong on one stored selected geometry—4,487 of 4,584 stored patterns were rejected—but that did not quantify alternative selections, `q`-vectors or `x>s`.

### N34 state 227

[`STATE_227_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_227_WHOLE_STATE.md) combines exact integer enumeration through `E=20`, two hand rigidity exclusions, a relaxed `h_2` threshold/top-k tail for `E=21,...,34`, and the incoming-capacity ceiling beyond that. It moved the frontier from `994 / 4,584` to `995 / 4,583`.

### N34 state 279

[`STATE_279_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_279_WHOLE_STATE.md) uses exact low-excess enumeration through `E=15`, three hand-rigidity cases, and an `h_2` tail that is strict throughout `E=16,...,34`. It moved the frontier to `996 / 4,582`.

### N34 state 588

[`STATE_588_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_588_WHOLE_STATE.md) has

```text
a=15, b=18, t=1,
s=3^15,
rho=1^5,2,3^12,
r=43, S=45.
```

Its exact low-excess scan has one coarse equality, `E=9, e=0^12,3^3, q=3^6,6^6`; equality forces an endpoint-budget contradiction `sum C_i>=106>97`. A cheap `h_2` tail screen closes every `E=16,...,34` layer except `E=16` and `E=24`; exact replay closes those two exception layers (`200/200` and `1,009/1,009` profiles). The incoming-capacity ceiling excludes `E>=35`.

Replay: [`STATE_588_REPLAY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_588_REPLAY.md). Machine summary: [`STATE_588_WHOLE_STATE_VERIFICATION.json`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_588_WHOLE_STATE_VERIFICATION.json).

The current frozen frontier is therefore

```text
997 exclusions / 4,581 survivors,
4,503 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

Survival in this catalogue is not graph feasibility.

## What the three closures suggest

The emerging reusable architecture is two-sided:

1. **High-excess scarcity:** threshold counts `h_l` restrict which large-p sources can also have large q.
2. **Low-excess availability:** zero/low-excess labels need sufficiently low-p sources; the incoming ledger may consume those cheap sources.
3. **Endpoint budget:** forced source usage raises `C_i>=q_u+p_u` until the exact `sum C_i` ledger becomes impossible.

State 588 is especially useful because all base demands are three, showing that the mechanism is not tied to demand-two correction terms. It also suggests a better computational workflow: use a cheap `h_2` screen to rank states by non-strict excess layers, then exact-enumerate only the exceptional layers.

## How the preceding generalisation machinery reached this point

| Programme | Main recorded result | Limitation / role now |
|---|---|---|
| [General heavy load](releases/general-heavy-load-reviewer-v1/README.md) | All-threshold load/routing family; 595 alternative hand exclusions | Strong aggregate structure; does not by itself quantify all selected geometry |
| [Joint heavy routing](releases/general-joint-routing-reviewer-v1/README.md) | 729 further exact catalogue exclusions; 5,578 survivors | Frozen multiplier catalogue |
| [Compatible routing catalogue](releases/general-compatible-catalogue-reviewer-v1/README.md) | 994 retained full/pilot exclusions | Produced the 4,584-state frontier entering the quantifier programme |
| [Containment spill / pair overlap](project/research/general_n/2026-09-13-constraint-respecting-cross-v1/README.md) | Scalar spill witnesses for all 4,584; fixed-pattern pair/residual-cover failures | Exposed the quantifier gap |
| [Shared residual budgets](project/research/general_n/2026-09-13-shared-residual-budget-v1/README.md) | 4,487/4,584 stored patterns rejected; 97 rational joint witnesses | Very strong on fixed geometry; not a whole-state result by itself |
| [Alternative attacks](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md) | Selection-free/excess lemmas and whole-state closures of states 227, 279 and 588 | Current primary programme |

Detailed historical milestone narratives, original outputs and superseded counts remain preserved in the linked packages and Git history.

## Independent maximum-cut route

For any cut `X|Y`, if `I` is the number of internal edges and `M` the number of missing cross-pairs, exactly

```text
e(G)=|X||Y|+I-M.
```

Thus `I<=M` for some cut would prove Murty–Simon. Reconnaissance found zero violations among the preserved finite test sets, and a hand argument proves the cut inequality for positive independent-set blow-ups of `C5`. A direct one-internal-edge/one-cross-nonedge matching proof is false and is preserved as a failed route.

## Current research priorities

1. **Run cheap threshold triage across the remaining 4,581 survivors.** Rank states by the number/severity of non-strict `h_2` excess layers, then exact-enumerate only the exceptions.
2. **Extract a symbolic threshold/availability theorem.** Explain the shared state-227/state-279/state-588 mechanism in parameters `(a,b,rho,s,E,h_l)`.
3. **Continue the selection-free raw candidate-capacity projection.** Proper source subsets and thresholded source/label classes remain promising.
4. **Maintain the maximum-cut route independently.** Do not retry the falsified direct matching.
5. **Return to shared residual/pair/exact-destination geometry after quantified pruning.** Those constraints are powerful once the alternative-margin/profile space has been reduced.

## Trust boundary

The largest correlated mathematical risk is still the canonical bridge: its graph-to-quasi-edge implications, selected/residual ledger, forcing lemmas and endpoint consequences require independent specialist review. The state-227, state-279 and state-588 arithmetic is exact, but independent computational reproduction and external checking of the hand-rigidity arguments remain open. The candidate `7/12` theorem and later general lemmas also require novelty assessment and external review.

No solver timeout, floating infeasibility status or unsuccessful search is used as proof.

For restart-level detail, read [`CURRENT_STATE.md`](CURRENT_STATE.md). For the latest quantified advance, read [`STATE_588_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_588_WHOLE_STATE.md).
