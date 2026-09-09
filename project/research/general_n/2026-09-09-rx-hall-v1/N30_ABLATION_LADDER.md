# n=30 RX-Hall ablation ladder: isolating the surviving core

9 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: research checkpoint / exact finite falsification programme. Not an unrestricted theorem and not an independent review. The existing n=30 complete-candidate proof is unaffected.**

## 1. Scope

The laboratory is the difficult positive-demand zero-slack frontier at

```text
n=30, Delta=16, m=225,
(a,b,t)=(13,16,1).
```

After the already-audited preparation and exact row-threshold stages, there are 207 hard positive-demand rows considered by the stripped RX-Hall programme.

Every rejection counted below is backed by an exact integer Farkas certificate against the stated necessary-condition relaxation. A survivor is only a relaxation state, never an asserted graph.

## 2. Ablation ladder

| Retained structure | Exact rejections | Survivors | Interpretation |
|---|---:|---:|---|
| RX4 tiny Hall core; no R, P, Z | 126 / 207 | 81 | Local RX4/Hall geometry alone is insufficient at equality. |
| RX4 + exact grouped supplement transport P; no R, Z | 127 / 207 | 80 | Exact P transport removes only one additional state. |
| Exact residual budget R + RX1-RX3 + two-neighborhood Hall; no P, Z | 200 / 207 | 7 | The residual/degree-mass resource is the dominant missing ingredient. |
| Exact residual budget R + exact grouped P + RX1-RX3 Hall; no Z | 200 / 207 | 7 | Adding exact P removes none of the seven residual-budget survivors. |
| Exact residual budget R + original grouped source-label incidence Z; P weakened to nested necessary cuts | 207 / 207 | 0 | R+Z closes the seven without exact P transport. |

The preserved checkpoint files are:

```text
checkpoints/N30_RX4_CORE_RUN_34337412304.json
checkpoints/N30_RX4_TRANSPORT_RUN_34337661352.json
checkpoints/N30_RESIDUAL_BUDGET_RUN_34338075220.json
checkpoints/N30_RESIDUAL_TRANSPORT_RUN_34338113944.json
checkpoints/N30_RZ_SEVEN_RUN_34338683589.json
```

## 3. Structural conclusion from the ablation

On this n=30 equality frontier, exact supplement transport is not the source of the final contradiction. Once the exact residual budget is present, adding exact P transport changes nothing: the same seven `(s,rho)` profiles survive.

By contrast, restoring the original grouped source-label incidence layer Z eliminates all seven even while P is weakened back to its nested necessary projection.

Thus the smallest currently demonstrated closing core is

```text
positive-demand zero slack
+ exact residual / label-degree mass
+ source-type distributions and weak nested transport
+ RX1-RX3 compatibility
+ grouped source-label incidence / per-demand-group capacity Z.
```

No unordered-pair aggregate capacity and no cumulative-tail variables are needed in this ablation.

This is a materially sharper research target than the earlier full RX-Hall model.

## 4. Degree-mass projection

In the positive-demand zero-slack sector,

```text
d_i = R_i+s_i,
y_i = x_i-s_i,
sum_i R_i = r,
sum_i s_i = r+2t,
```

hence

```text
sum_i d_i = 2r+2t = 2(r+t)=2e(F).                 (DM1)
```

RX1-RX3 become

```text
s_i <= rho_u,                                     (DM2)
d_i <= rho_u+q_u-1,                               (DM3)
d_i+y_i >= q_u+p_u,                               (DM4)
0 <= y_i <= b-d_i.                                (DM5)
```

Therefore the residual variable R itself need not necessarily survive into a final symbolic theorem: its global role can be represented by the exact degree-mass identity DM1.

## 5. What Z contributes that coarse Hall did not

The grouped Z layer does more than require enough total compatible label capacity. For each source type `(rho,q,p)` and each equal-demand label group, it enforces a per-source/per-group unit-capacity condition before summing the source's total q selected incidences.

In graph language, one source cannot satisfy several selected incidences by repeatedly using the same actual A-label. Group compression must respect the finite number of distinct labels in each demand class.

The seven residual-budget survivors therefore point directly at a **distinct-label / partition-capacity phenomenon**, rather than supplement transport.

## 6. Next theorem target

The highest-value next step is to eliminate Z symbolically without losing its per-demand-group information.

A promising formulation is a partitioned Hall/majorization inequality. Let the A-labels be partitioned by equal demand `s`. A source type `u=(rho,q,p)` has a compatible subset in each demand block determined by DM2-DM5. It must choose q distinct labels, with at most one incidence to each actual label.

The desired symbolic statement should upper-bound the total selectable incidence mass from a collection of source types by a sum of blockwise capacities of the form

```text
sum_g min( source demand offered to block g,
           number of actual labels in g times available label load in g )
```

or, equivalently, by a small family of threshold/partition Hall inequalities indexed by demand level and possibly degree threshold.

The research objective is to derive such an inequality using only profile data `(s,rho)` plus the exact degree-mass identity, then test it against the seven preserved n=30 profiles and the exact n=29/n=30 certificate families.

## 7. Falsification results that should constrain the next attempt

Two tempting simplifications have already failed and should not be recycled unchanged:

1. RX4 plus full/large Hall geometry without residual mass is too weak on m=225.
2. The raw weighted-RX2 scalar inequality with independently maximized source q is far too weak: it rejects 0/8 even on the n=30 m=226 hard frontier.

Any useful symbolic projection must therefore retain both the exact global label-degree resource and a nontrivial distinct-label/group-capacity constraint on the source side.

## 8. Current interpretation

The computation is now giving a fairly coherent mathematical message:

```text
not pair capacity,
not cumulative tails,
not exact supplement transport,
not RX4 alone,

but

exact label-degree mass
+ distinct compatible-label capacity.
```

That is the next general-N attack surface.
