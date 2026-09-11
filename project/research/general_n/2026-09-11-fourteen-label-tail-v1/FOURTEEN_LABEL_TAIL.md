# A fourteen-label threshold-tail bound

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal review: ChatGPT/Geeps.

**Status: candidate hand lemma. Independent specialist review and novelty assessment OPEN.** The exact programs in this directory are regressions only; the proof below is intended to stand without proof-critical enumeration.

This is the next symbolic extension of the twelve- and thirteen-label threshold-tail arguments.

## 1. Definitions and claim

For `h>=2`, define

\[
C_h(z)=\frac{z(z-1)+h(h+1)}2,
\qquad \gamma_h(0)=0,
\]

and for `W>0` let `gamma_h(W)` be the least integer `z>=h` with `W<=C_h(z)`.

For fourteen demands `0<=s_i<=13`, put

\[
N_h=\#\{i:s_i\ge h\},\qquad
W_h=\sum_{s_i\ge h}s_i,\qquad p=N_1,
\]

\[
D(s)=\sum_{h=2}^{13}\bigl(N_h-\gamma_h(W_h)\bigr),
\qquad Q(s)=p+D(s).
\]

Then

\[
\boxed{D(s)\le9,\qquad Q(s)\le23.}
\]

Moreover

\[
\boxed{Q(s)=23}
\]

holds exactly for the following three multisets:

\[
3^{14},\qquad 3\,4^{13},\qquad 4^{14}.
\tag{1.1}
\]

## 2. Levels at least nine are harmless

Fix `h>=9` and put `N=N_h`. If `N=0`, the deficit is zero. If `0<N<h`, then `gamma_h>=h>N`, so the deficit is negative.

If `N>=h`, write `N=h+e`. Since there are fourteen labels,

\[
0\le e\le14-h\le5.
\]

A positive deficit would require `gamma_h<=N-1`, hence `hN<=C_h(N-1)`. But

\[
2hN-2C_h(N-1)=-e^2+3e+2h-2.
\]

This concave quadratic is positive throughout `0<=e<=5`: its endpoint values are `2h-2` and `2h-12`, the latter at least six. Thus

\[
N_h-\gamma_h(W_h)\le0\qquad(h\ge9).
\]

Therefore clipping every demand above eight down to eight cannot decrease `D`: all lower tail counts stay fixed, their weights decrease, and the removed high-level deficits were nonpositive.

## 3. Clip 8,7,6,5,4 down one level

Suppose the current maximum is `M`, with `k` entries equal to `M`, and replace those `k` entries by `M-1`. At the disappearing level `M`, the largest possible deficit is

\[
L_M(k)=k-\gamma_M(Mk).
\]

At every lower level `h<M`, the tail weight falls by exactly `k`, while `N_h` is unchanged. Hence the gain in the lower deficit is

\[
\gamma_h(W_h)-\gamma_h(W_h-k).
\]

For fixed `M,k`, the actual `W_h` lies in the safe interval

\[
Mk\le W_h\le Mk+(M-1)(14-k).
\tag{3.1}
\]

so it is enough to take the minimum gamma drop over that whole interval. The only cases in which the disappearing deficit is positive are the following. The last column is the sum, over `2<=h<M`, of those safe minimum lower-level gamma drops.

| `M` | `k` | disappearing loss `L_M(k)` | guaranteed lower-level gain |
|---:|---:|---:|---:|
| 8 | 14 | 1 | 6 |
| 7 | 13 | 1 | 5 |
| 7 | 14 | 1 | 6 |
| 6 | 11 | 1 | 3 |
| 6 | 12 | 1 | 4 |
| 6 | 13 | 1 | 4 |
| 6 | 14 | 2 | 5 |
| 5 | 10 | 1 | 3 |
| 5 | 11 | 1 | 3 |
| 5 | 12 | 2 | 3 |
| 5 | 13 | 2 | 3 |
| 5 | 14 | 3 | 4 |
| 4 | 9 | 1 | 2 |
| 4 | 10 | 1 | 2 |
| 4 | 11 | 2 | 2 |
| 4 | 12 | 2 | 2 |
| 4 | 13 | 3 | 3 |
| 4 | 14 | 3 | 3 |

Each guaranteed gain is at least the disappearing loss. If `L_M(k)<=0`, there is nothing to pay. Consequently each clipping step

\[
8\to7\to6\to5\to4\to3
\]

is nondecreasing for `D`.

Every entry of the table is direct finite arithmetic from the displayed formula for `C_h`; the regression script recomputes the complete safe interval (3.1), not just the tabulated minima.

## 4. The max-three domain

After clipping, let

\[
x=N_2,\qquad y=N_3,
\]

so `0<=y<=x<=14`. Then

\[
D=x+y-\gamma_2(2x+y)-\gamma_3(3y).
\tag{4.1}
\]

For `y<=12`,

\[
\gamma_3(3y)\ge y-3.
\tag{4.2}
\]

Indeed the assertion is trivial for small `y`, and for `7<=y<=12` it follows by testing `z=y-4`, since

\[
3y-C_3(y-4)=\frac{-y^2+15y-32}{2}>0.
\]

Also

\[
\gamma_2(2x+y)\ge x-5
\tag{4.3}
\]

except at `(x,y)=(14,0),(14,1),(14,2),(14,3)`. For the nontrivial range this follows by testing `z=x-6`:

\[
2x+y-C_2(x-6)=\frac{-x^2+17x+2y-48}{2}>0.
\]

The four exceptional pairs have `D=6,4,5,6` by direct substitution. Hence (4.1)-(4.3) give

\[
D\le8\qquad(y\le12).
\]

At `y=13`, direct substitution for the only possibilities `x=13,14` gives `D=8`. At `y=14`, necessarily `x=14`, and

\[
\gamma_2(42)=10,\qquad \gamma_3(42)=9,
\]

so

\[
D=28-10-9=9.
\]

Thus every max-three vector satisfies `D<=9`, with equality only at `3^14`.

Because all preceding clipping steps are nondecreasing for `D`, this proves `D<=9` in the full domain. Since `p<=14`,

\[
Q=p+D\le23.
\]

## 5. Equality classification

Suppose `Q=23`. Then necessarily `p=14` and `D=9`; in particular every demand is positive. Since clipping cannot decrease `D` and the final max-three vector has `D<=9`, every clipping stage must preserve `D=9`, and the final vector is `3^14`.

Immediately before the final `4->3` clipping there can therefore be only threes and fours. If `k` is the number of fours, direct substitution gives, for `k=0,...,14`,

```text
9, 5, 6, 7, 8, 8, 8, 7, 7, 8, 7, 8, 8, 9, 9.
```

Hence `D=9` only for

\[
k=0,13,14,
\]

which are precisely the three profiles in (1.1).

It remains to show that none can have arisen from a demand at least five while preserving `D=9`. The profile `3^14` has no four and hence no max-five preimage. For `3\,4^{13}`, replace `j=1,...,13` of its fours by fives; the resulting `D` values are

```text
5, 6, 7, 6, 7, 7, 6, 6, 6, 7, 7, 8, 8.
```

For `4^14`, replacing `j=1,...,14` fours by fives gives

```text
5, 6, 6, 7, 8, 7, 7, 7, 7, 7, 7, 8, 8, 8.
```

None equals nine. Therefore no equality vector contains a demand at least five, and (1.1) is the complete equality list.

## 6. Graph transfer when a=14

Under the canonical selected/residual bridge, take

\[
a=n-1-\Delta=14,\qquad b=\Delta,
\qquad t=m-b(a+1)>0.
\]

Residual activity and the tail identity give

\[
r=b+\sum_{h=2}^{14}z_h,
\]

threshold capacity gives `z_h>=gamma_h(W_h)`, and the demand ledger gives `S>=r+2t`. Therefore

\[
Q(s)=S-\sum_{h=2}^{13}\gamma_h(W_h)\ge b+2t.
\]

Combining with the hand bound yields the fourteen-label scalar inequality

\[
\boxed{b+2t\le23.}
\tag{6.1}
\]

If equality holds in (6.1), then the demand profile must be one of the three profiles in (1.1). This is the scalar reduction needed for the remaining `n=32, Delta=17` branch.
