# Alpha-beta coercivity, integrated source-product bounds, and beta cylinders

**Status:** internal structural lemmas / candidate research checkpoint, 18 September 2026.  These statements belong to the near-full unmatched-antipode branch.  They do **not** assert an eventual second-extremal theorem.  The published order-12, size-32 `X_3` graph has `u=0` and is not touched by any result below.

## 1. Setup

Use the current partial-Boolean notation.  There are `p` tight antipode fibres and `u` unmatched vertices.  For fibre `i`, write

- `u_i^0+u_i^1=u`;
- `d_i=u_i^0-u_i^1`;
- `m_i=min(u_i^0,u_i^1)=(u-|d_i|)/2`;
- `h_i^0,h_i^1` for the alpha-oriented P--U source counts, `h_i=h_i^0+h_i^1`;
- `r_i^s=u_i^s-h_i^s` for the beta-oriented source counts;
- `e_i^0,e_i^1` for the endpoint slacks of the tight pair, so `e_i^0+e_i^1=lambda+1`.

As before,

`H=sum_i d_i^2`,

`P_alpha=sum_i P_i`, where

`P_i=h_i^0(u_i^1+1)+h_i^1(u_i^0+1)`,

and the beta-side slack charge in fibre `i` is

`T_i=r_i^0 e_i^1+r_i^1 e_i^0`.

The preserved beta-endpoint slack theorem gives

`sum_i T_i <= p L_A`.

The directional deficiency--Hamming budget is

`J+H/2+P_alpha <= p u(p+1-lambda-u/2)+u h_alpha+2p q+pE_U`,

with

`J=sum_x (p-ell_x)(u-d_U(x))`.

Throughout Sections 2--4 we assume `lambda>=0`, so `lambda+1>0`.

---

## 2. Fibrewise alpha-beta diversion coercivity

### Lemma 2.1 (alpha payment)

For each fibre,

`P_i >= (m_i+1)h_i`.

Indeed both opposite-side populations are at least `m_i`, hence each alpha orientation costs at least `m_i+1` in the directional Hall count.

### Lemma 2.2 (beta slack payment after alpha diversion)

For each fibre,

`T_i >= (lambda+1)(m_i-h_i)_+`.

Proof.  Since `r_i^s=u_i^s-h_i^s`,

`r_i^s >= m_i-h_i^s >= m_i-h_i`.

Thus

`min(r_i^0,r_i^1) >= (m_i-h_i)_+`.

For nonnegative `r_i^0,r_i^1,e_i^0,e_i^1` with `e_i^0+e_i^1=lambda+1`,

`r_i^0 e_i^1+r_i^1 e_i^0 >= (lambda+1)min(r_i^0,r_i^1)`.

This proves the claim.

### Theorem 2.3 (alpha-beta diversion coercivity)

For every fibre,

> `P_i + ((m_i+1)/(lambda+1)) T_i >= m_i(m_i+1)`.      `(ABF)`

Equivalently,

> `(lambda+1)P_i+(m_i+1)T_i >= (lambda+1)m_i(m_i+1)`.

Proof.  If `h_i<=m_i`, Lemmas 2.1--2.2 give

`P_i+((m_i+1)/(lambda+1))T_i`

`>= (m_i+1)h_i+(m_i+1)(m_i-h_i)=m_i(m_i+1)`.

If `h_i>m_i`, Lemma 2.1 alone gives the result.

This is the intended coercivity statement: diverting a balanced fibre from beta to alpha cannot erase its cost; it merely transfers the cost from endpoint slack to directional Hall payment.

### Corollary 2.4 (global coercivity)

Since `m_i+1<=floor(u/2)+1` and `sum_i T_i<=pL_A`,

> `P_alpha + [p(floor(u/2)+1)/(lambda+1)] L_A`
>
> `>= sum_i m_i(m_i+1)`.                                 `(ABG)`

The right side has the exact form

> `sum_i m_i(m_i+1)`
>
> `=pu^2/4+pu/2+H/4-((u+1)/2)sum_i |d_i|`.              `(MI)`

By Cauchy, `sum_i|d_i|<=sqrt(pH)`.  If

`z=u-sqrt(H/p)>=0`, then

> `sum_i m_i(m_i+1) >= (p/4) z(z+2)`.                    `(MIC)`

So balanced U-code columns necessarily pay through `P_alpha`, `L_A`, or both.

---

## 3. Integrating the whole source-tuple scarcity profile

The finite-deficit source-tuple theorem says that for every integer `r>=3` and every `K` with `0<=K<=p-r`,

`N_K:=|{x in A:p-ell_x<=K}|`

satisfies

`N_K <= C_r(K)`,

where

`C_r(K)=((K+r)/r) binom(u,r)/binom(p-K,r)`.

Put

`C_hat_r(K)=floor(C_r(K))`.

### Theorem 3.1 (integrated source-tuple deficit)

For any subset `L subseteq A` of size `N`,

> `sum_{x in L}(p-ell_x) >= Phi_r(N)`,                   `(IST)`

where

> `Phi_r(N)=sum_{K=0}^{p-r} (N-C_hat_r(K))_+`.

Proof.  For an integer deficit `k_x=p-ell_x`, the tail identity gives

`sum_{x in L} k_x = sum_{K>=0}|{x in L:k_x>K}|`.

For every `K<=p-r`, at most `C_hat_r(K)` vertices in the whole A-layer have `k_x<=K`; therefore at least `(N-C_hat_r(K))_+` vertices of `L` have `k_x>K`.  Summing those certified tails proves `(IST)`.

This is strictly more informative than choosing one deficit cutoff: it charges the complete staircase of source-tuple scarcity bounds at once.

---

## 4. Side-occupancy threshold plus the integrated deficit profile

Fix a real threshold `T>0` and let

`j=min(p,floor(H/T^2))`.

At most `j` fibres have `|d_i|>T`.

The total beta load is

`B=sum_x ell_x=pu-h_alpha`.

If `j<p`, put

> `N_T=ceil((B-aj)_+/(p-j))`.                             `(NT)`

At least `N_T` A-vertices satisfy `ell_x>j`: otherwise the total beta load is at most `aj+N_T(p-j)` with the corresponding integer rounding, contradicting `(NT)`.

Every such vertex targets more fibres than the number of `T`-bad fibres, so it targets some coordinate `i` with `|d_i|<=T`.  The preserved side-occupancy lemma then gives

`d_U(x)-1 <= (u+T)/2`,

hence

`u-d_U(x) >= w_T`, where

`w_T=(u-T)/2-1`.

### Theorem 4.1 (integrated product lower bound)

Whenever `j<p` and `w_T>0`,

> `J=sum_x(p-ell_x)(u-d_U(x))`
>
> `>= w_T Phi_r(N_T)`.                                   `(IP)`

Proof.  Apply Theorem 3.1 to the at least `N_T` vertices with `ell_x>j`; each has `u-d_U(x)>=w_T`.

This is an exact finite inequality.  It simultaneously couples beta-load scarcity, Hamming imbalance, beta deficit and U-degree deficiency.  It should replace one-cutoff estimates whenever the full deficit distribution matters.

---

## 5. Integrated positive-lambda master inequality

Let

`C_0=S_req-2`,

so an above-`M(n)` candidate obeys `E_U+L_A<=C_0`, and put

`C_beta=p(floor(u/2)+1)/(lambda+1)`.

Combining `(DHB)` with `(ABG)` gives

`J+H/2+sum_i m_i(m_i+1)`

`<=p u(p+1-lambda-u/2)+u h_alpha+2p q+pE_U+C_beta L_A`.

Since `E_U,L_A>=0`,

`pE_U+C_beta L_A <= max(p,C_beta)C_0`.

Therefore Theorem 4.1 yields the exact necessary condition

> **INTEGRATED POSITIVE-LAMBDA MASTER**
>
> `w_T Phi_r(N_T)+H/2+sum_i m_i(m_i+1)`
>
> `<=p u(p+1-lambda-u/2)+u h_alpha+2p q`
>
> `  +max(p,C_beta)C_0`,                                 `(IPM)`

whenever `lambda>=0`, `j<p`, and `w_T>0`.

The term `sum_i m_i(m_i+1)` may be replaced by the explicit lower bound `(MIC)`.

This is not yet a contradiction theorem.  Its value is that it brings the two previously separate coercive mechanisms -- source-tuple deficit and alpha/beta fibre payment -- into the same exact scorecard inequality.

---

## 6. Beta-cylinder localisation: a direct `(k_x,epsilon_x,d_U(x))` bridge

The preceding inequalities are aggregate.  There is also a useful exact local structure.

Fix `x in A` with beta target set `I_x`, `|I_x|=ell_x`, and deficit

`k_x=p-ell_x`.

For every `i in I_x`, selected-witness uniqueness supplies a distinct designated beta source `y_i in U`.  Beta criticality determines a fixed **central side** `sigma_x(i)` of fibre `i` such that every neighbour of `x` in `A union U`, except `y_i`, lies on that side at coordinate `i`.  The source `y_i` lies on the opposite side at its own coordinate.  For `j!=i`, the source `y_j` is an ordinary neighbour relative to coordinate `i`, hence lies on the central side there.

Define the central Boolean cylinder

`C_x={z in A union U : c(z)|_{I_x}=sigma_x}`.

The `ell_x` designated beta sources are exactly the neighbours of `x` outside this cylinder.  All A-neighbours of `x` lie inside it.

Because every A-vertex has exactly `p` matched-B neighbours,

`d(x)=p+d_U(x)+d_A(x)`.

Since `epsilon_x=2p+u-d(x)`,

> `d_A(x)+d_U(x)=p+u-epsilon_x`.                          `(DEG)`

Thus

> `|N(x) cap C_x|=d_A(x)+(d_U(x)-ell_x)`
>
> `=u+k_x-epsilon_x`.                                    `(CY1)`

More importantly, `d_U(x)<=u` gives

> `N_A(x) subseteq C_x`, and
>
> `d_A(x)>= (p-epsilon_x)_+`.                             `(CY2)`

So low slack forces many A-neighbours into a cylinder of codimension `ell_x=p-k_x`.

### Corollary 6.1 (finite-deficit cylinder multiplicity)

Only `2^{k_x}` full partial Boolean codes extend the central restriction on `I_x`.  Consequently some A-code class inside `C_x` contains at least

> `ceil((p-epsilon_x)_+/2^{k_x})`                         `(CY3)`

A-neighbours of `x`.

In particular, bounded beta deficit together with `epsilon_x=o(p)` forces an A-code class of linear size.  This is the first direct local bridge obtained here between the desired variables `k_x`, `epsilon_x` and the geometry of the A-layer.

No claim is yet made that an arbitrary repeated A-code class has the same capacity bound as a projective alpha class; that is precisely a point to prove rather than assume.

---

## 7. Audit and trust boundary

The accompanying checker `check_alpha_beta_coercivity_integrated_product.py` replays:

- 213,180 exact fibrewise alpha/beta coercivity configurations;
- 72,084 exact Hamming/right-side identities and Cauchy checks;
- 83,226 admissible finite-deficit tail configurations;
- 184,730 beta-load threshold configurations;
- 79,079 abstract beta-cylinder degree/bookkeeping configurations.

Total: 632,299 checks, with no failures in the preserved run.

These computations audit the algebra only.  The promoted content of this note is the hand injection/counting argument above.

## 8. Strategic consequence

The next useful target is no longer another numerical improvement of `27/14`.  There are now two complementary ways to price a beta-heavy A-witness:

1. globally, its deficit contributes through the complete staircase `Phi_r` and hence `(IPM)`;
2. locally, low slack forces at least `(p-epsilon_x)_+` A-neighbours into a codimension-`p-k_x` cylinder, and therefore a repeated A-code class of size at least `(CY3)`.

A high-value next theorem would bound the reuse of these cylinder code classes using A-edge criticality / residual defect, or show that many such cylinders force additional `L_A`.  That would convert the new joint `(k_x,epsilon_x,d_U(x))` structure directly into the second-extremal scorecard rather than merely refining the `u/p` constant.
