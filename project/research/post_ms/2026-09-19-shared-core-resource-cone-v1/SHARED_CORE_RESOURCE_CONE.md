# Shared-core resource collapse and asymptotic imbalance cone

Date: 2026-09-19

Status: internal conditional mathematics inside the audited rigid one-code / positive-buffer / minimal-reservoir branch. This note does **not** assert graph realizability, the false all-order 2019 Dailly–Foucaud–Hansberg conjecture, or a global eventual theorem. The order-12 graph `X_3` remains a mandatory negative control.

## 1. Audit reconciliation

Before forward mathematics this run reread `CURRENT_STATE.md`, the root `README.md`, the latest commits through `519c9c6f0b96f57bed36a314e4b715492e375a43`, the 19 September daily adversarial audit, `SOURCE_PREMISE_REPAIR.md`, the actual-D2C graph-level regression status, and the fixed-foot target-injectivity handoff.

The binding trust boundary remains unchanged:

- distinct physical beta-source identity is accepted only at the raw singleton-criticality level proved in the repair note;
- `(source,coordinate)` uniqueness means selected-representative uniqueness, not raw-witness uniqueness;
- the finite source-tuple capacity theorem is not unconditional graph-level closure;
- the actual-D2C regression retains `X_3`, reports zero recorded graph/formula mismatches, and still has no positive bounded fixture realizing all rigid complete-cut hypotheses;
- exact pair-local `S_P/Ccap_P` remains mandatory; `(ONE-P)` and `(CROWD)` are used only where already proved dominated by stronger physical bills;
- the four-exception gate remains subordinate.

There is no departure from the audit priority order. The predecessor explicitly asked whether the corrected shared-core family can be analytically closed by the exact pair gate, and if not to parameterize the surviving asymptotic family and feed it back through the rooted residual ledger. That is exactly the work below.

## 2. Exact shared-core coordinates

Stay in the corrected shared-core `t=1,E=2,k>=3` branch from the fixed-foot theorem. Thus

- `g=p-1`;
- `x=g+k=p+k-1`;
- `m=g+1=p` in the minimal outside-reservoir notation;
- the common witness is anticomplete to all `H_M`, so `A=g`;
- `G[X]` is a star forest with the two radius-two defects isolated, core leaves of degree at most one, and `J+e(X)<=k`.

Write

`N:=u-k-2`.

Since `a=2p+u-lambda-1`, `y=a-x`, we have the exact coordinate conversion

`u=N+k+2`,

`y=N-lambda+p+2`,

and equivalently

`lambda=N+p+2-y`.

The feasibility inherited from the minimal reservoir gives `N>=g=p-1`.

Put `e=e(X)` and

`Emax=binom(p-1,2)+k(p-1)`.

The predecessor's exact pair-local inequality is

`p^2+M+e+[D+2(Emax-e)]_+ <= C0-sigma_P`,

where `0<=M<=N`, `0<=e<=k`, and `sigma_P` is the least pair-local score satisfying exact `Ccap_P`.

## 3. Unit I — one common resource currency

After substituting `g=p-1`, `x=p+k-1`, `u=N+k+2` and `lambda=N+p+2-y`, the Hall residual at `M=0` plus the maximum internal-X correction simplifies to

`R0 := D(M=0)+2Emax`

`= Nk+k^2+2kp-ky-k+p^2-py+p+y-2`.

For general `M,e`, the Hall payment is exactly bounded by

`L_X >= [R0-kM-2e]_+`.

Thus define the single physical resource function

> **`W(M,e):=M+e+[R0-kM-2e]_+`.**

The exact pair gate becomes

> **`W(M,e) <= B_P := C0-sigma_P-p^2`.**

Since `sigma_P>=P0`, where

`P0=k(p+k)+1+y(p+2)`, 

we also have the weaker explicit budget

`W(M,e)<=B0:=C0-P0-p^2`.

Writing `epsilon=lambda mod 2`, exact substitution gives

> **`2B0 = N^2+2Nk+2Np+6N-epsilon -2k^2-2ky+8k -p^2-2py+8p-y^2-2y-2`.**

Now feed the same geometry into the rooted physical ceiling. Combining the exact rooted identity, the physical `q`/`E_U` upper bounds already preserved in the branch, and the safe star-forest slot floor gives

> **`2(W(M,e)+1_{e>0}) <= Aroot`,**

where

> **`Aroot = 2Nk+2Ny+N-epsilon +2kp+2k+p^2+2p-y^2-2y-8`.**

This is the useful synthesis: pair score and rooted triangle/residual capacity price the **same** resource `W`, rather than producing unrelated scalar relaxations.

In particular every survivor satisfies the safe indicator-free pair of necessary conditions

`W(M,e)<=B_P<=B0`,

`2W(M,e)<=Aroot`.

## 4. Unit II — exact closed minimizer for W

Let

`W_*:=min_{0<=M<=N, 0<=e<=k} W(M,e)`.

For `k>=3`, direct integer minimization gives the exact four-piece formula

> **`W_*=0` if `R0<=0`;**
>
> **`W_*=ceil(R0/k)` if `0<R0<=kN`;**
>
> **`W_*=N+ceil((R0-kN)/2)` if `kN<R0<=kN+2k`;**
>
> **`W_*=N+R0-kN-k` if `R0>=kN+2k`.**

The companion checker brute-forces this formula over a large integer box.

Hence the entire shared-core family obeys the parameter-only necessary conditions

> **`W_*<=B_P<=B0`,**
>
> **`2W_*<=Aroot`.**

Unlike the previous bounded scan, these inequalities apply over the full integer parameter range of the conditional shared-core branch.

## 5. Unit III — deep-arm equality and stability

Define the residual after saturating the outside-defect variable,

`r_N:=R0-kN`

`=k^2+2kp-ky-k+p^2-py+p+y-2`.

Suppose `r_N>2k`. Then even at `M=N,e=k` the positive-part argument remains positive, so throughout the admissible rectangle

`W(M,e)=R0-(k-1)M-e`.

Therefore

> **`W-W_*=(k-1)(N-M)+(k-e)`.**

In particular the exact minimizer is unique:

> **`M=N`, `e(X)=k`.**

By the predecessor conservation law `J+e(X)<=k`, exact equality also forces

> **`J=0`.**

So the deep-arm equality geometry is physically located:

- the common outside witness misses all `N` remaining outside-U vertices;
- the X-star uses all `k` core leaves;
- there is no selected wrong-head traffic.

At this equality geometry the rooted triangle ceiling simplifies to

> **`q <= (N^2+2Nk+N+2)/2`.**

There is also exact stability. If the available resource budget lies at most `s` above `W_*`, then

> **`(k-1)(N-M)+(k-e)<=s`.**

Consequently

`N-M<=floor(s/(k-1))`,

`k-e<=s`,

and, using `J+e<=k`,

`J<=s`.

Thus near equality forces almost all of the remaining U-reservoir to be physically nonadjacent to the common witness and almost all core heads to be consumed by X-edges.

## 6. Unit IV — asymptotic resource cone

Consider any sequence of conditional shared-core survivors with `p->infinity` and finite limits

`k/p -> kappa>=0`,

`N/p -> alpha`,

`y/p -> beta`.

Because `N>=p-1`, necessarily `alpha>=1`.

The exact minimizer has the limit

> **`W_*/p^2 -> w=(kappa+1)(kappa+1-beta)_+`.**

The weak exact pair budget has limit

> **`B0/p^2 -> b=(alpha^2+2alpha*kappa+2alpha-2kappa*beta-1-2beta-beta^2)/2`.**

The rooted budget has limit

> **`Aroot/(2p^2) -> h=(2alpha*kappa+2alpha*beta+2kappa+1-beta^2)/2`.**

Therefore every such asymptotic survivor must satisfy

> **`w<=b` and `w<=h`.**

This is the shared-core pair/root resource cone.

## 7. Unit V — explicit beta interval and unmatched-reservoir gap

In the nontrivial regime `beta<kappa+1`, the pair condition simplifies exactly to

> **`beta^2 <= alpha^2+2alpha*kappa+2alpha-2kappa^2-4kappa-3`.**

The rooted condition becomes

> **`beta^2-2(alpha+kappa+1)beta +(2kappa^2+2kappa+1-2alpha*kappa)<=0`.**

Thus beta lies in the explicit interval

> **`rho(alpha,kappa) <= beta <= U(alpha,kappa)`,**

where

`rho(alpha,kappa)=alpha+kappa+1-sqrt(alpha^2+4alpha*kappa+2alpha-kappa^2)`,

`U(alpha,kappa)=sqrt(alpha^2+2alpha*kappa+2alpha-2kappa^2-4kappa-3)`.

Already the pair side implies the asymptotic unmatched-reservoir lower bound

> **`alpha >= sqrt(3kappa^2+6kappa+4)-(kappa+1)`**

whenever `beta<kappa+1`.

If `beta>=kappa+1`, evaluating the pair condition at its smallest possible beta gives the stronger lower bound based on `sqrt(4kappa^2+8kappa+5)`, so the displayed lower bound is globally safe.

For small positive `kappa`, the safe bound expands as

`alpha >= 1+kappa/2+O(kappa^2)`.

Thus the shared-core family cannot remain in a balanced `N~p` regime once the core surplus has positive density.

## 8. Unit VI — fixed/sublinear-k imbalance constant

For `k=o(p)`, so `kappa=0`, the nontrivial cone becomes

`alpha+1-sqrt(alpha^2+2alpha) <= beta <= sqrt((alpha-1)(alpha+3))`.

The two boundary curves first meet at

> **`alpha0 = 1.017515183827867...`,**

where `alpha0` is the unique real root greater than one of

> **`3 alpha^4+12 alpha^3+8 alpha^2-8 alpha-16=0`.**

At the pinch,

`beta0 = 0.265268763664312...`,

and therefore

`lambda/p -> alpha0+1-beta0 = 1.752246420163555...`.

If instead `beta>=1`, the pair inequality alone yields the stronger `alpha>=sqrt(5)-1`. Hence every fixed- or sublinear-k asymptotic shared-core survivor satisfies the clean unconditional branch consequence

> **`liminf N/p >= 1.017515183827867...`.**

Since `u=N+k+2`, the same statement is

> **`liminf u/p >= 1.017515183827867...`**

for `k=o(p)`.

This is an asymptotic structural obstruction, not a closure: a sufficiently unmatched-heavy tail remains analytically possible.

## 9. Unit VII — exact Ccap_P is asymptotically base-saturated in the fixed-k tail

The audit requires exact pair-local `Ccap_P`, so the preceding cone must not be justified by silently replacing `sigma_P` with `P0` where that replacement changes the leading order.

For `k=o(p)` and finite `alpha,beta`, at the base pair score

`P0/p^2 -> beta`.

Also

`lambda/p -> ell=alpha+1-beta`,

and the code-diameter term in `Ccap_P` obeys

`Dcode/p -> d=2+2alpha+3beta`.

The pair-radius factor therefore tends to

`(d+sqrt(d^2+12beta))/3`.

Since `alpha>=1`, this radius density is strictly larger than `2beta`, while the remaining multiplicative factor in `Ccap_P` is `1+2beta/ell>=1`. The crossing target density is

`2xy/p^2 -> 2beta`.

Hence exact crossing capacity is already satisfied at `P0` with strict asymptotic margin throughout this fixed/sublinear-k cone. Therefore

> **`sigma_P/p^2 -> beta = P0/p^2`.**

The imbalance obstruction above is not an artifact of discarding exact `Ccap_P`. In this tail pair capacity base-saturates at leading order; the remaining bottleneck must come from physical U-geometry, rooted triangle/residual capacity, or source-tuple/beta capacity.

## 10. Independent arithmetic audit

The companion checker verifies, independently of the hand simplification:

- 13,176 exact coordinate/parity identities for `B0` and `Aroot`;
- 28,350 brute-force tests of the four-piece `W_*` formula;
- 45,300 direct same-currency rooted identities;
- the quartic value `alpha0` to numerical tolerance;
- finite weak pair/root minima for `k=3` approaching the predicted pinch (`N/p` approximately `1.02, 1.015, 1.018, 1.017` at `p=100,200,500,1000`).

The checker is an exact arithmetic audit of the conditional inequalities only. It is not a D2C graph enumerator and makes no graph-realizability claim.

## 11. Consequence and next move

The corrected shared-core branch is **not** globally analytically closed by the present pair/root inequalities. This is an important correction to any temptation to extrapolate the predecessor's zero-survivor bounded box. What is now proved conditionally is sharper:

1. pair score and rooted residual capacity collapse to one exact resource `W`;
2. `W` has an exact closed minimizer over all `M,e`;
3. in the deep arm, equality uniquely forces `M=N,e=k,J=0` and has a linear stability theorem;
4. every asymptotic survivor lies in an explicit `(alpha,beta,kappa)` cone;
5. fixed/sublinear `k` forces `N/p>=1.017515...`, so balanced minimal reservoirs are excluded;
6. exact `Ccap_P` already base-saturates asymptotically in that tail, so another pair-score relaxation is unlikely to close it.

The highest-value next attack is therefore the **located physical equality geometry**, not another scalar inequality: feed the forced `z_*--U_o` nonedges (`M≈N`), the saturated X-star (`e≈k`), `J≈0`, and the exact triangle ceiling into the rooted residual identity `delta=r-e(F)` and into the finite source-tuple/beta-capacity theorem. If an analytic tail still survives, classify that tail directly before opening the tied one-core `R2+R2` and core-containing `R3` alternatives.

Keep `k=2,k=1,m=g+2`, loaded buffer, `z=2`, and the four-exception gate deferred. `X_3` remains unaffected because it has `u=0` and never enters the present positive-buffer/minimal-reservoir hypotheses.
