# Orientation target-capacity lemma

13 September 2026. **Candidate general lemma inside the canonical selected/residual bridge. External mathematical review remains OPEN.**

This note records a selection-independent capacity obstruction for the orientation of missing pairs inside `B`. It is especially strong on the exact-demand (`E=0`) layer, where active sources already obey the low-incoming-load bound `p_u <= rho_u-1`.

## 1. Setup

Use the canonical bridge notation. For `u in B`, write

```text
q_u   = outgoing selected count,
p_u   = incoming selected count,
rho_u = residual A-cross count,
c_u   = q_u + rho_u = |N_H(u) cap A|.
```

Let `J=overline{H[B]}` be the graph of missing `B`-pairs, oriented by the selected quasi-edge system. Thus every edge of `J` is oriented exactly once and

```text
d_J^+(u)=q_u,
d_J^-(u)=p_u.
```

For an oriented missing edge `u -> w`, let `i_w` denote the selected `A`-label whose cross edge at `u` is the quasi-edge for exception `w`. The `q_u` outgoing exceptions at `u` use distinct selected cross edges and hence distinct labels.

## 2. Target-capacity inequality for one oriented edge

### Lemma 2.1

If a missing pair is oriented

```text
u -> w,
```

then

```text
c_w >= q_u - 1.                                      (2.1)
```

### Proof

Besides `u -> w`, source `u` has `q_u-1` other outgoing missing edges

```text
u -> z.
```

For each such other exception `z`, its selected label `i_z` is distinct. Because `uw` is missing in `H[B]`, the pair `{u,i_z}` must dominate `w` unless `w` is the unique exception of that quasi-edge. But the unique exception is `z != w`, and `u` itself misses `w`. Therefore

```text
i_z w in E(H).
```

So `w` is cross-adjacent to all `q_u-1` distinct labels belonging to the other outgoing exceptions at `u`. Hence

```text
c_w=|N_H(w) cap A| >= q_u-1.
```

QED.

There is a companion inequality from viewing the same edge at its tail/target roles: because `u` is an incoming missing neighbour of `w`, every selected outgoing label at `w` must dominate `u`, giving `c_u >= q_w`. The threshold result below needs only (2.1).

## 3. Threshold orientation capacity

For an integer `k>=0`, define the low-cross-degree target set

```text
T_k={w in B : c_w<=k}.
```

By Lemma 2.1, any edge entering a vertex `w in T_k` can originate only at a source satisfying

```text
q_u-1 <= c_w <= k,
```

so necessarily

```text
q_u <= k+1.
```

Every source `u` has exactly `q_u` outgoing edges in total. Therefore

```text
sum_{w in T_k} p_w
 <= sum_{u:q_u<=k+1} q_u.                             (3.1)
```

This is a Hall-type target-capacity inequality for the missing-pair orientation. It is deliberately relaxed: the right side counts *all* outgoing edges of every eligible source even when some are forced to targets outside `T_k`. Hence (3.1) is a safe necessary condition.

## 4. Exact-demand scalar cut

On the exact-demand layer `E=0`, `x=s` for every selected label. The exact-demand corollary in `SELECTION_FREE.md` gives, for every active source,

```text
q_u>0  ==>  p_u<=rho_u-1.                             (4.1)
```

For an inactive source the existing canonical incoming-capacity bound gives

```text
p_u<=rho_u+2,
```

and simplicity always gives

```text
p_u<=17-q_u
```

in the frozen `b=18` family. Thus define the safe pointwise cap

```text
P_u = min(17-q_u, rho_u-1)    if q_u>0,
P_u = min(17-q_u, rho_u+2)    if q_u=0.               (4.2)
```

The exact-demand incoming total is

```text
Q=sum_u p_u=S.
```

Split this sum at `T_k`. Combining (3.1) with (4.2) gives the purely `q,rho` necessary condition

```text
Q
 <= sum_{u:q_u<=k+1} q_u
  + sum_{w:c_w>k} P_w                              (4.3)
```

for every integer `k`.

If the right side of (4.3) is smaller than `Q` for even one threshold, the entire `q`-profile is impossible; no enumeration of `p`, selected-label identities or residual placement is required.

## 5. N=34 low-demand consequences

`verify_e0_orientation_capacity.py` enumerates exactly the same nondecreasing `q`-partitions used by the frozen low-demand scanner for states 77 and 60 and tests (4.3) at every threshold.

The exact results are:

```text
state 77: 201670 q-profiles tested, 0 pass;
          maximum over profiles of the minimum cut capacity = 32 < Q=38.

state 60: 253001 q-profiles tested, 0 pass;
          maximum over profiles of the minimum cut capacity = 31 < Q=37.
```

Thus every exact-demand `q`-profile in both states violates a target-capacity cut, with a margin of at least six incoming incidences even at the closest profile.

This closes the `E=0` layer for both scalar states inside the frozen N=34 experiment. The separate joint-Hall replay had already made all of their other previously nonpositive excess layers strict.

## 6. Generalisation potential

The useful feature of (3.1) is that it does not depend on `E=0`; it is an orientation consequence of the quasi-edge domination rule itself. For positive excess, one can combine the same threshold target set with whatever pointwise or aggregate upper bounds are available for `p`. The exact-demand specialization is unusually strong because (4.1) sharply suppresses incoming load at every active source.

A stronger future form can also retain the companion condition `c_u>=q_w` for an arc `u->w`, giving an allowed-arc bipartite flow problem rather than the one-sided threshold relaxation used here.

## Trust boundary

The proof uses only:

1. the canonical orientation of missing `B`-pairs by distinct selected quasi-edges;
2. the defining domination property of a quasi-edge with its unique exception;
3. `c_u=q_u+rho_u`;
4. the already-recorded exact-demand active-source bound and canonical incoming/simple-degree caps.

It does not fix a selected geometry, does not assume a numerical optimizer is correct, and does not use the endpoint class-packing inequalities. External checking of the canonical bridge and this derivation remains open.