# n=29, t=3, A1 regime: hand elimination of the D1=2 branch

11 September 2026. Research direction: Paul Lenz. Mathematical development and hostile checking: ChatGPT/Geeps.

**Status: candidate hand lemma inside the RX-Hall programme.** This removes the previously unresolved `D1=2` pre-support branch from the A1 symbolic reduction. It is conditional on the same graph-to-profile / scalar-cutoff / Hall premises already stated in `N29_T3_A1_SYMBOLIC_COMPRESSION.md`. It is not a general-N theorem.

## 1. Setting

We are in the `n=29, Delta=16, t=3` A1 regime with

```text
a=12,
b=16,
h_res=4,
J=2 z_2-D_1=14,
S=r+6,
```

and now assume

```text
D_1=2.
```

Here `D_j=#{i:s_i=j}` and `z_2=#{u:rho_u>=2}`.

From `J=14`,

```text
z_2=8,
```

so exactly eight residual sources have degree one and eight are non-unit.

The one-label Hall condition together with `h_res=4` gives

```text
max_i s_i <=4.
```

Thus

```text
D_2+D_3+D_4=10.                           (1.1)
```

## 2. Zero slack and h=4 leave only nine demand histograms

The demand sum is

```text
S=2+2D_2+3D_3+4D_4
 =22+D_3+2D_4.
```

Since `S=r+6`,

```text
r=16+D_3+2D_4
 =36-2D_2-D_3.                            (2.1)
```

Eight residual rows have degree one, so the other eight have total residual mass

```text
N=r-8=28-2D_2-D_3.                        (2.2)
```

Because `h_res=4`, at least four of these eight non-unit rows have degree at least four. Every other non-unit row has degree at least two. Hence

```text
N >= 4*4+4*2=24.
```

Combining with (2.2),

```text
2D_2+D_3<=4.                              (2.3)
```

In particular

```text
D_2<=2,
D_4>=6.                                   (2.4)
```

This already reduces the branch to the nine integer pairs

```text
(D2,D3) =
(0,0),(0,1),(0,2),(0,3),(0,4),
(1,0),(1,1),(1,2),(2,0).
```

No finite graph or profile enumeration has been used.

## 3. The largest-eight Hall prefix

Take the eight largest demands. Because there are two unit demands and `D_2<=2`, all demand-1 and demand-2 labels lie among the four discarded smallest labels. Therefore every demand in the largest-eight prefix is either three or four.

Since `D_4>=6`, at most two members of the prefix have demand three. Let

```text
k = # demand-3 labels in the largest-eight prefix,
```

so

```text
0<=k<=2.                                  (3.1)
```

Write the eight non-unit residual rows as:

```text
X = # rows of degree 2,
Y = # rows of degree 3,
M = # rows of degree >=4.
```

Then

```text
X+Y+M=8.                                  (3.2)
```

The residual-mass lower bound is

```text
N >= 2X+3Y+4M
  = 16+Y+2M.
```

Using (2.2),

```text
Y+2M <= 12-2D_2-D_3.                     (3.3)
```

Let `L` be the scalar supplement cutoff and let `Q` be the total Hall supply to the largest-eight prefix.

Rows of degree one or two supply **nothing** to this prefix, because all eight demands are at least three. A degree-three row can meet at most the `k<=2` demand-three labels. A row of degree at least four has terminal selected-degree cap at most `L`. Hence

```text
Q <= kY+LM.                               (3.4)
```

The Hall condition requires `Q` to be at least the sum of the largest eight demands. We now show this is impossible for every possible L.

## 4. First, L<=7

For a residual-1 row,

```text
C(1)=D_1=2,
```

so its scalar score `rho+C(rho)` is only three.

If `L>=8`, the cutoff gate at level eight would require at least nine sources with score at least seven. None of the eight residual-1 sources qualifies, leaving only eight possible supporters. Therefore

```text
L<=7.                                     (4.1)
```

There are only three cases.

## 5. Case L<=5

From (3.4), `k<=2`, and (3.3),

```text
2Q <= 4Y+10M
   <= 5Y+10M
   = 5(Y+2M)
   <= 5(12-2D_2-D_3).                    (5.1)
```

If `(D_2,D_3)=(0,0)`, (5.1) gives `Q<=30`, while all ten non-unit demands are four and the largest-eight demand sum is

```text
32.
```

Otherwise `2D_2+D_3>=1`, so (5.1) gives

```text
2Q<=55,
```

hence the integer Q satisfies `Q<=27`. But `D_4>=6`, so the largest eight demands contain at least six fours and the other two demands are at least three; their sum is at least

```text
6*4+2*3=30.
```

Thus Hall fails throughout `L<=5`.

## 6. Case L=6

If `D_4>=8`, then the largest-eight prefix consists entirely of fours, so `k=0`. Apart from the special pair `(D_2,D_3)=(0,0)`, (2.3) gives

```text
12-2D_2-D_3 <=10.
```

Then (3.3) gives `M<=5`, so

```text
Q<=6M<=30<32.
```

If `D_4=7`, then `k=1`. The only possibilities allowed by (2.3) are

```text
(D_2,D_3)=(0,3) or (1,2).
```

Their right sides in (3.3) are respectively 9 and 8. Maximising `Y+6M` under `Y+2M<=9` gives at most 25, and under `<=8` gives at most 24. The corresponding largest-eight demand sum is 31. Hall fails.

If `D_4=6`, necessarily `(D_2,D_3)=(0,4)`, `k=2`, and (3.3) gives `Y+2M<=8`. Hence

```text
Q<=2Y+6M<=3(Y+2M)<=24<30.
```

It remains only `(D_2,D_3)=(0,0)`. Here all ten non-unit demands are four, so `k=0` and the largest-eight demand sum is 32.

Suppose `M=6`. Equation (2.2) gives `N=28`. Since the other two non-unit rows have degree at least two,

```text
N>=6*4+2*2=28,
```

so equality must hold everywhere: the residual multiset is

```text
rho_nonunit=(2,2,4,4,4,4,4,4).
```

For a residual-2 source,

```text
C(2)=#{i:s_i<=2}=2,
```

so its scalar score is only four. But `L=6` requires the level-six cutoff gate to have at least seven supporters of score at least five. Only the six residual-4 sources can qualify, contradiction.

Therefore `M<=5`, and again

```text
Q<=6M<=30<32.
```

So `L=6` is impossible.

## 7. Case L=7

The level-seven cutoff gate requires eight sources of score at least six. The residual-1 sources again fail, so **all eight non-unit residual sources must qualify**.

If `D_2+D_3>0`, then (2.2) gives `N<28`. If there were no residual-2 source, the eight non-unit rows, with at least four of degree at least four and the other four of degree at least three, would have total mass at least

```text
4*4+4*3=28,
```

contradiction. Hence a residual-2 source exists.

For such a source,

```text
C(2)=2+D_2,
score=2+C(2)=4+D_2.
```

The level-seven gate requires this score to be at least six, hence `D_2>=2`. By (2.3),

```text
D_2=2,
D_3=0,
D_4=8.                                   (7.1)
```

If instead `D_2=D_3=0`, then `N=28`. A residual-2 source has score four and already kills the level-seven gate. If no residual-2 source exists, equality in the lower bound `N>=4*4+4*3=28` forces four residual-3 and four residual-4 rows. But with ten demand-4 labels,

```text
C(3)=#{i:s_i<=3}=2,
```

so every residual-3 source has score five, again killing the level-seven gate. Thus this subcase is also impossible.

We are therefore in (7.1). Now (2.2) gives `N=24`. Since `h_res=4`, `M>=4`; (3.3) becomes

```text
Y+2M<=8,
```

so necessarily `M=4` and `Y=0`. The largest-eight prefix is exactly the eight demand-4 labels. Only the four rows of residual degree at least four can serve it, and each has cap at most `L=7`. Therefore

```text
Q<=4*7=28<32.
```

Hall fails.

## 8. Conclusion

Every possible scalar cutoff has been eliminated:

```text
L<=5: Hall contradiction,
L=6:  Hall contradiction,
L=7:  Hall contradiction,
L>=8: cutoff-gate contradiction.
```

Hence

```text
boxed: D_1=2 is impossible in the (h_res,J)=(4,14), t=3 A1 regime.
```

This removes the only pre-support branch that `N29_T3_A1_SYMBOLIC_COMPRESSION.md` still identified as requiring a 15,907-state exact enumeration.

The argument is structural: after the one-label reduction, it uses only zero slack, `h_res=4`, the scalar-cutoff gate, and one Hall inequality on the largest eight demands.

## 9. What remains

The A1 programme is now closer to a hand proof, but this note does **not** claim that all finite preparation has vanished. The `D_1=0` branch still contains the exact eleven-profile support class used by the current slack identity. The next compression target is to derive all support restrictions needed for the stable A1 envelope on that branch without histogram enumeration.
