# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** Sufficiently-large/eventual second-extremal diameter-2-critical classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 strengthening is not assumed. The published 2024 `X_3` graph (`n=12,m=32`) remains a mandatory hostile control. Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_ZERO_BUFFER_OUTSIDE_INDEPENDENCE_LAMBDA6_FRONTIER_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `7da23090824f02cfddb6a294e818b480c4148a1c`

LAST VERIFIED RESULT: `Raw criticality of any U_o--U_o edge contradicts the zero-buffer b-complete geometry, so U_o is independent. This yields exact q=(k+1)u_o-H, exact E_U=k(p+k-1)+u_o(rho-k-2)+J+2H, and exact L_X=x(lambda+1-rho)+k(x-1)+J-2e(X), where H is the W_0--U_o hole count and J the X--U_o hole count. Duplicate complement support gives e(X)<=k(rho-p-2). These local ledgers close the entire zero-buffer branch for lambda=3 and lambda=4. At lambda=5 they reduce to one equality state (p,rho,k)=(4,6,1), which raw criticality of the forced W_0--U_o edges kills. Therefore the zero-buffer branch is closed for lambda<=5. The next exact scalar frontier at lambda=6 consists of only four states: (p,rho,k)=(4,6,1),(4,6,2),(4,7,1),(4,7,2).`

UNPRESERVED WORK: `None. The outside-independence theorem, exact q/E_U/L_X ledgers, duplicate-support X-edge capacity, lambda<=5 closure, and lambda=6 four-state hand reduction are preserved under project/research/post_ms/2026-09-19-zero-buffer-outside-independence-v1/.`

DEFERRED ADMIN: `README remains lower-frequency. Refresh reviewer-facing status at the next daily adversarial checkpoint; do not spend the mathematics cadence on packaging or CI churn unless repository integrity fails.`

NEXT ACTION: `Stay in the zero-buffer branch and attack the four lambda=6 states directly, before moving to lambda=7 or positive buffer slack. Start with rho=6 (minimal complement support, hence e(X)=0): (4,6,1) and (4,6,2). Reuse raw triangle-edge criticality on forced W_0--U_o edges; for k=2 the score identity leaves only a very small (H,J,delta) window. Then treat rho=7, where there is exactly one duplicate complementary-code witness and e(X)<=k. Preserve any equality geometry and force additional holes/slack physically. Do not move to z=2.`

## Mandatory audit reconciliation

Before forward mathematics this run, `CURRENT_STATE.md`, root `README.md`, recent commits, the 19 September daily red-team audit/handoff, the repaired source-premise note, and the independent actual-D2C Hall/pair-capacity regression were reread.

The audit priority remains binding. The two source-tuple premises are repaired at the raw/selected interface, but the finite source-tuple theorem is not promoted as unconditional graph closure. The independent actual-D2C regression still includes `X_3` and reports zero graph/formula mismatches; no actual rigid complete Hall cut with `x>=3` has been found, so all one-code results below remain conditional hand implications. Exact pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)` remain valid secondary constraints. The four-exception gate remains subordinate. No weakened line was resumed.

The present advance does not use the finite source-tuple theorem. It uses raw edge criticality, exact Boolean support, and physical degree/nonedge ledgers.

## Mandatory negative control

`X_3`: `n=12`, `m=32>M(12)=31`, canonical root `a=3,b=8,p=4,u=0,Q=12,r=f=delta=0`. The zero-buffer branch here requires `u_o>=p+1`, so `X_3` is untouched.

## Retained zero-buffer/code-simplex structure

Use the unloaded common-buffer zero-slack branch:

- `X--Y` complete; Y one code d; `A_bar d=empty`;
- `g=p`, `k=x-p>0`, `x=p+k`;
- `U_-=U_bar d=W_0 dotcup {b}`, `|W_0|=k`, and `U_-` independent;
- b complete to X and U_o, anticomplete to Y;
- `rho:=u-k=u_o+1`;
- Y anticomplete to all U, hence
  `L_Y=rho(p+rho-lambda-1)`;
- exact X-code simplex
  `supp_A(X)={0^p,e_1,...,e_p}` with multiplicities k,1,...,1;
- exact support duality
  `supp_U(U_o)={1^p,1^p-e_1,...,1^p-e_p}`;
- therefore `p>=4` and `rho>=p+2`.

Let

- `H=e_bar(W_0,U_o)>=k`;
- `J=e_bar(X,U_o)>=max(x,u_o)`.

## New raw U_o-independence theorem

If `zz'` were an edge in U_o, the edge shares the root and hence any D2C singleton witness must lie in A. Y is anticomplete to U, so the witness lies in X. But b is adjacent to both U_o endpoints and to every X vertex, so b is an unavoidable second common neighbour in either singleton orientation.

Therefore

`e(G[U_o])=0`.

This supersedes the previous dense lambda=3 residue: those six algebraic score tuples are not graph-realizable.

## Exact local ledgers

Since U_- and U_o are both independent and b is complete to U_o,

`q=e(G[U])=(k+1)u_o-H`.

For z in U_o, with X-hole count h_X(z) and W_0-hole count h_W(z),

`epsilon_z=rho-k-2+h_X(z)+h_W(z)`.

Hence

`E_U=k(p+k-1)+u_o(rho-k-2)+J+2H`.

Adding q,

`q+E_U=k(p+k-1)+u_o^2+J+H`.

The X slack is exactly

`L_X=x(lambda+1-rho)+k(x-1)+J-2e(X)`.

## Duplicate-complement X-edge capacity

Put

`R=rho-p-2>=0`.

For p>=4, the simplex X-codes contain no complementary pair, so internal X-edges are not direct. At g=p all matched gamma codes are d/bar d, so matched-B witnesses cannot serve an X-source. Every internal X-edge must therefore use a complementary-code U_o witness.

Each X-source already consumes one physical source-witness pair in its buffer-X certificate with fixed common neighbourhood `{b}`. Only duplicate U_o witnesses in the same complementary code class can supply new pairs. There are R duplicates total, and the largest X code class has size k. Thus

`e(X)<=kR=k(rho-p-2)`.

Consequently

`L_X >= [x(lambda+1-rho)+k(x-1)+max(x,u_o)-2kR]_+`.

## Closure through lambda=5

Using the exact `L_Y`, the U-side floor from the exact ledgers, and the X-side duplicate-support floor:

- lambda=3: the score lower bound exceeds C0 throughout `p>=4,rho>=p+2`;
- lambda=4: only `(p,rho,k)=(4,6,2),(4,6,3)` survive the U-side floor, but both have strictly positive compulsory L_X, so they exceed C0;
- lambda=5: the scalar hand reduction leaves only `(p,rho,k)=(4,6,1)` at exact score equality.

In the lambda=5 equality state:

- U_o is independent;
- X is independent;
- `H=1`, `J=5`;
- the X--U_o holes are exactly the code-complement matching;
- the unique core witness w is adjacent to z_1,...,z_4 and nonadjacent to z_0.

For every i=1,...,4 the edge `wz_i` must be critical. A witness adjacent to w and nonadjacent to z_i cannot exist because w's only X-neighbour h_0 is adjacent to z_i. In the reverse orientation any possible matched head h_j, j!=i, has at least three common U_o neighbours with w. Thus no singleton orientation exists. Contradiction.

Therefore:

`ZERO-BUFFER SMALL-LAMBDA CLOSURE: no above-M candidate exists in this branch for lambda<=5.`

## Lambda=6 exact scalar frontier

Write `rho=p+s`, `s>=2`. The exact score floors are increasing in p on the allowed region, so p=4.

At p=4, with case A `k>=s-1` and case B `k<=s-2`, define the U-side score differences from C0:

A:
`D_A=k^2-ks-5k+2s^2+2s-26`;

B:
`D_B=k^2-ks-6k+2s^2+3s-27`.

The duplicate-support X-slack raw floors are

A:
`X_A=k^2-3ks+11k-4s+16`;

B:
`X_B=k^2-3ks+10k-3s+15`.

A candidate requires `D_A+[X_A]_+<=0` or `D_B+[X_B]_+<=0`.

For `s>=4` the integer minima are positive. The only remaining states are

- `(p,rho,k)=(4,6,1)`;
- `(4,6,2)`;
- `(4,7,1)`;
- `(4,7,2)`.

These are scalar necessity states, not realizability claims.

## Preserved package

`project/research/post_ms/2026-09-19-zero-buffer-outside-independence-v1/`

- `ZERO_BUFFER_OUTSIDE_INDEPENDENCE_AND_LAMBDA5_CLOSURE.md`
- `check_zero_buffer_outside_independence.py`

The checker is arithmetic audit support only. It independently verifies the lambda=3/4 empty scalar sets after the new floors, the unique lambda=5 equality state before its raw criticality rejection, and the four lambda=6 scalar states.

## Immediate frontier

Attack lambda=6 in this order:

1. `(4,6,2)` — minimal support, `e(X)=0`, and the score window gives only a few possible values of H and J; use forced W_0--U_o edges and the Unit-VIII criticality template.
2. `(4,6,1)` — also minimal support; quantify how many extra H/J holes are permitted by the score identity and show whether any W_0--U_o edge can remain critical.
3. `(4,7,1)` and `(4,7,2)` — one duplicate U_o code vertex only, so `e(X)<=k`; classify where that duplicate may lie and whether it can repair the criticality obstruction.

Only after these four states are exhausted should the branch advance to lambda=7. Do not move to z=2.

<!-- CURRENT-STATUS:END -->
