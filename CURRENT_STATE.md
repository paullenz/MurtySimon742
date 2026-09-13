# Murty–Simon / Erdős #742 — current state handoff

**Purpose.** Durable restart point after chat reset, client desynchronisation or context loss. The repository, not any chat transcript, is the source of truth. Read this file first, inspect later `main` commits, then follow the linked packages.

**Research state reconciled:** 13 September 2026 through the [alternative-attacks v1 checkpoint](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md), published after the [shared residual-budget continuation](project/research/general_n/2026-09-13-shared-residual-budget-v1/README.md). External mathematical review, novelty assessment and independent computational reproduction remain OPEN unless a later preserved checkpoint explicitly changes that status. Internal replay, same-assistant audit and repository publication are not external acceptance.

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

## Current general theory

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
- **new selection-free candidate-capacity bounds:** a raw candidate quasi-edge `ui->w` forces `d_i<=c_u-1` and `C_i>=mu_u`, yielding subset capacity `e(overline{H[B]}[U])<=sum_(u in U)|K_u|`, sharpened under positive surplus by residual activity;
- **new selected-excess bound:** on every selected positive-demand incidence,
  `p_u-rho_u+1<=x_i-s_i`, with summed form
  `sum q_u^+ max(0,p_u-rho_u+1)<=sum x_i(x_i-s_i)`;
- **exact-demand corollary:** when `x=s`, every active source satisfies `p_u<=rho_u-1` and every selected label at source `u` has raw B-degree in `[q_u+p_u,rho_u+q_u-1]`.

The unrestricted Murty–Simon conjecture is **not** proved by this project.

## Active generalisation frontier

The compatible-routing catalogue plus four retained pilot-only witnesses exclude `994` of the frozen `5,578` joint-routing survivors, leaving **4,584** states:

- `4,506` N34 equality-derived states;
- `78` N35 `m=306`-derived states.

The scalar spill projection has a positive exact-demand witness in all 4,584 states, so it adds zero whole-state exclusions. Pair-overlap repairs also show zero whole-state exclusions from the raw pair moment.

The shared residual-budget continuation is much stronger on one stored selected geometry per state:

| Stage | Additional fixed-pattern exclusions | Patterns left |
|---|---:|---:|
| Shared-label endpoint budget | 4,449 | 135 |
| Residual-placement control | 13 | 122 |
| Joint pair/shared-budget constraints | 25 | 97 |

Total fixed-pattern exclusions: **4,487 / 4,584**. The remaining 97 are rational joint-relaxation witnesses, not graphs or simultaneous integer residual placements. Alternative selected sets, `q`-vectors and `x>=s` mean that these results do **not** alter the whole-state frontier.

**Current whole-state generalisation record remains `994 exclusions / 4,584 survivors`.**

## Alternative-attacks v1 — current strategic pivot

Package: [`project/research/general_n/2026-09-13-alternative-attacks-v1/`](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md). Hand theory: [`SELECTION_FREE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/SELECTION_FREE.md). Audit/failures: [`AUDIT.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/AUDIT.md).

The key diagnosis is now a **quantifier problem**, not a shortage of scalar inequalities. Fixed-pattern models become very strong once label identities and shared budgets are retained, but a whole-state theorem must control alternative geometries.

### Geometry-quantified result already obtained

For N34 state 227, the saved exact-demand margins are

```text
rho = 1^7,2,3^10,
q   = 0^7,4,3,3,4,4,4,4,4,4,3,4,
x=s = 2^4,3^11.
```

[`MARGIN_CLASS_EXAMPLE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/MARGIN_CLASS_EXAMPLE.md) gives a hand proof that **no selected-incidence family whatsoever** with those row/column margins can satisfy the canonical endpoint/forcing constraints. This upgrades a fixed-pattern rejection to an **all-selected-geometries exclusion for one `(q,x)` margin class**. It is not a whole-state exclusion because alternative `q` and `x>s` choices remain.

The arithmetic replay passes independently of any optimizer. The proof uses the exact-demand incoming cap, source-degree intervals, a mod-three incidence obstruction and total raw B-cross degree.

### Direct graph-definition challenge

`verify_selection_free_small.py` reconstructs the bridge directly on 728 D2C graphs and all 1,169 minimum-degree complement roots. It checks:

- 3,856 raw candidate quasi-edges;
- 77,696 universal candidate-set subset inequalities;
- 2,338 deterministic legal representative systems against the selected-excess inequality;
- zero violations.

None of those small roots has positive surplus `t>0`, so the positive-surplus `c_u-1` sharpening is **not** tested by that finite experiment; its status rests on the hand proof.

### Independent maximum-cut route

For any cut `X|Y`, let `I` be its internal edges and `M` its missing cross-pairs. Exactly

```text
e(G)=|X||Y|+I-M.
```

Thus `I<=M` for some cut would imply Murty–Simon. The route is being retained as an independent proof architecture.

Deterministic reconnaissance found zero maximum-cut violations among 728 D2C instances checked through order 12 and 2,226 sampled positive `C5` blow-ups through order 30. A short hand argument proves the desired cut inequality for every positive independent-set blow-up of `C5`.

A tempting direct matching from every maximum-cut internal edge to a uniquely witnessed cross nonedge is **false**. Our local reconnaissance and an independent public order-10 obstruction both kill that naïve injection. Any viable proof must use aggregate charging, alternating exchanges or stability rather than one-edge/one-nonedge matching.

## Corrected interpretation of switching

The earlier degree-preserving `2x2` repairs live in the **relaxed selected-incidence matrix**. They are not automatically legal switches of actual graph quasi-edge representatives, because the switched cross-edge may not have the required exact total-domination exception. No active theorem is allowed to assume that stronger switching freedom.

Use either:

1. explicit all-geometry models where the matrix relaxation is stated as such; or
2. selection-free raw candidate data / genuinely legal representative availability at graph level.

## Most important correctness obligations

1. **External review of the canonical bridge**, especially the graph-to-quasi-edge implications and Sections 6, 8-12; this remains the main correlated correctness risk.
2. External review/novelty assessment of the candidate `7/12` theorem and later general lemmas, including selection-free candidate capacity and selected excess.
3. Independent reproduction of proof-critical computations where material.
4. Continue preserving failures, invalidated shortcuts, solver timeouts and publication/tooling mistakes. Never treat numerical infeasibility or noncompletion as proof.

## Current research priorities

### P1. Quantify alternative `q` and `x>s` geometries

This is now the primary attack. Start from the selected-excess inequality and exact-demand interval structure, not from another fixed-pattern refinement.

Use a nested hierarchy:

1. fixed `q,x`, quantify **all** selected sets;
2. variable `q`, exact demand `x=s`;
3. variable `q` and `x>=s`, charging every escape to selected-degree excess;
4. only then add shared residual budgets, pair deficits and exact destination/Hall realization.

The state-227 margin proof is the model outcome: use optimization only to discover structure, then replace negative solver status by a checkable counting/Hall/dual argument.

### P2. Project the raw candidate-capacity subset inequality

The selection-free set

```text
K_u={i: ui in E(H), d_i<=c_u-1, C_i>=mu_u}
```

gives a genuine graph-level subset capacity bound. Seek a useful projection in terms of degree/tail data that does not require knowing the entire raw graph. Proper subsets `U` and thresholded source/label classes are the likely place to gain over the old aggregate residual-activity inequality.

### P3. Maintain the maximum-cut route in parallel

Do **not** retry the falsified direct matching. Test aggregate Hall/charging or stability statements around a maximum cut, using the critical-edge local witness characterization and the local maximum-cut condition `d_cross(v)>=d_inside(v)`.

### P4. Return to concentration/shared-budget only as supporting theory

The balance-or-concentration branch remains useful, especially if P1 forces a restricted family of selected margins. It is no longer the default next attack because the broader obstacle is the quantifier over selected geometry.

### P5. Whole-domain application only after quantified obstruction

Do not alter the `994 / 4,584` frontier unless every admissible branch required for a whole-state claim is covered. Keep fixed pattern, margin class, `q`-profile and whole-state exclusions distinct.

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
3. read the alternative-attacks v1 package and its audit;
4. continue from P1 unless later preserved work changes priority;
5. preserve any material result or failure before relying on it downstream;
6. after a material change, update this handoff in the same repository-writing pass.

For the fuller reviewer-facing map use [`README.md`](README.md) and [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md).
