# Murty–Simon / Erdős #742 — current state handoff

**Purpose.** Durable restart point after chat reset, client desynchronisation or context loss. The repository, not any chat transcript, is the source of truth. Read this file first, inspect later `main` commits, then follow the linked packages.

**Research state reconciled:** 13 September 2026 through the **N34 state-227 whole-state closure** in [`project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_227_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_227_WHOLE_STATE.md). External mathematical review, novelty assessment and independent computational reproduction remain OPEN unless a later preserved checkpoint explicitly changes that status. Internal replay, same-assistant audit and repository publication are not external acceptance.

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
- selection-free candidate-capacity bounds: a raw candidate quasi-edge `ui->w` forces `d_i<=c_u-1` and `C_i>=mu_u`, yielding subset capacity `e(overline{H[B]}[U])<=sum_(u in U)|K_u|`, sharpened under positive surplus by residual activity;
- selected-excess bound on every selected positive-demand incidence:
  `p_u-rho_u+1<=x_i-s_i`;
- exact-demand corollary: when `x=s`, every active source satisfies `p_u<=rho_u-1` and every selected label at source `u` has raw B-degree in `[q_u+p_u,rho_u+q_u-1]`;
- **threshold excess-cap family:** if `h_l=#{i:x_i-s_i>=l}`, then
  `q_u>h_l => p_u<=rho_u+l-2`.

The unrestricted Murty–Simon conjecture is **not** proved by this project.

## Generalisation frontier before the quantifier pivot

The compatible-routing catalogue plus four retained pilot-only witnesses excluded `994` of the frozen `5,578` joint-routing survivors, leaving 4,584 scalar states:

- 4,506 N34 equality-derived states;
- 78 N35 `m=306`-derived states.

The scalar spill projection had a positive exact-demand witness in all 4,584. Pair-overlap repairs also gave zero whole-state exclusions. The shared residual-budget continuation was much stronger on one stored selected geometry per state:

| Stage | Additional fixed-pattern exclusions | Patterns left |
|---|---:|---:|
| Shared-label endpoint budget | 4,449 | 135 |
| Residual-placement control | 13 | 122 |
| Joint pair/shared-budget constraints | 25 | 97 |

Those 4,487 fixed-pattern exclusions did **not** initially change the whole-state frontier because alternative selected geometries, `q`-vectors and `x>=s` remained.

## Quantifier pivot and state-227 closure

Package: [`project/research/general_n/2026-09-13-alternative-attacks-v1/`](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md). Audit: [`AUDIT.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/AUDIT.md).

The central diagnosis is a **quantifier problem**, not a shortage of scalar inequalities. Fixed-pattern models become very strong once label identities and shared budgets are retained, but a whole-state theorem must control alternative geometries.

N34 state 227 became the test case. Its preserved progression was:

1. one fixed `(q,x=s)` margin class: all selected geometries excluded;
2. variable `q`, exact demand `x=s`: all possibilities excluded;
3. excess layers `E=sum(x_i-s_i)=1,...,8`: all excluded;
4. exact profile sweep extended through `E=20`;
5. a threshold-excess tail argument excluded every `E=21,...,34`;
6. total incoming capacity makes `E>=35` impossible.

The full proof is [`STATE_227_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_227_WHOLE_STATE.md), with machine summary [`STATE_227_WHOLE_STATE_VERIFICATION.json`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_227_WHOLE_STATE_VERIFICATION.json).

### Exact low/mid-excess sweep

For `E=0,...,20`:

```text
49,847 excess profiles,
40,548 strict endpoint/excess exclusions,
9,297 source-infeasible profiles,
2 equality profiles.
```

The two equality profiles are the previously preserved E=6 and E=7 cases and are excluded by endpoint-rigidity hand arguments.

### High-excess threshold argument

For

```text
h=#{i:x_i-s_i>=2},
```

a `rho=3` source with `q>h` must have `p<=3`; otherwise `p>=4` forces all q selected labels to have excess at least two. Combining that source cap with the top-k endpoint envelope gives strict whole-layer contradictions for every `E=21,...,34`; the minimum gap is 8.

The basic incoming cap gives `sum p<=75`, while `sum p=41+E`, so `E>=35` is impossible.

Therefore **state 227 is excluded as a whole scalar state**.

## Current whole-state generalisation record

The frontier is now

```text
995 exclusions / 4,583 survivors.
```

Breakdown:

```text
4,505 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

This is the first whole-state frontier improvement produced by the alternative-geometry/quantifier programme. It does not modify the already completed N34 fixed-order proof candidate.

## Independent maximum-cut route

For any cut `X|Y`, let `I` be its internal edges and `M` its missing cross-pairs. Exactly

```text
e(G)=|X||Y|+I-M.
```

Thus `I<=M` for some cut would imply Murty–Simon. The route remains an independent proof architecture.

Deterministic reconnaissance found zero maximum-cut violations among 728 D2C instances checked through order 12 and 2,226 sampled positive `C5` blow-ups through order 30. A short hand argument proves the desired cut inequality for every positive independent-set blow-up of `C5`.

A direct matching from every maximum-cut internal edge to a uniquely witnessed cross nonedge is **false**. Any viable proof must use aggregate charging, alternating exchanges or stability rather than one-edge/one-nonedge matching.

## Corrected interpretation of switching

Degree-preserving `2x2` repairs live in the **relaxed selected-incidence matrix**. They are not automatically legal switches of actual graph quasi-edge representatives, because the switched cross-edge may not have the required exact total-domination exception.

Use either:

1. explicit all-geometry models where the matrix relaxation is stated as such; or
2. selection-free raw candidate data / genuinely legal representative availability at graph level.

No active theorem assumes unrestricted graph-level switching.

## Most important correctness obligations

1. **External review of the canonical bridge**, especially the graph-to-quasi-edge implications and Sections 6, 8-12; this remains the main correlated correctness risk.
2. External review/novelty assessment of the candidate `7/12` theorem and later general lemmas, especially selection-free candidate capacity, selected excess and the threshold family.
3. Independent reproduction of the state-227 exact profile and tail computations.
4. Continue preserving failures, invalidated shortcuts, solver timeouts and publication/tooling mistakes. Never treat numerical infeasibility or noncompletion as proof.

## Current research priorities

### P1. Apply the threshold excess-cap family to all 4,583 survivors

This is now the primary attack. For each threshold `l>=1`, use

```text
h_l=#{i:x_i-s_i>=l},
q_u>h_l => p_u<=rho_u+l-2.
```

Start with `l=1,2,3`, couple it to the existing top-k endpoint envelope, and quantify `q`/excess profiles before returning to selected-set geometry. The immediate question is whether state 227 is an isolated success or the first member of a sizeable whole-state family.

### P2. Seek a symbolic threshold theorem

The state-227 tail closure uses only the `l=2` member of the family and deliberately ignores stronger restrictions. Extract a parameterized inequality in `(a,b,rho,s,E,h_l)` that can replace per-state enumeration for broad classes.

### P3. Project raw candidate-capacity subsets

The selection-free set

```text
K_u={i: ui in E(H), d_i<=c_u-1, C_i>=mu_u}
```

gives a genuine graph-level subset capacity bound. Seek a useful projection in terms of degree/tail data that does not require the entire raw graph.

### P4. Maintain the maximum-cut route in parallel

Do not retry the falsified direct matching. Test aggregate Hall/charging or stability statements around a maximum cut.

### P5. Use shared residual/pair geometry after quantified pruning

The shared-budget and exact-destination machinery remains powerful. Bring it back after P1/P2 have reduced the alternative-margin/profile space; do not default to another single stored selected pattern.

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
2. inspect `main` commits newer than the reconciliation point;
3. read the alternative-attacks v1 README, `STATE_227_WHOLE_STATE.md` and `AUDIT.md`;
4. continue from P1 unless later preserved work changes priority;
5. preserve any material result or failure before relying on it downstream;
6. after a material change, update this handoff in the same repository-writing pass.

For the fuller reviewer-facing map use [`README.md`](README.md) and [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md).
