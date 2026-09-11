# Hand proof of the n=29, Delta=16 threshold-tail bound

11 September 2026. Research direction: Paul Lenz. Mathematical development and hostile checking: ChatGPT/Geeps.

**Status: candidate hand lemma. Independent mathematical review remains open.**  
This replaces the *logical* dependence on the earlier 1,352,078-multiset maximisation for the scalar bound `Q(s)<=18`. The exhaustive checker remains preserved as an independent audit. The argument is conditional on the same graph-to-model, residual-activity, selected-incidence and threshold-capacity lemmas stated in the parent `README.md`.

## 1. Reformulate the score as a tail deficit

Let the twelve demand values satisfy

```text
0 <= s_i <= 11.
```

For `h>=1`, put

```text
N_h = #{i:s_i>=h},
```

and for `h>=2`

```text
W_h = sum_{i:s_i>=h} s_i.
```

Let `g_h(W_h)` be the least threshold-compatible source-tail size from the parent note:

```text
g_h(0)=0,

g_h(W)=min {z in {h,...,16}:
            2W <= z^2-z+h(h+1)}     (W>0).
```

Write

```text
p=N_1=#{i:s_i>0},
d_h=N_h-g_h(W_h),
D(s)=sum_{h=2}^{11} d_h.
```

The elementary Ferrers-tail identity is

```text
S=sum_i s_i = p + sum_{h=2}^{11} N_h.
```

Therefore the threshold-tail score is exactly

```text
Q(s)=S-sum_{h=2}^{11}g_h(W_h)
    =p+D(s).                                      (1)
```

Since `p<=12`, it is enough to prove

```text
D(s)<=6.                                          (2)
```

We now prove (2) without enumerating demand multisets.

For convenience define the threshold capacity

```text
C_h(z) = (z(z-1)+h(h+1))/2.
```

Thus `g_h(W)` is the least admissible `z>=h` with `W<=C_h(z)`.

## 2. High tails h>=7 never help D

Fix `h>=7` and put `N=N_h`.

If `N=0`, then `d_h=0`. If `0<N<h`, then `g_h>=h>N`, so `d_h<0`.

It remains to consider `N>=h`. Since every one of the `N` heavy labels contributes at least `h`,

```text
W_h>=hN.                                          (3)
```

Suppose for contradiction that `g_h<=N-1`. Then the monotonicity of `C_h` gives

```text
hN <= C_h(N-1).
```

Write `N=h+e`. Here

```text
0<=e<=12-h<=5.
```

Twice the difference between the two sides is

```text
2hN - [(N-1)(N-2)+h(h+1)]
 = -e^2+3e+2h-2.                                  (4)
```

The right side is concave in `e`, hence its minimum on `0<=e<=5` is at an endpoint. At `e=0` it is `2h-2>0`, and at `e=5` it is `2h-12>=2`. This contradicts the assumed capacity inequality.

Therefore

```text
g_h>=N_h,
d_h<=0                  for every h>=7.          (5)
```

## 3. Clip every demand above 6 down to 6

Replace every `s_i>6` by `6`, obtaining `s'`.

For `2<=h<=6`, the counts `N_h` are unchanged, while `W_h` can only decrease. Hence `g_h` can only decrease and `d_h=N_h-g_h` can only increase.

For `h>=7`, the new deficit is zero, while the old deficit is nonpositive by (5). Thus

```text
D(s')>=D(s).                                      (6)
```

It is enough from now on to assume

```text
max s_i<=6.                                       (7)
```

## 4. Clip 6 down to 5

Let `k=N_6`, the number of sixes.

For every level `h<=5`, clipping all sixes to five keeps `N_h` fixed and lowers `W_h`, so all lower deficits can only increase.

At level six,

```text
W_6=6k.
```

For `k<=10`, one has `g_6(6k)>=k`, hence `d_6<=0`. For `k<6` this is immediate from `g_6>=6`; for `6<=k<=10`, testing `z=k-1` gives the positive capacity defect

```text
12k-[(k-1)(k-2)+42]
 =-e^2+3e+10>0,
```

where `e=k-6` lies in `{0,1,2,3,4}`.

Only `k=11,12` need attention:

```text
k=11: g_6(66)=10, so d_6=1;
k=12: g_6(72)=11, so d_6=1.
```

If `k=11`, let `l` be 1 when the remaining demand is five and 0 otherwise. At level five,

```text
before: W_5=66+5l,
after:  W'_5=55+5l.
```

Using

```text
C_5(10)=60,
C_5(11)=70,
C_5(12)=81,
```

shows that `g_5` drops by at least one. If `k=12`, `W_5` drops from 72 to 60 and `g_5` drops from 12 to 10. In both cases the lower-level gain pays for the lost positive `d_6`.

Hence clipping sixes to fives cannot decrease `D`.

## 5. Clip 5 down to 4

Now assume `max s_i<=5` and let `k=N_5`.

For `k<=9`, `g_5(5k)>=k`, so `d_5<=0`. For `k<5` this is immediate; for `5<=k<=9`, the same `z=k-1` check gives

```text
10k-[(k-1)(k-2)+30]
 =-e^2+3e+8>0,
```

with `e=k-5 in {0,1,2,3,4}`.

For `k=10,11` one has `d_5=1`. Let `l` be the number of fours among the remaining `12-k` entries. At level four,

```text
before: W_4=5k+4l,
after:  W'_4=4(k+l).
```

The complete possibilities are tiny:

```text
(k,l)   W_4 -> W'_4     g_4 -> g'_4
(10,0)   50 -> 40        10 -> 9
(10,1)   54 -> 44        10 -> 9
(10,2)   58 -> 48        11 ->10
(11,0)   55 -> 44        10 -> 9
(11,1)   59 -> 48        11 ->10
```

so `g_4` always drops by at least one, paying for `d_5=1`.

If `k=12`, the vector is exactly `(5^12)`. Directly,

```text
(g_2,g_3,g_4,g_5)=(12,11,11,10),
D(5^12)=0+1+1+2=4<=6.
```

Thus every vector with a five either already satisfies (2), or can be clipped from five to four without decreasing `D`.

## 6. Clip 4 down to 3

Now assume `max s_i<=4` and let `k=N_4`.

For `k<=8`, `g_4(4k)>=k`, so `d_4<=0`. For `k<4` this is immediate; for `4<=k<=8`, testing `z=k-1` gives

```text
8k-[(k-1)(k-2)+20]
 =-e^2+3e+6>0,
```

with `e=k-4 in {0,1,2,3,4}`.

For `k=9,10`, `d_4=1`. Let `l` be the number of threes among the remaining entries. At level three the possible capacity jumps are

```text
k=9:  l=0,1,2,3 gives g_3 drops 2,1,1,1;
k=10: l=0,1,2   gives g_3 drops 1,2,1.
```

Thus the lost `d_4=1` is always paid for.

For `k=11`, `d_4=2`. If the remaining entry is at most two, the level-three `g_3` drops by two. If it is three, the vector is `(3,4^11)`; then clipping gives `(3^12)`, `g_3` drops `10->9` and `g_2` drops `10->9`, again paying exactly two.

For `k=12`, the vector is `(4^12)`; clipping to `(3^12)` changes

```text
(g_2,g_3) : (10,10) -> (9,9),
```

which pays for `d_4=2`.

Therefore clipping fours to threes cannot decrease `D`.

We have reduced the whole problem to

```text
max s_i<=3.                                       (8)
```

## 7. Final two-level inequality

Under (8), put

```text
x=N_2,
y=N_3,
0<=y<=x<=12.
```

Then

```text
W_2=2x+y,
W_3=3y,
D=x+y-g_2(2x+y)-g_3(3y).                         (9)
```

We use three ranges of `y`.

### Case A: 0<=y<=6

First,

```text
x-g_2(2x+y)<=5.                                  (10)
```

For `x<=7`, this follows from `g_2>=2` whenever `x>0`; for `8<=x<=12`, capacity at `z=x-6` is too small because

```text
2x-C_2(x-6)
 =(-x^2+17x-48)/2>0.
```

Second,

```text
y-g_3(3y)<=0.                                    (11)
```

For `y<=3` this is immediate from the baseline `g_3>=3` when `y>0`. For `4<=y<=6`, capacity at `z=y-1` is too small since

```text
3y-C_3(y-1)
 =(-y^2+9y-14)/2>0.
```

Hence `D<=5` in Case A.

### Case B: 7<=y<=10

Here

```text
y-g_3(3y)<=2.                                    (12)
```

Indeed capacity at `z=y-3` is too small because

```text
3y-C_3(y-3)
 =(-y^2+13y-24)/2>0.
```

Also

```text
x-g_2(2x+y)<=4.                                  (13)
```

If `g_2<=x-5`, then, because `x>=y>=7`,

```text
(2x+y)-C_2(x-5)
 =(-x^2+15x+2y-36)/2
 >=(-x^2+15x-22)/2>0
```

for `7<=x<=12`, contradiction.

Thus `D<=2+4=6` in Case B.

### Case C: 11<=y<=12

Now

```text
y-g_3(3y)<=3,                                    (14)
```

because capacity at `z=y-4` is too small:

```text
3y-C_3(y-4)
 =(-y^2+15y-32)/2>0.
```

Since `y<=x<=12`, only `x=11,12` are possible, and

```text
x-g_2(2x+y)<=3.                                  (15)
```

Indeed capacity at `z=x-4` is too small because

```text
(2x+y)-C_2(x-4)
 =(-x^2+13x+2y-26)/2
 >=(-x^2+13x-4)/2>0.
```

Therefore `D<=3+3=6` in Case C.

Combining the three cases proves

```text
boxed: D(s)<=6.                                  (16)
```

## 8. Consequence

By (1),

```text
Q(s)=p+D(s)<=12+6=18.
```

Thus the parent threshold-tail argument becomes entirely hand-written after the universal bridge:

```text
16+2t <= Q(s) <=18,
```

so

```text
t<=1.
```

For `n=29, Delta=16`, therefore,

```text
m=210 (t=2): impossible,
m=211 (t=3): impossible.
```

The old 1,352,078-multiset checker remains valuable as an independent exact regression and equality-case audit, but is no longer a logical dependency of this candidate route.

## 9. Equality audit

The preserved exhaustive checker shows that `Q=18` occurs only at

```text
(2,3^11),
(3^12),
(3,4^11),
(4^12).
```

The hand proof above does not require this equality classification, so the uniqueness statement remains an exact finite audit rather than a logical premise.
