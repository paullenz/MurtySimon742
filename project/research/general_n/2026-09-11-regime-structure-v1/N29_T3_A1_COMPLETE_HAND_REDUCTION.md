# n=29, t=3, A1 regime: complete hand reduction to the stable support class

11 September 2026. Research direction: Paul Lenz. Mathematical development and hostile checking: ChatGPT/Geeps.

**Status: candidate hand lemma inside the RX-Hall / 3-D potential programme.** Conditional on the existing n=29 graph-to-profile bridge, the scalar supplement-cutoff lemma, zero slack, charging and Hall necessary conditions. This note replaces the **logical** use of the earlier 236,885-state histogram enumeration in the A1 support reduction. The old enumerator remains preserved as an exact audit.

The target regime is

```text
n=29, Delta=16, t=3,
a=12, b=16,
h_res=4,
J = 2 #{u:rho_u>=2} - #{i:s_i=1} = 14,
S = sum_i s_i = sum_u rho_u + 6.
```

The conclusion is that every surviving state has

```text
D1=0,
s support {2,3,4},
rho support {1,3,4,5,6},
rho1=9,
scalar cutoff L=6.
```

This is exactly the support on which the existing A1 three-slack certificate identity is stable.

---

## 1. First reductions common to all branches

For the n=29, Delta=16 charging summand,

```text
f(s)=s(13-2s)/(12-s),
```

we have, for every integer `0<=s<=11`,

```text
f(s)<=5/2,
```

while `f(1)=1`.

The charging inequality requires

```text
sum_i f(s_i) >= 16+2t = 22.
```

If `D1=#{i:s_i=1}`, then

```text
22 <= D1 + (12-D1)(5/2)
   = 30-(3/2)D1,
```

so `D1<=5`.

The regime identity

```text
14 = 2 z2-D1,
```

where `z2=#{u:rho_u>=2}`, forces `D1` to be even. Hence

```text
D1 in {0,2,4}.                            (1.1)
```

The one-label Hall inequality and `h_res=4` also give

```text
max_i s_i<=4.                             (1.2)
```

Indeed a demand at least five would require at least five residual sources of degree at least five, contradicting residual h-index four.

We eliminate the three possible D1 branches separately.

---

## 2. The D1=4 branch is impossible

If `D1=4`, then `J=14` gives

```text
z2=9,
rho1=7.
```

There are nine non-unit residual rows. Since `h_res=4`, at least four have degree at least four; the other five have degree at least two. Therefore

```text
sum rho >= 7 + 4*4 + 5*2 = 33.
```

Zero slack gives

```text
S>=39.
```

But (1.2) and `D1=4` give

```text
S <= 4*1+8*4=36,
```

contradiction.

Thus

```text
D1!=4.                                    (2.1)
```

---

## 3. The D1=2 branch is impossible

This branch is proved in detail in

```text
N29_T3_A1_D1_2_HAND_ELIMINATION.md
```

with an independent exact audit in

```text
N29_T3_A1_D1_2_HAND_CHECK.json.
```

For completeness, the proof architecture is:

1. `J=14` gives eight residual ones and eight non-unit sources;
2. zero slack and `h_res=4` force

   ```text
   2D2+D3<=4,
   ```

   hence `D2<=2` and `D4>=6`;
3. the scalar cutoff satisfies `L<=7`;
4. one Hall inequality on the eight largest demands eliminates `L<=5`;
5. the same prefix plus the level-six cutoff gate eliminates `L=6`;
6. the level-seven gate reduces to `(D2,D3,D4)=(2,0,8)`, after which the eight-largest Hall supply is at most `4*7=28<32`.

A minor arithmetic wording issue in the first version of that note is corrected here: in the `L=6, D4>=8` subcase, outside `(D2,D3)=(0,0)` the budget is

```text
12-2D2-D3 <= 11,
```

not always `<=10`. The conclusion is unchanged, because `2M<=11` still gives the integer bound `M<=5` and hence `Q<=30<32`. The exact checker already used the correct integer cases.

Therefore

```text
D1!=2.                                    (3.1)
```

Combining (1.1), (2.1), and (3.1),

```text
D1=0.                                     (3.2)
```

---

## 4. Enter the D1=0 branch

Now `J=14` gives

```text
z2=7,
rho1=9.
```

There are seven non-unit residual sources. By (1.2), every demand is at most four, and because there are no unit demands,

```text
s_i in {2,3,4}.                           (4.1)
```

Write

```text
D2+D3+D4=12.
```

The demand sum is

```text
S=2D2+3D3+4D4
 =36-D2+D4.                               (4.2)
```

Zero slack gives `sum rho=S-6`; after removing the nine residual ones, the seven non-unit residual rows have total mass

```text
N=S-15
 =21-D2+D4.                               (4.3)
```

---

## 5. The scalar cutoff is exactly L=6

For a residual-one source,

```text
C(1)=#{i:s_i<=1}=0,
```

so its scalar score is only one.

If `L>=7`, the level-seven gate would require at least eight sources with score at least six. None of the nine residual-one sources can qualify, leaving only seven non-unit sources. Thus

```text
L<=6.                                     (5.1)
```

If `L<=5`, the nine unit rows have terminal selected cap zero and the seven non-unit rows have cap at most five, so total selected-incidence capacity is at most

```text
7*5=35.
```

On the other hand `h_res=4` forces at least four non-unit rows of degree at least four, while the other three non-unit rows have degree at least two. Hence

```text
sum rho >= 9+4*4+3*2=31,
S>=37,
```

contradicting total selected-incidence capacity.

Therefore

```text
L=6.                                      (5.2)
```

---

## 6. No residual degree can be at least seven

Let

```text
X = # non-unit rows of degree 2,
Y = # non-unit rows of degree 3,
M = # non-unit rows of degree >=4.
```

Then

```text
X+Y+M=7,
M>=4.                                     (6.1)
```

Assume one of the M rows has degree at least seven.

Because all demands are at most four, a source of residual degree `rho>=7` has

```text
C(rho)<=12-rho,
```

so, with `L=6`, its terminal-cap surplus over residual degree is at most

```text
q*-rho <= (12-rho)-rho <= -2.
```

A degree-two source has surplus at most

```text
min(D2,6)-2,
```

a degree-three source at most three, and every remaining degree-at-least-four source at most two.

The nine residual-one sources contribute `-9` to `sum(q*-rho)`. Since total capacity requires

```text
sum q* >= S = sum rho+6,
```

the seven non-unit sources must contribute at least 15.

Under the assumed high row, their contribution is at most

```text
X(min(D2,6)-2)+3Y+2(M-1)-2
 = 10 + Y + X(min(D2,6)-4).               (6.2)
```

Because `X+Y<=3`, (6.2) can reach 15 only if

```text
min(D2,6)=6,
```

so

```text
D2>=6.                                    (6.3)
```

But then, using `D4<=12-D2` in (4.3),

```text
N=21-D2+D4
 <=33-2D2
 <=21.
```

A residual degree at least seven together with `h_res=4` already forces the seven non-unit rows to have mass at least

```text
7+3*4+3*2=25,
```

contradiction.

Hence

```text
rho_u<=6 for every non-unit source.        (6.4)
```

---

## 7. A residual degree two is also impossible

Assume now

```text
X>=1.
```

Because all non-unit residual degrees are now in `{2,3,4,5,6}`, (6.1) still holds.

### 7.1 First D2<=5

If `D2>=6`, then as above

```text
N<=21.
```

But `h_res=4` with seven non-unit sources, four of degree at least four and the other three of degree at least two, gives

```text
N>=4*4+3*2=22,
```

contradiction. Thus

```text
D2<=5.                                    (7.1)
```

Therefore

```text
D3+D4=12-D2>=7,                           (7.2)
```

so the seven largest demands contain no demand-two label. A residual degree-two source contributes **zero** to the top-seven Hall prefix.

### 7.2 Total capacity forces D4>=6

Suppose first `D4<=5`.

Then a residual degree-three source has `C(3)=D2+D3=12-D4>=7`, hence terminal cap six. Degree 4,5,6 sources also have terminal cap at most six. Comparing terminal cap with residual degree gives the necessary total-capacity bound

```text
15
 <= X(D2-2)+3Y+2M
 = 14 + X(D2-4)+Y.
```

Hence

```text
X(D2-4)+Y>=1.                             (7.3)
```

The residual-mass lower bound is

```text
N >= 2X+3Y+4M
  = 28-2X-Y.
```

Using (4.3),

```text
2X+Y >= 7+D2-D4.                          (7.4)
```

Now use only `X>=1`, `X+Y<=3`, and `D4<=5`:

- `D2<=2`: (7.3) forces `Y>=1+2X`, impossible with `X+Y<=3`;
- `D2=3`: (7.3) forces `Y>=X+1`, hence `(X,Y)=(1,2)`; then (7.4) forces `D4>=6`;
- `D2=4`: (7.3) gives `Y>=1`, so `2X+Y<=5`, while (7.4) requires at least `11-D4>=6`;
- `D2=5`: `2X+Y<=6`, while (7.4) requires at least `12-D4>=7`.

Every case contradicts `D4<=5`. Thus

```text
D4>=6.                                    (7.5)
```

### 7.3 Top-seven Hall kills D4>=7

Suppose `D4>=7`.

For degree-three residual sources the terminal-cap surplus is at most

```text
(12-D4)-3=9-D4.
```

The necessary total-capacity inequality therefore gives

```text
15
 <= X(D2-2)+(9-D4)Y+2M
 =14+X(D2-4)+(7-D4)Y.
```

Hence

```text
X(D2-4)+(7-D4)Y>=1.                       (7.6)
```

Since `D4>=7`, the second term is nonpositive. With `D2<=5`, (7.6) forces

```text
D2=5.
```

Then `D3=12-D2-D4=7-D4>=0`, so necessarily

```text
(D2,D3,D4)=(5,0,7).                       (7.7)
```

Equation (4.3) gives `N=23`. The lower mass bound (7.4) becomes

```text
2X+Y>=5.
```

Since `X+Y<=3`, this forces `X+Y=3`, hence

```text
M=4.
```

The seven largest demands are all four. Degree-two and degree-three sources cannot serve them. Only the four degree-at-least-four sources contribute, each with terminal cap at most six. Thus top-seven Hall supply is at most

```text
4*6=24<28,
```

contradiction.

Therefore `D4>=7` is impossible under `X>=1`.

### 7.4 Top-seven Hall also kills D4=6

It remains `D4=6`. Then

```text
D3=6-D2>=1.
```

The seven largest demands are six fours and one three, with total demand

```text
27.
```

A degree-two source contributes zero. A degree-three source can contribute at most one (to the lone demand-three label). Every degree-at-least-four source contributes at most six. Hence top-seven Hall supply is at most

```text
Y+6M
 =42-6X-5Y.                               (7.8)
```

We show `6X+5Y>=16`.

The total-capacity condition (7.3) and mass condition (7.4), now with `D4=6`, give

```text
X(D2-4)+Y>=1,
2X+Y>=1+D2.                               (7.9)
```

Case by case:

- `D2<=2`: the first inequality in (7.9) is incompatible with `X+Y<=3`;
- `D2=3`: it forces `(X,Y)=(1,2)`, so `6X+5Y=16`;
- `D2=4`: it gives `Y>=1`, while the second inequality requires `2X+Y>=5`; hence `6X+5Y>=17`;
- `D2=5`: the second inequality requires `2X+Y>=6`, which with `X+Y<=3` forces `(X,Y)=(3,0)`, giving `18`.

Thus (7.8) gives Hall supply at most 26, strictly below 27. Contradiction.

We conclude

```text
X=0.                                      (7.10)
```

---

## 8. The stable support class follows

From (6.4) and (7.10), every non-unit residual degree is in

```text
{3,4,5,6}.
```

Together with the nine unit rows,

```text
rho support subset {1,3,4,5,6},
rho1=9.                                   (8.1)
```

The demand support was already (4.1), and the cutoff is (5.2). Thus every state surviving the A1 necessary conditions lies in the stable support class

```text
D1=0,
s support {2,3,4},
rho support {1,3,4,5,6},
rho1=9,
L=6.                                      (8.2)
```

No histogram enumeration is required for this reduction.

The old exact core enumerator remains valuable as an independent audit: it started from 236,885 broad histogram pairs and found exactly the same support class and exactly the 11 audited A1 profiles.

---

## 9. Completing the A1 certificate argument

Once (8.2) is known, the existing stable-envelope analysis applies.

The scalar-cutoff total-capacity argument on this support gives

```text
D4<=6.
```

Define

```text
U=sum_{s_i>=3} s_i,
V=sum_{s_i>=4} s_i,
Z=sum_{rho_u>=4} rho_u.
```

The exact A1 certificate identity is

```text
gap_A1
 = 1
 + (1454/135)(U-36)
 + (125/54)(24-V)
 + (23/9)(Z-16).                           (9.1)
```

On the support class:

- `D4<=6` gives `V<=24`;
- `h_res=4` gives `Z>=16`;
- zero slack plus `h_res=4` gives `U>=36` as in `N29_T3_A1_SYMBOLIC_COMPRESSION.md`.

Therefore every correction term in (9.1) is nonnegative and

```text
gap_A1>=1.
```

Equality is uniquely the histogram

```text
(D2,D3,D4)=(2,4,6),
(R3,R4,R5,R6)=(3,4,0,0),
```

matching audited frontier profile 1.

---

## 10. Consequence for the research programme

The A1 regime now has the architecture

```text
charging + J + one-label Hall
 -> D1 in {0,2,4}, max demand <=4
 -> D1=4 contradiction
 -> D1=2 hand Hall contradiction
 -> D1=0 hand support reduction
 -> stable support {2,3,4} / {1,3,4,5,6}, L=6
 -> three explicit nonnegative tail slacks
 -> exact gap >=1.
```

The earlier 236,885-state enumeration and the 15,907-state D1=2 sub-enumeration are no longer logical dependencies of the A1 certificate proof. They remain preserved as exact corroborating audits.

The next useful target is not further A1 enumeration. It is to repeat this style of symbolic compression for the adjacent t=3 regimes `(h_res,J)=(4,16)` and `(4,18)`, then identify which coefficients generalise in `(a,b,t,h,J)`.
