# Murty–Simon / Erdős #742 — current state handoff

**Purpose.** Durable restart point after chat reset, client desynchronisation or context loss. The repository, not any chat transcript, is the source of truth. Read this file first, inspect later `main` commits, then follow the linked packages.

**Research state reconciled:** 13 September 2026 through the **N34 state-153 whole-state exclusion**, the seventh quantified whole-state closure after states 227, 279, 588, 526, 382 and 519. External mathematical review, novelty assessment and independent computational reproduction remain OPEN unless a later preserved checkpoint explicitly changes that status. Internal replay, same-assistant audit and repository publication are not external acceptance.

The temporary branches `threshold-family-scan` and `state279-proof` were reconciled into `main` by merge commit `566e064447a9cd54a8fa253c9049de0ffbc09efe`. Their histories remain preserved.

## Headline fixed-order candidate status

- `n=25`: complete candidate, `e(G)<=156`, equality exactly `K(12,13)`; reviewer-v2; external specialist review open.
- `n=27`: complete candidate, `e(G)<=182`, equality exactly `K(13,14)`; reviewer-v2; external review open.
- `n=28`: complete candidate, `e(G)<=196`, equality exactly `K(14,14)`; reviewer-v2 plus analytic hardening; external review open.
- `n=29`: complete candidate, `e(G)<=210`, equality exactly `K(14,15)`; reviewer-v4; difficult `Delta=16` branch hand-closed; external review open.
- `n=30`: complete candidate, `e(G)<=225`, equality exactly `K(15,15)`; reviewer-v3; external review open.
- `n=31`: complete candidate, `e(G)<=240`, equality exactly `K(15,16)`; source-first reviewer-v1; external review open.
- `n=32`: complete candidate, `e(G)<=256`, equality exactly `K(16,16)`; source-first reviewer-v1; external review open.
- `n=33`: complete candidate, `e(G)<=272`, equality exactly `K(16,17)`; source-first reviewer-v1; external review open.
- `n=34`: complete candidate, `e(G)<=289`, equality exactly `K(17,17)`; reviewer-v2; final heavy certificate replaced by a short hand argument; external review open.
- `n=35`: complete candidate, `e(G)<=306`, equality exactly `K(17,18)`; reviewer-v1; external review open.

These fixed-order candidate proofs are closed on their own preserved ledgers. General-theory survivor counts below are **not** unresolved N34/N35 cases.

## Canonical general theory

Canonical graph-to-constraint framework: [`CANONICAL_BRIDGE.md`](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).

Current candidate general results include:

- all-order balanced-degree reduction and fixed-`a`/tail families;
- maximum-degree theorem candidate: for `n>=6`, `Delta(G)>=(7/12)n` implies `e(G)<floor(n^2/4)`;
- all-threshold heavy-load/routing inequalities, incoming-degree penalties and low-demand consequences;
- joint heavy-routing, demand/tail projection and equality rigidity;
- compatible-destination routing, closed compatible potential and fixed-neighbourhood Hall/flow criterion;
- co-singleton trace hierarchy and receiver-containment spill inequality;
- pair-overlap/residual-cover inequalities;
- shared residual-budget endpoint/pair inequalities and the balance-or-concentration alternative;
- selection-free candidate-capacity bounds;
- selected-excess bound on every selected positive-demand incidence: `p_u-rho_u+1<=x_i-s_i`;
- exact-demand corollary: when `x=s`, every active source satisfies `p_u<=rho_u-1`;
- threshold excess-cap family: if `h_l=#{i:x_i-s_i>=l}`, then `q_u>h_l => p_u<=rho_u+l-2`;
- refined baseline-3/order-statistic candidate lemma for the `s_i in {2,3}` family, preserving the exact score `rho_u+q_u-1` and negative zero-excess demand-two contribution;
- zero-excess endpoint-order candidate lemma: an exact-demand label of demand `d` requires at least `d` active sources with `rho_u>=d` and `p_u<=rho_u-1`, and its endpoint `C_i` is at least the `d`-th smallest eligible `q_u+p_u`;
- exact low-demand incidence-capacity scanner extending the audited adjacent-family verifier to a broader seven-state ring without rewriting its mathematical search logic.

The unrestricted Murty–Simon conjecture is **not** proved by this project.

## Quantifier pivot and whole-state closures

Package: [`project/research/general_n/2026-09-13-alternative-attacks-v1/`](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md).

The central diagnosis is a **quantifier problem**. Fixed-pattern models become very strong once label identities and shared budgets are retained, but a whole-state theorem must control alternative selected geometries, q-vectors and excess profiles.

### State 227

[`STATE_227_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_227_WHOLE_STATE.md) excludes N34 state 227. Exact enumeration handles `E=0,...,20`; a threshold-excess tail handles `E=21,...,34`; incoming capacity makes `E>=35` impossible. Frontier: `994/4,584 -> 995/4,583`.

### State 279

[`STATE_279_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_279_WHOLE_STATE.md) excludes N34 state 279. Exact low-excess replay covers `E=0,...,15`, with three hand-rigidity cases; the relaxed `h_2` threshold closes `E=16,...,34`; incoming capacity kills `E>=35`. Frontier: `995/4,583 -> 996/4,582`.

### State 588

[`STATE_588_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_588_WHOLE_STATE.md) excludes N34 state 588. Its unique low-excess equality is removed by an endpoint-budget contradiction `sum C_i>=106>97`; the cheap `h_2` tail leaves only `E=16` and `E=24`, both closed by exact replay. Frontier: `996/4,582 -> 997/4,581`.

### State 526

[`STATE_526_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_526_WHOLE_STATE.md) excludes N34 state 526. Its unique coarse equality is removed by source-availability/endpoint-budget rigidity; the tail is strict for `E=17,...,34`. Frontier: `997/4,581 -> 998/4,580`.

### State 382

[`STATE_382_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_382_WHOLE_STATE.md) excludes N34 state 382. Exact low-excess replay through `E=17` is strict; retaining the negative zero-excess demand-two baseline term makes the tail strict through `E=34`. Frontier: `998/4,580 -> 999/4,579`.

### State 519

[`STATE_519_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_519_WHOLE_STATE.md) excludes N34 state 519. Exact profile replay leaves only `E=6,8,9`; a stronger source-availability replay retaining the endpoint loads of two required low-p sources raises their gaps to `2,4,2`. The refined tail is strict through `E=34`. GitHub Actions run `34773463128` completed green. Frontier: `999/4,579 -> 1,000/4,578`.

The mechanism is extracted in [`ZERO_EXCESS_ENDPOINT_ORDER.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/ZERO_EXCESS_ENDPOINT_ORDER.md).

### State 153

[`STATE_153_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_153_WHOLE_STATE.md) is the seventh quantified closure:

```text
a=15, b=18, t=1,
s=2^5,3^10,
rho=1^7,2^2,3^9,
r=38, S=40.
```

The exact low-demand extension scanner is **strict on every excess layer `E=0,...,34`**, with global minimum gap `+1` and no nonpositive layers. The universal incoming cap gives

```text
sum p_u <= 7*3+2*4+9*5=74,
40+E=sum p_u<=74,
E<=34.
```

Thus the exact scan covers every possible excess value; no bespoke hand-rigidity exception is needed. GitHub Actions run `34780310971`, job `103786002313`, is green. Exact output is preserved in [`LOW_DEMAND_EXTENSION_153.tsv`](project/research/general_n/2026-09-13-alternative-attacks-v1/LOW_DEMAND_EXTENSION_153.tsv) with machine provenance in [`STATE_153_WHOLE_STATE_VERIFICATION.json`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_153_WHOLE_STATE_VERIFICATION.json). Frontier: `1,000/4,578 -> 1,001/4,577`.

## Current whole-state generalisation record

The frozen frontier is now

```text
1,001 exclusions / 4,577 survivors.
```

Breakdown:

```text
4,499 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

These are survivors in a frozen generalisation experiment, **not surviving graphs** and not unresolved fixed-order N34/N35 cases.

The extraction utility [`extract_frozen_survivors.py`](project/research/general_n/2026-09-13-alternative-attacks-v1/extract_frozen_survivors.py) is transport/replay infrastructure only; it does not apply a theorem.

## General-theory lesson from the seven closures

The closures support a reusable two-sided architecture:

1. **High-excess scarcity:** threshold counts `h_l` cap the incoming load of large-q sources.
2. **Zero/low-excess availability:** exact-demand labels require enough sufficiently low-p selected sources.
3. **Endpoint upper order statistics:** every selected source gives `d_i<=rho_u+q_u-1`, so the selected-source score distribution caps `C_i` from above.
4. **Endpoint lower order statistics:** a zero-excess exact-demand label forces `C_i` at least the appropriate eligible-source order statistic of `q_u+p_u`.
5. **Negative baseline terms matter:** a demand-two label at zero excess contributes negatively in baseline three and should not be discarded.
6. **Triage before exact enumeration:** cheap refined relaxations should rank states and excess layers before profile enumeration.
7. **Some whole states now close without bespoke rigidity:** state 153 is strict on all admissible excess layers under the reusable exact incidence-capacity verifier, which is encouraging for scale.

State 588 shows the mechanism does not depend on demand-two terms. State 526 exposes source-availability rigidity. State 382 gives the clean universal negative-baseline correction. State 519 upgrades that correction to an endpoint-load order statistic. State 153 shows the strengthened machinery can sometimes supply a clean whole-state closure directly.

## Broader low-demand extension matrix

Commit `60f89cb49a493b6b65ccca93bcaa83291bef6f21` parallelized the exact extension scan across seven additional frozen N34 states. GitHub Actions run `34780310971` completed green in all seven jobs.

The current layer summary is:

| State | minimum gap | nonpositive excess layers |
|---:|---:|---|
| 153 | `+1` | none — **whole state closed** |
| 283 | `-2` | `E=7 (-2)` |
| 122 | `-3` | `E=0 (-3)` |
| 154 | `-3` | `E=0 (-1), 6 (-1), 7 (-3)` |
| 231 | `-7` | `E=6 (-5), 7 (-2), 8 (-3), 9 (-7), 10 (-3)` |
| 77 | `-7` | `E=0 (-7), 1 (-3), 3 (0), 4 (0), 5 (0), 6 (-1), 7 (0)` |
| 60 | `-11` | `E=0 (-11), 1 (-5), 2 (-2), 3 (-3), 4 (-3), 5 (-5), 6 (-2), 7 (-3)` |

This is a useful compression. After state 153, **state 283 has only one exceptional layer (`E=7`) and state 122 only one (`E=0`)**. They are the immediate best closure targets. These are necessary-condition scan survivors, not graphs.

## Adjacent-family narrow scan

[`REFINED_H2_FAMILY_SCAN.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/REFINED_H2_FAMILY_SCAN.md) contains nine structurally adjacent N34 records. At scan time five were closed and four were active: states `230,282,385,519`. State 519 is now closed. The remaining active companions are

```text
230, 282, 385.
```

The old refined tail is already strict from `E=21` upward for 282 and 385, and `E=23` upward for 230. The endpoint-order term should still be propagated through this narrow family, but the broader matrix now offers smaller immediate targets in states 283 and 122.

## Independent maximum-cut route

For any cut `X|Y`, let `I` be its internal edges and `M` its missing cross-pairs. Exactly

```text
e(G)=|X||Y|+I-M.
```

Thus `I<=M` for some cut would imply Murty–Simon. A direct matching from every maximum-cut internal edge to a uniquely witnessed cross nonedge is **false**; any viable proof must use aggregate charging, alternating exchanges or stability.

## Corrected interpretation of switching

Degree-preserving `2x2` repairs live in the **relaxed selected-incidence matrix**. They are not automatically legal switches of actual graph quasi-edge representatives. No active theorem assumes unrestricted graph-level switching.

## Most important correctness obligations

1. **External review of the canonical bridge**, especially the graph-to-quasi-edge implications; this remains the main correlated correctness risk.
2. External review/novelty assessment of the candidate `7/12` theorem and later general lemmas, especially selection-free candidate capacity, selected excess, threshold family, refined baseline/order-statistic lemma and zero-excess endpoint-order lemma.
3. Independent reproduction of the exact computations for states 227, 279, 588, 526, 382, 519 and 153.
4. External checking of hand-rigidity/endpoint arguments in the closures that use them.
5. Preserve the complete seven-state extension outputs, not only the successful state-153 layer table, before relying on them downstream.
6. Continue preserving failures, invalidated shortcuts, solver timeouts and publication/tooling mistakes. Never treat numerical infeasibility or noncompletion as proof.

## Current research priorities

### P1. Attack the two one-layer extension survivors

Prioritize:

```text
state 122: E=0, current gap -3;
state 283: E=7, current gap -2.
```

Extract their minimizing q-vectors/profiles, then apply the strongest exact-demand endpoint-order/source-availability and threshold-incidence constraints. If either closes, package it as the next whole-state note immediately.

### P2. Continue with state 154

If P1 does not immediately close both states, analyze state 154's three residual layers `E=0,6,7`. Its small residual set makes it the next best exact target.

### P3. Seek a symbolic threshold/availability theorem

Extract a parameterized inequality in `(a,b,rho,s,E,h_l)` that explains the seven closures and the matrix compression, rather than accumulating isolated finite results.

### P4. Propagate the endpoint-order correction through 230/282/385

Complete the original adjacent-family P1 by adding the eligible-source `lambda_d` term to the generic scanner and reranking the three remaining narrow-family states.

### P5. Widen quantified pruning

Apply the strengthened scanner to the remaining 4,577 frozen scalar survivors wherever its hypotheses apply, preserving full inputs, outputs, hashes and failures.

### P6. Continue selection-free and maximum-cut routes in parallel

Seek useful raw candidate-capacity projections and aggregate maximum-cut charging/stability statements. Do not retry the falsified direct matching.

### P7. Return to shared residual/pair geometry after quantified pruning

Bring the stronger shared-budget and exact-destination machinery back after the threshold programme has reduced the alternative-margin/profile space.

## Research/preservation rules

The standing orders in [`project/N25_PROJECT_STANDING_ORDERS.md`](project/N25_PROJECT_STANDING_ORDERS.md) remain binding. In particular:

- chat must never be the sole durable record of material work;
- preserve code, parameters, inputs, outputs, survivor lists, hashes, commands, certificates and environment information where applicable;
- preserve failed approaches, counterexamples and corrected interpretations rather than deleting them;
- distinguish mathematical proof status, exact replay, internal audit, publication and external review;
- routine non-forced commits/pushes to canonical repository `paullenz/MurtySimon742` `main` are authorised without asking again;
- verify the branch head and key files after publication; do not use force-push or history rewriting.

## Restart protocol

On a fresh session:

1. open this file;
2. inspect `main` commits newer than this reconciliation point;
3. read the alternative-attacks README and the seven whole-state notes (227, 279, 588, 526, 382, 519, 153) plus verification summaries;
4. inspect `REFINED_BASELINE3_LEMMA.md`, `ZERO_EXCESS_ENDPOINT_ORDER.md`, `REFINED_H2_FAMILY_SCAN.md`, `make_low_demand_extension_scanner.py` and the preserved state-153 extension table;
5. continue from P1/P2 unless later preserved work changes priority;
6. preserve any material result or failure before relying on it downstream;
7. after a material change, update this handoff in the same repository-writing pass.

For the fuller reviewer-facing map use [`README.md`](README.md) and [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md).
