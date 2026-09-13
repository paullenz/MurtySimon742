# Orientation flow / Hall projection

13 September 2026. **Candidate general lemma inside the canonical selected/residual bridge. External mathematical review remains OPEN.**

This note strengthens [`ORIENTATION_TARGET_CAPACITY.md`](ORIENTATION_TARGET_CAPACITY.md). The earlier one-sided threshold inequality is a useful projection, but it discards two pieces of exact finite structure:

1. the companion endpoint condition on every selected orientation; and
2. simplicity of the missing-edge orientation: a source can use a target at most once and an unordered missing pair can be selected at most once.

The strongest clean general statement obtained here is therefore a pair of exact Hall/max-flow projections of every legal missing-edge orientation. They are necessary conditions for the Murty–Simon scalar branch. They are not asserted to be sufficient for a graph.

## 1. Setup

Use the notation of the canonical bridge. For `u in B`, let

```text
q_u   = selected missing-B edges oriented out of u,
p_u   = selected missing-B edges oriented into u,
rho_u = residual A-cross degree,
c_u   = q_u+rho_u = |N_H(u) cap A|.
```

Let `J=overline{H[B]}`. Every edge of `J` receives exactly one selected orientation and

```text
outdeg_J(u)=q_u,
indeg_J(u)=p_u.
```

Hence

```text
sum_u q_u=sum_u p_u=:Q.
```

## 2. Exact directed compatibility of one selected orientation

Suppose a missing pair `{u,w}` is selected with orientation

```text
u -> w.
```

The established supplement-forcing argument gives

```text
q_u-1 <= c_w.                                         (1)
```

The companion selected-edge bound, already recorded in the canonical bridge, gives

```text
q_w <= c_u.                                           (2)
```

Thus every actual oriented missing edge lies in the directed compatibility relation

```text
D(u,w)
 iff u!=w,
     q_u <= c_w+1,
     q_w <= c_u.                                      (3)
```

This is strictly more informative than retaining (1) alone.

### 2.1 Orientation-independent missing-pair compatibility

If `{u,w}` is missing, one of `u->w` or `w->u` occurs. Consequently every missing pair necessarily satisfies

```text
q_u <= c_w+1,
q_w <= c_u+1.                                         (4)
```

More sharply, define the potential-pair graph `K_D` by

```text
uw in E(K_D)
 iff D(u,w) or D(w,u).                                (5)
```

Then

```text
J subseteq K_D.                                       (6)
```

Since `d_J(u)=q_u+p_u`, this yields the pointwise cap

```text
p_u <= d_KD(u)-q_u.                                   (7)
```

This may be combined with the canonical incoming caps

```text
p_u <= rho_u+b-a-1,
p_u <= b-1-q_u.                                       (8)
```

Any negative right-hand side in (7) immediately excludes the `q` profile.

### 2.2 Forced orientations

If

```text
q_u=c_w+1,                                             (9)
```

then the reverse orientation `w->u` is impossible, because it would require `q_u<=c_w`. Therefore, if `{u,w}` is missing at all, it is forced to orient `u->w` (and must still satisfy `q_w<=c_u`).

If simultaneously

```text
q_u=c_w+1,
q_w=c_u+1,                                             (10)
```

then neither orientation is legal, so `uw` cannot be a missing pair.

These forced-direction cases are useful in exact finite replay even when the coarser flow projections below pass.

## 3. Source-to-target capacitated flow projection

Fix a `q,rho` profile and choose any valid pointwise upper bounds `P_w` with

```text
p_w<=P_w.                                              (11)
```

A universally valid choice is

```text
P_w=min(b-1-q_w,
        rho_w+b-a-1,
        d_KD(w)-q_w),                                  (12)
```

truncated below at zero. Stronger bounds from selected-excess, endpoint-class Hall or incidence-capacity arguments may replace (12) whenever their hypotheses apply.

Construct the bipartite network

```text
source -> u_L          capacity q_u,
u_L -> w_R       capacity 1 if D(u,w),
w_R -> sink            capacity P_w.                  (13)
```

Every legal missing-edge orientation induces a value-`Q` flow in (13): send one unit along `u_L -> w_R` for each actual arc `u->w`.

Therefore:

> **Orientation target-flow theorem.** If the scalar branch is legal, the network (13) has maximum flow `Q`.

Equivalently, for every source subset `W subseteq B`,

```text
sum_{u in W} q_u
 <= sum_{w in B} min(P_w,
                     |{u in W:D(u,w)}|).               (14)
```

This is the exact capacitated Hall criterion for the target-flow relaxation.

### Proof

For fixed `W`, a target `w_R` can absorb at most `P_w` units in total and at most one unit from each compatible source in `W`. Hence it can absorb at most

```text
min(P_w, |N_D^-(w) cap W|).
```

Max-flow/min-cut gives (14), exactly as in the selected-incidence Hall theorem. Conversely, if all cuts (14) hold then the bipartite network has an integral value-`Q` flow. QED for the relaxation.

### Important limitation

The bipartite flow permits both `u_L->w_R` and `w_L->u_R` simultaneously. An actual simple missing graph cannot use both orientations of the same unordered pair. Thus value `Q` flow is **necessary but not sufficient** for an actual orientation. Failure of the flow is a proof certificate; success is only survival of this relaxation.

## 4. Pair-choice flow projection: enforce unordered-pair capacity

The opposite projection keeps simplicity of the unordered missing pair and forgets incoming target capacities.

Create one right-hand node `e_{uw}` for every unordered pair `{u,w}` for which at least one of `D(u,w),D(w,u)` holds. Join source `u` to pair node `e_{uw}` exactly when `D(u,w)` holds. Give every pair node capacity one:

```text
source -> u            capacity q_u,
u -> e_{uw}       capacity 1 if D(u,w),
e_{uw} -> sink         capacity 1.                    (15)
```

Every actual orientation again gives a value-`Q` flow. Hence for every source subset `W`,

```text
sum_{u in W}q_u
 <= |{ {x,y}: some u in W can legally orient that pair out of u }|.  (16)
```

This is an exact Hall criterion for choosing `q_u` distinct unordered missing pairs for every source while respecting the allowed direction and the rule that a pair is used at most once.

The target-flow projection (14) and the pair-choice projection (16) are independent necessary conditions. Passing both does not by itself couple the chosen pair to the target-capacity allocation, so it still does not prove actual orientation feasibility.

## 5. Relation to the old one-sided threshold cut

The earlier lemma kept only

```text
q_u-1<=c_w
```

on an arc `u->w`. For

```text
T_k={w:c_w<=k},
```

it yielded

```text
sum_{w in T_k}p_w
 <= sum_{u:q_u<=k+1}q_u.                              (17)
```

After replacing unknown `p_w` by upper bounds `P_w`, one obtains the scalar necessary condition

```text
Q
 <= sum_{u:q_u<=k+1}q_u
    +sum_{w:c_w>k}P_w.                                (18)
```

Every legal orientation satisfies (18), but (18) is only a one-dimensional projection of (14). It ignores the companion inequality `q_w<=c_u`, diagonal deletion, unit source-target edges, and multi-source competition for the same compatible targets.

## 6. Red-team: one-dimensional prefix cuts are not sufficient

A small exact counterexample shows that the natural Ferrers-prefix hope fails in general.

Take

```text
b=5,
a=4,
q   =(0,1,3,3,0),
rho =(1,1,1,1,3),
c   =(1,2,4,4,3).
```

The canonical/simple target caps are

```text
P=(1,1,1,1,3),
Q=sum q=7.                                            (19)
```

For every integer threshold `k`, the old scalar quantity

```text
sum_{q_u<=k+1}q_u + sum_{c_w>k}P_w
```

is at least `7`; at the relevant thresholds `k=0,1,2,3,4` it equals

```text
8, 7, 12, 9, 7.                                      (20)
```

Moreover each active source individually has at least `q_u` directed-compatible targets.

Nevertheless the exact target-flow Hall cut fails for the two sources `W={2,3}`. Each has demand three. Their compatible-target multiplicities are

```text
d_W=(0,2,1,1,2).
```

Therefore

```text
sum_{u in W}q_u = 6,

sum_w min(P_w,d_W(w))
 =0+1+1+1+2
 =5.                                                  (21)
```

So the full max flow is at most six (and in fact equals six), strictly below `Q=7`.

This example is deliberately stronger than a singleton obstruction: both high-demand sources have enough targets separately; failure occurs only when their target competition is considered jointly.

The committed verifier [`verify_orientation_flow_hall.py`](verify_orientation_flow_hall.py) replays (19)-(21) exactly.

## 7. Why the relation is two-dimensional, not Ferrers in general

By (3), source `u` may send to target `w` exactly when

```text
c_w >= q_u-1,
q_w <= c_u.                                           (22)
```

Thus each source sees a rectangle in the two target coordinates

```text
(q_w,c_w).
```

If two sources satisfy

```text
q_u<=q_v and c_u>=c_v,
```

then (ignoring the deleted diagonal) `N_D(u)` contains `N_D(v)`. But arbitrary sources need not be comparable in this partial order. Their neighborhoods can cross, so there is no general single ordering with nested neighborhoods.

The correct symbolic description is therefore a **two-dimensional dominance Hall system**. Compression may still be possible by grouping identical `(q,c)` types or by restricting to extremal down-sets/antichains, but a single one-parameter prefix family cannot replace the exact flow in general.

## 8. Coupling to the selected-incidence Hall system

For fixed margins `(q,p,rho,x,e)`, a legal branch must satisfy two distinct finite flow systems:

1. [`SELECTED_INCIDENCE_FLOW.md`](SELECTED_INCIDENCE_FLOW.md): sources of degree `q_u` must place selected incidences into labels of degree `x_i` subject to demand/excess compatibility;
2. this note: the same source margins `q_u` must place oriented missing edges into compatible targets, while the target margins are bounded by `p_u` and the canonical incoming ledger.

The systems are coupled through the same `q,p,rho` margins. Checking them separately is a relaxation, because a selected label attached to `u->w` has additional endpoint geometry not retained by the two independent flows. But any failure of either Hall system is a quantifier-correct exclusion of the scalar branch under the stated bridge hypotheses.

This is the natural next computational layer after the cheaper threshold incidence and orientation-prefix screens.

## 9. Proof certificates

Both projections admit small integer cut certificates.

For target flow, record

```text
W,
sum_{u in W}q_u,
{d_W(w)},
{P_w},
sum_w min(P_w,d_W(w)),
deficiency.                                           (23)
```

For pair-choice flow, record

```text
W,
sum_{u in W}q_u,
number of reachable unordered pair nodes,
deficiency.                                           (24)
```

No floating-point solver status is needed.

## 10. Research consequence

The attempted Ferrers reduction has produced a useful negative result rather than a shortcut:

- the old one-sided prefix family is not complete;
- the exact directed relation is a two-dimensional dominance graph;
- full max flow gives the correct cheap exact test for that relaxation;
- unordered-pair uniqueness supplies a second Hall flow;
- forced one-way pairs and the degree cap `p_u<=d_KD(u)-q_u` are additional exact consequences.

The next frontier rescan should therefore use, in increasing cost order,

```text
pair-degree cap
 -> old threshold prefixes
 -> pair-choice Hall flow
 -> target-capacity Hall flow
 -> selected-incidence Hall flow
 -> exact branch-specific geometry only for survivors.
```

## Trust boundary

The abstract Hall/max-flow claims are standard finite combinatorics. Their Murty–Simon application depends on the canonical selected/residual bridge, especially supplement forcing, the companion endpoint bound, and the selected orientation ledger. Neither flow relaxation proves that a surviving margin profile extends to a diameter-two edge-critical graph. External mathematical review and independent computational reproduction remain open.
