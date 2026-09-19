# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_T1_SHARED_CORE_RESOURCE_CONE_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `519c9c6f0b96f57bed36a314e4b715492e375a43`

LAST VERIFIED RESULT: `In the corrected m=g+1,t=1,k>=3,E=2 shared-core core-target family, put N=u-k-2 and e=e(X). The exact pair-local Hall/traffic gate and the rooted q/E_U/slot ceiling collapse to the same resource W(M,e)=M+e+[R0-kM-2e]_+, where R0=Nk+k^2+2kp-ky-k+p^2-py+p+y-2. Pair capacity gives W<=B_P=C0-sigma_P-p^2<=B0, while the rooted ledger gives 2(W+1_{e>0})<=Aroot. The exact minimum W_* over 0<=M<=N,0<=e<=k has a four-piece closed form. On the deep arm R0-kN>2k, equality is unique: M=N,e=k and hence J=0; near equality obeys (k-1)(N-M)+(k-e)<=s. Asymptotically, with k/p->kappa,N/p->alpha,y/p->beta, W_*/p^2->(kappa+1)(kappa+1-beta)_+ and pair/root budgets force an explicit resource cone. For k=o(p), every survivor has liminf N/p>=alpha0=1.017515183827867..., the unique root >1 of 3a^4+12a^3+8a^2-8a-16=0; the pinch has beta=0.265268763664312... and lambda/p=1.752246420163555.... Exact Ccap_P is already satisfied at the base P0 with strict leading-order margin in this fixed/sublinear-k tail, so sigma_P/p^2->P0/p^2. Therefore the predecessor zero-survivor bounded diagnostic does not extend to a global analytic closure: a sharply parameterized unmatched-heavy tail remains. The next attack must use its located physical U-nonedges / saturated X-star / rooted triangle and source-capacity geometry, not another loose scalar relaxation.`

UNPRESERVED WORK: `None at this checkpoint. The theorem note and independent arithmetic audit are preserved under project/research/post_ms/2026-09-19-shared-core-resource-cone-v1/. The predecessor fixed-foot target-injectivity theorem remains load-bearing; its bounded zero-survivor result is retained as a diagnostic only and is not extrapolated globally.`

DEFERRED ADMIN: `README remains synchronized to the 19 September daily audit trust boundary and need not be rewritten for every mathematical checkpoint. Refresh reviewer-facing status at the next daily adversarial checkpoint unless repository integrity requires earlier repair.`

NEXT ACTION: `Stay on the surviving shared-core tail before opening other E2 topologies. Use the deep-arm stability to feed the physically located geometry M≈N,e(X)≈k,J≈0 into the exact rooted residual identity delta=r-e(F), the rooted triangle count q, E_U, and the finite source-tuple/beta-capacity theorem. In exact deep equality use q<=(N^2+2Nk+N+2)/2 and the fact that z_* misses every one of the N remaining outside-U vertices. Seek either an analytic contradiction for the unmatched-heavy cone or a still sharper structural equality family. Only after this tail is closed or cleanly parameterized should one-core R2+R2 and core-containing R3 be opened. Keep k=2,k=1,m=g+2,loaded buffer,z=2,and the four-exception gate deferred. Keep X_3 and the graph-level audit boundary explicit.`
<!-- CURRENT-STATUS:END -->

---

## 1. Mandatory audit gate

This run began by rereading `CURRENT_STATE.md`, root `README.md`, the latest commit chain through `519c9c6f0b96f57bed36a314e4b715492e375a43`, the 19 September daily adversarial audit, `SOURCE_PREMISE_REPAIR.md`, the actual-D2C graph-level regression status, and the fixed-foot target-injectivity handoff before forward mathematics.

Binding trust boundary:

- distinct physical beta-source identity: raw-criticality proved;
- `(source,coordinate)` uniqueness: selected representative only;
- finite source-tuple theorem: not unconditional graph-level closure;
- actual-D2C regression: 3,540 root-policy instances, 147 exact pair-capacity checks, 36 Hall decompositions, zero recorded mismatches, `X_3` retained;
- no bounded actual D2C fixture realizes the full rigid complete-cut hypotheses, so the live branch remains conditional hand mathematics;
- exact pair-local `S_P/Ccap_P` remains mandatory;
- four-exception gate remains subordinate.

There is no departure from the audit priority order. The predecessor asked first for an analytic treatment of the corrected shared-core pair gate and, if a tail survived, for that tail to be fed into the rooted residual geometry rather than hidden by more scalar relaxations. This checkpoint does exactly that.

---

## 2. Exact shared-core coordinates and one resource

Stay in `m=g+1,t=1,k>=3,E=2`, corrected shared-core `R2+R2`, core-target orientation. Then

`g=p-1`, `x=p+k-1`, `N=u-k-2`, `u=N+k+2`, `lambda=N+p+2-y`,

and `N>=p-1`.

The predecessor gives `A=g`, star-forest `G[X]`, isolated radius-two defects, core X-degree at most one, and

`J+e(X)<=k`.

Write `e=e(X)` and

`R0=Nk+k^2+2kp-ky-k+p^2-py+p+y-2`.

The Hall bill is

`L_X >= [R0-kM-2e]_+`.

Define

`W(M,e)=M+e+[R0-kM-2e]_+`.

The exact pair-local gate is

`W(M,e)<=B_P=C0-sigma_P-p^2`.

Since `sigma_P>=P0`, `P0=k(p+k)+1+y(p+2)`, also `W<=B0=C0-P0-p^2`.

With `epsilon=lambda mod 2`,

`2B0=N^2+2Nk+2Np+6N-epsilon-2k^2-2ky+8k-p^2-2py+8p-y^2-2y-2`.

The rooted q/E_U ceiling together with the star slot floor prices exactly the same resource:

`2(W+1_{e>0})<=Aroot`,

`Aroot=2Nk+2Ny+N-epsilon+2kp+2k+p^2+2p-y^2-2y-8`.

This common-resource reduction is the main algebraic synthesis of the checkpoint.

---

## 3. Exact W minimizer

Let `W_*` be the minimum over `0<=M<=N,0<=e<=k`. Then for `k>=3`:

- `W_*=0` for `R0<=0`;
- `W_*=ceil(R0/k)` for `0<R0<=kN`;
- `W_*=N+ceil((R0-kN)/2)` for `kN<R0<=kN+2k`;
- `W_*=N+R0-kN-k` for `R0>=kN+2k`.

Every shared-core survivor therefore satisfies

`W_*<=B_P<=B0`,

`2W_*<=Aroot`.

The companion checker brute-forces this exact minimization independently.

---

## 4. Deep-arm equality and stability

Put

`r_N=R0-kN=k^2+2kp-ky-k+p^2-py+p+y-2`.

If `r_N>2k`, then

`W-W_*=(k-1)(N-M)+(k-e)`.

Hence exact equality uniquely forces

`M=N`, `e(X)=k`, `J=0`.

This is physically meaningful: the common outside witness misses all `N` remaining outside-U vertices and the X-star consumes every core leaf.

At exact equality,

`q <= (N^2+2Nk+N+2)/2`.

If resource slack above the optimum is at most `s`, then

`(k-1)(N-M)+(k-e)<=s`,

so `N-M<=floor(s/(k-1))`, `k-e<=s`, and `J<=s`.

---

## 5. Asymptotic resource cone

For a convergent survivor sequence with

`k/p->kappa`, `N/p->alpha`, `y/p->beta`,

we have `alpha>=1` and

`W_*/p^2 -> w=(kappa+1)(kappa+1-beta)_+`,

`B0/p^2 -> b=(alpha^2+2alpha*kappa+2alpha-2kappa*beta-1-2beta-beta^2)/2`,

`Aroot/(2p^2) -> h=(2alpha*kappa+2alpha*beta+2kappa+1-beta^2)/2`.

Necessary conditions are `w<=b` and `w<=h`.

For `beta<kappa+1`, this gives

`beta^2<=alpha^2+2alpha*kappa+2alpha-2kappa^2-4kappa-3`,

and

`beta^2-2(alpha+kappa+1)beta+(2kappa^2+2kappa+1-2alpha*kappa)<=0`.

Equivalently beta lies between

`alpha+kappa+1-sqrt(alpha^2+4alpha*kappa+2alpha-kappa^2)`

and

`sqrt(alpha^2+2alpha*kappa+2alpha-2kappa^2-4kappa-3)`.

Pair capacity alone already yields the safe reservoir gap

`alpha>=sqrt(3kappa^2+6kappa+4)-(kappa+1)`.

---

## 6. Fixed/sublinear-k pinch

For `k=o(p)` the cone is

`alpha+1-sqrt(alpha^2+2alpha)<=beta<=sqrt((alpha-1)(alpha+3))`.

The two curves first meet at

`alpha0=1.017515183827867...`,

the unique root greater than one of

`3alpha^4+12alpha^3+8alpha^2-8alpha-16=0`.

At the pinch,

`beta0=0.265268763664312...`,

`lambda/p=1.752246420163555...`.

If `beta>=1`, pair capacity gives the stronger `alpha>=sqrt(5)-1`. Therefore any fixed/sublinear-k shared-core asymptotic survivor satisfies

`liminf N/p>=1.017515183827867...`,

and likewise `liminf u/p>=1.017515183827867...`.

This is a real structural imbalance theorem inside the conditional branch, not a global closure.

---

## 7. Exact pair-capacity audit

The exact `Ccap_P` obligation was retained rather than discarded. In the fixed/sublinear-k tail,

`P0/p^2->beta`,

`lambda/p->alpha+1-beta`,

and the pair-radius density at `P0` is

`(d+sqrt(d^2+12beta))/3`, where `d=2+2alpha+3beta`.

Since `alpha>=1`, this is strictly larger than the crossing target density contribution `2beta`, and the remaining capacity multiplier is at least one. Thus exact crossing capacity already holds at `P0` with strict leading-order margin:

`sigma_P/p^2->beta=P0/p^2`.

Therefore the surviving asymptotic tail is not an artifact of replacing exact `Ccap_P` by a loose score budget.

---

## 8. Independent arithmetic audit

Preserved checker:

`project/research/post_ms/2026-09-19-shared-core-resource-cone-v1/check_shared_core_resource_cone.py`

It independently verifies:

- 13,176 exact coordinate/parity identities;
- 45,300 root same-resource rearrangements;
- 28,350 brute-force instances of the closed `W_*` formula;
- the `alpha0` quartic root to numerical tolerance;
- finite `k=3` weak pair/root minima approaching the predicted pinch: `N/p=1.02,1.015,1.018,1.017` at `p=100,200,500,1000`.

This is an arithmetic audit of conditional inequalities only, not graph-realizability evidence.

---

## 9. Corrected interpretation and next work

The predecessor bounded box had zero corrected shared-core survivors, but the full analytic treatment shows that this cannot be promoted to a global closure. An unmatched-heavy asymptotic cone remains.

That negative result is useful: another pair/global score inequality is not the right next move. The surviving tail is physically rigid, especially on the deep arm, where near equality forces `M≈N`, `e≈k`, `J≈0`.

The next attack is to combine those located U-nonedges and X-star edges with:

1. the exact rooted triangle count `q` and residual identity `delta=r-e(F)`;
2. the finite source-tuple/beta-capacity theorem at its repaired trust boundary;
3. raw criticality of the many specific `z_*--U_o` nonedges.

Only after this shared-core tail is closed or sharply classified should the tied one-core `R2+R2` and core-containing `R3` alternatives be opened.
