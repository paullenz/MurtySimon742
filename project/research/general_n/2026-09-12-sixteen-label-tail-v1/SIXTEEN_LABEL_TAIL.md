# A sixteen-label threshold-tail bound

12 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate structural theorem. Independent specialist review and novelty assessment remain OPEN.** The proof uses monotone clipping down to a finite 4,845-state max-five terminal domain. No exhaustive 300-million-profile scan is a proof premise.

## 1. Statement

For `h>=2`, define

\[
C_h(z)=\frac{z(z-1)+h(h+1)}2,
\]

and let `gamma_h(W)` be the least integer `z>=h` with `W<=C_h(z)` for `W>0`, with `gamma_h(0)=0`.

For sixteen demands `0<=s_i<=15`, put

\[
N_h=\#\{i:s_i\ge h\},\qquad W_h=\sum_{s_i\ge h}s_i,
\qquad p=N_1,
\]

\[
D(s)=\sum_{h=2}^{15}(N_h-\gamma_h(W_h)),
\qquad Q(s)=p+D(s).
\]

Then

\[
\boxed{D(s)\le13,\qquad Q(s)\le29.}
\tag{1.1}
\]

Moreover equality holds exactly for

\[
\boxed{4^{16},\qquad5^{16}.}
\tag{1.2}
\]

## 2. High levels are harmless

For `h>=11`, write `N_h=h+e` when `N_h>=h`. Since there are sixteen labels,

\[
0\le e\le16-h\le5.
\]

Exactly as in the fourteen- and fifteen-label arguments,

\[
2hN_h-2C_h(N_h-1)=-e^2+3e+2h-2>0.
\]

Hence

\[
N_h-\gamma_h(W_h)\le0\qquad(h\ge11),
\]

and clipping every demand above ten down to ten cannot decrease `D`.

## 3. Monotone clipping 10 -> 9 -> 8 -> 7 -> 6 -> 5

Suppose the current maximum is `M` with `k` entries equal to `M`, and replace them by `M-1`. The disappearing loss is

\[
L_M(k)=k-\gamma_M(Mk).
\]

For every lower level `h<M`, the tail weight drops by exactly `k`. The actual lower-tail weight lies in

\[
Mk\le W_h\le Mk+(M-1)(16-k).
\]

Taking the minimum gamma drop on the whole safe interval yields the complete positive-loss table:

| `M` | positive-loss `k` values | losses | guaranteed lower-level gains |
|---:|---|---|---|
| 10 | 16 | 1 | 8 |
| 9 | 15,16 | 1,1 | 5,7 |
| 8 | 14,15,16 | 1,1,1 | 4,6,7 |
| 7 | 13,14,15,16 | 1,1,2,2 | 4,5,5,6 |
| 6 | 11,12,13,14,15,16 | 1,1,1,2,2,3 | 1,4,4,4,4,6 |

Every guaranteed gain is at least the disappearing loss. Thus each clipping step

\[
10\to9\to8\to7\to6\to5
\]

is nondecreasing for `D`.

This is the final label count for which the same safe-interval clipping mechanism works without repair; the corresponding `a=17` step fails at `(M,k)=(6,11)`, recorded separately as the next research obstruction.

## 4. Terminal max-five domain

After clipping, all demands lie in `{0,1,2,3,4,5}`. Put

\[
x=N_2,\quad y=N_3,\quad z=N_4,\quad w=N_5,
\]

so

\[
0\le w\le z\le y\le x\le16.
\]

The tail weights are

\[
W_2=2x+y+z+w,
\]
\[
W_3=3y+z+w,
\]
\[
W_4=4z+w,
\]
\[
W_5=5w.
\]

Therefore

\[
\begin{aligned}
D={}&x+y+z+w
-\gamma_2(2x+y+z+w)
-\gamma_3(3y+z+w)\\
&-\gamma_4(4z+w)
-\gamma_5(5w).
\end{aligned}
\tag{4.1}
\]

There are only

\[
\binom{20}{4}=4845
\]

integer quadruples in this domain. Exact substitution in (4.1) gives

\[
D\le13,
\]

with equality only at

\[
(x,y,z,w)=(16,16,16,0),
\qquad(16,16,16,16).
\]

These are precisely

\[
4^{16},\qquad5^{16}.
\]

Since `p<=16`, (1.1) follows.

## 5. Equality cannot lift through 6 -> 5

If `Q=29`, then `p=16` and `D=13`, so every clipping stage preserves equality.

The terminal equality vector `4^16` has no five and therefore cannot have a max-six preimage under the final `6->5` clipping.

For `5^16`, replace `j=1,...,16` of its fives by sixes. The resulting `D` values are

```text
8,7,8,9,9,10,10,10,9,9,10,10,10,10,9,10.
```

None equals 13. Therefore no equality vector can contain a six immediately before the final clipping step, and hence no original equality vector can contain any demand at least six.

Thus (1.2) is the complete equality classification.

## 6. Graph transfer when a=16

Under the canonical bridge let

\[
a=n-1-\Delta=16,
\qquad b=\Delta,
\qquad t=e(G)-17b>0.
\]

Residual activity, threshold capacity and the demand ledger give exactly as before

\[
Q(s)\ge b+2t.
\]

Combining with (1.1), every positive-surplus `a=16` bridge image satisfies

\[
\boxed{b+2t\le29.}
\tag{6.1}
\]

If equality holds, the demand multiset is exactly `4^16` or `5^16`.

## 7. First obstruction at a=17

The clean clipping mechanism used for `a=12,...,16` does **not** continue unchanged.

For seventeen labels, the proposed `6->5` clipping with exactly eleven sixes has

```text
L_6(11)=1,
```

but the safe lower-level gamma-drop sum can be zero. Thus clipping can decrease `D` in that local configuration, and the proof architecture genuinely needs a new ingredient from `a=17` onward.

This is a useful falsification result: the sequence of tail theorems is not being extrapolated blindly. The next symbolic target is to understand or repair precisely this `(a,M,k)=(17,6,11)` obstruction.

## 8. Trust boundary

The proof-critical finite arithmetic consists only of:

1. the safe clipping table in Section 3;
2. the 4,845 terminal quadruples in Section 4;
3. the sixteen equality preimages in Section 5.

The graph transfer remains conditional on the canonical selected/residual bridge and threshold-capacity lemma.