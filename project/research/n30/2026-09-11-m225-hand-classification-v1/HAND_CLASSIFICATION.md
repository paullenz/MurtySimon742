# Hand classification of the N30 equality demand frontier

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal arithmetic audit: ChatGPT/Geeps.

**Candidate hand argument with explicit bounded arithmetic tables. Arithmetic REPRODUCED; independent specialist review OPEN. No governed theorem-ledger promotion.**

This note derives the complete 100-profile `n=30, Delta=16, m=225` demand frontier. It replaces the historical full demand-multiset sweep as the completeness premise of this supplementary route. It does not claim a table-free proof: every arithmetic rule is stated below, the longer preimage tables are printed in [PREIMAGE_ARITHMETIC.md](PREIMAGE_ARITHMETIC.md), and the program is an internal audit of those tables. The separate four-envelope arithmetic and the other degree branches still need full assembly review.

## 1. Statement and threshold notation

Let thirteen integers satisfy `0<=s_i<=12`. For `h>=1` put

$$
N_h=\#\{i:s_i\ge h\},\qquad W_h=\sum_{s_i\ge h}s_i.
$$

For `h>=2`, define

$$
C_h(z)=\frac{z(z-1)+h(h+1)}2,
\qquad g_h(0)=0,
$$

and, when `W>0`, let `g_h(W)` be the least `z` in `{h,...,16}` with `W<=C_h(z)`. If no such `z` exists, the profile is threshold-inadmissible and is excluded immediately; equivalently assign it score minus infinity. All subsequent finite calculations have defined thresholds.

Write

$$
p=N_1,\quad D=\sum_{h=2}^{12}(N_h-g_h(W_h)),\quad
Q=\sum_i s_i-\sum_{h=2}^{12}g_h(W_h)=p+D. \tag{1}
$$

The last identity is the Ferrers-tail sum. The established graph bridge at `t=m-224=1` requires `Q>=16+2t=18`.

**Classification.** Exactly 100 demand multisets have `Q>=18`. Seventy have maximum demand at most four and appear in Table 1. The other thirty contain fives and appear in Table 2. None contains a demand at least six. Their scores are distributed as follows.

| Q | Number of profiles |
|---|---:|
| 18 | 64 |
| 19 | 29 |
| 20 | 6 |
| 21 | 1 |

In particular `Q<=21`, and equality holds only for `(3^13)`.

## 2. Monotone clipping, including zeros and ones

The clipping arguments in the [earlier m226 profile proof](../2026-09-11-threshold-tail-v1/N30_M226_HAND_PROFILE_REDUCTION.md) do not require the lower bound `s_i>=2`. Here are the details needed to apply them to arbitrary demands.

For `h>=8`, let `N=N_h`. If `0<N<h`, then `g_h>=h>N`. Otherwise write `N=h+e`, where `0<=e<=13-h<=5`. Because `W_h>=hN`, a positive deficit would require `hN<=C_h(N-1)`. But

$$
2hN-2C_h(N-1)=-e^2+3e+2h-2>0. \tag{2}
$$

This concave quadratic is positive at both endpoints of `[0,5]`: the endpoint values are `2h-2` and `2h-12`. Thus every deficit at level at least eight is nonpositive. Clipping demands above seven to seven removes only nonpositive deficits; at lower levels it leaves `N_h` fixed and decreases `W_h`. It cannot decrease `D` or `Q`, and preserves `p`.

Now clip seven to six. If the number `k` of sevens is at most twelve, its level-seven deficit is nonpositive: for `k>=7`, the same capacity defect is `12+3e-e^2>0` with `e=k-7<=5`. The only positive case is `(7^13)`, whose level-seven deficit is one. The level-six threshold drops from `g_6(91)=13` to `g_6(78)=12`, paying that unit. All lower deficits improve or stay fixed.

For clipping six to five, the level-six deficit is nonpositive unless `k=11,12,13`; in those three cases it is one. Let `l` count the fives already present. The complete positive-deficit payment table is:

| k | l | Drop in g5 |
|---:|---:|---:|
| 11 | 0 | 1 |
| 11 | 1 | 2 |
| 11 | 2 | 1 |
| 12 | 0 | 2 |
| 12 | 1 | 1 |
| 13 | 0 | 1 |

Each drop is `g_5(6k+5l)-g_5(5(k+l))`, so it pays the lost level-six deficit.

Finally clip five to four. The level-five deficit is nonpositive for `k<=9`, one for `k=10,11`, and two for `k=12,13`. If `l` counts the existing fours, then `g_4(5k+4l)-g_4(4(k+l))=1` in every positive-deficit case: `l=0,...,3` for `k=10`, `l=0,...,2` for `k=11`, `l=0,1` for `k=12`, and `l=0` for `k=13`.

When another unit is needed, it comes from level three:

| k,l | W3 before | W3 after | Guaranteed drop in g3 |
|---|---|---|---:|
| 12,0 | 60 or 63 | 48 or 51 | 1 |
| 12,1 | 64 | 52 | 1 |
| 13,0 | 65 | 52 | 1 |

In the first row the remaining entry is any of `0,1,2,3`; it contributes three precisely when it is three. This explicitly covers the low-demand cases absent from the earlier endpoint assumptions.

Consequently, clipping an arbitrary demand vector to four by this sequence preserves `p` and never decreases `Q`. It also preserves `N_2` and `N_3`. Completeness requires examining the reverse lifts; Sections 5–6 do so.

## 3. Only four low-dimensional cases remain at cap four

At cap four put `x=N_2`, `y=N_3`, `z=N_4`. Then

$$
0\le z\le y\le x\le p\le13,
\quad D_4(x,y,z)=x+y+z-g_2(2x+y+z)-g_3(3y+z)-g_4(4z). \tag{3}
$$

The multiset is `(0^(13-p),1^(p-x),2^(x-y),3^(y-z),4^z)`.

For `x>=1`, adjoining a demand two to the part counted by `x` cannot decrease `D_4`: it increases `x` by one and `W_2` by two, and increases `g_2` by at most one. Indeed `C_2(z+1)-C_2(z)=z>=2` once `g_2>=2`. Thus when `1<=x<=10` it suffices to bound `D_4(10,y,z)`; `x=0` has deficit zero.

At `z=0`, the deficits for `y=0,...,10` are

$$
(3,1,2,3,3,2,2,3,3,4,4).
$$

For `0<=z<=8`, `z-g_4(4z)<=0`, while increasing `z` cannot improve either of the first two terms in (3). Hence `D_4<=4`. For `z=9,10`, the only pairs `(y,z)` are `(9,9),(10,9),(10,10)`, with deficits `2,3,2`. We have proved `x<=10 => D_4<=4`.

If `x=11` and `y<=10`, comparison with `x=10` gives `D_4<=5`. At `x=y=11`, the values for `z=0,...,11` are

$$
(5,2,2,3,4,4,4,3,3,4,3,4).
$$

Thus `x<=11 => D_4<=5`. The requirement `p+D_4>=18` now forces exactly one of

$$
(p,x)=(12,12),(13,11),(13,12),(13,13). \tag{4}
$$

Indeed `p<=11` gives `Q<=16`; `p=12,x<=11` gives `Q<=17`; and `p=13,x<=10` gives `Q<=17`.

## 4. The seventy cap-four profiles

Table 1 lists every permitted value of `y` for each `z` and each pair in (4). A dash means the set is empty. The inequalities `z<=y<=x` are always imposed.

| z | p=12,x=12 | p=13,x=11 | p=13,x=12 | p=13,x=13 |
|---:|---|---|---|---|
| 0 | 11,12 | 9,11 | 0,7,9,10,11,12 | 0,3,4,5,7,8,9,10,11,12,13 |
| 1 | — | — | — | — |
| 2 | — | — | — | 13 |
| 3 | — | — | 12 | 10,12,13 |
| 4 | — | — | 10,11,12 | 9,10,11,12,13 |
| 5 | — | — | 12 | 11,12,13 |
| 6 | — | — | 12 | 11,12,13 |
| 7 | — | — | — | 11,12,13 |
| 8 | — | — | — | 11,12,13 |
| 9 | — | — | 11,12 | 10,11,12,13 |
| 10 | — | — | 12 | 10,11,12,13 |
| 11 | 12 | — | 11,12 | 11,12,13 |
| 12 | 12 | — | 12 | 12,13 |
| 13 | — | — | — | 13 |
| **Count** | **4** | **2** | **18** | **46** |

Here is a direct method to verify both inclusion and omission in this table, without a demand search. Fix `p,x,z`; substitute (3) into `p+D_4>=18`. The only changing thresholds are `g_2(2x+y+z)` and `g_3(3y+z)`. Their changes occur just after

$$
y=C_2(a)-2x-z,\qquad
y=\left\lfloor\frac{C_3(b)-z}{3}\right\rfloor. \tag{5}
$$

Within each resulting integer interval both thresholds are constant, so `Q` is `y` plus a fixed integer. Intersect that interval with the resulting lower bound on `y`. Check `y=z=0` separately, since `g_3(0)=0`. This produces exactly Table 1.

For example, at `p=13,x=12,z=0`, (3) gives

$$
Q=25+y-g_2(24+y)-g_3(3y).
$$

For `y=0,...,12`, its values are

$$
(18,15,16,17,17,17,17,18,17,18,18,19,19),
$$

yielding the indicated six values of `y`. Each other row uses precisely the same two threshold boundaries. The capacity values needed for this table and the lifts below are:

| z | C2(z) | C3(z) | C4(z) | C5(z) | C6(z) |
|---:|---:|---:|---:|---:|---:|
| 2 | 4 | — | — | — | — |
| 3 | 6 | 9 | — | — | — |
| 4 | 9 | 12 | 16 | — | — |
| 5 | 13 | 16 | 20 | 25 | — |
| 6 | 18 | 21 | 25 | 30 | 36 |
| 7 | 24 | 27 | 31 | 36 | 42 |
| 8 | 31 | 34 | 38 | 43 | 49 |
| 9 | 39 | 42 | 46 | 51 | 57 |
| 10 | 48 | 51 | 55 | 60 | 66 |
| 11 | 58 | 61 | 65 | 70 | 76 |
| 12 | 69 | 72 | 76 | 81 | 87 |
| 13 | 81 | 84 | 88 | 93 | 99 |

All threshold arguments in Sections 3–6 are at most 78, so these capacities suffice; no threshold above thirteen is needed there.

## 5. All cap-five preimages: thirty more profiles

Any cap-five profile with `Q>=18` clips to Table 1. To recover it, replace `k` of the `z` fours by fives, where `1<=k<=z`. Its exact score is

$$
\begin{aligned}
Q_5(p,x,y,z,k)={}&p+x+y+z+k\\
&-g_2(2x+y+z+k)-g_3(3y+z+k)\\
&-g_4(4z+k)-g_5(5k). \tag{6}
\end{aligned}
$$

The complete solutions are Table 2. All have `p=x=13`.

| y | z | Permitted k | Number |
|---:|---:|---|---:|
| 12 | 10 | 5 | 1 |
| 12 | 12 | 5,6,7,12 | 4 |
| 13 | 10 | 5,6 | 2 |
| 13 | 11 | 5,6,7,8,10,11 | 6 |
| 13 | 12 | 4,5,6,7,10,12 | 6 |
| 13 | 13 | 3,4,5,6,7,8,9,10,11,12,13 | 11 |
| **Total** | | | **30** |

The corresponding multiset is `(2^(13-y),3^(y-z),4^(z-k),5^k)`.

To check completeness, apply the same interval argument to (6). Its threshold changes occur just after

$$
\begin{split}
k={}&C_2(a)-(2x+y+z),\\
k={}&C_3(b)-(3y+z),\\
k={}&C_4(c)-4z,\\
k={}&\lfloor C_5(d)/5\rfloor. \tag{7}
\end{split}
$$

Between changes, `Q_5=k+constant`; intersect with `Q_5>=18`. Table 1 has altogether 366 possible positive lifts, split by (7) into 230 affine intervals. The [complete preimage appendix](PREIMAGE_ARITHMETIC.md) prints every interval, its constant threshold vector, the formula for `Q_5`, and its accepted integers. It includes rejected lifts from **every** Table 1 row with `z>0`, including those with a zero or a one. Thus Table 2 is not an inference from the historical survivor list.

## 6. No original profile containing six or more is hidden by clipping

Suppose an original profile with `Q>=18` contains a value at least six. After clipping to six it still has `Q>=18` and contains a six. After the next clipping, it is a Table 2 profile containing fives. Therefore it suffices to lift one of the thirty profiles in Table 2: raise `j` of its `k` fives to six, where `1<=j<=k`.

The exact score of that lift is

$$
\begin{aligned}
Q_6(y,z,k,j)={}&26+y+z+k+j\\
&-g_2(26+y+z+k+j)-g_3(3y+z+k+j)\\
&-g_4(4z+k+j)-g_5(5k+j)-g_6(6j). \tag{8}
\end{aligned}
$$

Again, the score is `j+constant` between threshold changes. The changes occur just after the four capacities minus their displayed bases, and after `floor(C_6(d)/6)`. The maximum on each interval is its value at the right endpoint. This gives:

| y | z | k ranges from Table 2 | Maximum Q6 over all permitted k and 1<=j<=k |
|---:|---:|---|---:|
| 12 | 10 | 5 | 14 |
| 12 | 12 | 5,6,7,12 | 15 |
| 13 | 10 | 5,6 | 15 |
| 13 | 11 | 5,6,7,8,10,11 | 15 |
| 13 | 12 | 4,5,6,7,10,12 | 16 |
| 13 | 13 | 3,4,5,6,7,8,9,10,11,12,13 | 16 |

For example, lifting `(5^13)` gives

$$
Q_6=65+j-g_2(65+j)-g_3(65+j)-g_4(65+j)-g_5(65+j)-g_6(6j).
$$

At `j=1,...,13`, these scores are

$$
(13,14,15,16,16,16,16,15,15,15,16,15,15).
$$

There are only 225 positive six-lifts in total, divided into 131 affine intervals. Every interval and its maximum is printed in the second half of the appendix. All have score at most sixteen, contradicting `Q>=18`.

This rules out all original demands at least six, including seven through twelve: the forward clipping already proved that none could disappear without leaving a six-lift with a score at least as large. Together with Sections 4–5, this proves the classification. QED.

## 7. How this changes the endpoint dependency chain

The list [HAND_CLASSIFIED_PROFILES.txt](HAND_CLASSIFIED_PROFILES.txt) is derived from Tables 1–2. It agrees exactly, including scores and order, with the historical 100-profile list. That agreement is corroboration, not a premise of the argument.

The [threshold-slack identity](../2026-09-11-threshold-tail-v1/N30_M225_THRESHOLD_SLACK_REDUCTION.md) then reconstructs the residual tails using `Q-18<=3` slack units. It yields the same 272 rows, of which 61 are excluded by the ledger argument. The [four-envelope argument](../2026-09-11-m225-resource-envelope-v1/FOUR_ENVELOPE_REDUCTION.md) excludes the other 211 rows using four shared integer certificates.

An end-to-end replay supplies the newly derived profiles directly to the unchanged envelope checker: all 211 rows are covered, with minimum assigned gap one. Its field `profile_completeness_is_input=true` correctly records that this downstream checker does not itself prove completeness; the present note supplies that mathematical premise in the combined route.

What is removed is the need to trust the historical exhaustive profile enumeration. What remains includes the universal bridge, review of the explicit bounded arithmetic here, the residual-tail/ledger argument, all 211 envelope evaluations, the complete N30 assembly, and the separate finite components at `Delta=17`. The frozen reviewer-v2 package and governed theorem ledger are unchanged. This is not a claim of external acceptance or an unrestricted Murty–Simon theorem.
