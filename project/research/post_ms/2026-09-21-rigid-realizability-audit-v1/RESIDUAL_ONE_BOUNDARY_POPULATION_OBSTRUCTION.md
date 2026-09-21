# One-code residual dimension one: boundary population obstruction

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

Assume p is large enough that at least two private heads exist (`p>=4` is more than sufficient for the asymptotic programme).

## 2. Full boundary exposure and no universal coordinate

Exactly as on the half-ray:

> **`I(d,X)=[p]`.**                                      `(2.1)`

At residual coordinate j, every private head agrees with d. At private coordinate i, any other private head agrees with d.

Also

> **`C(d,X)=empty`.**                                    `(2.2)`

Head h_i disagrees with d at private coordinate i, and every K-head disagrees with d at residual coordinate j.

Hence the matched-forward arm of the boundary trichotomy is unavailable on every coordinate.

## 3. Reverse capacity

For coordinate i, a reverse boundary certificate must use the forced X-code class `X_{gamma_i}`. Every X-code class has size at most k (taking k>=1), so

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

This gives the main theorem.

### Theorem 4.1 — residual-one population obstruction

For a rigid complete one-code residual-one realization with `p>=4`,

> **if `u<p`, then `y<=k=u-c+1`.**                       `(4.2)`

Equivalently, every residual-one realization satisfies the dichotomy

> **`u>=p`  or  `c+y<=u+1`.**                            `(4.3)`

This is a literal graph-realizability restriction, not an asymptotic score inequality.

## 5. Consequences

1. **All fixed-k high-y residual-one rays with u<p die immediately.** If k is bounded while y grows, `(4.2)` fails.
2. The corrected intermediate half-ray has `u=t+1<p=2t` and `k=2<y=t`, so it is impossible for every t>=4, recovering the companion closure with no score calculation.
3. The obstruction identifies the only residual-one escape regimes still worth considering:
   - the **large-U regime** `u>=p`; or
   - the **large residual-class regime** `k>=y`, equivalently `u>=c+y-1`.
4. Since k itself counts U-certified X-heads, the second regime is exactly where reverse boundary capacity can plausibly absorb all y outside heads without opening every coordinate-distinct U-forward class.

This is a substantial compression of the residual-one parameter space before pair-local `Ccap_P`, `(ONE)`, `(CROWD)`, rooted-Q, or H--U carrier analysis is invoked.

## 6. Next target

The natural next theorem is to price the remaining `k>=y` regime. If many coordinates reverse-certify all or almost all Y-heads, then their forced gamma classes must have size at least y. Because X has only x vertices and repeated gamma patterns incur collision slack, this should interact directly with `RIGID_CUT_REVERSE_GAMMA_MULTIPLICITY.md`.

The alternative `u>=p` should be fed back into the exact minimum-source identities and residual defect ledger to see whether it is already incompatible with a sufficiently-large near-extremal graph except in a much narrower range.

## 7. Scope

This theorem remains conditional on the rigid complete one-code interface. Bounded actual-D2C regression has no positive rigid complete pair-family cut with `x>=3`, and X_3 remains the mandatory negative control.
