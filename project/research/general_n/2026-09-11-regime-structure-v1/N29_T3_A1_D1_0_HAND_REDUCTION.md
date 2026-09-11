# n=29, t=3, A1 regime: hand support reduction for the D1=0 branch

11 September 2026. Research direction: Paul Lenz. Mathematical development and hostile checking: ChatGPT/Geeps.

**Status: candidate hand lemma inside the RX-Hall programme.** Conditional on the same graph-to-profile, scalar-cutoff and Hall premises as `N29_T3_A1_SYMBOLIC_COMPRESSION.md`. This is not a general-N theorem.

## 1. Setting

Work in the `n=29, Delta=16, t=3` A1 regime

```text
a=12,
b=16,
h_res=4,
J=2 z_2-D_1=14,
S=r+6,
```

and assume

```text
D_1=0.
```

Here `D_j=#{i:s_i=j}` and `z_2=#{u:rho_u>=2}`.

The one-label Hall condition and `h_res=4` give

```text
max_i s_i<=4.
```

Thus

```text
D_2+D_3+D_4=12.                            (1.1)
```

From `J=14` and `D_1=0`,

```text
z_2=7,
```

so exactly nine residual sources have degree one and seven are non-unit.

## 2. Zero slack gives the first demand restriction

The demand sum is

```text
S=2D_2+3D_3+4D_4
 =36-D_2+D_4.
```

Hence

```text
r=S-6=30-D_2+D_4.                          (2.1)
```

The seven non-unit residual rows therefore have total mass

```text
N=r-9=21-D_2+D_4.                         (2.2)
```

Because `h_res=4`, at least four of these seven rows have residual degree at least four; the other three have residual degree at least two. Thus

```text
N>=4*4+3*2=22.
```

Combining with (2.2),

```text
D_4>=D_2+1.                               (2.3)
```

Together with (1.1), this gives

```text
D_2<=5.                                   (2.4)
```

## 3. The scalar cutoff is exactly L=6

There are only seven non-unit residual sources. A cutoff gate at level seven would require eight supporting sources, while every residual-1 source has scalar score one because `D_1=0`. Therefore

```text
L<=6.                                     (3.1)
```

On the other hand, if `L<=5`, the total terminal selected-degree capacity is at most

```text
7*5=35,
```

because the nine residual-1 sources have selected cap zero. But `N>=22` gives `r>=31`, so zero slack gives

```text
S=r+6>=37.
```

Since `sum x_i=sum q_u` and `x_i>=s_i`, total selected capacity must be at least S. Contradiction.

Hence

```text
boxed: L=6.                               (3.2)
```

In particular, the level-six cutoff gate requires all seven non-unit sources to have scalar score at least five.

## 4. No residual degree can exceed six

For a source of residual degree rho, let

```text
g(rho)=q_u^*-rho
```

be its maximum selected-capacity surplus over residual mass under `L=6`.

For the possible source types:

- a residual-2 source has `q_u^*<=D_2<=5`, so `g(2)<=3`;
- a residual-3 source has `q_u^*<=6`, so `g(3)<=3`;
- residual 4,5,6 have gains at most 2,1,0 respectively;
- a residual degree at least 7 has `q_u^*<=12-rho`, hence `g(rho)<=-2`.

Total capacity requires

```text
sum_nonunit q_u^* >= S = r+6 = N+15,
```

so

```text
sum_nonunit g(rho_u)>=15.                 (4.1)
```

Assume one of the seven non-unit rows has residual degree at least seven. Since `h_res=4`, at least three further rows have degree at least four. To maximise the left side of (4.1), give those three rows the maximal gain 2 and give each of the remaining three rows the maximal low-degree gain 3. Even then

```text
sum g <= -2 + 3*2 + 3*3 = 13 < 15,
```

contradiction.

Therefore

```text
rho_u<=6 for every residual source.       (4.2)
```

At this stage the only possible non-unit residual degrees are 2,3,4,5,6.

## 5. If residual degree two occurs, then D2>=3

Suppose there is a residual-2 source. Since `L=6`, every one of the seven non-unit sources must support the level-six gate, hence must have scalar score at least five.

For residual degree two,

```text
C(2)=#{i:s_i<=2}=D_2,
score=2+D_2.
```

Therefore

```text
D_2>=3.                                   (5.1)
```

By (2.4), only

```text
D_2=3,4,5                                 (5.2)
```

remain.

We show each is impossible using total-capacity bookkeeping followed by one Hall inequality on the seven largest demands.

## 6. Exact capacity-surplus identity

Let

```text
X = # residual-2 rows,
Y = # residual-3 rows,
H_j = # residual-j rows  (j=4,5,6),
M=H_4+H_5+H_6.
```

Then

```text
X+Y+M=7.                                  (6.1)
```

Let

```text
g_3=min(6,12-D_4)-3
```

be the selected-capacity surplus of a residual-3 row.

The excess residual mass of the high rows over degree four is

```text
E=H_5+2H_6.
```

Using (2.2) and (6.1),

```text
E=D_4-D_2-7+2X+Y.                         (6.2)
```

The total selected-capacity surplus of all seven non-unit rows is at most

```text
G
 =X(D_2-2)+Y g_3+2H_4+H_5
 =21+D_2-D_4+X(D_2-6)+Y(g_3-3).          (6.3)
```

Total selected capacity requires

```text
G>=15.                                    (6.4)
```

Also

```text
E>=0.                                     (6.5)
```

These two elementary inequalities almost completely determine the residual histogram in each remaining D2 case.

## 7. Case D2=3

By (2.3), `D_4>=4`.

Equation (6.3) gives

```text
G=24-D_4-3X+Y(g_3-3).
```

Since `g_3<=3`, (6.4) implies

```text
D_4+3X<=9.
```

As `X>=1`, we get `D_4<=6` and therefore `g_3=3`.

Now (6.2) becomes

```text
E=D_4-10+2X+Y>=0.
```

Also `h_res=4` gives `M>=4`, hence `X+Y<=3`.

The inequality `D_4+3X<=9` with `D_4>=4` forces `X=1`. Then

```text
Y>=8-D_4,
Y<=2.
```

Hence `D_4=6`, `Y=2`, and `M=4`.

The seven largest demands are six 4s and one 3, of total

```text
27.
```

A residual-2 row supplies nothing to this prefix; each of the two residual-3 rows supplies at most the single demand-3 label; and the four rows of degree at least four have cap at most six. Thus Hall supply is at most

```text
2*1+4*6=26<27.
```

Contradiction.

## 8. Case D2=4

Now `D_4>=5`.

If `D_4<=6`, then `g_3=3` and (6.3) becomes

```text
G=25-D_4-2X.
```

If `D_4=5`, (6.2) gives

```text
2X+Y>=6,
```

while `X+Y<=3`; this is impossible together with `X>=1` and (6.4), which gives `X<=2`.

Thus `D_4=6`. Then (6.4) gives `X<=2`, while (6.2) gives

```text
2X+Y>=5.
```

With `X+Y<=3`, necessarily

```text
X=2,
Y=1,
M=4.
```

The seven largest demands are six 4s and one 3, total 27. The two residual-2 rows supply nothing, the single residual-3 row supplies at most one, and the four high rows supply at most 24. Hence

```text
Q<=25<27,
```

contradiction.

If `D_4>=7`, then

```text
g_3-3=6-D_4<=-1.
```

Equation (6.3) and `G>=15` give

```text
2X+(D_4-6)Y<=10-D_4.                     (8.1)
```

But (6.2) gives

```text
2X+Y>=11-D_4.                            (8.2)
```

Since `D_4-6>=1`, the left side of (8.1) is at least the left side of (8.2), whereas `11-D_4>10-D_4`. Contradiction.

Thus D2=4 is impossible.

## 9. Case D2=5

By (2.3), `D_4>=6`, while (1.1) gives `D_4<=7`.

### 9.1 D4=6

Here `D_3=1` and `g_3=3`. Equation (6.2) gives

```text
2X+Y>=6.
```

But `X+Y<=3`, so necessarily

```text
X=3,
Y=0,
M=4.
```

The seven largest demands are six 4s and one 3, total 27. Only the four high rows can serve that prefix, each with cap at most six. Hence

```text
Q<=24<27,
```

contradiction.

### 9.2 D4=7

Now `D_3=0`. Equation (6.2) gives

```text
2X+Y>=5,
```

with `X+Y<=3`. Thus the only possibilities are

```text
(X,Y)=(2,1) or (3,0),
```

and in either case `M=4`.

The seven largest demands are all 4s, total 28. Residual-2 and residual-3 rows cannot serve a demand-4 label, so only the four high rows contribute, each with cap at most six:

```text
Q<=24<28.
```

Contradiction.

Thus D2=5 is impossible.

## 10. Hand-derived support class

Sections 5--9 show that a residual-2 source cannot exist. Section 4 already excluded residual degree at least seven. Therefore the residual support is exactly contained in

```text
{1,3,4,5,6}.
```

Together with `D_1=0`, `max s_i<=4`, and positive demands, the demand support is contained in

```text
{2,3,4}.
```

We have also proved

```text
rho_1=9,
L=6.
```

These are precisely the support restrictions assumed by the stable A1 envelope and three-slack identity in `N29_T3_A1_SYMBOLIC_COMPRESSION.md`.

Thus **the A1 support class is now derived without histogram enumeration**.

The existing three-slack identity then gives

```text
gap_A1
 =1 + (1454/135)(U-36)
    + (125/54)(24-V)
    + (23/9)(Z-16)
 >=1,
```

with equality only at the already identified extremal profile.

## 11. Consequence for the A1 regime

The complete A1 regime now has a hand reduction:

```text
J=14, h_res=4
 -> D1 in {0,2,4}
 -> D1=4 impossible by elementary mass bounds
 -> D1=2 impossible by the largest-eight Hall argument
 -> D1=0 forces L=6 and support s in {2,3,4}, rho in {1,3,4,5,6}
 -> three nonnegative tail slacks
 -> gap_A1>=1.
```

The historical 236,885-state exact core replay remains valuable corroborating evidence, but it is no longer a logical dependency of the symbolic A1 certificate argument.

The next research target is to seek the analogous symbolic support reduction and slack decomposition for the adjacent `A530` regimes `(h_res,J)=(4,16)` and `(4,18)`.
