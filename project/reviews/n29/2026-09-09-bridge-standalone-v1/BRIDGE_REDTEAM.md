# Hostile audit of the standalone n=29 Delta=16 graph-to-model bridge

9 September 2026. Audit performed by ChatGPT/Geeps. Same-assistant red-team only; independent expert review remains open.

## Verdict

No blocking counterexample has been found in the bridge after rederiving the implications from the graph definitions.

One real exposition defect was found immediately in the first standalone draft: the threshold-capacity lemma was stated with an over-compressed justification. It is now expanded separately in `THRESHOLD_CAPACITY_LEMMA.md`. The defect was in exposition/traceability, not a discovered reversal of the inequality.

The current highest-risk hand obligations remain the quasi-edge injection, residual-activity lemma, and the `delta(C)=0` exclusion. These should receive external review before any theorem promotion.

## Audit method

For every displayed implication in `GRAPH_TO_MODEL_BRIDGE.md`, the audit asked:

1. Is the conclusion necessary for every actual graph, or only typical?
2. Is an injection being assumed where only a many-to-one map is known?
3. Can two forced residual edges collide?
4. Can a cross-edge counted as residual actually be selected in the opposite orientation?
5. Does a selected-edge claim rely on the exception being in `B`?
6. Is an upper bound substituted where a lower bound is required, or vice versa?
7. Does grouping or sorting silently assume graph symmetry?

## RT-BRIDGE-001 — complement/quasi-edge construction

**Attack.** After adding a missing `B`-edge `uw` to `H`, could the new adjacent total-dominating pair avoid both `u,w`, or equal `{u,w}`, or use an auxiliary outside `A`?

**Resolution.** No other adjacency changes, so a genuinely new adjacent pair must use `u` or `w`. The pair `{u,w}` still misses `v`. If the pair is `{u,i}`, then `u` misses `v`, so domination of `v` forces `iv in H`, hence `i in A`. Before insertion `{u,i}` covered every vertex except `w`, otherwise it would already have been total-dominating in `H`.

**Verdict:** survives.

## RT-BRIDGE-002 — selected-edge injection

**Attack.** Could two missing unordered `B`-pairs select the same cross-edge `ui`?

**Resolution.** The cross-edge determines its `B` source `u`; the unique vertex omitted by `N_H(u) union N_H(i)` determines the supplement `w`. Thus the missing pair `{u,w}` is recovered from the selected edge.

At a fixed source, selected labels are distinct because the selected objects are edges. Supplements are distinct because the same source-supplement pair is one missing unordered `B`-pair, for which only one selected orientation is chosen.

**Verdict:** survives.

## RT-BRIDGE-003 — exact ledger

Starting from

```text
q_total + e(H[B]) = C(b,2),
```

and

```text
e(H)=a+e(C)+r+q_total+e(H[B]),
```

with `e(C)=C(a,2)-e(F)` and `n=a+b+1`, direct simplification gives

```text
m=e(G)=b(n-b)+e(F)-r.
```

Therefore

```text
t=m-b(n-b)=e(F)-r,
e(F)=r+t.
```

No approximate or asymptotic identity is used.

**Verdict:** survives.

## RT-BRIDGE-004 — demand implication

Minimum `H`-degree gives

```text
x_i >= d_i-R_i,
```

hence `x_i>=s_i=max(0,d_i-R_i)`.

Also

```text
S=sum s_i >= sum(d_i-R_i)
             =2(r+t)-r
             =r+2t.
```

The inequality is in the safe direction: replacing `max(0,d_i-R_i)` by `d_i-R_i` only lowers the sum.

**Verdict:** survives.

## RT-BRIDGE-005 — source-demand injection `s_i<=rho_u`

Fix selected `ui->w` and an `F`-neighbour `j` of `i`. Then `uj in H` because `{u,i}` must dominate `j`.

If `uj` is residual, charge `j` to one of the `rho_u` residual source slots.

If `uj` is selected, write `uj->z`. Distinct selected labels at source `u` have distinct supplements. Since `ui->w` must dominate `z != w` and `uz` is missing in `H[B]`, `iz in H`. Moreover `iz` cannot itself be selected: both `i` and `z` miss `j` (`ij` is an `F`-edge and `z` is the exception of `uj->z`), whereas a selected cross-edge has its unique exception in `B`, not in `A`. Thus `iz` is residual.

This injects every `F`-neighbour not charged to a residual source edge into a distinct residual edge at label `i`, yielding

```text
d_i<=rho_u+R_i,
s_i<=rho_u.
```

**Verdict:** survives; this is one of the most important bridge steps.

## RT-BRIDGE-006 — pair residual inequality `d_i<=rho_u+rho_w`

Again fix `ui->w` and `F`-neighbour `j`.

If `uj` is residual, charge to `rho_u`. Otherwise `uj->z` with `z!=w`. Since that quasi-edge must dominate `w` and `uw` is missing, `jw in H`.

The edge `jw` cannot be selected from source `w`: both `w` and `j` miss `i` (`wi` is missing because `w` is the exception of `ui->w`, and `ji` is an `F`-edge), which would leave an `A`-vertex undominated. Therefore `jw` is residual.

Distinct `j` give distinct residual `w-j` edges, proving

```text
d_i<=rho_u+rho_w.
```

**Verdict:** survives.

## RT-BRIDGE-007 — supplement forcing

For every other selected `uj->z` at source `u`, `z!=w`. The pair `{u,j}` must dominate `w`; since `uw` is missing, `jw in H`. The `q_u-1` other selected labels are distinct, so `w` has at least `q_u-1` cross-neighbours among those labels. They are partitioned into residual and selected edges at source `w`, hence

```text
rho_w+q_w>=q_u-1.
```

**Verdict:** survives.

## RT-BRIDGE-008 — exact `q+p` missing degree and endpoint load

Every missing unordered `B`-pair incident with `u` is oriented either outward from `u` or inward to `u`, exactly once. Thus `q_u+p_u` is exactly the missing degree of `u` in `H[B]`.

For selected `ui->w`, the following `B`-vertices are distinct neighbours of `i`:

- `u`;
- supplements of the other `q_u-1` outward arcs at `u`;
- sources of the `p_u` incoming arcs into `u`.

An incoming source cannot equal an outgoing supplement, because that would assign both orientations to the same missing unordered pair. For an incoming source `z`, the pair `uz` is missing and `z!=w`; since `ui->w` must dominate `z`, `iz in H`. The same covering argument handles outgoing supplements.

Therefore

```text
R_i+x_i>=q_u+p_u.
```

**Verdict:** survives.

## RT-BRIDGE-009 — residual activity

Assume `rho_u=0`, put `U=N_A(u)`, `T=A\U`.

Because every `u-i` with `i in U` is selected, an `F`-edge from `U` to `T` would contradict the selected quasi-edge's need to dominate its `T` endpoint. Hence `F(U,T)` is empty.

For each `F`-edge `ij` in `U`, the two selected edges from `u` to `i,j` have distinct supplements. Cross-domination forces two residual edges `i-w_j` and `j-w_i`. They are residual because each would otherwise fail to dominate the opposite `A` endpoint. The mapping from the ordered endpoints of `F[U]` to these residual edges is injective.

For an `F`-edge `ij` in `T`, adding `ij` to `H` creates a quasi-edge. Its auxiliary cannot be `v` (the pair would miss `u`), cannot be `u` (no adjacency), and cannot lie in `A`: to dominate `u`, an `A` auxiliary would have to lie in `U`, but being the auxiliary for exception in `T` would require an `F(U,T)` edge. Therefore an auxiliary lies in `B`, producing a residual cross-edge with `A` endpoint in `T`. Different `F[T]` pairs give different cross-edges because the edge plus its unique `A` exception recover the pair.

The `F[U]` and `F[T]` residual families are disjoint by their `A` endpoints. Hence

```text
r>=2e(F[U])+e(F[T])>=e(F)=r+t,
```

contradicting `t>0`.

**Verdict:** survives after explicit collision audit.

## RT-BRIDGE-010 — charging inequality

For each label choose `s_i` actual selected incidences. Each chosen source satisfies `rho_u>=s_i`. A chosen source also has `q_u>=1`, so `rho_u<=a-1`; the denominator `a-rho_u` is never zero.

Source `u` has at most `a-rho_u` selected incidences in total. Charging each chosen incidence by

```text
(rho_u-1)/(a-rho_u)
```

therefore charges source `u` by at most `rho_u-1`. The charge function is increasing in integer `rho` on `[1,a-1]`, so a demand-`s_i` label receives at least

```text
s_i(s_i-1)/(a-s_i).
```

Summation gives the claimed inequality.

**Verdict:** survives.

## RT-BRIDGE-011 — threshold-capacity proof compression

**Finding:** the first standalone draft did not contain enough detail to justify

```text
2W_h<=z_h^2-z_h+h(h+1).
```

This was an exposition/traceability failure and was not accepted silently.

**Repair:** `THRESHOLD_CAPACITY_LEMMA.md` now gives the complete high-load-source/unordered-pair proof. It uses only:

- `s_i<=rho_u`;
- distinct selected labels and supplements;
- one selected orientation per missing unordered `B`-pair.

No old `pair_capacity()` implementation is a dependency.

**Verdict after repair:** no mathematical defect found.

## RT-BRIDGE-012 — `delta(C)=0` exclusion

This remains the least compact bridge step. The hostile audit rechecked the counting logic used to obtain

```text
b<=[C(a,2)-t]-C(a-1,2).
```

For `a=12,b=16,t in {2,3}` the right side is only `9` or `8`, respectively, so any valid version of the injection has large slack.

The proof depends on separating a family of residual cross-edges forced by missing pairs inside `A\{x}` from an additional family covering all `B` endpoints, using residual activity. No collision was found in the rederivation, but this is specifically marked for external review because it compresses several quasi-edge uniqueness arguments.

**Verdict:** no defect found; elevated review priority.

## Overall conclusion

The bridge has now been reduced to a small set of hand obligations with explicit injection/collision arguments. The finite trusted kernel begins only after these obligations.

No theorem status is promoted. A single counterexample to any universal bridge lemma overrides every green workflow downstream.
