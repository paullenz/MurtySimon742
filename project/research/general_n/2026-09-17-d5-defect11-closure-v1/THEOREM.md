# Five-label defect eleven is impossible

**17 September 2026. Internal candidate theorem; external review and novelty open.**
Research directed by Paul Lenz. Derivation and implementations by ChatGPT/Geeps.

## Statement

Retain the actual selected-representative system and the whole exact block

    |T|=|H|=5,
    D=L+beta+2mu

from the checked five-label support-cover theorem. Then

    D >= 12.

Consequently

    W >= 5+4m+12 >= 37,

and if there is an extra high-source selection, m>=10 and therefore

    W >= 57.

This is still an exact-block theorem. Exact-block existence/coverage for arbitrary counterexamples, sharpness, novelty and independent acceptance remain open. No catalogue result is promoted.

## 1. What equality at eleven would force

For every nonempty tight support S subseteq T define the predecessor cost

    c(S)=max(0,4-|S|).

The checked support-cover theorem proves that criticality and pair coverage give

    D=2mu+L+beta >= 2mu+tau(Q) >= 11,

where tau(Q) is the minimum c-cost of supports whose threat sets cover E(Q).

Assume D=11. Every inequality in this chain is then equality. In particular Q must be one of the 25 auxiliary minimizers found by the preceding exhaustive calculation:

- 10 labelled copies of K5 minus one edge, with mu=1 and tau=9;
- 15 labelled graphs with two missing edges forming a matching, with mu=2 and tau=7.

Equality also removes every source of slack between actual defect and c-cost.

For k in K, let S_k=N_G(k) intersect T and l_k=w_k-|S_k|. If k has zero demand and S_k is non-full, then

    l_k=5-|S_k|=c(S_k)+1,

which would make the actual defect strictly exceed the auxiliary c-cost. Therefore every non-full K-label used at D=11 has positive demand.

For x in O=B minus (H union V), its missing tight neighbours are residual incidences and contribute

    q_x=5-|S_x|

to beta. Whenever q_x>0 this is again c(S_x)+1. Equality therefore forces no residual tight incidence outside the full pools:

    beta=0.                                             (1)

After deleting duplicate or unused support types from the actual critical-edge cover, the remaining support family is a c-optimal cover of Q.

## 2. Every D=11 optimal cover needs a singleton support

The two new checkers independently refine the preceding 1024-graph dynamic programme. They minimize lexicographically

    (total c-cost, number of singleton supports).

Among all 25 graphs with 2mu+tau(Q)=11, the minimum number of singleton supports in any c-optimal cover is:

- 3 for K5 minus one edge;
- 1 for the two-missing-edge matching family.

Thus every putative D=11 realization contains a K-label k whose tight support is exactly

    S_k={t}.                                            (2)

It is a K-label rather than an O-vertex because beta=0, and it has positive demand by the equality observation above.

This singleton necessity can also be seen directly in the two degree types, but the exact finite calculation is retained to avoid hiding a case split.

## 3. Positive-demand singleton supports contradict residual-union

Let k satisfy (2) and s_k>0. Since x_k>=s_k, k has a selected occurrence (u,k)->v.

K is residual at every high vertex, so neither endpoint of this selected obligation can be high: k is not selected at a high source, and a high destination already contains k in J and therefore cannot be its exception. Hence u and v are low and

    |R_v|<=4.                                           (3)

At every low selected source of k, its tight F-neighbours are residual. Thus t is residual at u. By beta=0, every low residual occurrence of a tight label lies in one of the full receiver pools. Therefore

    u in V_r for some r!=t,
    R_u=T minus {r}.                                    (4)

In particular R_u contains no non-tight labels. The established residual-union implication for (u,k)->v is

    N_F(k) subseteq R_u union R_v.                      (5)

The support of k inside T has size one. Of the four labels in R_u, only t belongs to N_F(k). Equation (3) and (5) therefore give

    deg_F(k)=|N_F(k)| <= 1+4=5.                         (6)

But k is residual at all five high vertices, so the scalar residual count R_k is at least five. Positive demand means

    s_k=max(0,deg_F(k)-R_k)>0,

and hence deg_F(k)>=R_k+1>=6, contradicting (6).

Thus D=11 is impossible. Since the preceding theorem already gives D>=11 and D is integral, D>=12.

## 4. Verification

`check_d11_singletons.py` and `check_d11_singletons.cpp` independently enumerate all 1024 labelled tight graphs, all 31 nonempty supports and the exact support-cover dynamic programme. Their complete row streams agree byte-for-byte.

The shared row SHA256 is

    858941a3e47b59631433e61bd8ced65f6a9e7cb302a0de0281201e6074e0df77.

They find exactly 25 D=11 auxiliary graphs. Every c-optimal cover requires a singleton: three in the mu=1 family and one in the mu=2 matching family. This finite check verifies only the auxiliary classification. The residual-union contradiction is the hand argument above. Both implementations and the proof were written by the same assistant, not by independent external reviewers.

## 5. Next target

The new frontier is D=12. Unlike D=11, one unit of slack beyond the old support-cover minimum can permit residual tight incidence outside the full pools, so the beta=0 equality shortcut cannot simply be reused. The next unit should classify the D=12 support/row possibilities while tracking where singleton sources obtain their required residual tight occurrence. Exact-block coverage remains a separate essential gap.
