# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** Sufficiently-large/eventual second-extremal diameter-2-critical classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 strengthening is not assumed. The published 2024 `X_3` graph (`n=12,m=32`) remains a mandatory hostile control. Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_ZERO_BUFFER_COMPLETE_CLOSURE_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `d533b50323aa7576c6bdb2078674b36f18379131`

LAST VERIFIED RESULT: `The zero-buffer g=p subbranch of the rigid one-code unloaded common-buffer geometry is now closed for every admissible lambda, not merely lambda<=6. Raw criticality first forces X--U_o anticomplete: one orientation is killed by the root/buffer or by code complementarity into U_bar d, while the reverse orientation has no A/U witness and any matched foot would require gamma=c(x), impossible because g=p gives only gamma codes d,bar d and X contains neither. The same classification then forces X independent. Consequently every unmatched vertex except b has degree one in A union U, so E_U=(u-1)(p+u-2), q=rho-1, L_Y=rho y and L_X=x lambda+k(x-1) exactly. The score gap factors as S-C0=2[H_lambda+(k-1)(k+p+rho-2)+(rho-p-2)+rho(y-2)+3]. This is positive for y>=2; when y=1, lambda=p+rho-2>=2p and H_lambda>=p^2+p, so the gap is again positive. Hence no above-M candidate realizes zero buffer slack.`

UNPRESERVED WORK: `None. The X--U_o anticompleteness theorem, X independence, exact slack/score identities, universal score-gap factorization and arithmetic diagnostic are preserved under project/research/post_ms/2026-09-19-zero-buffer-complete-separation-v1/.`

DEFERRED ADMIN: `README remains lower-frequency. Refresh reviewer-facing status at the next daily adversarial checkpoint; do not spend the mathematics cadence on packaging or CI churn unless repository integrity fails.`

NEXT ACTION: `Do not return to zero buffer or the closed mixed {4,5} ladder. Resume the corrected unloaded common-buffer branch with positive buffer slack t=p-g>=1. Re-read COMMON_BUFFER_X_EDGE_CRITICALITY_REPAIR.md and COMMON_CORE_EXACT_SLACK_AND_REVERSE_DEFICIT.md, retain the corrected matched/outside witness dichotomy, and classify the first positive-buffer geometry before scalar relaxation. Intersect it locally with exact Ccap_P, ONE-P and CROWD, then feed surviving physical holes/slack through the rooted residual ledger. Keep the four-exception gate subordinate and do not move to z=2 while this positive-buffer branch remains live.`

## Mandatory audit reconciliation

Before forward mathematics this run, `CURRENT_STATE.md`, root `README.md`, latest commits, the 19 September daily red-team audit/handoff, the source-premise repair and the independent actual-D2C Hall/pair-capacity regression were reread.

The audit priority remains binding. Distinct physical beta sources and selected `(source,coordinate)` uniqueness are repaired at the exact raw/selected interface; the finite source-tuple theorem is not promoted as unconditional graph closure. The independent actual-D2C regression retains `X_3`, reaches rooted partitions, slots, codes, Hall objects and exact `Ccap_P`, and has no recorded graph/formula mismatch. No actual rigid complete Hall cut with `x>=3` has been found, so all rigid one-code conclusions remain conditional hand implications. Exact pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)` remain valid; the four-exception gate remains subordinate.

The departure from the predecessor's lambda=7 state-by-state plan is mathematically forced by a stronger raw theorem: the first criticality classification proves `X--U_o` is empty for the whole zero-buffer branch. Continuing the lambda=7 finite geometry after that discovery would preserve a superseded frontier rather than follow the strongest verified structure.

## Mandatory negative control

`X_3`: `n=12`, `m=32>M(12)=31`, canonical root `a=3,b=8,p=4,u=0,Q=12,r=f=delta=0`. The zero-buffer theorem below requires the rigid one-code unmatched/common-buffer structure with `k>0` and `u_o>=p+1`; it does not apply to `X_3`.

## Retained zero-buffer hypotheses

Inside the unloaded common-buffer zero-slack branch:

- `X--Y` complete, `x=p+k`, `k>0`, `y>0`;
- all Y vertices have code d, while X has neither d nor bar d;
- `g=p`, so every matched endpoint has gamma code d or bar d;
- `U_-=U_bar d=W_0 dotcup {b}`, `|W_0|=k`, and `U_-` is independent;
- b is complete to X and U_o, anticomplete to Y;
- Y is anticomplete to all U;
- every W_0 vertex has one graph-fixed X core head;
- U_o is independent and `W_0--U_o` is anticomplete;
- `rho=u-k=u_o+1>=p+2`, `p>=4`;
- `y=p+rho-lambda-1>=1`.

## New theorem 1: X--U_o anticompleteness

For `x in X`, `z in U_o`, suppose `xz` is an edge. It lies in a triangle through b.

In the orientation `t~x`, `t!~z`, `N(z) cap N(t)={x}`:

- a B-witness shares the root with z;
- an X-witness shares b with z;
- a Y-witness of code d would have to be code-complementary to z, forcing `c(z)=bar d` and hence `z in U_-`.

In the reverse orientation `t~z`, `t!~x`, `N(x) cap N(t)={z}`:

- the root has many common B-neighbours with x;
- a Y-witness is not adjacent to z;
- an X-witness shares every Y vertex with x;
- b is adjacent to x, W_0 is anticomplete to U_o, and U_o is independent;
- a matched foot q would force `c(x)=gamma(q)`, but at g=p every gamma code is d or bar d, neither present in X.

Thus

`e(X,U_o)=0`.

## New theorem 2: X is independent

If `xx'` were an internal X-edge, one singleton orientation must have a witness adjacent to one endpoint and nonadjacent to the other.

- Y and b are adjacent to both endpoints;
- another X-witness has b and all of Y as extra common neighbours;
- U_o is anticomplete to X;
- a W_0 witness would force the source code to be d by tight-coordinate complementarity;
- a matched foot would force the source code to equal a gamma code in `{d,bar d}`.

All possibilities contradict the retained X-code support. Hence

`e(X)=0`.

## Exact unmatched and A-side ledgers

Every `w in W_0` now has exactly one neighbour in `A union U`, its core head. Every `z in U_o` has exactly one neighbour in `A union U`, namely b. The buffer has zero slack.

Therefore

`q=e(G[U])=u_o=rho-1`,

`E_U=(u-1)(p+u-2)`.

For Y,

`L_Y=rho y`.

For X, summing degrees over the complete X--Y cut, the x buffer edges and the k core-head edges gives

`L_X=x lambda+k(x-1)`.

Hence the total score is exact:

`S=(u-1)(p+u-2)+rho y+x lambda+k(x-1)`.

## Universal zero-buffer score gap

Let

`H_lambda=floor((lambda+1)^2/4)`

and use the preserved above-M ceiling

`C0=(lambda+3)p+(lambda+2)u-2H_lambda-4`.

With `u=k+rho`, `x=p+k`, `y=p+rho-lambda-1`, exact expansion gives

`S-C0`

`=2[H_lambda+(k-1)(k+p+rho-2)+(rho-p-2)+rho(y-2)+3]`.

If `y>=2`, the bracket is at least 3, contradiction.

If `y=1`, then `lambda=p+rho-2>=2p`, so

`H_lambda>=floor((2p+1)^2/4)=p^2+p`.

The bracket reduces to

`H_lambda+(k-1)(k+p+rho-2)-p+1>=p^2+1>0`.

Thus:

`ZERO-BUFFER COMPLETE CLOSURE: no above-M candidate realizes the rigid one-code unloaded common-buffer branch with g=p.`

The prior lambda=0,...,7 staircase is subsumed by this theorem.

## Preserved package

`project/research/post_ms/2026-09-19-zero-buffer-complete-separation-v1/`

- `ZERO_BUFFER_COMPLETE_SEPARATION_AND_CLOSURE.md`
- `check_zero_buffer_complete_separation.py`

The checker is arithmetic audit support only; the criticality theorems and score factorization above are the proof.

## Immediate frontier

The zero-buffer route is finished. Return to positive buffer slack `t=p-g>=1` in the corrected `r=0` common-buffer branch. Preserve the repaired two-orientation buffer-X criticality theorem: at most g reverse matched heads exist, while the remaining buffer-X edges use either matched feet with the appropriate gamma code or outside unmatched witnesses that create physical Y-holes/slack. Do not scalarize away the one-code pair before using exact `Ccap_P`, `(ONE-P)` and `(CROWD)`. The desired next milestone is a compact positive-buffer structural dichotomy that either forces a quadratic local score payment or sharply parameterizes the surviving geometry for the rooted residual ledger.

<!-- CURRENT-STATUS:END -->
