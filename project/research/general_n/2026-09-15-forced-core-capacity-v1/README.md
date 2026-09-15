# Forced-core receiver-capacity partition obstruction

15 September 2026. Structural successor to [`singleton-destination-trap-v1`](../2026-09-15-singleton-destination-trap-v1/README.md), using the exact fixed-neighbourhood routing criterion preserved in [`2026-09-12-arc-realisation-pilot-v1`](../2026-09-12-arc-realisation-pilot-v1/FIXED_NEIGHBOURHOOD_FLOW.md). **Necessary-condition proof; external mathematical review OPEN.**

This package excludes the last two non-rejections in the original 713-profile synthetic boundary sample:

```text
newly excluded: 160, 338
original synthetic sample: 713 / 713 rejected
canonical finite frontier: unchanged at 4,626 exclusions / 952 survivors / 3,632 whole-state closures
```

These are synthetic necessary-condition profiles, not realized graphs and not canonical whole-state promotions. No unrestricted Murty-Simon proof is claimed.

## 1. Forced-core receiver-capacity lemma

Use the canonical selected/residual cross sets `S_u,R_u`, with `N_u=S_u union R_u`, `|S_u|=q_u`, `|R_u|=rho_u`, and selected-incidence eligibility

```text
i in S_u  =>  s_i <= rho_u.
```

The fixed-neighbourhood routing theorem says that a selected obligation `(u,i)` may use destination `v` only if

```text
S_u minus N_v = {i},
S_v subset N_u,
```

and destination `v` receives at most

```text
c_v = rho_v + b - a - 1
```

such arcs.

Set

```text
A = {i : s_i <= 1},
h = |A|,
U = {u : rho_u=1 and q_u=h}.
```

For every `u in U`, eligibility and `|S_u|=h` force **the same selected set**

```text
S_u = A.
```

Take any obligation `(u,i)` with `u in U` and `i in A`. If it can use destination `v`, then `A minus N_v={i}` and `S_v subset N_u`. Since `i` is absent from `N_v`, it is absent from `S_v`; but `N_u` has size `h+1`, so

```text
S_v subset N_u minus {i},
q_v <= h.
```

Also `A minus {i}` is contained in `N_v`, hence

```text
q_v + rho_v >= h-1.
```

A second source in `U` cannot be the destination because its selected set is exactly `A`, which contains `i`. Therefore every forced-core obligation must go to the relaxed receiver set

```text
D = {v not in U : q_v<=h and q_v+rho_v>=h-1}.
```

Most importantly, a fixed receiver `v` can serve forced-core obligations for **at most one label** `i in A`, because `A minus N_v` cannot equal two different singleton sets. Thus the receiver capacities are indivisible across the `h` core labels. Each label occurs once at every source in `U`, so each label requires total receiver capacity at least `|U|`.

This gives a finite capacity-partition necessary condition. Failure excludes the profile before constructing any detailed selected/residual set family.

## 2. Row160: three core labels, only three capacity-5 receivers

For row160,

```text
A = {0,1,2},  h=3,
U = {0,1,2,3,13,16,17,19,25,26},  |U|=10.
```

The relaxed candidate receivers are exactly

```text
D = {4,9,10,14,15,18,22}
```

with capacities

```text
5,5,5,4,4,4,4.
```

There are ten obligations for each of the three core labels, so the seven indivisible receiver capacities must be partitionable into three bins each of capacity at least10. They are not.

A hand proof is immediate. Every label needs at least two receivers. With seven receivers divided among three labels, at least two labels get at most two receivers. A two-receiver bin reaches10 only as `5+5`, so those two labels would require four capacity-5 receivers. Only three exist.

The exact enumerator independently checks every assignment of the seven receivers to the three labels or to an unused bin. The greatest possible minimum label capacity is **9**; one maximizing split has sums `10,9,12`. Hence row160 is impossible under the necessary canonical routing conditions.

## 3. Row338: total forced-core receiver capacity is already short

For row338,

```text
A = {0,1},  h=2,
U = {6,7,9,10,11,14,15,22,26,27},  |U|=10.
```

Only receivers

```text
D = {0,1,3}
```

survive the relaxed structural filter, with capacities

```text
6,6,5.
```

The ten forced sources create twenty core-label obligations, but the total candidate receiver capacity is only

```text
6+6+5 = 17 < 20.
```

So row338 is excluded even before using the one-label-per-receiver partition restriction. The exact partition enumerator gives best minimum label capacity6 against the required10.

## 4. Exact replay and challenge

[`verify_forced_core_capacity.py`](verify_forced_core_capacity.py) reads the preserved original relaxed-profile corpus and checks its source digest. It reconstructs the forced core, the deliberately relaxed receiver superset, canonical incoming capacities and every receiver-to-label partition. It also exhaustively enumerates 290 tiny selected/residual destination patterns, containing82 eligible obligation cases, and checks the two structural consequences used in the proof.

Frozen parsed result: [`RESULT.json`](RESULT.json). Canonical JSON SHA-256:

```text
8784209ee05bb1ec6cd6da559e8845dbfeee3e041a96dcce9f41360c6d12920e
```

Run [`run_replay.py`](run_replay.py) from the repository root. A dedicated remote workflow is installed by this checkpoint; it is not called successful until inspected.

## 5. Scope and next use

This closes the **original synthetic namespace at 713/713**, but it does not alter the promoted canonical finite frontier and does not prove the unrestricted conjecture. Its value is structural: the obstruction couples selected-label eligibility, exact labelled exceptions, and receiver capacities in a form substantially smaller than the earlier simultaneous MILP.

The natural next steps are to scan the seven retained fresh-seed profiles with this lemma and its singleton predecessor, then test whether the same forced-core partition mechanism occurs systematically among the 952 canonical survivors or can be generalized to `rho=r>1` cores. Preserve every non-rejection and keep namespace boundaries explicit.
