# One-code boundary exposure forces unmatched mass and rooted triangle pressure

## Scope and audit status

This note is conditional downstream mathematics inside the rigid complete-Hall-cut / one-code branch. It does **not** assert that an actual diameter-2-critical graph realizes that interface. The 2026-09-21 daily red-team audit remains binding: bounded graph-level regression has no positive rigid complete-Hall-cut fixture with `x>=3`, and `X_3` remains a mandatory negative control. The invalidated H-U private-foot route and the old repeated-code reverse-gamma route are not used here.

Notation is chosen to avoid collisions. Let `rho` denote the residual count that earlier one-code notes sometimes called `r`, let `q_U=e(G[U])`, let `f=e(G[A])`, and let `ell=|L(C)|` for the legitimate matched-witness support of a repeated outside A-code class `C`.

## Lemma 1 — boundary exposure forces unmatched mass

Assume the hypotheses of `ONE_CODE_FULL_BOUNDARY_EXPOSURE_THEOREM.md`. Its raw boundary-realizability inequality is

\[
p \le (c-\rho)+\ell.
\]

The one-code occupancy identities give

\[
e=c-\rho=u-k.
\]

Hence

\[
\boxed{c\ge p+\rho-\ell}
\]

and, equivalently,

\[
\boxed{u\ge p+k-\ell}.
\]

In the generic matched-support-free subbranch `ell=0`, this becomes

\[
\boxed{c\ge p+\rho,\qquad u\ge p+k.}
\]

For residual one (`rho=1`), the generic repeated-code branch therefore satisfies `c>=p+1` and `u>=p+k`.

### Proof

The first inequality is just a rearrangement of the already-audited raw boundary-realizability theorem. Substituting `c-rho=u-k` gives the unmatched form. No score inequality, source-tuple capacity theorem, or H-U private-foot claim is used. In particular this consequence survives even if the source-tuple capacity theorem remains only conditional on its two upstream premise checks.

## Lemma 2 — boundary exposure forces rooted triangle pressure

The exact rooted neighborhood identity from `ROOTED_TRIANGLE_RESIDUAL_AND_BETA_DEGREE_SUPPLY.md` is

\[
Q=e(G[B])=p(p+u-1)+q_U.
\]

Using Lemma 1,

\[
p+u-1 \ge 2p+k-\ell-1,
\]

so

\[
\boxed{Q\ge p(2p+k-\ell-1)+q_U.}
\]

In particular, since `q_U>=0`,

\[
\boxed{Q\ge p(2p+k-\ell-1).}
\]

Thus raw repeated-code boundary realizability has a direct rooted consequence: it forces a large triangle count at the root before any score/capacity optimization is invoked.

## Lemma 3 — exact A-side compensation inequality

The rooted score window gives

\[
T\le D_M-1+\lambda(p+u)-p-E_U,
\]

while `T=Q-f`. Therefore

\[
f\ge Q-D_M+1-\lambda(p+u)+p+E_U.
\]

Substituting the exact identity for `Q` yields

\[
\boxed{f\ge (p-\lambda)(p+u)+q_U+E_U-D_M+1.}
\]

When `p>=lambda`, Lemma 1 may be substituted monotonically to obtain

\[
\boxed{
 f\ge (p-\lambda)(2p+k-\ell)+q_U+E_U-D_M+1.
}
\]

No such substitution is legitimate when `p<lambda`, because the coefficient of `p+u` is then negative; in that regime the exact form must be retained.

## Structural interpretation

These inequalities expose a useful feedback loop that was obscured when the boundary theorem was treated only as a local witness-capacity statement:

1. a repeated code class demands enough exposed boundary population;
2. exposed boundary population is literally unmatched `U` mass (`u-k`);
3. unmatched `U` mass increases the exact rooted triangle count `Q`;
4. an above-threshold survivor must compensate that increase through `f=e(G[A])`, `E_U`, or the global score margin.

Thus future use of the one-code boundary theorem should feed directly into the rooted residual ledger rather than be optimized in isolation.

## Immediate next checks

- intersect Lemma 1 with the exact pair-local `Ccap_P`, `(ONE)` and `(CROWD)` inequalities once their current audited statements are re-opened;
- independently replay the two upstream source-tuple premises before treating the finite source-tuple capacity theorem as unconditional inside the branch;
- classify `ell>0`, especially the `m<=1` and `y=1` regimes, instead of silently setting `ell=0`.
