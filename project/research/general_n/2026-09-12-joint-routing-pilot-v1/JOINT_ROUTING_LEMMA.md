# A count-conditioned heavy-routing load inequality

12 September 2026. Candidate general bridge lemma. Exact internal verification
supports its recorded applications; external mathematical review, novelty
assessment and external reproduction remain OPEN.

## Statement

Use the [canonical bridge](../2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md)
and the notation and label-potential inequality of the
[heavy-load family](../2026-09-12-heavy-load-family-v1/HEAVY_LOAD_FAMILY.md).
Fix integers h>=1 and T>=h. Set

`Z={u:rho_u>=h}`, `z=|Z|`, `W=sum_{s_i>=h}s_i`,
`G=sum_{s_i>=h}max(T,s_i)`, `r=sum_u rho_u`,
`f(L)=max(0,T-max(h,L))`.

H_u is the actual number of heavy selected incidences from u, and p_u its
full supplement indegree. Put J={u:H_u>h}, j=|J|, and

`c_u=min(a-rho_u, #{i:h<=s_i<=rho_u})`, `P_u=rho_u+b-a-1`.

The local domain is

`0<=H<=c_u`, `0<=p<=min(P_u,b-1-H)`, with H,p integers.

For an actual canonical profile these caps are nonnegative. An empty domain
already contradicts the bridge. The second cap follows from H<=q and q+p<=b-1;
we do not assume H=q. Zero-demand labels are allowed.

For any nonnegative rational lambda, mu and eta, define for e=0,1:

`A_u(e;j) = max { (h+eta)H + H f(H+p)`
`                 -(lambda+mu)H e + lambda min(p,j-e) :`
`                 (H,p) in the local domain, [H>h]=e }`.

A_u(0;j) is always defined. Only sources with c_u>h can belong to J.
For j>=1, sort their differences A_u(1;j)-A_u(0;j) in decreasing order,
with multiplicity, and denote the sum of the first j by D_j. Set D_0=0;
A_u(1;0) is unnecessary. Finally put

`K_j=j(z-j)+j(j-1)/2`,
`U_j=h r + sum_u A_u(0;j) + D_j + mu K_j - eta W`.

**For the actual value of j, necessarily hG<=U_j.** Consequently, a profile
is excluded if every possible j is either ruled out by an existing necessary
capacity condition or admits nonnegative multipliers with hG>U_j. Multipliers
may differ between j values. There are at most z+1 such cases.

In particular, writing L=sum_u min(h,c_u), and c_(1)>=... for the capacities
strictly above h, a j value is impossible whenever

`W > L-jh+min(sum_{i<=j}c_(i),K_j)`.

This is the existing source-capped threshold condition, applied to a specified
j instead of taking its maximum. It must not be counted as a new exclusion
when it already excludes every j.

## Proof of the joint routing step

Every heavy selected arc from J has its supplement in Z, by heavy-label
forcing. Let y_u count just these incoming arcs at u. Then

`sum_{u in J}H_u = sum_{u in Z}y_u`.

A selected arc represents a distinct unordered missing pair of B vertices.
For each destination u, at most one can come from each source in J, and none
can come from u itself. Also these arcs are part of its full indegree. Thus

`y_u<=min(p_u,j-[u in J])`.

The pairs they occupy are inside Z and incident with J. There are K_j of
those pairs: j(z-j) crossing pairs and binomial(j,2) internal pairs. It follows
that, with D=sum_{u in J}H_u,

`D<=sum_{u in Z}min(p_u,j-[u in J])`, and `D<=K_j`.       (1)

These inequalities combine destination eligibility, incoming-degree limits,
absence of loops and the single-orientation rule. They are necessary
aggregate consequences of an actual routing. They do not characterize all
possible routings or assert that independent local maximizers coexist.

## Proof of the load bound

The earlier label inequality and decreasing-potential transport give

`hG<=h r_h+sum_{u in Z}(hH_u+H_u f(q_u+p_u))`
`   <=h r+sum_{u in Z}(hH_u+H_u f(H_u+p_u))`.            (2)

Here r_h is the residual mass on heavy labels, r_h<=r, and q_u>=H_u.
Also W<=sum_Z H_u. Add eta times this inequality to (2), then use (1),
multiplied respectively by lambda and mu. The result is

`hG+eta W <= h r+mu K_j + sum_{u in Z} { (h+eta)H_u`
`       +H_u f(H_u+p_u) -(lambda+mu)H_u[u in J]`
`       +lambda min(p_u,j-[u in J]) }`.

Each summand is at most A_u([u in J];j). There are exactly j members of J.
The sum is therefore bounded by sum_u A_u(0;j) plus the j largest eligible
differences. Rearrangement proves hG<=U_j. This is a finite elementary maximum
for arbitrary parameters, with no numerical solver in the statement or proof.

For an exact certificate, multiply everything by a common positive integer
denominator. Local maxima, sorted differences and the final strict gap then
use integer arithmetic only.

## What is new, and what is still lost

The previous load argument used D<=sum_Z p and maximized each source
independently. The new family conditions on j and uses the sharper incoming
cap min(p,j-[u in J]), while retaining the weighted heavy incidence demand W.
This can prevent the high local costs assumed by the separate argument from
occurring together.

The pilot uses T=4h. Its ablations keep the same source domain, j cases,
incidence-demand term and existing source-capacity screen:

- `local`: lambda=mu=0;
- `aggregate`: incoming term p in place of min(p,j-e), with mu=0;
- `pair`: lambda=0;
- `joint`: the full statement above.

Failure to find a strict witness in a bounded search is not feasibility or a
graph construction. The comparison isolates the destination cap within this
search, not optimality over every possible potential or multiplier.

The model still forgets the individual arc allocation, the stronger endpoint
eligibility rho_destination+q_destination>=q_origin-1, label/supplement degree
compatibility, and correlations between different h thresholds. Those are
possible later refinements. This lemma does not improve the existing 7/12
maximum-degree theorem by itself or prove the unrestricted conjecture.

## A short new exclusion at h=3

The preserved N35 306-edge state 6 has

`s=(1,2,3,3,4^11)`, `rho=(1^8,2,3,4^9)`.

Take h=3,T=12. Then W=50, G=156, r=49 and z=10. The eligible source
capacities are 2,11^9, with incoming caps 6,7^9. The specified-j capacity
bounds, for j=0,...,9, are

`29,35,40,44,47,49,50,50,49,47`.

Only j=6 and j=7 remain. In both cases use mu=0:

| j | lambda | eta | denominator | scaled A for the capacity-2 source | scaled A(0), A(1) for each capacity-11 source | scaled hG | scaled U_j |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 6 | 28/5 | 43/10 | 10 | 562 | 645, 469 | 4,680 | 4,631 |
| 7 | 5 | 3 | 1 | 50 | 59, 42 | 468 | 459 |

For example, the first upper bound is
`10*3*49 + 562 + 9*645 + 6*(469-645) - 43*50 = 4631`.
Both remaining j values contradict the required lower bound. The local
maxima in the table are checked over H=0,...,c and
p=0,...,min(P,b-1-H); the separate verifier uses step indicators and a
cardinality recurrence. This state passes all previous hand filters and the
previous heavy-load family. Its historical adaptive certificate is preserved.
