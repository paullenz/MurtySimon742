# Singleton-destination trap and cardinality arc-slot Hall test

15 September 2026. Structural successor to the selected-label/destination coupling recorded in [`2026-09-14-source-pricing-witnesses-v1`](../2026-09-14-source-pricing-witnesses-v1/README.md). **Exact necessary-condition argument; external mathematical review OPEN.**

This package excludes three of the five original synthetic profiles that remained after the row108 result:

```text
newly excluded: 347, 471, 586
still not rejected by this route: 160, 338
original synthetic sample: 711 / 713 rejected
```

These are synthetic necessary-condition profiles, not canonical scalar states or realized graphs. The promoted canonical frontier remains **4,626 exclusions / 952 survivors / 3,632 whole-state closures**. The fresh-seed namespace is not scanned or changed here.

## 1. The singleton-destination lemma

For the canonical selected-label/orientation bridge, let `S_u` be the selected-label set of source `u`, so `|S_u|=q_u`. For every canonical arc `u->w`, the retained destination-coupling inequalities are

```text
1 <= |S_u \ S_w| <= rho_w+1,
|S_w \ S_u| <= rho_u.
```

The orientation is simple: it has outdegree `q_u`, no loops, and no opposite arc pair.

Suppose now that

```text
q_u = rho_u = 1.
```

Because `S_u` is a singleton and `1 <= |S_u \ S_w|`, its unique label is absent from `S_w`. Hence `S_u` and `S_w` are disjoint. Therefore

```text
q_w = |S_w| = |S_w \ S_u| <= rho_u = 1.
```

So **every outgoing arc of a `(q,rho)=(1,1)` source must end at a distinct vertex with `q<=1`**.

Let

```text
T = {u : q_u=1 and rho_u=1},
L = {w : q_w<=1}.
```

Every `u in T` needs exactly one outgoing arc to `L\{u}`. Associate it with the unordered pair slot `{u,w}`. Since opposite arcs are forbidden, one unordered pair slot can be used at most once. Consequently a necessary condition is a matching that assigns every `u in T` to one of these pair slots. Any Hall deficiency excludes the profile.

This is only a necessary condition. Passing it does not imply that compatible selected-label sets or a graph exist.

## 2. Immediate hand exclusions

The current five original non-rejections give:

| row | `T={q=rho=1}` | `L={q<=1}` | singleton matching | consequence |
|---:|---|---|---:|---|
| 160 | 14,18 | 6,9,14,18,21 | 2 / 2 | not rejected |
| 338 | 3 | 0,1,3 | 1 / 1 | not rejected |
| 347 | 16 | 16 | **0 / 1** | **excluded** |
| 471 | 3,4 | 3,4 | **1 / 2** | **excluded** |
| 586 | 8 | 8 | **0 / 1** | **excluded** |

For rows347 and586 the sole `(1,1)` source is itself the only vertex with `q<=1`, so it has no legal destination. For row471 the two `(1,1)` sources can only point to one another; both need an outgoing arc, but that would use both orientations of the same unordered pair, which is forbidden.

Thus the final `e_L=47` row471 branch is unnecessary: row471 is excluded before any block-excess split. The earlier exact `e_L=39,40,41,42,43` work remains preserved as independent evidence and as the route by which the stronger destination obstruction was reached.

## 3. Stronger all-source cardinality arc-slot relaxation

The verifier also checks a broader necessary relaxation using only the cardinalities of `S_u` and `S_w`.

For a proposed direction `u->w`, put `I=|S_u intersect S_w|`. The two local coupling inequalities and the fact that both sets lie in an `a`-label universe require an integer `I` with

```text
max(0,
    q_u+q_w-a,
    q_u-rho_w-1,
    q_w-rho_u)
<= I <=
min(q_u,q_w,q_u-1).
```

If no such integer exists, that direction is impossible even before choosing actual labels. Build one capacity-one node for every unordered source pair on which at least one direction is cardinality-compatible. Source `u` has demand `q_u` and may use a pair node only if direction `u->w` is compatible. A max-flow smaller than `sum q_u` is therefore another exact necessary-condition contradiction.

The five current original profiles give:

| row | required outgoing arcs | compatible pair slots | max flow | result |
|---:|---:|---:|---:|---|
| 160 | 81 | 261 | 81 | not rejected |
| 338 | 101 | 272 | 101 | not rejected |
| 347 | 129 | 307 | **127** | **excluded** |
| 471 | 96 | 214 | **95** | **excluded** |
| 586 | 109 | 274 | **108** | **excluded** |

For the rejected profiles the residual min-cut exposes small deficient source sets. Row471 is exactly the two-source singleton obstruction; row586 is the single source8 obstruction. Row347 has a stronger three-source cardinality deficit as well, although its singleton source16 already gives the one-line proof.

The all-source flow is deliberately a relaxation: it chooses a potentially different intersection size for each pair and does not require one globally consistent family of label sets. Therefore its failures are valid exclusions, while full flow on rows160 and338 is only a non-rejection.

## 4. Exact replay and scope

[`verify_singleton_destination.py`](verify_singleton_destination.py) uses Python standard library only. It reads the preserved original profile corpus, checks its source digest, reconstructs both matching relaxations, and preserves rows160 and338 as non-rejections.

The frozen parsed result is [`RESULT.json`](RESULT.json), canonical JSON SHA-256

```text
9a89c420f82a0bd89eb8e99a34dd3109ace9c1829879e62e819d452f408313f7
```

Run [`run_replay.py`](run_replay.py) from repository root. A dedicated remote workflow is installed by this package and is not called successful until inspected.

The result updates only the **original synthetic sample** from `708/713` to **`711/713`**, leaving rows **160 and338**. It does not alter the canonical `4,626 / 952 / 3,632` finite frontier and does not prove the unrestricted conjecture.

## 5. Next target

Rows160 and338 pass both the singleton matching and the all-source cardinality arc-slot flow, so repeating cardinality-only orientation search is unlikely to be decisive. The next attack should enforce **one actual selected-label family** together with destination compatibility and the shared residual-neighbourhood condition

```text
| (union_{w:u->w} S_w) \ S_u | <= rho_u.
```

The previously preserved uncoupled witnesses for rows160 and338 already fail these stronger coupling tests. The task is now to exclude every realization, not merely those particular witnesses.