# Hand profile and residual-row reduction for the n=30, Delta=16, m=226 endpoint

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate analytic hardening. Independent mathematical review remains open.**

This note removes the remaining proof-critical exhaustive classification at the upper `n=30, Delta=16` endpoint. Combined with `N30_M226_HAND_ENDPOINT_REDUCTION.md`, it gives a hand route from the threshold-tail bridge to the contradiction at `m=226`.

The historical 5,200,300-demand sweep, residual-row enumeration and exact Farkas certificates are retained as independent corroboration. Nothing here changes the still-computational `m=225, Delta=16` equality branch.

## 1. Threshold-tail notation

For `n=30, Delta=16`, put

```text
a=13,
b=16,
t=m-224.
```

At the endpoint `m=226`, `t=2`.

Let the thirteen demand values be

```text
0 <= s_i <= 12.
```

For `h>=1`, write

```text
N_h = #{i:s_i>=h},
```

and for `h>=2`,

```text
W_h = sum_{i:s_i>=h} s_i.
```

Define the threshold capacity

```text
C_h(z) = (z(z-1)+h(h+1))/2,
```

and let `g_h(W)` be the least `z in {h,...,16}` with

```text
W <= C_h(z)
```

for `W>0`, with `g_h(0)=0`.

Put

```text
p = N_1,
d_h = N_h-g_h(W_h),
D(s) = sum_{h=2}^{12} d_h.
```

The Ferrers-tail identity gives

```text
Q(s)=sum_i s_i-sum_{h=2}^{12} g_h(W_h)
    =p+D(s).                                      (1)
```

The graph-to-model bridge gives the necessary endpoint inequality

```text
Q(s) >= 16+2t = 20.                              (2)
```

We shall prove by hand that exactly seven demand multisets satisfy (2), with `Q<=21` and equality only at `(3^13)`.

We use one already-proved hand lemma from the `n=29` threshold-tail note: for any twelve-entry demand vector with entries in `{0,...,11}`, its corresponding tail deficit is at most six.

## 2. Every endpoint demand is at least two

First suppose `p<=12`. Delete zero entries and pad with zeros to obtain twelve entries. If an entry equals 12, clip it to 11. At level 12 one always has

```text
N_12 <= 12 <= g_12(W_12)
```

when `W_12>0`, so `d_12<=0`; at every lower level the clipping only decreases `W_h`, hence can only decrease `g_h` and increase the deficit. Thus this clipping cannot decrease `D`.

The twelve-label hand lemma now gives

```text
D<=6,
Q=p+D<=18,
```

contrary to (2).

Now suppose `p=13` but some demand equals 1. Delete one such 1. All `N_h,W_h` for `h>=2` are unchanged. Again clip any 12 to 11 if necessary and apply the twelve-label lemma. Hence

```text
D<=6,
Q=13+D<=19,
```

again contrary to (2).

Therefore every endpoint candidate satisfies

```text
2 <= s_i <= 12 for all thirteen labels.          (3)
```

In particular `p=13`, so `Q=13+D`; the endpoint condition `Q>=20` is exactly

```text
D>=7.                                             (4)
```

## 3. Clip every demand above seven down to seven

Fix `h>=8` and put `N=N_h`.

If `N=0`, then `d_h=0`. If `0<N<h`, then `g_h>=h>N`, so `d_h<0`.

It remains to consider `N>=h`. Write

```text
N=h+e,
0<=e<=13-h<=5.
```

Because each of the `N` heavy labels contributes at least `h`,

```text
W_h>=hN.
```

If `g_h<=N-1`, then monotonicity of `C_h` would force

```text
hN <= C_h(N-1).
```

But twice the difference between the two sides is

```text
2hN-[(N-1)(N-2)+h(h+1)]
 = -e^2+3e+2h-2.                                  (5)
```

This concave quadratic has its minimum on `0<=e<=5` at an endpoint. At `e=0` it is `2h-2>0`; at `e=5` it is `2h-12>=4`. Contradiction.

Thus

```text
d_h<=0 for every h>=8.                            (6)
```

Clipping every demand above seven down to seven keeps every `N_h` with `h<=7` fixed while decreasing the corresponding `W_h`, so the lower deficits can only increase. The removed `h>=8` deficits were nonpositive by (6). Hence the clipping cannot decrease `D`.

It is enough to study vectors with

```text
max s_i<=7.                                       (7)
```

## 4. Clip seven down to six

Let `k=N_7`, the number of sevens.

For `k<=12`, one has `g_7(7k)>=k`, hence `d_7<=0`. For `k<7` this is immediate from `g_7>=7`. For `k=7+e`, `0<=e<=5`, testing `z=k-1` gives twice the capacity defect

```text
14k-[(k-1)(k-2)+56]
 = 12+3e-e^2 >0.                                  (8)
```

Only `k=13` has positive `d_7`. There

```text
g_7(91)=12,
d_7=1.
```

Clipping `(7^13)` to `(6^13)` makes the level-six threshold fall

```text
g_6(91)=13 -> g_6(78)=12,
```

which pays exactly for the lost unit at level seven. Every lower deficit can only increase.

Therefore clipping all sevens to sixes cannot decrease `D`.

## 5. Clip six down to five

Now assume `max s_i<=6` and let `k=N_6`.

For `k<=10`, `d_6<=0`. The only positive cases are

```text
k=11,12,13: d_6=1.                                (9)
```

Let `l` be the number of fives among the other `13-k` entries. At level five, clipping all sixes to fives changes

```text
W_5: 6k+5l -> 5(k+l).
```

The complete positive cases are

```text
(k,l)    g_5 before -> after
(11,0)      11 -> 10
(11,1)      12 -> 10
(11,2)      12 -> 11
(12,0)      12 -> 10
(12,1)      12 -> 11
(13,0)      12 -> 11
```

so `g_5` always drops by at least one, paying for (9). Lower levels only improve.

Thus clipping six to five cannot decrease `D`.

## 6. Clip five down to four

Now assume `max s_i<=5` and let `k=N_5`.

For `k<=9`, `d_5<=0`. The positive cases are

```text
k=10,11: d_5=1,
k=12,13: d_5=2.                                   (10)
```

Let `l` be the number of fours among the other `13-k` entries. At level four,

```text
W_4: 5k+4l -> 4(k+l).
```

For every positive case the level-four threshold drops by one:

```text
k=10, l=0,1,2,3;
k=11, l=0,1,2;
k=12, l=0,1;
k=13, l=0.
```

This already pays (10) when `k=10,11`.

For `k=12,13`, one further unit is needed. It is always supplied at level three:

```text
k=12,l=0:  W_3 is 60 or 63 -> 48 or 51,
             g_3 drops by at least 1;
k=12,l=1:  W_3: 64 -> 52,  g_3: 12 -> 11;
k=13:      W_3: 65 -> 52,  g_3: 12 -> 11.
```

Therefore clipping five to four cannot decrease `D`.

Combining Sections 3--6, every vector with `D>=7` maps, without decreasing `D`, to a vector all of whose entries lie in

```text
{2,3,4}.                                          (11)
```

## 7. The cap-four problem has only two variables

Under (11), put

```text
y=N_3,
z=N_4,
0<=z<=y<=13.
```

Then

```text
W_2=26+y+z,
W_3=3y+z,
W_4=4z,                                           (12)
```

and

```text
D=(13-g_2(W_2))+(y-g_3(W_3))+(z-g_4(W_4)).       (13)
```

There are only 105 integer pairs `(y,z)`, but even that tiny table is unnecessary. The following short split classifies the pairs with `D>=7`.

### 7.1 z=0

Here `g_2=8` for `y<=5` and `g_2=9` for `y>=6`. Direct threshold capacities for `g_3(3y)` give

```text
y:  0 1 2 3 4 5 6 7 8 9 10 11 12 13
D:  5 3 4 5 5 5 4 5 5 6  6  7  7  8.
```

Thus `D>=7` occurs exactly at

```text
(y,z)=(11,0),(12,0),(13,0).                       (14)
```

### 7.2 1<=z<=3

Increasing `z` from zero can only increase `g_2` and `g_3`, so the first two terms of (13) do not increase. Meanwhile

```text
z-g_4(4z) = -3,-2,-1
```

for `z=1,2,3`. Since the `z=0` first-two-term total is at most seven for `y<=12`, all those cases have `D<=6`. At `y=13`, direct substitution gives `D=4,5,6` for `z=1,2,3`.

Hence there is no new `D>=7` pair.

### 7.3 4<=z<=8

Here

```text
g_4(4z)=z,
```

so the third term in (13) is zero. The first two terms are nonincreasing in `z`, so it is enough to check `z=4`. For `y=4,...,13`, the resulting `D` values are

```text
3,3,3,4,4,5,5,5,6,6.
```

Again there is no `D>=7` pair.

### 7.4 9<=z<=13

Only a handful of pairs remain. Exact capacities give

```text
z=9:   D(y=9,...,13)  = 4,5,6,6,7;
z=10:  D(y=10,...,13) = 5,5,6,6;
z=11:  D(y=11,...,13) = 6,6,7;
z=12:  D(y=12,13)     = 6,7;
z=13:  D(y=13)        = 7.
```

Therefore the complete cap-four list is

```text
(y,z)        D     (g_2,g_3,g_4)
(11,0)       7       (9,8,0)
(12,0)       7       (9,9,0)
(13,0)       8       (9,9,0)
(13,9)       7      (10,10,8)
(13,11)      7      (11,10,9)
(13,12)      7     (11,10,10)
(13,13)      7     (11,11,10).                    (15)
```

These correspond to the seven cap-four demand multisets

```text
(2^2,3^11),
(2,3^12),
(3^13),
(3^4,4^9),
(3^2,4^11),
(3,4^12),
(4^13).                                           (16)
```

## 8. No hidden preimage containing a five

The clipping proof so far shows that every `D>=7` vector maps to one of (16). To show that (16) are the *original* vectors, we must rule out a preimage containing a five.

The first three profiles in (16) have `z=0`, so a cap-five preimage cannot contain a five: every five would become a four.

For the remaining four profiles, `y=13` and `z in {9,11,12,13}`. If the cap-five preimage contains exactly `k>=1` fives, it has

```text
13-z threes,
z-k fours,
k fives.                                          (17)
```

Put

```text
W=39+z+k.
```

Since all thirteen entries are at least three,

```text
D = A(W) + d_4 + d_5,
A(W)=26-g_2(W)-g_3(W),
d_4=z-g_4(4z+k),
d_5=k-g_5(5k).                                    (18)
```

The relevant capacities give

```text
A(W)=5 for 49<=W<=51,
     =4 for 52<=W<=58,
     =3 for 59<=W<=61,
     =2 for 62<=W<=65.                            (19)
```

Also

```text
d_5(k) = -4,-3,-2,-1 for k=1,2,3,4;
         0          for 5<=k<=9;
         1          for k=10,11;
         2          for k=12,13.                  (20)
```

For the four possible values of `z`, the level-four term is

```text
z=9:   d_4=1 for k=1,2;       0 thereafter;
z=11:  d_4=2 for k=1,2;       1 thereafter;
z=12:  d_4=2 for k=1,...,7;   1 thereafter;
z=13:  d_4=3 for k=1,2,3;     2 thereafter.       (21)
```

Substitution into (18) gives the exact maxima over `k>=1`:

```text
z      max D with at least one five
9                 4
11                5
12                6
13                6.                              (22)
```

Thus no cap-five preimage containing a five has `D>=7`.

Consequently, a genuine `D>=7` original vector had no entry at least five: any original 5 remains a 5 until the final clipping, and any original 6 or larger becomes a 5 by the preceding clipping chain. Therefore (16) are exactly the original `D>=7` profiles.

We have proved the full demand classification by hand:

```text
Q(s)<=21,
Q(s)=21 only for (3^13),
Q(s)>=20 exactly for the seven profiles in (16). (23)
```

In particular the bridge inequality `Q>=16+2t` immediately excludes every `Delta=16` scope with `t>=3`, i.e. every

```text
m>=227.                                           (24)
```

No 5,200,300-profile sweep is logically needed for (23)--(24).

## 9. The seven profiles force exactly nine residual rows

Let

```text
z_h = #{u:rho_u>=h}
```

be the residual-degree tail counts. Residual activity gives sixteen positive residual degrees and hence

```text
r = 16 + sum_{h>=2} z_h.                          (25)
```

At `t=2`, the demand ledger gives

```text
S >= r+4 = 20 + sum_{h>=2} z_h.                  (26)
```

Threshold capacity gives

```text
z_h >= g_h(W_h).                                  (27)
```

Define the nonnegative integer ledger slack

```text
lambda = S-20-sum_{h>=2} z_h.
```

Then

```text
Q=S-sum_h g_h
 =20+lambda+sum_h(z_h-g_h).                       (28)
```

For each of the six profiles with `Q=20`, every nonnegative term on the right of (28) must vanish. Thus the ledger is tight and every residual tail is exactly its minimum `g_h`. This gives the six unique rows

```text
s=(2^2,3^11), rho=(1^7,2,3^8),       r=33;
s=(2,3^12),   rho=(1^7,3^9),         r=34;
s=(3^4,4^9),  rho=(1^6,3^2,4^8),     r=44;
s=(3^2,4^11), rho=(1^5,2,3,4^9),     r=46;
s=(3,4^12),   rho=(1^5,2,4^10),      r=47;
s=(4^13),     rho=(1^5,3,4^10),      r=48.        (29)
```

For `(3^13)`, one has

```text
Q=21,
g_2=g_3=9,
g_h=0 for h>=4.
```

Equation (28) leaves exactly one unit of total slack. There are only three possibilities compatible with the monotonic residual tails:

```text
1. lambda=1 and z=(9,9,0,...),
2. lambda=0 and z_2 increases to 10,
3. lambda=0 and a new z_4=1 appears.               (30)
```

Increasing `z_3` alone would force `z_2>=z_3` and cost at least two units; placing the unit first at level five or above would force all intervening tails positive and again cost at least two.

The three rows from (30) are

```text
s=(3^13), rho=(1^7,3^9),       r=34;
s=(3^13), rho=(1^6,2,3^9),     r=35;
s=(3^13), rho=(1^7,3^8,4),     r=35.              (31)
```

Together (29)--(31) are exactly the nine historical endpoint rows, now derived by hand.

## 10. Consequence for the m=226 endpoint

The companion note `N30_M226_HAND_ENDPOINT_REDUCTION.md` excludes those nine rows without the historical grouped LP/Farkas step:

1. the `s=(3^13), rho=(1^7,3^9), r=34` row dies immediately from demand-ledger equality;
2. the other eight rows contradict a label-excess upper bound against supplement-Hall lower certificates.

Combining that note with the present profile/row reduction yields a hand proof of the complete

```text
n=30, Delta=16, m=226
```

upper endpoint, conditional only on the universal graph-to-model / threshold-tail lemmas already used by the project.

Therefore the following historical computations are no longer logical dependencies of the `m=226, Delta=16` exclusion:

- the 5,200,300-demand threshold-tail maximisation;
- the residual-row enumeration producing the nine rows;
- the final grouped LP and exact Farkas certificates.

They remain valuable independent regression evidence.

This does **not** remove the exact finite work currently used at `m=225, Delta=16` to establish the equality classification for the full `n=30` candidate theorem. Independent specialist review remains open.
