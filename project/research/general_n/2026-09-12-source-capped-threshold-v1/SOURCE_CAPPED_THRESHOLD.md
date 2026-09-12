# Source-capped heavy-incidence capacity

12 September 2026. Research direction: Paul Lenz. Development and internal
audit: ChatGPT/Geeps. **Candidate universal bridge lemma; external review OPEN.**

Use the [canonical selected/residual bridge](../2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).
Fix an integer h>=1 and let

`I={i:s_i>=h}`, `W=sum_{i in I}s_i`, `Z={u:rho_u>=h}`, `z=|Z|`.

For each u in Z define the integer capacity

`c_u=min(a-rho_u, #{i:h<=s_i<=rho_u})`.

Put `L=sum_{u in Z}min(h,c_u)`. Sort the capacities strictly greater than h
as `c_(1)>=...>=c_(k)>h`, and let `P_j=sum_{i=1}^j c_(i)`, with P_0=0.
Then necessarily

`W <= max_{0<=j<=k} { L-jh+min(P_j, jz-j(j+1)/2) }`.       (1)

This refines the ordinary threshold capacity by retaining the individual
source capacities. Its finite maximum involves at most z+1 explicit integers;
no optimization solver is part of the statement or proof.

## Proof

Call an actual selected incidence heavy if its label lies in I, and let
ell_u count heavy incidences at u. Selected-incidence forcing puts every
heavy source in Z and requires its label's demand to be at most rho_u.
Distinct incidences at u use distinct labels. Also ell_u<=q_u<=a-rho_u.
Thus `ell_u<=c_u`, and the required label incidences give `W<=sum_Z ell_u`.

Let `J={u in Z:ell_u>h}` and j=|J|. Each member of J has c_u>h, so j<=k.
For u outside J, ell_u<=min(h,c_u). Since min(h,c_u)=h for u in J,

`sum_{u in Z\J}ell_u <= L-jh`.                            (2)

The sum over J is bounded by its source capacities, hence by P_j.
It also satisfies

`sum_{u in J}ell_u <= j(z-j)+binomial(j,2)`
`= jz-j(j+1)/2`.                                         (3)

For completeness, every heavy arc ui->w from a source with ell_u>h has
at least h other heavy labels k at u. The quasi-edge property forces each
kw to be an H-edge. If all these edges are residual, rho_w>=h. If any is
selected from w, its heavy label has demand at least h, again forcing
rho_w>=h. Therefore w lies in Z. Distinct selected arcs represent distinct
unordered missing B-pairs, so they use at most the pairs inside Z incident
with J, giving (3).

Combining (2) and (3) with the P_j bound gives (1) for the actual j. Taking
the maximum over every allowable j proves the statement. QED.

The proof does not assume equal residual degrees, that every source is
heavy, or that total selected outdegree equals heavy outdegree. It remains
valid with zero-demand labels, since only labels in I are counted.

## A small explicit N34 example

At `(a,b,t)=(15,18,1)`, consider

`s=(2^11,4^4)`, `rho=(1^9,2^4,3,4^4)`.

At h=3, W=16 and Z consists of one degree-three and four degree-four
sources. Their capacities are `0,4,4,4,4`, so L=12 and P_j=4j.
The five bounds in (1), for j=0,...,4, are `12,13,13,12,10`.
Thus W<=13, contradicting W=16. This is an elementary hand exclusion.

## Zero-deficit extension of exact-budget envelopes

The [exact demand-deficit identity](../2026-09-12-exact-budget-threshold-v1/BRIDGE_REFINEMENTS.md)
states

`E=S-r-2t=sum_{s_i=0}(R_i-d_i)`.

Each summand is nonnegative. If E=0, every zero-demand label has d_i=R_i,
regardless of the number of zero labels. Thus the earlier envelope domain
extends safely from at most one zero label to **E=0 or at most one zero
label**. If E>0 and more than one zero label is present, their shared deficit
must be allocated explicitly; this shortcut is not applicable.

The N34 equality sweep checks that domain condition state by state. Both
extensions here are universal consequences of the existing bridge; their
complete application to a fixed-order frontier remains finite arithmetic.
