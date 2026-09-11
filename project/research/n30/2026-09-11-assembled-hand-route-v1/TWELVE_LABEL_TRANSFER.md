# A source-independent twelve-label tail bound

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal review: ChatGPT/Geeps.

**Candidate hand lemma and corollaries. Independent specialist review and novelty assessment OPEN.**

The N29 twelve-label tail argument does not depend on having sixteen sources. Making that fact explicit closes the remaining N30 Delta=17 scopes, and the same padding argument covers all higher non-star degrees. No demand-profile enumeration or Hall dual is a premise of this result.

## 1. Remove the source cutoff from the definition

For each integer `h>=2`, set

$$
C_h(z)=\frac{z(z-1)+h(h+1)}2,\qquad
\gamma_h(0)=0,
$$

and, for `W>0`, define `gamma_h(W)` as the least **integer z>=h**, with no upper cutoff, for which `W<=C_h(z)`. This minimum always exists.

For twelve demands `0<=s_i<=11`, put

$$
N_h=\#\{i:s_i\ge h\},\quad W_h=\sum_{s_i\ge h}s_i,
\quad p=N_1,
$$

$$
D=\sum_{h=2}^{11}(N_h-\gamma_h(W_h)),\qquad
Q=\sum_i s_i-\sum_{h=2}^{11}\gamma_h(W_h)=p+D.
$$

We prove `D<=6`, hence **Q<=18**. This is the [earlier N29 hand argument](../../general_n/2026-09-11-threshold-tail-collapse-v1/N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md) with the artificial source-count cutoff removed explicitly. The proof below uses only lower bounds on gamma and small capacity values; no step needs `z<=16`.

## 2. Clip high demands to six

For `h>=7`, let `N=N_h`. If `0<N<h`, then `gamma_h>=h>N`. Otherwise write `N=h+e`, with `0<=e<=12-h<=5`. Since `W_h>=hN`, a positive deficit would imply `hN<=C_h(N-1)`. But

$$
2hN-2C_h(N-1)=-e^2+3e+2h-2>0.
$$

The concave quadratic is positive at both endpoints of `[0,5]`, where it has values `2h-2` and `2h-12`. Thus every deficit at level at least seven is nonpositive.

Clipping all demands above six to six removes these nonpositive deficits. At lower levels it keeps `N_h` fixed and decreases `W_h`, so it cannot decrease `D`.

## 3. Clip six, five and four

When the maximum is six, let `k` count the sixes. Their level-six deficit is nonpositive for `k<=10`. For `k=11,12` it equals one. If `l` counts existing fives, the required payments are:

| k,l | W5 before | W5 after | gamma5 drop |
|---|---:|---:|---:|
| 11,0 | 66 | 55 | 1 |
| 11,1 | 71 | 60 | 2 |
| 12,0 | 72 | 60 | 2 |

Each drop pays the lost positive level-six deficit. Thus six-to-five clipping never decreases `D`.

At maximum five, the level-five deficit is nonpositive for `k<=9`, and equals one for `k=10,11`. If `l` counts fours, the five possibilities `(k,l)=(10,0),(10,1),(10,2),(11,0),(11,1)` all have

$$
\gamma_4(5k+4l)-\gamma_4(4(k+l))=1.
$$

This pays the lost deficit. The exceptional vector `(5^12)` is discharged directly: its thresholds `(gamma2,gamma3,gamma4,gamma5)=(12,11,11,10)` give `D=4`. Thus every vector is either already bounded or clips to maximum four without decreasing `D`.

At maximum four, the level-four deficit is nonpositive for `k<=8`, one for `k=9,10`, and two for `k=11,12`. Let `l` count threes. For `k=9`, the gamma3 drops at `l=0,1,2,3` are `2,1,1,1`; for `k=10`, the drops at `l=0,1,2` are `1,2,1`. These pay the deficit one.

For `k=11` with the last entry at most two, gamma3 drops by two. If the last entry is three, both gamma3 and gamma2 drop from ten to nine. For `(4^12)`, both again drop from ten to nine. These pay the deficit two. Clipping to maximum three therefore cannot decrease `D`.

All these statements are direct substitutions in `C_h(z)`. Nonpositive-deficit cutoffs can also be checked by testing `z=k-1`, exactly as in Section 2. Lower levels not used for payment only improve.

## 4. Two tail counts finish the bound

At maximum three, set `x=N_2`, `y=N_3`, so `0<=y<=x<=12`. Then

$$
D=x+y-\gamma_2(2x+y)-\gamma_3(3y).
$$

The following three ranges suffice.

| Range | x-gamma2(2x+y) at most | y-gamma3(3y) at most | D at most |
|---|---:|---:|---:|
| 0<=y<=6 | 5 | 0 | 5 |
| 7<=y<=10 | 4 | 2 | 6 |
| 11<=y<=12 | 3 | 3 | 6 |

For completeness, the strict capacity defects proving the entries are:

- For the first range, `x<=7` is immediate from `gamma2>=2` when `x>0`; for `8<=x<=12`, testing `z=x-6` gives `2x-C_2(x-6)=(-x^2+17x-48)/2>0`. The y-bound is immediate for `y<=3`; for `4<=y<=6`, test `z=y-1` to get `3y-C_3(y-1)=(-y^2+9y-14)/2>0`.
- For `7<=y<=10`, test `z=y-3` in gamma3: the defect is `(-y^2+13y-24)/2>0`. Test `z=x-5` in gamma2: the defect is `(-x^2+15x+2y-36)/2>=(-x^2+15x-22)/2>0` for `7<=x<=12`.
- For `11<=y<=12`, test `z=y-4` in gamma3, obtaining `(-y^2+15y-32)/2>0`. Only `x=11,12` are possible; testing `z=x-4` in gamma2 gives `(-x^2+13x+2y-26)/2>=(-x^2+13x-4)/2>0`.

The empty tails have gamma equal to zero and are handled separately in the first range. Positivity over each listed interval follows by checking the endpoints of the concave quadratics. Therefore `D<=6` and `Q<=p+6<=18`. QED.

## 5. Transfer to actual graphs with any source count

Use the [canonical parameterized bridge](../../general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md). Let

$$
a=n-1-\Delta,\quad b=\Delta,\quad
t=m-b(a+1)>0.
$$

An actual graph gives positive residual degrees on all b sources and demands `0<=s_i<=a-1`. Its residual tails `z_h` satisfy `z_h>=gamma_h(W_h)` whenever the demand tail is nonempty. For empty demand tails, the right side is zero. Extend these zeros to all residual levels. The tail-sum identity and demand ledger give

$$
S\ge r+2t=b+2t+\sum_{h=2}^{a}z_h
\ge b+2t+\sum_{h=2}^{a-1}\gamma_h(W_h),
$$

so

$$
Q\ge b+2t. \tag{1}
$$

There is no issue when gamma would exceed b: then no actual residual tail could satisfy the necessary capacity inequality in the first place.

If `1<=a<=12`, pad the demand vector with zeros to length twelve. The score is unchanged because all added higher tails have zero demand. Section 4 therefore gives `Q<=18`, regardless of b.

Consequently, if `1<=a<=12` and `b>=17`, positive integer surplus would give

$$
19\le b+2t\le Q\le18,
$$

a contradiction. We obtain the candidate general corollary

$$
1\le n-1-\Delta\le12,\quad \Delta\ge17
\quad\Longrightarrow\quad
e(G)\le\Delta(n-\Delta).
$$

This bound is attained by the corresponding complete bipartite graph; no uniqueness assertion at this bound is made. It is a consequence of the project's candidate universal bridge and this hand lemma, not a claim of independent novelty or an unrestricted solution.

## 6. N30 consequences

For `n=30,Delta=17`, `(a,b)=(12,17)` and `t=m-221`. Every `m>=222` has positive surplus, so

$$
e(G)\le221.
$$

This simultaneously removes the historical 15-profile m227 check, 250-profile m226 threshold check, and the 1,155-profile m225 charging/threshold/source-count chain with its 18 final Hall duals from the new route.

For `Delta=18,...,28`, one has `1<=a<=11` and `Delta(30-Delta)<=216<225`; the same corollary excludes every `m>=225` without any charging-domain enumeration. `Delta=29` is the elementary universal-vertex/star case.

The independent regression enumerates all 1,352,078 twelve-demand multisets using the unbounded gamma definition and finds maximum Q equal to eighteen with no clipping failure. That regression corroborates the argument above; it is not its proof premise.
