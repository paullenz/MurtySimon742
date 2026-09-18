# Residual split, aligned matched-B capacity, and one-dimensional feasibility

Date: 2026-09-18

Status: internal structural theorem package for the eventual / sufficiently-large diameter-2-critical second-extremal programme around

`M(n)=floor((n-1)^2/4)+1`.

The published order-12, size-32 graph `X_3` remains the mandatory negative control. Nothing here asserts the false all-order 2019 strengthening.

## 1. Reassessment

The preceding checkpoint produced the complete actual-slack A-edge capacity

> `f <= a R_A(L_A) + [R_code(S)/(2(lambda+1))](2L_A+S)`.

Two pieces of information were still being lost before this bound was compared with the residual target:

1. the exact residual identity already contains `E_U`, so replacing it by the older `F_min` discards one unit of forced A-edge demand for every unit of unmatched slack;
2. the matched-B channel was capped by `a R_A(L_A)`, although the preserved matched-foot polarization theorem and the aligned-code crowding theorem together give a second, independent cap involving the total number `p` of tight fibres.

This note records those compositions and reduces the global scalar problem to one monotone slack variable. A finite diagnostic at the end shows that the resulting scalar system is still not a generic closure mechanism; that negative result is strategically important.

Throughout put

`L=lambda+1`,

`Q=p(p+u-1)+q`,

`S=E_U+L_A`,

`a=2p+u-lambda-1`.

## 2. Exact residual split

The preserved rooted identity is

> `delta=E_U+Q-f-lambda(p+u)+p`.                          `(RQ3)`

Substituting `Q=p(p+u-1)+q` and rearranging gives the exact form

### Lemma 2.1 — unmatched-slack residual split

> `f=(p-lambda)(p+u)+q+E_U-delta`.                        `(RSF)`

For an above-`M(n)` candidate, `delta<=D_M-1`, hence

> `f >= F_0 + q + E_U`,                                  `(RSF+)`

where

> `F_0=(p-lambda)(p+u)-D_M+1`.

The older rooted lower bound was

> `F_min=F_0+q`.

Thus `(RSF+)` strengthens it by the **full unmatched slack `E_U`**.

This is not a new inequality added to the model; it is the exact residual identity written in the coordinate system needed by the complete A-edge channel theorem.

### Negative control

For `X_3`,

`p=lambda=4`, `u=q=E_U=delta=f=0`.

Hence `(RSF)` is exactly `0=0`. The exceptional graph lies at the zero-unmatched-slack endpoint and is not suppressed.

## 3. A cross-edge lower bound for q

Recall

> `E_U=u(p+u-1)-2q-s`,                                   `(EU)`

where `s=e_G(A,U)`.

Since `s<=au`,

`2q >= u(p+u-1)-au-E_U`.

Using

`p+u-1-a=lambda-p`,

we obtain:

### Lemma 3.1 — unmatched cross-edge q floor

> `q >= ceil( [u(lambda-p)-E_U]_+ / 2 )`.                `(QL)`

Equivalently, if an independent argument gives `q<=Q_*`, then

> `E_U >= [u(lambda-p)-2Q_*]_+`.                          `(EQL)`

This is useful only when `lambda>p`; when `lambda<=p`, the floor is zero.

## 4. Compress the load-one term in the beta-sensitive q ceiling

The preserved beta-sensitive theorem is

> `q<=au-B_beta+N_1`,                                    `(BQ)`

where

`N_1=|{x in A:ell_x=1}|`.

Put

> `m_0=min(p,u)`.

Every beta load satisfies `0<=ell_x<=m_0`. If `m_0>=2`, then

`B_beta=sum_x ell_x`

`<=N_1 + m_0(a-N_1)`

`=m_0a-(m_0-1)N_1`.

Therefore:

### Lemma 4.1 — load-one compression

For `m_0>=2`,

> `N_1 <= floor((m_0a-B_beta)/(m_0-1))`.                 `(N1)`

Consequently

> `q`
> ` <= au-B_beta`
> `    +floor((m_0a-B_beta)/(m_0-1))`.                   `(QB1)`

The right side is nonincreasing in `B_beta`. Hence, using the preserved beta floor

> `B_beta>=B_*`,

one gets the parameter-only ceiling

> `Q_beta^*`
> ` := min( binom(u,2),`
> `          au-B_*+floor((m_0a-B_*)/(m_0-1)) )`         `(QB*)`

for `m_0>=2`.

If `B_*>m_0a`, the tuple is impossible already. For `m_0=1`, `(BQ)` adds nothing beyond the trivial graph bound `q<=binom(u,2)`.

Combining `(QB*)` with `(EQL)` produces a new unmatched-slack floor

> `E_cross=[u(lambda-p)-2Q_beta^*]_+`.                    `(ECROSS)`

It should be combined with the preserved source/Hall floor `E_*` by

> `E_hat=max(E_*,E_cross)`.                               `(EHAT)`

## 5. An aligned-code cap for the complete matched-B channel

Let `P_B` be the chosen matched-B traffic in the exact A-edge channel decomposition

> `f=D+P_B+C`.

The preserved matched-foot complement-pair theorem gives, for each unordered gamma-code pair `Pi={c,bar c}`,

> `P_Pi`
> ` <= g_Pi max(n_c,n_bar c)`
> `    +sum_{i in I_Pi}min(t_i^0,t_i^1)`.                 `(CP4)`

Here `g_Pi=|I_Pi|` is the number of tight fibres whose two matched endpoints have gamma codes `c,bar c`. The gamma pairs partition the `p` tight fibres, so

> `sum_Pi g_Pi=p`.                                        `(GP)`

The preserved aligned-code crowding theorem says that if a complementary pair has slack `S_Pi`, then

> `n_c,n_bar c <= R_code(S_Pi)/2`
> `              <=R_code(S)/2`.                          `(AC)`

The preserved fibre-polarization inequality gives

> `(lambda+1)sum_i min(t_i^0,t_i^1)`
> ` <= mu_gamma L_A`,                                    `(POL)`

and `mu_gamma<=R_A(L_A)`.

Summing `(CP4)` and using `(GP)`, `(AC)`, `(POL)` gives:

### Theorem 5.1 — aligned-code matched-B capacity

Put

> `R=R_code(S)`, `r=R_A(L_A)`.

Then

> `P_B <= pR/2 + r L_A/(lambda+1)`.                      `(AMB)`

Together with the older self-pricing cap `P_B<=ar`,

> `P_B`
> ` <= min( ar, pR/2 + rL_A/(lambda+1) )`.               `(AMB+)`

This composition uses only already-preserved global matched-foot source uniqueness, opposite-endpoint gamma complementarity, fibre polarization, and aligned-code crowding. No cylinder multiplicity assumption is needed in the final inequality.

## 6. Refined complete A-edge capacity

The previous combined direct+A/U theorem gives

> `D+C <= [R_code(S)/(2(lambda+1))](2L_A+S)`.             `(GCC')`

Adding `(AMB+)` yields:

### Theorem 6.1 — refined complete A-edge capacity

With `R=R_code(S)` and `r=R_A(L_A)`,

> `f`
> ` <= min( ar, pR/2+rL_A/(lambda+1) )`
> `    + [R/(2(lambda+1))](2L_A+S)`.                     `(ACE+)`

This is never weaker than the previous `(ACE)` and can be strictly stronger when the matched-B channel would otherwise saturate `ar`.

## 7. One-dimensional split feasibility

Above `M(n)`, define as before

> `C_0=2(D_M-1)+lambda(p+u)-p`,

so `S<=C_0`.

For a fixed `S`, write `L_A=S-E` and define

`Cap(S,E)` to be the right side of `(ACE+)` after that substitution.

Two monotonicities are immediate:

1. for fixed `E`, `Cap(S,E)` is nondecreasing in `S`;
2. for fixed `S`, `Cap(S,E)` is nonincreasing in `E`.

Also

> `chi(E):=E+ceil([u(lambda-p)-E]_+/2)`                   `(CHI)`

is nondecreasing in `E`.

Every above-threshold candidate therefore satisfies

> `F_0+chi(E_U) <= Cap(S,E_U)`.                           `(SF0)`

Using `S<=C_0` and `E_U>=E_hat` gives the scalar necessary condition

### Theorem 7.1 — source-conditioned split feasibility

> `F_0+chi(E_hat) <= Cap(C_0,E_hat)`.                     `(SCF)`

If `(SCF)` fails, the parameter tuple cannot contain an above-`M(n)` graph in the live branch.

This is the cleanest scalar synthesis currently available:

`beta/source support -> E_hat -> exact residual A-edge demand -> refined complete channel capacity`.

It has no free `q`, `f`, `L_A`, matched-B collision size, or direct/AU channel split.

## 8. Diagnostic outcome and strategic obstruction

The companion checker audits the new algebra and also runs a conservative finite parameter diagnostic using only:

- the root-imbalance beta floor `p(lambda+1-2p)_+`;
- the `r=3` integrated source-support profile;
- the new load-one compression;
- `(SCF)`.

On the grid `3<=p<=30`, `1<=u<=2p`, and all nonnegative `lambda` with `a>0` and `C_0>=0`, it finds:

- 56,238 scalar parameter tuples;
- 10,298 already impossible from beta capacity/support;
- 45,940 remaining scalar tuples;
- **zero** additional generic closures from the old collapsed channel criterion;
- **zero** additional generic closures from `(SCF)`.

The new matched-B cap can reduce the old complete-channel numerical allowance (the minimum observed ratio is `9/11 = 0.81818...`), but on all 21,739 scanned tuples with positive base rooted A-edge demand `F_0>0`, the matched branch `ar` is already the smaller matched-B cap. In that forced-`f` region, `(AMB+)` therefore does not improve the scalar envelope.

This is a significant obstruction, not a theorem failure:

> **Further global scalar tightening of the same slack/code radii is unlikely to close the live branch.**

The remaining gain has to be local: retain complementary-pair allocation, or feed the direct bounded-surplus stability theorem into the forced-A-edge traffic before summing all code pairs. In particular, the next move should not be another replacement of actual pair slack by `S` or `C_0`.

## 9. Trust boundary

- `(RSF)` is exact algebra from the preserved rooted residual identity.
- `(QL)` uses only `s<=au`.
- `(N1)` uses only `ell_x<=min(p,u)`.
- `(AMB)` is a composition of preserved matched-foot pair capacity, fibre polarization, the partition of the `p` tight fibres by gamma complementary pairs, and preserved aligned-code crowding.
- `(ACE+)` and `(SCF)` are hand consequences of the preceding exact inequalities.
- The finite scan is diagnostic only and is not part of any proof.
- The order-12 `X_3` graph has `u=0` and remains explicitly allowed.
- No eventual theorem is claimed.
