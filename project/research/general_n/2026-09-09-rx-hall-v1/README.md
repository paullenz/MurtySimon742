# General-N RX-Hall kernel reconnaissance

9 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: general-N reconnaissance / candidate structural reduction. Not a theorem. Numerical infeasibility in this checkpoint is not accepted as proof evidence until exact certificates are added. Independent mathematical review remains OPEN.**

## 1. Motivation

Mining the exact n=29 and n=30 Delta=16 Farkas certificates exposed a substantial simplification of the final finite model.

The first recurrent certificate family was the already-known positive-demand zero-slack identity. If every demand `s_i>0`, then `d_i-R_i=s_i` at every label, so the exact ledgers give

```text
S=sum_i s_i = sum_i(d_i-R_i) = r+2t.
```

Thus any positive-demand state with `S != r+2t` is impossible before source-flow modelling. The old final LP was rediscovering this equality in hundreds of its Farkas rays.

After removing those states, the remaining certificates repeatedly use source/supplement flow plus endpoint load. The key local simplification is recorded below.

## 2. The local RX inequalities

Work in the generic complement/quasi-edge framework. For a selected cross-edge from B-source `u` to A-label `i`, write

- `rho_u` for the source residual degree;
- `q_u` for its selected outdegree;
- `p_u` for its supplement indegree;
- `s_i=max(0,d_i-R_i)` for label demand;
- `R_i` for label residual column degree;
- `x_i` for actual selected label degree.

In the positive-demand sector `s_i>0`, one has exactly

```text
d_i = R_i+s_i.
```

The already-audited selected-edge inequalities give

```text
d_i <= rho_u+R_i,
d_i <= rho_u+q_u-1,
R_i+x_i >= q_u+p_u.
```

Therefore every selected incidence satisfies

```text
s_i <= rho_u,                                      (RX1)
R_i+s_i <= rho_u+q_u-1,                           (RX2)
R_i+x_i >= q_u+p_u.                               (RX3)
```

Eliminating `R_i` from RX2-RX3 gives the especially transparent necessary condition

```text
x_i-s_i >= p_u-rho_u+1.                           (RX4)
```

So a source whose incoming selected-pair load is large relative to its residual degree forces extra selected degree above the label's basic demand.

## 3. Source supplement-flow transport

The selected missing B-pairs form an oriented source/supplement flow. A source type `(rho,q,p)` must send `q` selected-pair arcs and receive `p` arcs. A selected arc from source `u` to supplement `w` satisfies

```text
rho_w+q_w >= q_u-1.
```

The generic source-type bounds are

```text
q_u+rho_u <= a,
p_u <= rho_u+(b-a-1),
q_u+p_u <= b-1.
```

The RX-Hall model retains this source/supplement transportation constraint but deliberately **drops the unordered-pair capacity constraints**. This makes it a weaker relaxation: an actual graph still maps to it, while extra false survivors may be introduced. Therefore infeasibility of the weakened model is still a valid necessary-condition contradiction once certified exactly.

## 4. The RX-Hall label model

In the positive-demand zero-slack sector, `d_i` is redundant. A label can be represented by only

```text
(s_i,R_i,x_i),
```

with

```text
0 <= R_i <= dmax-s_i,
s_i <= x_i <= b-R_i,
sum_i R_i = r.
```

A source type `(rho,q,p)` may select that label only if RX1-RX3 hold.

The incidence system then consists of:

1. source-type distributions for each residual-degree class;
2. source/supplement transport satisfying `rho_w+q_w>=q_u-1`;
3. label `(R,x)` type distributions for each equal-demand class;
4. the exact residual-column budget `sum R_i=r`;
5. selected source-label incidence with row total `q` and label total `x`;
6. at most one incidence from one source to any one actual A-label.

No cumulative-tail `T` variables are needed. No `d` variables are needed for positive demands. No unordered-pair capacity is used.

This is an all-parameter `(a,b,t)` construction rather than an n=29- or n=30-specific model.

## 5. Reconnaissance results so far

Using floating-point HiGHS only as a reconnaissance feasibility oracle, the weakened RX-Hall model gives zero survivors on every fully tested hard positive-demand frontier:

```text
n=29, Delta=16, m=211, (a,b,t)=(12,16,3): 94/94 infeasible;
n=30, Delta=16, m=226, (a,b,t)=(13,16,2):   8/8 infeasible;
n=30, Delta=16, m=225, (a,b,t)=(13,16,1): 207/207 infeasible.
```

The first 50 hard positive-demand states at

```text
n=29, Delta=16, m=210, (a,b,t)=(12,16,2)
```

were also infeasible. A sharded clean-runner scan is supplied to check the complete 902-state hard positive-demand frontier reproducibly.

These counts are **reconnaissance only** until exact Farkas certificates are produced for the RX-Hall system.

## 6. Why this matters for the unrestricted attack

The old final LP suggested that pair-capacity, cumulative selected-degree tails, label degree options, source types and endpoint flow all had to be handled simultaneously.

Certificate mining now suggests a much smaller conceptual core:

```text
positive-demand zero slack
        + source/supplement transportation
        + exact residual-column budget
        + RX1-RX3 Hall incidence.
```

The unordered-pair capacity appears unnecessary on all completely tested scopes. The cumulative-tail variables are an implementation device, not evidently a mathematical necessity.

This points toward a general theorem of the following kind:

> supplement-flow compatibility together with the RX endpoint inequalities forces a global incidence/resource inequality that is incompatible with positive surplus in the near-balanced maximum-degree band.

The next research objective is to eliminate the fractional RX-Hall transport symbolically, preferably as one or a small family of threshold/Hall inequalities in the demand and residual profiles.

## 7. Trust boundary and next steps

Highest priorities:

1. complete the n=29 `t=2` sharded RX-Hall reconnaissance;
2. add exact integer Farkas certificate generation/checking to this stripped model;
3. inspect the stripped duals for repeated threshold weights;
4. derive a symbolic Hall inequality replacing the LP;
5. test that inequality parametrically across the remaining `Delta/n` band below 293/500;
6. use n=31 only as a falsification laboratory for the proposed general inequality.

A failure of the universal graph-to-demand bridge overrides every result in this checkpoint. Same-assistant computation is not external review.