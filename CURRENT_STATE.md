# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The live graph-theory problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The 2019 Dailly–Foucaud–Hansberg all-order strengthening is false: the published 2024 order-12, size-32 D2C graph remains a mandatory hostile control. Existing Murty–Simon / Erdős #742 work and the standalone-paper programme remain preserved, but they are not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `Q0_INDEPENDENT_NEIGHBORHOOD_BRANCH_CLOSED_NOT_PROMOTED`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. This unit critically reassessed the peeled `Q=0` / saturated-source route. The decisive simplification was to apply cross-edge criticality to **every** `B`-source, not just saturated ones. That turns the remaining branch into a star and then contradicts the required triangularity of `F`.

**INSPECTED PREDECESSORS:**

- `4608632b1e2510e1b4493c915a044a630b15b449` — maximum-triangle-or-twin reduction;
- `f7596142c35a86e83ff48a6faf001c45dca2faf8` — `Q=0` critical-arm orientation and saturated-source obstruction.

The saturated-source work remains preserved, but the new proof supersedes it for closing the `Q=0` branch.

## New theorem — independent-neighbourhood defect bound

Let `G` be non-bipartite D2C and let `v` be a maximum-degree root with

`B=N(v)`, `A=V(G)\N[v]`, `b=Delta(G)`, `F=G[A]`, `f=e(F)`.

Assume

`Q=e(G[B])=0`,

so `B` is independent. For `x in A` put

`R_x=b-|N_B(x)|`, `d_x=d_F(x)`, `e_x=R_x-d_x=b-d_G(x)>=0`.

Then the exact defect identity is

> `delta=b(n-b)-m=f+sum_x e_x`.                        (Q0)

The new internal candidate theorem is:

> **Q0-INDEPENDENT-NEIGHBOURHOOD DEFECT THEOREM.**
>
> `delta >= b-1`.

Equivalently,

`m <= b(n-b)-(b-1) = b((n-1)-b)+1 <= M(n)`.

Therefore **no above-threshold non-bipartite D2C graph can have a maximum-degree root with `Q=0`.**

Full hand proof:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/Q0_INDEPENDENT_NEIGHBORHOOD_DEFECT_THEOREM.md`

## Core proof mechanism

Assume for contradiction `delta<=b-2`.

1. The preserved triangle-free `F`-edge payment says every edge of `F` must lie in a triangle.
2. For any source `u in B`, let `S_u=N_A(u)`, `T_u=A\S_u`, `t_u=|T_u|`.
3. If `x in S_u` is nonisolated in `F[S_u]`, then the cross edge `ux` lies in a triangle. Criticality of `ux` has two possible arm directions.
4. One direction immediately gives `delta>=b-1` by a `b-1` endpoint payment. Therefore under the counterexample assumption only the other direction survives, producing a private foot in `T_u` for every nonisolated vertex of `F[S_u]`.
5. Hence

   `nu(F[S_u]) <= t_u`                                (SF)

   for every `u in B`.
6. Since `F` is nonempty, (SF) implies every source has `t_u>=1`.
7. The exact missing-incidence ledger gives

   `sum_u t_u = r = f+delta <= 2delta <= 2b-4 < 2b`.

   With `b` positive integer source loads, some source has `t_u=1`.
8. For that source, `F[A\{c}]` has at most one nonisolated vertex, hence is edgeless. Therefore `F` is a nonempty star centred at the unique missed vertex `c`.
9. Every star edge must nevertheless be triangular. Since the star has no A-side triangle support, a `B`-source `w` sees both the centre and a leaf `x`.
10. Then `x` is nonisolated in `F[S_w]`, so (SF) demands a private foot outside `S_w` adjacent to `x`. But `x` is a star leaf whose only `F`-neighbour is the centre, already inside `S_w`. Contradiction.

Thus `delta>=b-1`.

## Consequence — maximum-triangle-root scope is fully resolved

For every non-bipartite D2C graph with

`m>=M(n)+1`,

every maximum-degree root satisfies

> `Q=e(G[N(v)])>0`.

So **every maximum-degree vertex lies in a triangle**. The earlier false-twin peeling branch is no longer an unresolved alternative; it was a valid reduction, but Q0-IN eliminates its core.

This is stronger than the originally sought existential maximum-triangle-root statement.

## Combination with preserved all-private theorem

The preserved all-private edge-witness theorem states that for

`n>=14`, `m>=M(n)+1`,

once a maximum-degree root has `Q>0`, the all-private branch is impossible. Hence every such above-threshold graph is now forced into the **disjoint-support antipode branch**:

> there exist `u,w in N(v)` with
>
> `uw notin E(G)` and `N(u) intersect N(w)={v}`.

Thus, modulo external review of the internal lemmas, the scope issue is gone: the antipode branch is the single remaining structural branch for the eventual second-extremal attack.

## Mandatory controls

The published 2024 order-12, size-32 exception remains untouched. The independent `X_3` reconstruction has

`n=12`, `m=32`, `M(12)=31`, `Delta=8`, `Q=12` at its unique maximum root.

It therefore lies outside the Q0-IN hypothesis and remains in the maximum-triangle / antipode branch, as required.

The expanded-`C5` equality family is sharp for Q0-IN: at maximum roots it has

`Q=0`, `delta=b-1`, `m=M(n)`.

The non-bipartite hypothesis is essential: complete bipartite graphs have `Q=0` and `delta=0`.

## Verification

Companion regression:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/check_q0_independent_neighborhood_defect.py`

Recorded summary:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/Q0_INDEPENDENT_NEIGHBORHOOD_DEFECT_CHECK_SUMMARY.json`

Finite evidence:

- 21 D2C graph-atlas classes through order 7;
- 10 non-bipartite D2C classes;
- 17 non-bipartite maximum-root `Q=0` instances;
- 18 triangle-free `F`-edge payment records;
- zero violations of the exact defect identity or `delta>=b-1`;
- explicit `X_3` hostile control replayed as D2C with `12/32`, `M(12)=31`, and `Q=12>0`.

The atlas happens not to contain a `Q=0` instance with the new internal-source-foot obstruction active, so that local lemma is primarily hand mathematics rather than independently stress-tested by the small atlas. External review remains important.

## Trust boundary

Q0-IN is an internal hand theorem with finite regression. It has not received external mathematical review or novelty assessment. **No eventual second-extremal theorem is claimed.**

The remaining live branch is now singular:

1. choose a maximum-degree root `v`; Q0-IN forces `Q>0` above the threshold;
2. for `n>=14`, all-private edge-witness pricing forces a disjoint-support antipode `u,w in B`;
3. convert that antipode plus the residual defect ledger into `delta` large enough to contradict `m>=M(n)+1`, while preserving the order-12 `X_3` control.

**UNPRESERVED WORK:** None after this current-state commit.

**NEXT ACTION:** Reassess the antipode branch from the new stronger starting point. Use an actual maximum-degree root with `Q>0` and an antipodal pair

`uw notin E(G)`, `N(u) intersect N(w)={v}`.

The preserved coarse payment only gives `Q+r>=a` / `2delta+2f+b(2b-n)>=a`, which is too weak near balance and is satisfied by `X_3`. The next unit should exploit the **partition of A into disjoint supports of u and w plus the uncovered remainder**, and price criticality of edges incident to the two supports. Look specifically for a stability theorem whose error term vanishes only in a cube/Boolean-flow configuration; the order-12 `X_3` profile (`F=empty`, `delta=0`) must remain an allowed finite obstruction. Do not return to Q0 peeling, the closed mixed `{4,5}` ladder, or first-proof optimization for Erdős #742.
<!-- CURRENT-STATUS:END -->
