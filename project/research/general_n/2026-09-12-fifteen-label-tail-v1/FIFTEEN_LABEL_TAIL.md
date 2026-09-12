# A fifteen-label threshold-tail bound

12 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate structural theorem. Independent specialist review and novelty assessment remain OPEN.** The proof reduces the full demand domain by monotone clipping to a finite 816-triple terminal table. A separate exhaustive 77,558,760-multiset regression is corroboration only.

## 1. Definitions and claim

For `h>=2`, define

\[
C_h(z)=\frac{z(z-1)+h(h+1)}2,
\qquad \gamma_h(0)=0,
\]

and for `W>0` let `gamma_h(W)` be the least integer `z>=h` with `W<=C_h(z)`.

For fifteen demands

\[
0\le s_i\le14,
\]

put

\[
N_h=\#\{i:s_i\ge h\},\qquad
W_h=\sum_{s_i\ge h}s_i,\qquad
p=N_1,
\]

\[
D(s)=\sum_{h=2}^{14}\bigl(N_h-\gamma_h(W_h)\bigr),
\qquad Q(s)=p+D(s).
\]

Then

\[
\boxed{D(s)\le11,\qquad Q(s)\le26.}
\tag{1.1}
\]

Moreover

\[
\boxed{Q(s)=26}
\]

holds exactly for

\[
\boxed{3^2\,4^{13},\qquad 4^{15}.}
\tag{1.2}
\]

## 2. Levels h>=10 are nonpositive

Fix `h>=10` and write `N=N_h`. If `N=0`, the deficit is zero. If `0<N<h`, then `gamma_h>=h>N`.

If `N>=h`, write `N=h+e`. Since there are fifteen labels,

\[
0\le e\le15-h\le5.
\]

A positive deficit would require `gamma_h<=N-1`, hence `hN<=C_h(N-1)`. But

\[
2hN-2C_h(N-1)=-e^2+3e+2h-2.
\]

This concave quadratic is positive at both endpoints of `0<=e<=5`; at `e=5` it is `2h-12>=8`. Thus

\[
N_h-\gamma_h(W_h)\le0\qquad(h\ge10).
\]

Therefore clipping every demand above nine down to nine cannot decrease `D`.

## 3. Monotone clipping 9 -> 8 -> 7 -> 6 -> 5 -> 4

Suppose the current maximum demand is `M`, with exactly `k` entries equal to `M`, and replace those `k` entries by `M-1`.

At the disappearing level `M`, the largest possible loss is

\[
L_M(k)=k-\gamma_M(Mk).
\]

At every lower level `h<M`, `N_h` is unchanged while `W_h` falls by exactly `k`, so the gain in the lower-level deficit is

\[
\gamma_h(W_h)-\gamma_h(W_h-k).
\]

For fixed `M,k`, the actual lower-tail weight lies in

\[
Mk\le W_h\le Mk+(M-1)(15-k).
\tag{3.1}
\]

Taking the minimum gamma drop over this entire safe interval gives the following complete list of positive disappearing losses.

| `M` | `k` values with `L_M(k)>0` | loss(es) | guaranteed total lower-level gain |
|---:|---|---|---|
| 9 | 15 | 1 | 7 |
| 8 | 14,15 | 1,1 | 6,7 |
| 7 | 13,14,15 | 1,1,2 | 5,5,5 |
| 6 | 11,12,13,14,15 | 1,1,1,2,2 | 2,4,4,4,5 |
| 5 | 10,11,12,13,14,15 | 1,1,2,2,3,3 | 2,3,3,3,3,4 |

Every guaranteed gain is at least the disappearing loss. If `L_M(k)<=0`, there is nothing to pay. Hence each clipping step

\[
9\to8\to7\to6\to5\to4
\]

is nondecreasing for `D`.

The checker in this directory recomputes every safe interval in (3.1) exactly; the displayed table is the proof-critical finite arithmetic summary.

## 4. Terminal max-four domain

After clipping, all demands lie in `{0,1,2,3,4}`. Put

\[
x=N_2,\qquad y=N_3,\qquad z=N_4,
\]

so

\[
0\le z\le y\le x\le15.
\]

The tail weights are

\[
W_2=2x+y+z,
\qquad W_3=3y+z,
\qquad W_4=4z,
\]

and therefore

\[
D=x+y+z
-\gamma_2(2x+y+z)
-\gamma_3(3y+z)
-\gamma_4(4z).
\tag{4.1}
\]

There are only

\[
\binom{18}{3}=816
\]

integer triples `0<=z<=y<=x<=15`. Direct exact substitution in (4.1) gives the following maximum for each fixed `z`:

| `z` | `max D` | one maximising `(x,y)` |
|---:|---:|---:|
| 0 | 10 | (15,14) |
| 1 | 7 | (15,15) |
| 2 | 8 | (15,15) |
| 3 | 9 | (15,15) |
| 4 | 9 | (15,14) |
| 5 | 9 | (15,15) |
| 6 | 9 | (15,15) |
| 7 | 8 | (15,14) |
| 8 | 8 | (15,14) |
| 9 | 9 | (15,14) |
| 10 | 9 | (15,15) |
| 11 | 10 | (15,15) |
| 12 | 10 | (15,15) |
| 13 | **11** | **(15,15)** |
| 14 | 10 | (15,14) |
| 15 | **11** | **(15,15)** |

Hence

\[
D\le11.
\]

Equality in the terminal domain occurs only at

\[
(x,y,z)=(15,15,13),\qquad(15,15,15),
\]

which correspond respectively to

\[
3^2\,4^{13},\qquad4^{15}.
\tag{4.2}
\]

Since `p<=15`, (1.1) follows immediately.

## 5. Equality cannot come from a demand >=5

If `Q=26`, then `p=15` and `D=11`. Every clipping step must therefore preserve `D=11`, and the final max-four vector must be one of (4.2).

Immediately before the final `5->4` clipping, the only possible preimages are obtained by raising some of the fours in (4.2) to fives.

For `3^2 4^13`, raising `j=1,...,13` fours to five gives `D` values

```text
6,7,8,7,8,8,8,8,8,9,9,9,9.
```

For `4^15`, raising `j=1,...,15` fours to five gives

```text
7,7,8,9,10,9,9,9,9,9,9,10,9,10,10.
```

None equals 11. Therefore no equality vector can contain a five immediately before the last clipping stage. A fortiori no original equality vector can contain any demand at least five, because all higher demands have already been clipped down to five without decreasing `D`.

Thus (1.2) is the complete equality classification.

## 6. Graph transfer when a=15

Under the canonical selected/residual bridge, let

\[
a=n-1-\Delta=15,
\qquad b=\Delta,
\qquad t=e(G)-b(a+1)=e(G)-16b>0.
\]

Residual activity gives

\[
r=b+\sum_{h=2}^{15}z_h,
\]

threshold capacity gives

\[
z_h\ge\gamma_h(W_h),
\]

and the demand ledger gives

\[
S\ge r+2t.
\]

Therefore

\[
Q(s)=S-\sum_{h=2}^{14}\gamma_h(W_h)
\ge b+2t.
\]

Combining with (1.1), every positive-surplus `a=15` bridge image satisfies

\[
\boxed{b+2t\le26.}
\tag{6.1}
\]

If equality holds in (6.1), the demand multiset is exactly one of

\[
3^2\,4^{13},\qquad4^{15}.
\]

This is the fifteen-label analogue of the twelve-, thirteen- and fourteen-label source-independent tail bounds.

## 7. Significance

The sequence of hand/finite tail theorems now reaches

```text
a=12 : Q<=18
a=13 : Q<=21
a=14 : Q<=23
a=15 : Q<=26
```

The `a=15` proof is not an extrapolation from the earlier orders: it has its own monotone clipping argument and exact terminal reduction. Its finite proof-critical arithmetic is only the safe clipping table and the 816 max-four triples; the full 77,558,760-demand scan is retained solely as a hostile regression.

The next theoretical target is to understand the parameter pattern in these tail bounds rather than merely continue the sequence order by order.

## 8. Trust boundary

The combinatorial tail theorem above is independent of graph computation. Its graph transfer remains conditional on the canonical selected/residual bridge and threshold-capacity lemma.

Independent specialist review should focus on:

1. the safe-interval clipping argument in Section 3;
2. the terminal formula (4.1) and 816-triple table;
3. the equality-preimage exclusion in Section 5;
4. the canonical bridge transfer in Section 6.