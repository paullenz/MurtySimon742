# One-code residual dimension one: boundary population and gamma/U tradeoff

Date: 2026-09-21

Status: conditional structural theorem inside the rigid complete one-code cut, derived directly from raw boundary criticality. It strictly generalizes the corrected intermediate half-ray closure and does not use the audit-sensitive source-tuple capacity theorem.

## 1. Residual-one normal form

Assume the one-code rigid branch has residual matched-coordinate dimension

`r=p-m=1`.

Let j be the unique residual coordinate. Then the matched-singleton heads are

`H={h_i:i!=j}`,

with

`c(h_i)=d xor e_i`,

so `|H|=p-1`. The remaining X-heads form the U-certified residual class K, all of code

`d xor e_j`.

Write

`k=|K|=x-(p-1)=x-p+1`.

Using the minimum-source identity `x=p+u-c`, this is equivalently

> **`k=u-c+1`.**                                         `(1.1)`

Thus every occupied X-code class has size one except the residual class, which has size k.

Assume `p>=4`, so at least two private heads exist.

## 2. Full boundary exposure and no universal coordinate

Exactly as on the half-ray:

> **`I(d,X)=[p]`.**                                      `(2.1)`

At residual coordinate j, every private head agrees with d. At private coordinate i, any other private head agrees with d.

Also

> **`C(d,X)=empty`.**                                    `(2.2)`

Head h_i disagrees with d at private coordinate i, and every K-head disagrees with d at residual coordinate j.

Hence the matched-forward arm of the boundary trichotomy is unavailable on every coordinate.

## 3. Reverse capacity

For coordinate i, a reverse boundary certificate must use the forced X-code class `X_{gamma_i}`. Every X-code class has size at most k (taking `k>=1`), so

> `r_i:=|X_{gamma_i}|<=k`.                                `(3.1)`

For the fixed matched source `q_i^{d_i}`, distinct Y-heads require distinct physical reverse witnesses. Therefore at most k of the y boundary edges at coordinate i can reverse-certify.

If

> **`y>k`,**                                              `(3.2)`

then every coordinate has at least one U-forward boundary certificate.

## 4. Distinct U-code classes force u>=p

A U-forward witness at coordinate i has code

`bar d xor e_i`.

Under `(3.2)`, each of the p distinct one-match U-code classes is nonempty. Hence

> **`u>=p`.**                                             `(4.1)`

### Theorem 4.1 — residual-one population obstruction

For a rigid complete one-code residual-one realization with `p>=4`,

> **if `u<p`, then `y<=k=u-c+1`.**                       `(4.2)`

Equivalently, every residual-one realization satisfies the dichotomy

> **`u>=p`  or  `c+y<=u+1`.**                            `(4.3)`

This is a literal graph-realizability restriction, not an asymptotic score inequality.

## 5. The surviving k>=y branch pays a gamma/U tradeoff

Assume now

`2<=y<=k` and `p>=y`.

Let

`g=|{i in [p]: gamma_i=d xor e_j}|`,

the number of coordinates whose reverse witness class is the unique residual K-code class.

At every coordinate outside this g-set, the forced gamma class has size at most one. Hence at least `y-1>0` Y-heads must U-forward there, and the partial U-forward slack theorem gives

> `E_U >= (p-g)(p-1)`.                                   `(5.1)`

Moreover each such coordinate needs a nonempty, coordinate-distinct one-match U-code class, so

> `p-g<=u`,                                               `(5.2)`

or

> **`g>=p-u`.**                                           `(5.3)`

The g residual-gamma coordinates share the same physical gamma class. The preserved gamma-collision theorem therefore gives

> `L_A>=g(g-1)`                                           `(5.4)`

(for g<3 the displayed right side is harmless anyway).

Adding the two score currencies,

> **`E_U+L_A >= (p-g)(p-1)+g(g-1)`.**                   `(5.5)`

Equivalently,

`E_U+L_A >= p(p-1)-g(p-g)`.                              `(5.6)`

Without using `(5.3)`, the right side is minimized when g is nearest p/2, giving the universal residual-one boundary floor

> **`E_U+L_A >= 3p^2/4-p`** for even p,                  `(5.7a)`

and

> **`E_U+L_A >= (3p^2-4p+1)/4`** for odd p.             `(5.7b)`

If `u<p/2`, then `(5.3)` forces `g>p/2`, and the convex function in `(5.5)` is minimized at the boundary `g=p-u`, yielding the stronger located tradeoff

> **`E_U+L_A >= u(p-1)+(p-u)(p-u-1)`.**                 `(5.8)`

Thus the only small-U residual-one escape left by Theorem 4.1 cannot use reverse capacity for free: concentrating enough coordinates into the sole large X-code class forces a quadratic gamma-collision A-slack bill, while spreading them away from that class forces a quadratic U-slack bill.

## 6. Consequences

1. **All fixed-k high-y residual-one rays with u<p die immediately.** If k is bounded while y grows, `(4.2)` fails.
2. The corrected intermediate half-ray has `u=t+1<p=2t` and `k=2<y=t`, so it is impossible for every `t>=4`, with no score calculation.
3. The only residual-one escape regimes worth considering are:
   - the **large-U regime** `u>=p`; or
   - the **large residual-class regime** `k>=y`, equivalently `u>=c+y-1`.
4. In the second regime, `(5.5)`--`(5.8)` supply a direct boundary-criticality score floor before pair-local `Ccap_P`, `(ONE)`, `(CROWD)`, rooted-Q, or H--U carrier analysis is invoked.

This is a substantial compression of the residual-one parameter space.

## 7. Next target

Feed `(5.5)` together with the exact one-code score ceiling and the residual defect/rooted-Q identities, retaining `g>=p-u`. This should determine whether the large residual-class branch survives asymptotically at all, and if so force a narrow ratio window for `u/p`, `y/p`, and `c/p`.

The alternative `u>=p` should separately be inserted into the minimum-source identities and the eventual second-extremal residual ledger; because u is then at least the full tight dimension, the old low-k escape geometry is no longer relevant.

## 8. Scope

This theorem remains conditional on the rigid complete one-code interface. Bounded actual-D2C regression has no positive rigid complete pair-family cut with `x>=3`, and X_3 remains the mandatory negative control.
