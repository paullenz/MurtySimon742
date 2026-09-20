# Residual-one k=2 quadratic-defect coefficient and weighted-ledger gap

Date: 2026-09-20

Status: **same-session candidate synthesis / stop-pivot note**, conditional on the preceding five-class theorem. The asymptotic optimization is analytic; no finite scan is used.

The global defect theorem proved only a coarse pigeonhole coefficient. Because all five class bounds live inside the same nonnegative physical functional

`D_phys=E_U+Z_X+Z_Y+M_U`,

one can optimize the five lower bounds simultaneously and get a substantially sharper asymptotic constant. The result still does **not** close the exact low-k ray against the present rooted/score ceilings; that failure identifies the next required step precisely.

## 1. Five simultaneous lower bounds

Write the five escape-class sizes as

`r+d+f1+s+m=p-1`,

for K-heavy, W_s-free non-K-heavy, one-W_s K-free, W-heavy, and mixed vertices respectively.

The preceding theorem gives

`D_phys >= r(r-1)/3`,

`D_phys >= d(p-2)/2`,

`D_phys >= f1(p-1)`,

`D_phys >= s(p-1)`,

`D_phys >= m(p+1)`.                                      `(WL-5)`

These are simultaneous inequalities; they are not being added, so no overlap issue arises.

Normalize

`alpha=r/p`, `beta=d/p`, `gamma=f1/p`, `sigma=s/p`, `mu=m/p`.

Along any unbounded sequence, their sum tends to one. If

`D_phys <= (T+o(1))p^2`,

then `(WL-5)` forces asymptotically

`alpha <= sqrt(3T)`,

`beta <= 2T`,

`gamma,sigma,mu <= T`.

Therefore a necessary condition for the five classes to sum to one is

> `sqrt(3T)+5T >= 1`.                                    `(WL-CAP)`

The equality equation has the positive solution

> **`tau=(13-sqrt(69))/50 = 0.0938675227...`.**           `(WL-TAU)`

Hence

> **`liminf D_phys/p^2 >= tau`.**                         `(WL-MAIN)`

So the physical quadratic defect is not merely nonzero: every hypothetical realization of the exact low-k ray must spend at least about **9.39% of p^2** in total U-slack / X--U holes / Y--U holes / missing U--U pairs, before any further raw-criticality refinement.

The extremal mixture for this coarse max-optimization is characterized by saturation of the five capacities:

`alpha=sqrt(3 tau)`,

`beta=2 tau`,

`gamma=sigma=mu=tau`.

Thus the coarse minimizing picture is genuinely mixed across all five classes rather than concentrated in one endpoint. This is useful strategic information: a proof that eliminates or materially raises the cost of even one of the three linear-price classes changes the asymptotic minimum immediately.

## 2. Exact rooted and score ceilings still permit this amount of defect

The preserved score inequality is

`E_U+L_A <= C0`.                                         `(WL-SCORE)`

The preserved exact rooted identity can be written as

`Z+L_A <= u(p-lambda)+2e(U)+C0`,                         `(WL-ROOT0)`

where `Z=Z_X+Z_Y`.

With

`M_U=binom(u,2)-e(U)`,

this becomes

> `Z+L_A+2M_U`
> `<=u(p-lambda)+2binom(u,2)+C0`.                        `(WL-ROOT)`

On the exact low-k ray, `p=lambda` and `u=p+1`, so

`Z+L_A+2M_U <= p(p+1)+C0`.                              `(WL-RAY-ROOT)`

Adding `(WL-SCORE)` gives the safe combined ceiling

> `E_U+Z+2M_U+2L_A <= p(p+1)+2C0`.                       `(WL-COMB)`

Since

`C0=floor((3p^2+10p-4)/2)`,

the right side has leading coefficient 4 in p^2. The new lower bound `(WL-MAIN)` has coefficient only about 0.09387 in the coarsened functional. Therefore the mere fact of a quadratic physical defect is **not yet enough** to contradict the current scalar/rooted ceilings.

This is a genuine method boundary, not a negative mathematical result. The problem is now coefficient/location, not order of growth.

## 3. What the next optimization must retain

The next step should not strengthen `D_phys` as an undifferentiated total. It must use the fact that the five classes spend their defect in very different currencies:

- mixed vertices spend directly in `E_U`, hitting the score ceiling with coefficient one;
- F1 and W-heavy vertices spend primarily in `Z_Y`;
- W_s-free non-K-heavy vertices split a forced sector deficit among `Z_X`, `Z_Y`, and `M_U`, with `M_U` carrying coefficient two in the rooted identity;
- K-heavy vertices obey the sharper coupled inequality
  `3E_R+2E_F+3A+yq>=r(r-1)`, not merely the coarsened `D_phys>=r(r-1)/3`;
- X-anticomplete repair witnesses place an entire block into `Z_X`.

A weighted partition optimization using `(WL-SCORE)` and `(WL-ROOT)` simultaneously should therefore improve dramatically over `(WL-MAIN)`. The variables to retain are at minimum

`(r,d,f1,s,m; E_R,E_F,A,q; Z_X^D,Z_Y^D,M_U^D)`.

If that weighted program still has an asymptotic feasible point, its minimizing class proportions are the next literal geometry for raw-criticality attack. If it does not, the exact low-k ray becomes finite-order.

## 4. Stop/pivot conclusion

The current session has therefore moved the live question from

> “can the escape reservoir remain only linearly expensive?”

which is now answered **no**, to

> “can roughly 9.4% p^2 or more of mandatory physical defect be placed in the four rooted/score currencies with the exact allowed coefficients?”

That is the correct next calculation. Further unweighted scalar inequalities would discard the information just obtained.

Global caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; all conclusions remain conditional downstream mathematics pending hostile replay.