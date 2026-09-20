# Residual-one k=2 nonhub cross-code U--U edge localization

Date: 2026-09-20

Status: **same-session raw re-derivation plus accounting correction**, conditional on the rooted coded-layer setup and `J2=empty`. This deliberately derives the needed statement from rooted B-edge criticality rather than extrapolating the same-code theorem. No finite scan is used.

This note materially strengthens the preceding code-class independence result. At the all-radius-one endpoint, two q_j-nonneighbour U-vertices with proper private supports cannot be adjacent **even when their codes are different**.

## 1. General rooted U--U edge complement requirement

Take an edge `wt` with `w,t in U`. Since both lie in the rooted B-neighbourhood, the root is a common neighbour of w and t. Thus deleting wt cannot make the pair w,t itself have distance greater than two. Raw D2C edge criticality must use one of the two singleton orientations, say

`N(w) cap N(a)={t}`                                      `(CE-OR)`

with the witness `a` outside the rooted B-layer. A witness inside B would share the root with w, giving an additional common neighbour distinct from t. Hence `a in A`.

Now inspect the p tight matched fibres. The singleton head t lies in U, not in a matched fibre. Therefore w and a can have **no common matched endpoint**. In the rigid coded layer, each code records which endpoint of every tight pair is seen. Zero common matched endpoints is equivalent to coordinatewise complementarity:

> **`c(a)=bar(c(w))`.**                                   `(CE-COMP)`

If the opposite orientation is used, the symmetric conclusion is `c(a)=bar(c(t))`.

Therefore every U--U edge satisfies the necessary condition

> **`wt in E(U)` implies `A_{bar(c(w))}!=empty` or `A_{bar(c(t))}!=empty`.** `(CE-GEN)`

This argument does not assume `c(w)=c(t)`. The familiar same-code U--U theorem is the diagonal special case.

## 2. Complement repertoire at `J2=empty`

At residual dimension one with all matched heads radius one, the complete A-code repertoire relative to d is

- `d` on Y;
- `d xor e_j` on K;
- `d xor e_i` on h_i, `i in I`.

Take a q_j-nonneighbour U-vertex w. Write

`c(w)=d xor S`, `S subseteq I`.

Its complementary code has support relative to d

`{j} union (I\S)`.

Because this support contains j, it belongs to the A-code repertoire **only** when it is exactly `{j}`. Hence

> **`A_{bar(c(w))}!=empty` iff `S=I`.**                  `(CE-REP)`

So among q_j-nonneighbours, the only code whose complement is represented in A is the full-private-support code `d xor I=bar C`, complemented by the K-code C.

## 3. All proper-support q_j-nonneighbours form one independent set

Let

`P={w in U : wq_j notin E and supp(c(w) xor d) proper subset I}`.

For any two vertices `w,t in P`, both complementary A-code classes are empty by `(CE-REP)`. The general edge necessity `(CE-GEN)` therefore forbids wt.

> **`G[P]` is independent.**                             `(CE-IND)`

This is strictly stronger than saying each individual proper-support code class is independent. Different sparse supports do not evade the obstruction.

Consequently, for any subset N of proper-support q_j-nonneighbours,

> **`M_U(N)>=binom(|N|,2)`.**                            `(CE-BILL)`

## 4. Impact on the sparse D1 endpoint

The preceding private-spoke theorem showed that any D1 sequence approaching the old R+D1 additive envelope has

- all but o(p) D1 vertices missing q_j;
- total private-support incidence `L=o(p^2)`.

A full support `S=I` has size `p-1`. Therefore `L=o(p^2)` permits only `o(p)` full-support D1 vertices. All but o(p) of the linear D1 population lie in P.

If the D1 density is beta, the new independent-set bill gives asymptotically

> **`M_U(D1) >= (beta^2/2-o(1))p^2`.**                   `(CE-D1)`

Thus the formerly permissive distinct-singleton-support model fails: changing the support code does not permit U--U adjacency when neither endpoint has a represented complementary A-code.

### Accounting caveat

`(CE-D1)` must **not** simply be added to the predecessor unweighted D-sector lower bound. The D-sector proof already converts the exact sector deficit into a lower bound containing `M_U`, and the same missing D1--D1 pairs can be part of that conversion. The new theorem is therefore primarily a **location theorem**: it forces a quadratic portion of the D1 defect specifically into missing U--U pairs.

That location matters because the exact rooted residual inequality weights `M_U` with coefficient two, whereas H--U and Y--U holes enter with coefficient one. Future optimization must retain this coefficient rather than treating `(CE-D1)` as an independent additive `D_phys` term.

## 5. Weighted strategic consequence

The current D1 optimizer should now be revisited in the exact weighted rooted ledger with the simultaneous constraints

- the exact D1 sector identity;
- `M_U(D1)>=binom(|P_D|,2)`, where `P_D` is the proper-support nonhub D1 population;
- the q_j-neighbour penalty from the weighted split theorem;
- the private-support-density penalty from the nonhub spoke theorem;
- the independent K-heavy conservation bill.

The structural effect is strong even before that optimization: any cheap linear D1 population is pushed toward q_j-nonneighbours and sparse support, but those same conditions make almost the whole D1 population an independent set in U. Thus its unavoidable quadratic defect is now **rooted-weighted in the expensive U-edge currency** rather than freely distributable among H/Y/U sectors.

The next exact calculation should ask whether this location change is enough to rule out the former `(7-sqrt(33))/8` coarse optimizer. If not, the minimizing weighted R:D1 geometry is the correct next raw-criticality target.

Global caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; the theorem is conditional on reaching the coded rigid interface.