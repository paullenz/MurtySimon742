# A thirteen-label threshold-tail bound and its equality case

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal review: ChatGPT/Geeps.

**Status: candidate hand lemma. Independent specialist review and novelty assessment OPEN.** The exact script in this directory is a regression only; the proof below is intended to stand without proof-critical enumeration.

This note extends the source-independent twelve-label tail method by one label. The numerical bound is weaker than the twelve-label bound, but its equality case is rigid enough to close the `n=31, Delta=17, m=240` endpoint.

## 1. Definitions

For each integer `h>=2`, define

\[
C_h(z)=\frac{z(z-1)+h(h+1)}2,
\qquad \gamma_h(0)=0,
\]

and, for `W>0`, let `gamma_h(W)` be the least integer `z>=h` for which

\[
W\le C_h(z).
\]

For thirteen demands `0<=s_i<=12`, put

\[
N_h=\#\{i:s_i\ge h\},\qquad
W_h=\sum_{s_i\ge h}s_i,\qquad p=N_1,
\]

\[
D(s)=\sum_{h=2}^{12}\bigl(N_h-\gamma_h(W_h)\bigr),
\qquad
Q(s)=p+D(s).
\]

We prove

\[
\boxed{D(s)\le 8,\qquad Q(s)\le21,}
\]

and moreover

\[
\boxed{Q(s)=21\iff s_1=\cdots=s_{13}=3.}
\]

The definition of `gamma` has no source-count cutoff. As in the twelve-label transfer, if `gamma_h(W_h)` exceeds the actual number of residual sources, the graph instance is already impossible.

## 2. Levels at least eight are harmless

Let `h>=8` and `N=N_h`. If `N=0`, the deficit is zero. If `0<N<h`, then `gamma_h>=h>N`, so the deficit is negative.

Suppose `N>=h`. Write `N=h+e`, so

\[
0\le e\le 13-h\le5.
\]

Since `W_h>=hN`, a positive deficit would force `gamma_h<=N-1`, hence `hN<=C_h(N-1)`. But twice the strict defect is

\[
2hN-2C_h(N-1)=-e^2+3e+2h-2.
\]

This concave quadratic is positive at both endpoints `e=0,5`: its values are `2h-2` and `2h-12`, the latter at least four. Hence

\[
N_h-\gamma_h(W_h)\le0\qquad(h\ge8).
\]

Therefore clipping every demand above seven down to seven cannot decrease `D`: lower-level counts are unchanged while their tail weights decrease, and all removed higher deficits were nonpositive.

## 3. Clip seven, six, five and four

We now lower the current maximum one level at a time. At a step `M -> M-1`, lower-level `N_h` stay fixed and their `W_h` decrease, so every lower deficit can only improve. We only need to pay for a positive deficit at the disappearing level `M`.

### 3.1 Seven to six

With maximum seven, let `k=N_7`. The level-seven deficit is nonpositive for `k<=12`. At `k=13` it equals one. Then all thirteen entries are seven, and at level six

\[
W_6:91\longrightarrow78,
\qquad
\gamma_6:13\longrightarrow12.
\]

The lost unit is paid exactly.

### 3.2 Six to five

With maximum six, the level-six deficit is positive only for `k=11,12,13`, and is one in each case. If `l` is the number of fives, the possible drops in `gamma_5` are

| `k` | allowed `l` | `gamma_5` drop |
|---:|---:|---:|
| 11 | 0,1,2 | 1,2,1 |
| 12 | 0,1 | 2,1 |
| 13 | 0 | 1 |

Thus six-to-five clipping never decreases `D`.

### 3.3 Five to four

With maximum five, the level-five deficit is one for `k=10,11`, two for `k=12,13`, and nonpositive below that.

For `k=10,11`, the drop in `gamma_4` is always at least one and pays the deficit.

For `k=12,13`, the drop in `gamma_4` is one and the drop in `gamma_3` is at least one. The only possibilities are:

- `k=12,l=0`: at level three, `60 -> 48` (or `63 -> 51` if the remaining entry is three);
- `k=12,l=1`: `64 -> 52`;
- `k=13`: `65 -> 52`.

Direct substitution in `C_3` gives a `gamma_3` drop of at least one in every case. Hence the two lost units are paid.

### 3.4 Four to three

With maximum four, the level-four deficit is

\[
1,1,2,2,3
\]

for `k=9,10,11,12,13` fours respectively, and is nonpositive for `k<=8`. Let `l` be the number of threes.

For `k=9`, the possible `gamma_3` drops for `l=0,1,2,3,4` are

\[
2,1,1,1,1;
\]

for `k=10` and `l=0,1,2,3` they are

\[
1,2,1,1.
\]

These pay the one-unit deficit.

For `k=11`, the `gamma_3` drops for `l=0,1,2` are `2,1,1`. The `l=0` case is already paid; for `l=1,2`, `gamma_2` drops by at least one.

For `k=12`, the `gamma_3` drop is one for both `l=0,1`, and `gamma_2` drops by at least one.

For `k=13`, `gamma_3` drops by two and `gamma_2` drops by two, paying the three-unit deficit.

Thus clipping four to three cannot decrease `D`. Combined with the earlier stages, every demand vector clips to maximum three with `D` nondecreasing.

All numerical statements in this section are one-line substitutions into the capacities `C_h(z)`. The regression script rechecks every current-maximum multiset for these four clipping stages, but the script is not a premise of the proof.

## 4. The max-three domain

After clipping, let

\[
x=N_2,\qquad y=N_3,
\]

so `0<=y<=x<=13`. Then

\[
D=x+y-\gamma_2(2x+y)-\gamma_3(3y).
\tag{4.1}
\]

First,

\[
\gamma_2(2x+y)\ge x-5.
\tag{4.2}
\]

For `x<=7` this is immediate. For `8<=x<=13`, test `z=x-6`; the strict capacity defect is

\[
2x+y-C_2(x-6)
=\frac{-x^2+17x+2y-48}{2}>0,
\]

with positivity following from the endpoints `x=8,13` and `y>=0`.

Second, for `y<=12`,

\[
\gamma_3(3y)\ge y-3.
\tag{4.3}
\]

This is immediate for `y<=6`. For `7<=y<=12`, test `z=y-4`:

\[
3y-C_3(y-4)
=\frac{-y^2+15y-32}{2}>0.
\]

Equations (4.2)-(4.3) already give `D<=8` for `y<=12`. In fact the inequality is strict there. To see this, `gamma_2(2x+y)>=x-4` holds for all `x<=11`, for `x=12,y>=1`, and for `x=13,y>=6`; testing `z=x-5` gives

\[
2x+y-C_2(x-5)
=\frac{-x^2+15x+2y-36}{2}>0.
\]

The omitted cases are `(x,y)=(12,0)` and `(13,0),...,(13,5)`, where direct substitution gives `D<=5`. Hence

\[
D\le7\qquad(y\le12).
\tag{4.4}
\]

If `y=13`, then necessarily `x=13`, and

\[
\gamma_2(39)=9,\qquad \gamma_3(39)=9,
\]

so

\[
D=26-18=8.
\tag{4.5}
\]

Thus the clipped vector has `D=8` only when all thirteen entries equal three.

## 5. Equality in Q is unique

Since clipping preserves `p` and does not decrease `D`, Sections 2-4 give

\[
Q=p+D\le13+8=21.
\]

Suppose `Q=21`. Then `p=13` and `D=8`. The clipped vector must therefore also have `D=8`, so by (4.5) it is `3^13`. Hence every original demand is at least three.

It remains to rule out an original demand above three. After the higher clipping stages, such a vector would reach a nonconstant `3/4` vector with `k>=1` fours. For that vector

\[
D=26+k-\gamma_2(39+k)-\gamma_3(39+k)-\gamma_4(4k).
\tag{5.1}
\]

If `1<=k<=3`, the three gamma terms are at least `10,9,4`, giving `D<=6`. If `4<=k<=9`, they are at least `10,10,k-1`, giving `D<=7`. If `10<=k<=12`, they are at least `11,10,k-2`, again giving `D<=7`. At `k=13` they are exactly `11,11,10`, giving `D=7`.

The two variable lower bounds used here follow by testing `z=k-2` for `4<=k<=9` and `z=k-3` for `10<=k<=12` in `gamma_4(4k)`; the corresponding strict defects are

\[
\frac{-k^2+13k-26}{2}>0,
\qquad
\frac{-k^2+15k-32}{2}>0.
\]

Therefore every nonconstant `3/4` vector has `D<=7`, contradicting the nondecreasing clipping of an original vector with `D=8`. Hence

\[
Q=21\quad\Longrightarrow\quad s=(3,3,\ldots,3).
\]

The reverse implication is the direct calculation in (4.5), so equality is unique.

## 6. Transfer to a graph with a=13

Use the canonical parameterized bridge. Let

\[
a=n-1-\Delta=13,\qquad b=\Delta,
\qquad t=m-b(a+1)>0.
\]

Residual activity and the residual tail sum give

\[
r=b+\sum_{h=2}^{13}z_h.
\]

Threshold capacity gives `z_h>=gamma_h(W_h)`, while the demand ledger gives `S>=r+2t`. Hence

\[
Q(s)=S-\sum_{h=2}^{12}\gamma_h(W_h)\ge b+2t.
\tag{6.1}
\]

Combining with the hand lemma,

\[
\boxed{b+2t\le21.}
\tag{6.2}
\]

This is the thirteen-label analogue needed for N31. Unlike the twelve-label result, it does not by itself forbid every positive surplus for all source counts; the endpoint equality structure matters.

## 7. The N31 Delta=17 endpoint

For `n=31, Delta=17`, one has `(a,b)=(13,17)` and

\[
t=m-238.
\]

If `m>=241`, then `t>=3`, so (6.1) gives `Q>=23`, contradicting `Q<=21`. Thus only `m=240` needs attention.

At `m=240`, `t=2` and (6.1) gives `Q>=21`; therefore equality holds throughout and Section 5 forces

\[
s_i=3\qquad(i=1,\ldots,13),
\qquad S=39.
\tag{7.1}
\]

Now `gamma_2(39)=gamma_3(39)=9`. Hence

\[
r\ge17+9+9=35.
\]

But `S>=r+2t=r+4` gives `r<=35`. Therefore

\[
r=35,
\qquad z_2=z_3=9,
\qquad z_h=0\ (h>=4).
\tag{7.2}
\]

The residual source degrees are consequently

\[
3^9,1^8.
\tag{7.3}
\]

Every selected incidence has a label of demand three, so selected-incidence forcing says its source has residual degree at least three. Thus all selected incidences originate in the nine high sources `Z=Z_2=Z_3`.

At threshold `h=2`, `W_2=39` and the capacity bound is exact because

\[
C_2(9)=39.
\]

The proof of threshold capacity gives the chain

\[
39=W_2\le\sum_{u\in Z}q_u
\le (9-j)2+9j-\frac{j(j+1)}2
\le39,
\]

where `J={u in Z:q_u>2}` and `j=|J|`. Thus equality holds everywhere. The final scalar gap is

\[
39-\left((9-j)2+9j-\frac{j(j+1)}2\right)
=\frac{(7-j)(6-j)}2,
\]

so

\[
j\in\{6,7\}.
\tag{7.4}
\]

Equality also implies every source in `Z\J` has `q_u=2`; in particular every high source is active, and

\[
\sum_{u\in J}q_u
\ge39-2(9-j)
=21+2j
\in\{33,35\}.
\tag{7.5}
\]

For each selected edge from a source in `J`, the threshold-capacity proof forces its exception back into `Z`. Hence (7.5) implies

\[
\sum_{w\in Z}p_w\ge33.
\tag{7.6}
\]

On the other hand equality in the first part of the chain gives exactly 39 selected incidences. Since each of the thirteen labels has selected degree at least three, every label has selected degree exactly three. With `s_i=3`, this gives

\[
x_i=3,\qquad d_i-R_i=3,
\qquad R_i+x_i=d_i.
\tag{7.7}
\]

Take any active high source `u` and one of its selected labels `i`. The bridge's endpoint-load and source-selected-degree inequalities give

\[
q_u+p_u\le R_i+x_i=d_i
\le \rho_u+q_u-1=q_u+2,
\]

because `rho_u=3`. Therefore

\[
p_u\le2\qquad(u\in Z).
\tag{7.8}
\]

Summing over the nine high sources yields

\[
\sum_{u\in Z}p_u\le18,
\]

contradicting (7.6). Hence `Delta=17,m=240` is impossible.

So for N31 the entire `Delta=17` branch satisfies

\[
\boxed{e(G)\le239.}
\]

The exact regression checks the finite clipping arithmetic, the unique `Q=21` terminal profile, and the endpoint equalities. It is independent corroboration, not a proof premise.
