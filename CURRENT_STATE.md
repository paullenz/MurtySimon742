# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** Sufficiently-large/eventual second-extremal diameter-2-critical classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 strengthening is not assumed. The published 2024 `X_3` graph (`n=12,m=32`) remains a mandatory hostile control. Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_ZERO_BUFFER_LAMBDA7_SINGLETON_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `db8963a3dc5b33015a67df436c9dff32a0cc7843`

LAST VERIFIED RESULT: `Raw criticality proves the common core W_0 is anticomplete to U_o. Together with U_o independence this makes the unmatched graph exact: q=u_o, H=e_bar(W_0,U_o)=k u_o, E_U=k(p+u-2)+u_o(rho-2)+J, and q+E_U=k(p+u-2)+u_o^2+J, where J=e_bar(X,U_o)>=max(x,u_o). The exact X-slack identity remains L_X=x(lambda+1-rho)+k(x-1)+J-2e(X), with e(X)<=k(rho-p-2) from duplicate complementary-witness capacity. The stronger exact core/outside separation kills all four previous lambda=6 scalar survivors, so the zero-buffer branch is closed for lambda<=6. At lambda=7 the hand score reduction leaves exactly (p,rho,k)=(4,6,1); there e(X)=0, q=5, H=5, S=55+2J and C0=67, so only J=5 or 6 (delta=-4 or -3) remain. Thus the live zero-buffer problem is a five-by-five X--U_o incidence geometry with at most one hole beyond the code-complement matching.`

UNPRESERVED WORK: `None. The W_0--U_o anticompleteness theorem, exact unmatched ledgers, lambda=6 closure, lambda=7 one-state hand reduction and arithmetic diagnostic are preserved under project/research/post_ms/2026-09-19-zero-buffer-core-outside-separation-v1/.`

DEFERRED ADMIN: `README remains lower-frequency. Refresh reviewer-facing status at the next daily adversarial checkpoint; do not spend the mathematics cadence on packaging or CI churn unless repository integrity fails.`

NEXT ACTION: `Attack the lambda=7 five-by-five geometry directly. For each remaining edge h_i--z_j (i!=j) in the J=5 matching-hole state, classify both triangle-edge criticality orientations. A B-witness is impossible in the orientation whose U endpoint is the singleton source because of the root; A-witnesses are constrained by X independence and the two common Y-neighbours. The only live possibility appears to be a matched-B witness in the reverse orientation. Prove its exact coordinate/gamma restriction and show it forces an additional X--U_o hole or violates singleton common-neighbourhood. Repeat for J=6. One forced extra hole beyond J=6 closes lambda=7. Do not advance to lambda=8 or z=2 until this local geometry is exhausted.`

## Mandatory audit reconciliation

Before forward mathematics this run, `CURRENT_STATE.md`, root `README.md`, recent commits, the 19 September daily red-team audit/handoff, the repaired source-premise note, and the independent actual-D2C Hall/pair-capacity regression were reread.

The audit priority remains binding. The two source-tuple premises are repaired at the raw/selected interface, but the finite source-tuple theorem is not promoted as unconditional graph closure. The independent actual-D2C regression includes `X_3`, reaches rooted partitions/codes/Hall objects/exact `Ccap_P`, and still reports zero graph/formula mismatches. No actual rigid complete Hall cut with `x>=3` has been found, so the one-code results below remain conditional hand implications. The four-exception gate remains subordinate. No weakened or invalidated line was resumed.

The present advance does not use source-tuple capacity. It is raw D2C criticality plus exact physical incidence and Boolean-code support.

## Mandatory negative control

`X_3`: `n=12`, `m=32>M(12)=31`, canonical root `a=3,b=8,p=4,u=0,Q=12,r=f=delta=0`. Every zero-buffer theorem below requires `u_o>=p+1`; `X_3` is untouched.

## Retained zero-buffer/code-simplex structure

Use the unloaded common-buffer zero-slack branch:

- `X--Y` complete; Y one code d; `A_bar d=empty`;
- `g=p`, `k=x-p>0`, `x=p+k`;
- `U_-=U_bar d=W_0 dotcup {b}`, `|W_0|=k`, and `U_-` independent;
- b complete to X and U_o, anticomplete to Y;
- `rho:=u-k=u_o+1`;
- Y anticomplete to all U, so
  `L_Y=rho(p+rho-lambda-1)`;
- exact X-code simplex
  `supp_A(X)={0^p,e_1,...,e_p}` with multiplicities k,1,...,1;
- exact support duality
  `supp_U(U_o)={1^p,1^p-e_1,...,1^p-e_p}`;
- hence `p>=4`, `rho>=p+2`;
- U_o is independent.

## New core/outside anticompleteness theorem

For `w in W_0`, `z in U_o`, suppose wz is an edge. It shares the root, so a singleton witness must lie in A; since Y is anticomplete to U, it lies in X.

If the witness is adjacent to w and nonadjacent to z, it must be w's unique core head; but b is adjacent to z and every X vertex, giving a second common neighbour.

In the reverse orientation the witness is adjacent to z and nonadjacent to w, with singleton `N(w) cap N(a)={z}`. The absence of a matched common neighbour forces `c(a)=bar c(w)=d`, but X contains no code d.

Therefore

`e(W_0,U_o)=0`.

## Exact unmatched and slack ledgers

Let `u_o=rho-1` and `J=e_bar(X,U_o)`.

The U graph now consists exactly of the b--U_o star:

`q=e(G[U])=u_o`.

For every `z in U_o`,

`epsilon_z=rho-2+h_X(z)`.

The exact U-side score is

`E_U=k(p+u-2)+u_o(rho-2)+J`.

Hence

`q+E_U=k(p+u-2)+u_o^2+J`.

The X-side identity is exactly

`L_X=x(lambda+1-rho)+k(x-1)+J-2e(X)`.

Put `R=rho-p-2`. Internal X-edges are neither direct nor matched-foot certified; they require complementary-code U_o witnesses. One physical source-witness pair per X-source is already consumed by its buffer-X certificate, so only the R duplicate complementary witnesses supply residual pairs. Since the largest X code class has size k,

`e(X)<=kR`.

Thus

`L_X >= [x(lambda+1-rho)+k(x-1)+max(x,u_o)-2kR]_+`.

## Closure through lambda=6

The previous package had reduced lambda=6, under a weaker core/outside hole floor, to

`(p,rho,k)=(4,6,1),(4,6,2),(4,7,1),(4,7,2)`.

Exact core/outside anticompleteness replaces the old H=k lower bound by H=k u_o, increasing the U-side score by `2k(u_o-1)`. That increase is 8,16,10,20 on the four states, while their old score margins were -6,-2,0,-2. All are now strictly over C0.

Therefore the zero-buffer branch is closed for every `lambda<=6`.

## Lambda=7 hand reduction

Write `rho=p+s`, `s>=2`. Let case A be `k>=s-1` (x>=u_o) and case B `k<=s-2` (x<u_o).

Using the exact U-side floor and duplicate-support X floor, before positive-part truncation the score differences from C0 are

A:
`D_A=k^2+2kp+ks-10k+3p^2+5ps-29p+2s^2-20s+38`;

B:
`D_B=k^2+2kp+ks-11k+3p^2+5ps-29p+2s^2-19s+37`.

The raw X-slack floors are

A:
`X_A=k^2-3ks+12k-p^2-ps+9p`;

B:
`X_B=k^2-3ks+11k-p^2-ps+9p+s-1`.

A candidate requires `D_A+[X_A]_+<=0` or `D_B+[X_B]_+<=0`.

Monotonicity in p,k,s reduces p>=6 immediately; at p=5 the only D_A-nonpositive points are `(s,k)=(2,1),(2,2)`, and adding X_A gives 6 and 20. At p=4 all states are positive after X-slack except

`(s,k)=(2,1)`.

Thus lambda=7 has one scalar state:

`(p,rho,k)=(4,6,1)`.

## Exact lambda=7 singleton geometry

Here

- `u=7`, `u_o=5`;
- `x=5`, `y=2`;
- `R=0`, so `e(X)=0`;
- `q=5`;
- `L_Y=12`;
- `E_U=29+J`;
- `L_X=14+J`;
- `S=55+2J`;
- `C0=67`.

Since `J>=5`, only

`J=5` or `J=6`

survive. The exact residual identity gives

`delta=J-9`,

so the possibilities are `(J,delta)=(5,-4),(6,-3)`.

At J=5, the X--U_o nonedges are exactly the five code-complement pairs. At J=6 there is exactly one additional X--U_o hole.

## Preserved package

`project/research/post_ms/2026-09-19-zero-buffer-core-outside-separation-v1/`

- `ZERO_BUFFER_CORE_OUTSIDE_SEPARATION_AND_LAMBDA7_FRONTIER.md`
- `check_zero_buffer_core_outside.py`

The checker is arithmetic audit support only. It independently verifies the lambda=6 empty scalar set under the exact separation floor and the unique lambda=7 scalar state plus its J/delta pair.

## Immediate frontier

Classify criticality of the remaining X--U_o edges in the 5x5 lambda=7 incidence matrix. In the J=5 state every off-diagonal `h_i z_j` is an edge; in J=6 all but one off-diagonal pair remain. The edge lies in a triangle through b. One singleton orientation has no B witness because the U endpoint and any B witness share the root. A-witnesses are constrained by X independence and the two common Y-neighbours, leaving a narrowly specified matched-B orientation to analyze.

A single theorem forcing two or more extra X--U_o holes closes both J=5 and J=6. Stay on this local problem before lambda=8 or z=2.

<!-- CURRENT-STATUS:END -->
