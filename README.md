# Murty–Simon / Erdős Problem #742

Candidate proofs and reproducible research. **Updated 13 September 2026 through the N34 state-227 whole-state exclusion. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.** Repository publication, green replay and same-assistant hostile audit are not external acceptance and do not prove the unrestricted conjecture.

**External reviewers:** start with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md). Canonical theorem-level packages are indexed in [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). The project actively welcomes hostile review, counterexamples, literature corrections and genuinely independent reproduction; GitHub Issues are the preferred place to report a suspected flaw.

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
2. **Use computation for discovery and finite closure.** Search for useful inequalities/certificates, but accept a computational exclusion only after exact verification and coverage checks. A floating-point solver status, timeout or unsuccessful search is never proof.
3. **Extract simpler explanations.** Identify which constraints actually make a certificate work and replace large computational objects with hand arguments where possible.
4. **Generalise with explicit hypotheses.** Formulate parameterized lemmas, prove their graph-level implications and test their reach against preserved hard cases and failures.
5. **Quantify alternative geometry.** A strong inequality on one selected representative system does not exclude the graph/state unless every admissible alternative geometry is controlled.

That fifth step is now central to the project and has produced the first new whole-state frontier exclusion described below.

## Failures, audit challenges and corrections are part of the record

**Failed approaches, counterexamples to proposed lemmas, incomplete computations, audit challenges, discovered bugs, corrections and unresolved proof obligations are preserved alongside successful results.** They help identify which hypotheses matter and prevent superseded reasoning from silently re-entering the active proof chain.

The [preservation standing orders](project/N25_PROJECT_STANDING_ORDERS.md) require material work to be saved with enough provenance for reconstruction and audit: code, parameters, inputs, outputs, survivor lists, certificates and review findings as applicable. Original evidence and superseded arguments are retained. Invalidated evidence is labelled and excluded from active proofs. Missing evidence is recorded as a recovery obligation; reconstructions are identified as such.

Examples include the [N29 normalization bug and audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md), the [general-foundations corrections](project/reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md), the [N34 failed relaxation and hand replacement](project/reviews/n34/2026-09-12-heavy-independent-v1/README.md), and the [alternative-attacks audit](project/research/general_n/2026-09-13-alternative-attacks-v1/AUDIT.md), which preserves the failure of unrestricted selected-incidence switching and of a naïve maximum-cut matching proof.

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
| Generalisation frontier | **995 exclusions / 4,583 survivors** after the state-227 whole-state closure; these are states in a frozen generalisation experiment, not surviving graphs |

The unrestricted Murty–Simon conjecture remains unsolved by this project.

## Fixed-order frontier through n=35

The canonical reviewer packages are:

- [`n=25 reviewer-v2`](releases/n25-reviewer-v2/README.md)
- [`n=27 reviewer-v2`](releases/n27-reviewer-v2/README.md)
- [`n=28 reviewer-v2`](releases/n28-reviewer-v2/README.md)
- [`n=29 reviewer-v4`](releases/n29-reviewer-v4/README.md)
- [`n=30 reviewer-v3`](releases/n30-reviewer-v3/README.md)
- [`n=31 reviewer-v1`](releases/n31-reviewer-v1/README.md)
- [`n=32 reviewer-v1`](releases/n32-reviewer-v1/README.md)
- [`n=33 reviewer-v1`](releases/n33-reviewer-v1/README.md)
- [`n=34 reviewer-v2`](releases/n34-reviewer-v2/README.md)
- [`n=35 reviewer-v1`](releases/n35-reviewer-v1/README.md)

These fixed-order candidates have their own complete ledgers. The generalisation survivor counts below are **not** unresolved obligations in those fixed-order proofs.

## Current general structural results

Important candidate all-order or parameterized results include:

- balanced-degree reduction and fixed-`a`/tail families;
- the `7/12` maximum-degree theorem candidate;
- all-threshold heavy-load/routing inequalities with incoming-degree penalties and demand-only consequences;
- joint heavy routing, demand/tail projection and equality rigidity;
- compatible-destination routing and a closed compatible potential;
- fixed-neighbourhood exact Hall/flow routing;
- co-singleton trace hierarchy and receiver-containment spill;
- pair-overlap/residual-cover inequalities;
- shared residual budgets and a balance-or-concentration alternative;
- selection-free raw candidate-capacity subsets;
- selected-excess inequality and the new threshold excess-cap family.

### Selected excess and threshold capacity

For every selected positive-demand incidence, the [selection-free/excess package](project/research/general_n/2026-09-13-alternative-attacks-v1/SELECTION_FREE.md) proves the candidate inequality

```text
p_u-rho_u+1 <= x_i-s_i.                              (1)
```

When `x=s`, every active source therefore has `p_u<=rho_u-1`, and selected labels at source u have raw B-degree in

```text
[q_u+p_u, rho_u+q_u-1].
```

More generally put

```text
e_i=x_i-s_i,
h_l=#{i:e_i>=l}.
```

Equation (1) implies the threshold family

```text
q_u>h_l => p_u<=rho_u+l-2.                            (2)
```

This simple consequence is the mechanism that closes the high-excess tail of state 227 and is now the primary candidate for broader whole-state progress.

## Quantifier pivot: N34 state 227 is now a whole-state exclusion

The [alternative-attacks package](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md) was created because the shared-residual continuation had become extremely strong on **one stored selected geometry**—4,487 of 4,584 stored patterns were rejected—but that did not quantify alternative selections, `q`-vectors or `x>s`.

State 227 became the test case for climbing that quantifier hierarchy. Its state data are

```text
a=15, b=18, t=1,
s=2^4,3^11,
rho=1^7,2,3^10,
r=39,
S=41.
```

Write

```text
E=sum_i(x_i-s_i),
Q=41+E.
```

The preserved progression is:

1. [`MARGIN_CLASS_EXAMPLE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/MARGIN_CLASS_EXAMPLE.md): all selected geometries excluded for one saved exact-demand `(q,x)` margin class.
2. [`EXACT_DEMAND_ALL_Q.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/EXACT_DEMAND_ALL_Q.md): exact demand `x=s` excluded for every possible `q`-vector.
3. [`LOW_EXCESS_LAYERS.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/LOW_EXCESS_LAYERS.md): all profiles with `E=1,2,3` excluded.
4. [`EXCESS_SWEEP_TO_8.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/EXCESS_SWEEP_TO_8.md): all profiles through `E=8` excluded, with hand rigidity for two equality profiles.
5. [`STATE_227_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_227_WHOLE_STATE.md): the exact sweep reaches `E=20`, the threshold argument closes `E=21,...,34`, and total incoming capacity kills `E>=35`.

### Exact E=0,...,20 sweep

The exact integer replay [`verify_state227_exact_to20.cpp`](project/research/general_n/2026-09-13-alternative-attacks-v1/verify_state227_exact_to20.cpp) covers

```text
49,847 excess profiles,
40,548 strict endpoint/excess exclusions,
9,297 source-infeasible profiles,
2 equality profiles.
```

The two equality profiles are the already preserved `E=6` and `E=7` cases and are excluded by direct endpoint-rigidity arguments.

### High-excess tail E=21,...,34

Let

```text
h=#{i:e_i>=2}.
```

For a `rho=3` source, (1) implies

```text
p_u>=4 => q_u<=h,
```

so a source with `q_u>h` has `p_u<=3`. Combining only this relaxed cap with the top-k endpoint envelope gives a strict contradiction for every `E=21,...,34`. The weakest global gap is still +8. The replay is [`verify_state227_tail.cpp`](project/research/general_n/2026-09-13-alternative-attacks-v1/verify_state227_tail.cpp).

Finally

```text
sum p_u <= 7*3 + 1*4 + 10*5 =75,
```

while `sum p_u=41+E`; therefore `E>=35` is impossible.

Thus **state 227 has no realization satisfying the canonical bridge**. The machine summary is [`STATE_227_WHOLE_STATE_VERIFICATION.json`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_227_WHOLE_STATE_VERIFICATION.json).

This is a whole-state advance in the generalisation experiment, not a new N34 fixed-order proof obligation.

## Current generalisation frontier

Before the quantifier pivot, the compatible-routing catalogue plus four retained pilot-only witnesses had excluded 994 of the 5,578 joint-routing survivors, leaving 4,584 states:

```text
4,506 N34 equality-derived states,
78 N35 m=306-derived states.
```

State 227 was one of those survivors. Its whole-state exclusion changes the record to

```text
995 exclusions / 4,583 survivors,
```

with

```text
4,505 N34 equality-derived survivors,
78 N35 survivors.
```

Survival in this catalogue is not graph feasibility.

## How the preceding generalisation machinery reached this point

| Programme | Main recorded result | Limitation / role now |
|---|---|---|
| [General heavy load](releases/general-heavy-load-reviewer-v1/README.md) | All-threshold load/routing family; 595 alternative hand exclusions; demand-only tail consequences | Strong aggregate structure; does not by itself quantify all selected geometry |
| [Joint heavy routing](releases/general-joint-routing-reviewer-v1/README.md) | 729 further exact catalogue exclusions; 5,578 survivors | Frozen multiplier catalogue |
| [Demand/tail projection](releases/general-routing-tail-reviewer-v1/README.md) | 114 whole layer/profile exclusions before residual enumeration | No further exclusions among the 5,578 state survivors |
| [Compatible routing catalogue](releases/general-compatible-catalogue-reviewer-v1/README.md) | 990 full-catalogue exclusions plus four retained pilot-only = 994 | Produced the 4,584-state frontier |
| [Closed compatible potential](releases/general-closed-compatible-reviewer-v1/README.md) | Exact local formula; 832 already handled cases | Adds no frontier exclusions by itself |
| [Fixed-neighbourhood routing](releases/general-arc-realisation-reviewer-v1/README.md) | Exact Hall/flow criterion once cross-neighbourhoods are fixed | Conditional on fixed neighbourhood geometry |
| [Containment spill / pair overlap](project/research/general_n/2026-09-13-constraint-respecting-cross-v1/README.md) | Scalar spill witnesses for all 4,584; fixed-pattern pair/residual-cover failures | Exposed the quantifier gap |
| [Shared residual budgets](project/research/general_n/2026-09-13-shared-residual-budget-v1/README.md) | 4,487/4,584 stored patterns rejected; 97 rational joint witnesses | Very strong on fixed geometry; zero whole-state exclusions until geometry is quantified |
| [Alternative attacks](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md) | Selection-free/excess lemmas and first new whole-state exclusion: state 227 | Current primary programme |

Detailed historical milestone narratives, original outputs and superseded counts remain preserved in the linked packages and Git history.

## Independent maximum-cut route

The alternative-attacks package also maintains a genuinely independent architecture. For any cut `X|Y`, if `I` is the number of internal edges and `M` the number of missing cross-pairs, then exactly

```text
e(G)=|X||Y|+I-M.
```

Thus `I<=M` for some cut would prove Murty–Simon. Reconnaissance found zero violations among 728 D2C instances checked through order 12 and 2,226 sampled positive `C5` blow-ups; a hand argument proves the cut inequality for all positive independent-set blow-ups of `C5`.

A direct one-internal-edge/one-cross-nonedge matching proof is false and is preserved as a failed route. Any viable maximum-cut proof must use aggregate charging, alternating exchanges or stability.

## Current research priorities

1. **Apply the threshold excess-cap family to all 4,583 survivors.** Start with `l=1,2,3` in (2), retain the top-k endpoint envelope and quantify source degrees/excess profiles before selected geometry.
2. **Extract a symbolic threshold theorem.** State 227 closes using only the `l=2` member in its high-excess tail; seek a parameterized inequality in `(a,b,rho,s,E,h_l)` that closes families at once.
3. **Continue the selection-free raw candidate-capacity projection.** Proper subsets of sources and thresholded source/label classes remain promising.
4. **Maintain the maximum-cut route independently.** Do not retry the falsified direct matching.
5. **Return to shared residual/pair/exact-destination geometry after quantified pruning.** Those constraints are powerful once the alternative-margin/profile space has been reduced.

## Trust boundary

The largest correlated mathematical risk is still the canonical bridge: its graph-to-quasi-edge implications, selected/residual ledger, forcing lemmas and endpoint consequences require independent specialist review. The state-227 arithmetic is exact, but independent computational reproduction remains open. The candidate `7/12` theorem and the later general lemmas also require novelty assessment and external review.

No solver timeout, floating infeasibility status or unsuccessful search is used as proof.

For the current restart-level detail, read [`CURRENT_STATE.md`](CURRENT_STATE.md). For the latest quantified advance, read [`STATE_227_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_227_WHOLE_STATE.md).
