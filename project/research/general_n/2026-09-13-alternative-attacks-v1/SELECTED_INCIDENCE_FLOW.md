# Selected-incidence Hall/flow theorem

13 September 2026. **Candidate general theorem inside the canonical selected/residual bridge. External mathematical review remains OPEN.**

The recent demand-compatible excess-order, threshold-incidence and forced-incidence lemmas are all projections of one exact finite object: a capacitated simple bipartite graph whose left vertices are selected sources and whose right vertices are selected labels.

This note states the exact Hall/max-flow criterion for that incidence system. It is purely combinatorial; the Murty–Simon content enters through the definition of which source-label incidences are allowed.

## 1. Abstract capacitated incidence problem

Let `U` be a finite source set and `I` a finite label set. Prescribe nonnegative integer degrees

```text
q_u  for u in U,
x_i  for i in I,
```

with equal total

```text
Q=sum_u q_u=sum_i x_i.                                (1)
```

Let `Gamma` be a bipartite allowed-incidence graph on `U union I`. We ask whether there is a **simple** bipartite subgraph `K subset Gamma` with exact degrees

```text
d_K(u)=q_u,
d_K(i)=x_i.                                          (2)
```

Equivalently construct the network

```text
source -> u      capacity q_u,
u -> i           capacity 1  when ui in E(Gamma),
i -> sink        capacity x_i.                          (3)
```

Because all capacities are integral, a flow of value `Q` is equivalent to an integral incidence system satisfying (2).

## 2. Exact Hall criterion

For a source subset `W subset U`, let

```text
d_W(i)=|N_Gamma(i) cap W|.                            (4)
```

Thus label `i` can absorb at most

```text
min(x_i,d_W(i))                                       (5)
```

incidences emitted by `W`: it has total capacity `x_i`, but simplicity permits at most one edge from each allowed source in `W`.

**Theorem (capacitated Hall criterion).** An exact incidence system (2) exists if and only if for every source subset `W subset U`,

```text
sum_{u in W} q_u
 <= sum_{i in I} min(x_i,d_W(i)).                     (6)
```

### Proof by max-flow/min-cut

The network (3) has total source capacity `Q`. A flow of value `Q` exists iff every `s-t` cut has capacity at least `Q`.

Fix the source vertices `W` placed on the source side of a cut. For each label `i`, there are two choices:

- put `i` on the sink side, paying the `d_W(i)` unit-capacity source-label arcs from `W` to `i`;
- put `i` on the source side, paying its label-sink capacity `x_i`.

For fixed `W`, the minimum contribution of label `i` is therefore

```text
min(x_i,d_W(i)).
```

The source arcs of vertices outside `W` contribute

```text
sum_{u notin W} q_u.
```

Hence the minimum cut having precisely `W` source vertices on the source side has capacity

```text
sum_{u notin W}q_u + sum_i min(x_i,d_W(i)).           (7)
```

Requiring (7) to be at least `Q=sum_u q_u` is exactly (6). This for every `W` is equivalent to every cut having capacity at least `Q`, proving the theorem. Integrality of max flow supplies a simple incidence graph. QED.

Since the total right-hand capacity is also `Q`, any value-`Q` flow saturates every label capacity as well as every source demand, so the right degrees in (2) are exact rather than merely upper bounds.

## 3. Murty–Simon compatibility graph in an all-positive-demand branch

Return to a fixed selected/residual scalar branch in which every selected label has positive demand. For each source define

```text
L_u=max(0,p_u-rho_u+1).                               (8)
```

For each label put

```text
e_i=x_i-s_i>=0.                                       (9)
```

Selected-edge forcing and selected-excess imply that a selected incidence `ui` can occur only if

```text
s_i<=rho_u,
e_i>=L_u.                                             (10)
```

Define `Gamma(p)` by

```text
ui in E(Gamma(p))
 iff s_i<=rho_u and e_i>=L_u.                         (11)
```

Every legal selected incidence system is a subgraph of `Gamma(p)`. Therefore (6) is a necessary condition for the scalar branch:

```text
sum_{u in W} q_u
 <= sum_i min(x_i,
              #{u in W:s_i<=rho_u, e_i>=L_u})        (12)
```

for every source subset `W`.

If the canonical inequalities (10) are the only incidence restrictions being retained in a relaxation, then (12) is also sufficient for an incidence system inside that relaxation.

This theorem does **not** assert that such an incidence system extends to a graph satisfying all Murty–Simon constraints. It exactly solves only the selected source-label matching layer defined by (10).

## 4. Earlier lemmas as projections of the flow theorem

### 4.1 Demand-compatible excess order

Take `W={u}`. Then the right side of (12) counts the number of labels compatible with source `u`, because `min(x_i,1)` is one for every selected label with positive degree. Thus

```text
q_u <= #{i:s_i<=rho_u,e_i>=L_u}.                     (13)
```

Solving (13) for `L_u` is precisely the demand-compatible excess order-statistic source cap.

### 4.2 Threshold incidence capacity

Take a source class

```text
W={u:rho_u<=R,L_u>=ell,q_u>0}.                        (14)
```

Every source in `W` can use only labels satisfying

```text
0<s_i<=R,
e_i>=ell.
```

Bounding `d_W(i)` by `|W|` and then `min(x_i,d_W(i))<=x_i` yields

```text
sum_{u in W}q_u
 <= sum_{i:0<s_i<=R,e_i>=ell} x_i,                   (15)
```

which is the threshold incidence-capacity lemma. Thus that lemma is a deliberately cheap relaxation of the exact Hall cut.

### 4.3 Forced-incidence source score

Suppose `W` emits more incidences than all allowed labels except target `j` can absorb. In flow language, deleting `j` lowers the right-hand side of the Hall cut below `sum_{u in W}q_u`; hence every feasible flow must use at least one edge from `W` to `j`.

The forced-incidence source-score lemma is exactly this one-target consequence, followed by

```text
d_j<=rho_u+q_u-1
```

on the forced edge.

The previous pigeonhole proof is therefore a special visible cut certificate of the same max-flow structure.

## 5. Deficiency and proof certificates

Define the Hall deficiency of a source subset `W` by

```text
def(W)
 =sum_{u in W}q_u
  -sum_i min(x_i,d_W(i)).                             (16)
```

Then

```text
max_W def(W)>0                                        (17)
```

is an exact certificate that no selected incidence system exists inside `Gamma(p)`.

A max-flow implementation automatically returns such a certificate via a minimum cut. This is useful for proof production: rather than reporting only "matching infeasible", a verifier can record

```text
W,
sum_{u in W}q_u,
{d_W(i)},
sum_i min(x_i,d_W(i)),
def(W).                                               (18)
```

All quantities are small integers and can be replayed independently without trusting a solver's numerical status.

## 6. Forced use of a source class by a target label

The flow formulation gives a stronger version of the earlier target-forcing rule.

Fix a source subset `W` and target label `j`. If

```text
sum_{u in W}q_u
 > sum_{i != j} min(x_i,d_W(i)),                      (19)
```

then every feasible selected incidence system contains at least

```text
k_j(W)
 = sum_{u in W}q_u
   - sum_{i != j} min(x_i,d_W(i))                     (20)
```

incidences from `W` to target `j`, capped of course by `min(x_j,d_W(j))`.

In particular, `k_j(W)>=1` forces at least one such incidence. If every source in `W` has selected-source score at most `M`, then

```text
d_j<=M,
C_j<=M+e_j.                                           (21)
```

This replaces the coarse absorption term `min(x_i,|W|)` by the exact compatible-neighbour count `d_W(i)`.

## 7. Nested compatibility structure

The Murty–Simon compatibility condition (10) is monotone in two source parameters:

- larger `rho_u` weakens the demand restriction;
- smaller `L_u` weakens the excess restriction.

Thus sources can be grouped by pairs `(rho,L)`, and labels by `(s,e)`. The allowed graph is a two-dimensional dominance graph:

```text
(s_i,e_i) is allowed at (rho_u,L_u)
 iff s_i<=rho_u and e_i>=L_u.                         (22)
```

This structure may make the exponentially many Hall cuts compressible. The threshold-incidence inequalities use rectangular source classes in this partial order; the exact theorem suggests searching for a finite canonical family of extremal cuts determined by `(rho,L)` classes rather than arbitrary labelled subsets.

That is the next symbolic target.

## 8. Generalisation beyond the all-positive-demand branch

The theorem in Sections 1-2 is completely general. What needs care outside an all-positive-demand Murty–Simon branch is the definition of the allowed graph: selected-excess (10) was proved for positive-demand selected incidences.

If zero-demand selected labels are possible, split the incidence system into the positive-demand portion with row degrees `q_u^+` and the remaining selected incidences, or prove an additional compatibility rule for the zero-demand class before applying (12) to total `q_u`.

No such extension is assumed here.

## 9. Consequence for the research programme

The nine quantified whole-state exclusions are no longer best viewed as unrelated scalar tricks. The later chain can be organized around one object:

```text
source margins (q,rho,p)
        |
        v
compatibility graph Gamma(p)
        |
        v
capacitated Hall / max-flow feasibility
        |
        +--> deficiency cut: branch impossible
        |
        +--> tight cut: forced incidences / sharper d_i bounds
        |
        v
baseline / endpoint contradiction.
```

The immediate computational programme is therefore to scan the remaining frozen N34 survivors for families where the compatibility graph has a small Hall deficiency or a small set of tight cuts, before returning to graph-level shared-residual geometry.

## Trust boundary

The abstract max-flow/Hall theorem is standard finite combinatorics. Its Murty–Simon application depends on the canonical selected/residual bridge, selected-edge forcing and selected-excess. It does not prove that an incidence-feasible scalar branch extends to a graph. External review of the bridge and of the way the compatibility graph is embedded in the conjecture remains open.
