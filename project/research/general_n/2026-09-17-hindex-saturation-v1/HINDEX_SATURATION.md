# Residual h-index saturation and the exact-block equality face

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal hand theorem; not promoted; external review and novelty open.** This is a scope-bridging result. It does not assume the five-label block and does not claim that every unresolved graph lies on the equality face.

## Statement

Use the general residual setup of `project/research/general_n/2026-09-07-residual-hindex-v1/README.md`. Thus A has size a, B has size b, t=m-b(n-b)>0 is the edge surplus, r is the total residual cross count, rho_u is the residual degree of a B-source, and

    s_i=max(0,d_i-R_i)

is the demand of an A-label. Positive surplus gives rho_u>=1 for every u in B. Let h be the residual h-index,

    h=max{q : at least q vertices u have rho_u>=q}.

Write

    |{u:rho_u>=h}|=h+u,
    k=|{i:s_i=h}|.

Then

    b+2t <= (a-h-u)(h-1)+k                         (S)

or, equivalently, relative to the preceding coarse h-index bound,

    b+2t <= (a+1)h-h^2 - [a-k+u(h-1)].             (S')

Thus the older scalar inequality has an explicit stability loss: one unit for every A-label below maximum demand, plus h-1 units for every residual source beyond the h-index threshold.

If u=0, then necessarily

    k<=h.                                            (R)

Consequently the exact square block

    |H_h|=h, |T_h|=h

is the unique maximum-demand equality face once the high-source threshold itself is saturated. More precisely, when u=0,

    b+2t <= (a-h)(h-1)+h-(h-k).                     (E)

So a non-square level k<h loses at least one further unit.

## Proof of the stability inequality

The preceding selected-edge injection gives s_i<=h for every label: a label with demand q>0 needs at least q selected sources of residual degree at least q, so q cannot exceed the residual h-index.

Only k labels attain h. Therefore

    sum_i s_i <= kh+(a-k)(h-1)=a(h-1)+k.             (1)

The exact residual ledger is

    r+2t=sum_i(d_i-R_i)<=sum_i s_i.                  (2)

There are h+u B-vertices of residual degree at least h, while every remaining B-vertex has residual degree at least one by positive-surplus activity. Hence

    r>=h(h+u)+(b-h-u)
     =b+h(h-1)+u(h-1).                               (3)

Combining (1)--(3) yields

    b+h(h-1)+u(h-1)+2t <= a(h-1)+k,

which is (S). Expanding the old quadratic `(a+1)h-h^2` gives (S'). No graph realization or finite enumeration is used.

## Why source saturation forces k<=h

Assume u=0, so H_h={u:rho_u>=h} has exactly h vertices. Every label i with s_i=h requires at least h distinct selected sources, and eligibility restricts all of them to H_h. Thus every high source selects every one of the k maximum-demand labels.

Fix a high source x and one such label i, and consider its selected obligation `(x,i)->v`. The destination v cannot lie in H_h: every high vertex selects i, whereas a destination must omit i from its selected/residual neighbourhood. Hence rho_v<h.

All other k-1 maximum-demand labels selected at x must be present at v by forward containment. Since rho_v<h, eligibility prevents v from selecting a demand-h label. Therefore all k-1 are residual at v, so

    k-1 <= rho_v <= h-1.

This proves k<=h. Equality k=h is exactly the whole square block used by the current exact-block theory.

## Operational corollaries

Let

    sigma=((a+1)h-h^2)-(b+2t)

be the slack in the old h-index inequality. Then every realization satisfies

    sigma >= a-k+u(h-1).                              (4)

Hence:

- if sigma<h-1, the high-source level is forced saturated: u=0;
- once u=0 is known, sigma>=a-h; equality sigma=a-h forces k=h and therefore the exact square block;
- with u=0 but k<h, sigma>=a-h+1.

For h=5 and u=0, the sharp source-saturated bound is

    b+2t <= 4(a-5)+k <= 4a-15,

and the top value 4a-15 forces k=5. The non-square case k<=4 is bounded by 4a-16.

These statements do not say that u=0 always holds. The remaining scope problem is now explicit: control the excess-high-source branch u>0, or prove that the relevant dense frontier has insufficient h-index slack to support it.

## Relation to the five-label theorem

When h=5, u=0 and k=5, the hypotheses are exactly

    |H|=|T|=5.

The current five-label treatment can then be invoked; as of commit `dca77e87652a79b655dc7c6473973c19dfceab24` it gives D>=12. Thus the unrestricted programme can be separated cleanly into two tasks:

1. force or approach the saturated h-index equality face using (S);
2. apply the increasingly strong exact-block criticality theory on that face.

This is a structural bridge, not a claim that task 1 is complete.
