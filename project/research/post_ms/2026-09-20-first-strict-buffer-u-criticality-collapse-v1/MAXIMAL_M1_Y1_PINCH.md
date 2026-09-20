# Final maximal-selection one-witness slice: y=1 pinches to one parameter point

Date: 2026-09-20

Status: internal conditional structural reduction. It treats the only one-witness slice left after `MAXIMAL_M1_YGE2_CLOSURE.md`.

## 1. Setup and internal-X bound

Under maximal witness selection, `m=1` gives `T=0`, `U_o={z}`, `u=k+2`. The all-R arm is empty, so this is all-F. Put `Y={y}` and `X'=X\{a_0}`.

The same-code/raw-criticality argument used in `MAXIMAL_M1_X_COLLAPSE.md` does not require y>=2 for the following two facts: one Y-vertex is already an illicit extra common neighbour when needed. Thus

- `G[X']` is edgeless;
- `d_{X'}(a_0)<=1`.

Write `t=e(X)`, so

> `0<=t<=1`.                                             `(Y1-T)`

The aggregate X--U edge count is exact even though the k core heads need not saturate X': b contributes x-1 edges, the k core vertices contribute exactly one distinct head edge each, and z contributes none. Hence

`e(X,U)=x-1+k`.

Since every X-vertex is adjacent to y and the only internal-X contribution is t,

> `E_X=x(p+k)-k+1-2t`.                                  `(Y1-EX)`

Also

`epsilon_y=p-g+2`,

while the exact U-ledger remains

`E_U=(k+1)(p+k)+(p-g+1)`, `q=1`.

## 2. Total-score and rooted constraints

Here

`lambda=2p-g`, `x=k+g`.

Let `eta` be 1 when `lambda+1` is odd and 0 otherwise. Comparing the weakest exact degree ledger `E_X+epsilon_y+E_U` with C0 gives

> `eta-g^2-4gk+2g-4k^2+4k+4p+4t-9 >=0`.              `(Y1-SCORE)`

The exact rooted ledger gives

> `r=gk+gp+g+k^2+k-p^2+2 >=0`.                         `(Y1-R)`

Put `s=p-g>=1`. Since `t<=1` and `eta<=1`, `(Y1-SCORE)` implies

> `4s >= (g+2k-3)^2+8k-5`.                             `(Y1-S)`

while `(Y1-R)` is exactly

> `s(s+g) <= (k+1)(g+k)+2`.                            `(Y1-RS)`

## 3. k must equal one

From `(Y1-S)`, for `k>=2` we have the integer lower bound

`s>=2k-1`.

Then the left side of `(Y1-RS)` is at least `(2k-1)(2k-1+g)`. Minus its right side this equals

`gk-2g+3k^2-5k-1`,

which is positive already for k=2 and remains positive for all k>=2, g>=0. Contradiction.

Hence

> `k=1`.                                                 `(Y1-K1)`

Since `x=k+g>=3`, `g>=2`.

## 4. Only three arithmetic points survive score plus r>=0

With k=1,

`4s >= (g-1)^2+3`,

`s(s+g)<=2g+4`.

If `g>=4`, the score bound gives `s>=g-1`, while

`(g-1)(2g-1)>2g+4`,

contradicting the rooted bound. Therefore `g in {2,3}`.

- `g=2` gives `s in {1,2}`, hence `(p,k,g)=(3,1,2)` or `(4,1,2)`;
- `g=3` forces `s=2`, hence `(p,k,g)=(5,1,3)`.

The latter two points have exact `r=0`. But the all-F Hamming-slot theorem gives

`r>=x+[p-1-floor((p-2)/x)]>0`,

so both are impossible.

Thus the entire maximal one-witness branch is reduced to the single parameter point

> `(p,k,g,x,y,u,lambda)=(3,1,2,3,1,3,4)`.             `(Y1-POINT)`

At this point

> `q=1`, `r=5`.

Finally `(Y1-SCORE)` shows that t=0 would exceed the available score, so

> `e(X)=t=1`.                                            `(Y1-EDGE)`

Therefore `a_0` has exactly one neighbour in X'.

## 5. Remaining literal geometry

The one-witness first-strict problem is no longer asymptotic. Under maximal representative selection, all y>=2 cases are empty and y=1 reduces to one order-14 rooted parameter point with p=3, one common-core vertex, two non-buffer core-code dimensions `g=2`, one outside witness, q=1, r=5 and exactly one internal X-edge.

The next task is a direct raw-criticality reconstruction of this single geometry. If it fails, maximal-selection `m=1` is completely closed and the live first-strict frontier moves to `m>=2`.
