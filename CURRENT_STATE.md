# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** Sufficiently-large/eventual second-extremal diameter-2-critical classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 strengthening is not assumed. The published 2024 `X_3` graph (`n=12,m=32`) remains a mandatory hostile control. Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_ZERO_BUFFER_CODE_SIMPLEX_LAMBDA3_LAST_STATE_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `77ca7487e18c82d5411ed5ee92477b517f4b4f40`

LAST VERIFIED RESULT: `Raw criticality of every zero-buffer b--U_o edge forces U_o anticomplete to Y and complement-code witnesses in X. Together with the already-proved buffer--X reverse collapse, this gives exact support duality between X and U_o. The matched crossing heads/core heads force the exact X-code simplex {0,e_1,...,e_p}, so u_o>=p+1 and p>=4. Hence Y is anticomplete to all U, L_Y=rho*y exactly, and the physical A--U hole ledger strengthens to Z>=yu+k(x-1)+max(x,u_o). The resulting quadratic score gate closes lambda=1 and lambda=2 (lambda=0 was already closed). Lambda=3 collapses to (p,rho,k)=(4,6,1),(4,6,2),(4,6,3); minimal-support extra slack closes k=3, minimal-support X-independence plus the rooted residual ledger closes k=2. The sole remaining lambda=3 state is (p,rho,k)=(4,6,1), with exactly six possible (delta,E_U,q,L_X) score tuples.`

UNPRESERVED WORK: `None. The hand derivation and arithmetic diagnostic are preserved under project/research/post_ms/2026-09-19-zero-buffer-code-simplex-v1/.`

DEFERRED ADMIN: `README remains lower-frequency. Do not spend this mathematics cadence on reviewer/CI packaging unless repository integrity fails; refresh reviewer-facing status at the next daily adversarial checkpoint.`

NEXT ACTION: `Stay on the sole lambda=3 zero-buffer state (p,rho,k)=(4,6,1). Attack the delta=7 equality tuple first: (delta,E_U,q,L_X)=(7,7,19,0), where the U graph is at its coarse maximum q=19 subject to the two forced U-holes, X is independent, the simplex/complement support is exact, and U_o is very dense. Apply raw triangle-edge criticality to U_o--U_o and W_0--U_o edges and preserve the first forced extra hole/slack or contradiction. Then test the five delta=8/9 tuples. Only after this lambda=3 residue is exhausted should the zero-buffer branch advance to lambda=4 or positive buffer slack; do not move to z=2.`

## Mandatory audit reconciliation

Before forward mathematics this run, `CURRENT_STATE.md`, `README.md`, recent commits, the 19 September daily red-team audit/handoff, the repaired source-premise note, and the independent actual-D2C Hall/pair-capacity regression were reread.

The audit priority order remains binding. The raw distinct-source premise is proved from beta singleton criticality; selected `(source,coordinate)` uniqueness is a selected-representative convention; the finite source-tuple capacity theorem is not treated as unconditional graph closure. The actual-D2C regression reaches the rooted residual identities, codes, Hall cuts and exact `Ccap_P`, reports zero graph/formula mismatches, and retains `X_3`. No actual rigid complete Hall cut with `x>=3` has been found, so the current one-code results remain conditional hand implications. The four-exception gate remains subordinate. No weakened/invalidated line was resumed.

This run did not need the finite source-tuple theorem: the advance comes from raw `b--U_o` criticality plus physical Boolean-code incidence.

## Mandatory negative control

`X_3`: `n=12`, `m=32>M(12)=31`, canonical root `a=3,b=8,p=4,u=0,Q=12,r=f=delta=0`. Every theorem below requires a nonempty zero-buffer unmatched layer with `u_o>=p+1`; `X_3` is untouched.

## Zero-buffer branch retained

Use the unloaded common-buffer branch:

- `X--Y` complete, `x>=3`, Y one code d, `A_bar d=empty`;
- `g=p`, `k=x-p>0`, `x=p+k`;
- `U_-=U_bar d=W_0 dotcup {b}`, `|W_0|=k`, `e(G[U_-])=0`;
- `epsilon_b=0`, so b is complete to X and U_o and anticomplete to Y;
- `rho:=u-k=u_o+1`, hence `u=k+rho`, `y=p+rho-lambda-1`;
- every buffer--X edge has an outside witness in U_o;
- `E_core=k(p+k-1)+H_core`, `H_core>=k`, hence `E_core>=k(p+k)`.

## New raw b--U_o criticality theorem

For every `z in U_o`, the edge bz has only one possible triangle-edge orientation:

`ba_z in E`, `za_z notin E`, `N(z) cap N(a_z)={b}`

with `a_z in X`. The reverse orientation would put its A-witness in Y, but then all of X would be common neighbours with b.

Consequences:

- `z` is anticomplete to Y;
- `c(a_z)=bar(c(z))`;
- since W_0 and b are already anticomplete to Y, `e(Y,U)=0`;
- `U_d=empty`;
- every Y-source has exact slack `epsilon_y=rho`, so

  `L_Y=y rho=rho(p+rho-lambda-1)`;

- every Y-source has beta load zero.

## Exact code simplex and support duality

Orient tight coordinate i by the gamma-d endpoint `q_i`. Its X-neighbourhood is the singleton `{h_i}`, and the p matched heads are distinct. Therefore

- matched head `h_i` has code `e_i`;
- every core head has code `0^p`.

Thus

`supp_A(X)={0^p,e_1,...,e_p}`

with multiplicities k,1,...,1.

Every x in X has a buffer-edge witness in U_o of complementary code, and every z in U_o has the new b--z witness in X of complementary code. Hence

`supp_U(U_o)={1^p,1^p-e_1,...,1^p-e_p}`.

Therefore

`u_o>=p+1`, equivalently `rho>=p+2`.

The outside pair P must be disjoint from all X pairs. Direct pair-space inspection excludes p=1,2,3, so

`p>=4`.

## Physical hole/rooted-residual strengthening

Y contributes all `yu` A--U holes. The k core witnesses contribute exactly `k(x-1)` X--W_0 holes. In X--U_o, the buffer-X certificates cover every X row by a hole and b--U_o criticality covers every U_o column by a hole, so there are at least `max(x,u_o)` such holes.

Hence

`Z>=yu+k(x-1)+max(x,u_o)`.

Since `Z=u(p-lambda)+2q+E_U` and `y-(p-lambda)=u_o`,

`2q+E_U>=u u_o+k(x-1)+max(x,u_o)`.

This is the live rooted residual bridge.

## Quadratic score gate and small-lambda closure

The disjoint physical costs give

`S>=k(p+k)+rho(p+rho-lambda-1)`,

and simultaneously

`S>=k(p+k)+max{p(p-1),rho(p+rho-lambda-1)}`.

Comparing with

`C0=(lambda+3)p+(lambda+2)u-2 floor((lambda+1)^2/4)-4`

gives the hand necessary condition

`(k+rho-lambda-3)p + k(k-lambda-2) + rho(rho-2lambda-3) + 2 floor((lambda+1)^2/4)+4 <=0`.

With `p>=4`, `rho>=p+2`:

- lambda=1 is impossible;
- lambda=2 is impossible;
- lambda=0 was already impossible from the previous checkpoint.

Thus the zero-buffer branch is closed for `lambda<=2`.

For lambda=3 the gate forces exactly

`p=4`, `rho=6`, `k in {1,2,3}`.

## Minimal-support layer rho=p+2

When `rho=p+2`, U_o has exactly one vertex in every complementary simplex code. Let z_0 be the unique vertex complementary to the core code `0^p`.

Every core head must use z_0 as its buffer-X witness. Thus z_0 is nonadjacent to all k core heads and all k corresponding W_0 vertices, and it is anticomplete to Y. Its degree identity forces

`epsilon_{z_0}>=k`.

Hence

`S>=k(p+k)+L_Y+k`.

This closes the lambda=3,k=3 state: its lower score is 60 while C0=57.

In the same minimal-support layer, X has no internal edge:

- its simplex codes are noncomplementary for p>=4, so no direct X-edge;
- all matched gamma codes are d/bar d, so no matched witness can serve an X-source;
- the unique A/U witness of complementary code for each X-source is already the buffer-edge witness with fixed common neighbourhood `{b}` and cannot certify a different X-edge.

Therefore `e(X)=0`, and with `e(Y)=0` and X--Y complete,

`f=xy`.

For lambda=3,p=4,rho=6,k=2 this gives f=36. The physical hole ledger requires `2q+E_U>=56`, while `E_U>=14`, `delta<=10`, and the residual identity gives `q+E_U=24+delta`, hence `2q+E_U<=54`. Contradiction. So k=2 is closed.

## Sole lambda=3 residue

Only

`(lambda,p,rho,k)=(3,4,6,1)`

remains in the zero-buffer branch.

Its exact data are

- `u=7`, `u_o=5`, `x=5`, `y=6`, `a=11`, `n=27`;
- `f=30`, `D_M=10`;
- `L_Y=36`, `E_U>=6`;
- `2q+E_U>=44`;
- `S=2delta+29`;
- `q=e(G[U])<=19`, because `U` has seven vertices and at least the forced nonedges `wb` and `wz_0`;
- `q+E_U=19+delta`.

Thus `delta in {7,8,9}` and exactly six algebraic/physical score tuples remain:

`(delta,E_U,q,L_X)`

- `(7,7,19,0)`;
- `(8,8,19,1)`, `(8,9,18,0)`;
- `(9,9,19,2)`, `(9,10,18,1)`, `(9,11,17,0)`.

These are necessity states, not graph realizability claims.

## Preserved evidence

New package:

`project/research/post_ms/2026-09-19-zero-buffer-code-simplex-v1/`

- `ZERO_BUFFER_CODE_SIMPLEX_AND_SMALL_LAMBDA_CLOSURE.md`
- `check_zero_buffer_code_simplex.py`

The checker is arithmetic audit support only. It verifies the quadratic algebra, bounded small-lambda reduction, lambda=3 k=2/k=3 arithmetic, and the six final score tuples. It is not a D2C realizability proof.

## Immediate frontier

Attack the delta=7 equality state first. It has

`(delta,E_U,q,L_X)=(7,7,19,0)`.

At the coarse physical ledger level U is missing only the two already-forced U-edges, X has zero slack and no internal edges, and the five U_o code classes are fixed. The next highest-value move is raw triangle-edge criticality on the dense U_o--U_o and W_0--U_o edge set. A single forced additional U-hole or slack unit may remove this equality state; then test the five delta=8/9 states.

Do not move to `z=2` while this residue is live. If lambda=3 closes, advance to lambda=4 within the same zero-buffer/code-simplex framework before abandoning the branch.

<!-- CURRENT-STATUS:END -->
