# A flow criterion for fixed selected/residual cross-neighbourhoods

12 September 2026. Candidate general combinatorial reduction. Independent
external mathematical review and novelty assessment remain OPEN.

## 1. The object being tested

Use the [canonical bridge](../2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).
For each B-source u fix disjoint subsets S_u and R_u of the A-labels:
selected and residual cross-neighbours. Write N_u=S_u union R_u,
q_u=|S_u|, rho_u=|R_u|. Assume the fixed cross data satisfy their source
capacities, label demands and selected-incidence eligibility.

A **B-side routing** assigns each selected incidence (u,i), i in S_u,
one destination v different from u. Distinct incidences use distinct missing
unordered B-pairs. If (u,i) is assigned to v, require:

1. i is absent from N_v;
2. every other missing B-neighbour w of u contains i in N_w;
3. each destination v receives at most c_v=rho_v+b-a-1 arcs.

Assume c_v>=0. Negative c_v is separately impossible even with no arcs.
These conditions are necessary for the canonical selected representatives.
Conversely they describe only B-side routing: H[A], its degree ledger,
A-side domination and edge-criticality remain outside this model.

## 2. Pair compatibility determines orientation and label

Define the eligible destinations for an obligation (u,i) by

    D_(u,i)={v != u : S_u minus N_v = {i}, and S_v is contained in N_u}.

**Lemma.** A B-side routing can use the arc u->v with label i only if
v belongs to D_(u,i). Conversely any selection of such eligible arcs, using
each obligation exactly once and respecting destination capacities, is a
B-side routing.

For necessity, i is absent at v. Every other selected label at u has an
exception different from v, because there is only one orientation per missing
unordered pair; its representative must dominate v. Hence all those other
labels are in N_v, proving S_u minus N_v={i}.

Every selected label at v has its exception different from u, since the pair
{u,v} is already oriented u->v. Its representative must dominate u, giving
S_v contained in N_u.

For sufficiency, first note two automatic injectivity properties. For a fixed
ordered pair (u,v), the singleton difference identifies at most one label.
If u->v is eligible, S_v minus N_u is empty, so v->u is ineligible for every
label. Thus no two obligations can use the same unordered pair, and distinct
labels at one source have distinct destinations.

Consider an assigned incidence (u,i) with destination v and any other chosen
missing pair incident with u, with opposite endpoint w. If that pair is
u->w with label j, then j differs from i and S_u minus N_w={j}; hence i is
in N_w. If the pair is w->u, eligibility requires S_u contained in N_w,
again placing i in N_w. Also S_u minus N_v={i} gives i absent at v.
All three defining B-side conditions follow.

The subset condition cannot be dropped: it is what enforces domination
across incoming missing pairs and prevents opposite orientations.

## 3. Exact flow and a Hall-type certificate

Create one obligation node for each (u,i) with i in S_u and one destination
node for each v in B. Let Q=sum q_u. Join a source to every obligation with
capacity 1, every obligation to its eligible destinations with capacity Q+1,
and destination v to the sink with capacity c_v. All capacities are integers.

The lemma shows that a B-side routing exists exactly when this network has
a flow of value Q. An integer augmenting-path algorithm gives an integral
flow, so each obligation chooses one destination. There is no fractional
rounding step. Pair injectivity follows from the lemma rather than an
additional capacity shared by two opposite arcs.

Equivalently, for every subset T of obligations, it is necessary and
sufficient that

    |T| <= sum_(v in union_(u,i in T) D_(u,i)) c_v.            (1)

Necessity counts the distinct assignments of T. For sufficiency, run integer
augmentations to exhaustion. If the flow is less than Q, take all nodes
reachable from the source in the residual network. Let T be its obligation
nodes and U its destination nodes. An obligation-destination arc has capacity
Q+1, greater than the total flow; thus every neighbour of T is reachable.
Conversely every reached destination is reached through an obligation edge,
so U is exactly that neighbour union. No sink is reachable. The cut has
capacity Q-|T|+sum_(v in U)c_v, which equals the attained flow and is less
than Q. Therefore T violates (1).

The certificate is just the fixed cross sets, T and its full neighbour union;
an independent checker can recompute the integer deficit without trusting
the algorithm. If Q=0, the empty routing is immediate.

This is the standard integer flow/Hall mechanism applied to the eligibility
reduction above; no claim that max-flow or Hall's theorem is new is intended.
The augmenting-path argument here states the needed finite implication.

## 4. Receiver conflict and inherited constraints

Let I_v be the set of distinct labels on arcs entering v. For a B-side routing,

    I_v is disjoint from N_v,
    |I_v| <= a-rho_v-q_v,
    S_u intersect I_v = {i} whenever (u,i)->v.                (2)

The first two statements follow because incoming labels are absent. For the
third, S_u minus N_v={i}; all of I_v is outside N_v, and i belongs to both
S_u and I_v. In particular two incoming incidences with different labels
cannot have one sender select the other incidence's label.

This retains identities of labels. The earlier scalar condition
rho_v+q_v>=q_u-1 only counts the q_u-1 labels forced into N_v.

Endpoint load follows as in canonical Section 8: for a selected (u,i), u and
all missing neighbours of u except its one exception are distinct neighbours
of i, giving R_i+x_i>=q_u+p_u. Heavy destination forcing also follows: if
more than h selected labels at u have demand at least h, every heavy arc's
destination contains at least h other heavy labels; either all are residual
or a selected one supplies rho_v>=h by eligibility. Thus the flow criterion
with valid cross data implies the degree-routing model's load, eligibility
and every heavy threshold constraint.

## 5. Scope and use in this pilot

The MILP searches over cross sets as well as arcs. The flow reduction fixes
the cross sets first. A failed flow certificate excludes that precise cross
pattern, including every possible rerouting of it. It does **not** exclude
all cross patterns with the same demand and residual sequences.

This reduction was derived while the pre-frozen six-state MILP pilot ran.
The subsequent fixed-pattern flow analysis is explicitly post-pilot analysis
of its outputs, with no replacement or extension of the original sample.
An independent tiny-instance exhaustive challenge checks the pair equivalence
and flow criterion. Finite checks supplement the general argument above.
