# N32, Delta=17, m=257: exact nine-rectangle closure

12 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate exact finite closure inside the established graph-to-RX/Hall bridge. Integer acceptance is green; independent mathematical review remains OPEN.** This note does not claim an unrestricted Murty-Simon theorem.

## 1. Scope

Take

```text
n=32,
Delta=b=17,
a=n-1-b=14,
t=m-b(a+1)=m-255.
```

At `m=257` one has `t=2`. The fourteen-label hand theorem gives

```text
Q(s) <= 23,
```

while the canonical bridge gives

```text
Q(s) >= b+2t = 21.
```

An independent exhaustive score program over all `20,058,300` nondecreasing fourteen-demand multisets in `{0,...,13}` finds exactly

```text
Q=21 : 50 profiles
Q=22 : 18 profiles
Q=23 :  3 profiles
------------------
total: 71 profiles.
```

Every surviving demand is at most five.

Exactly one frontier profile has a zero demand, namely

```text
0,3,3,...,3   (thirteen 3s).
```

The remaining 70 profiles have positive demand.

## 2. Completeness of the residual-profile expansion

For a demand profile `s`, let

```text
z_h^min = gamma_h(W_h),
```

with `z_1=17`, and let `rho^min` be the residual-degree multiset determined by these tail counts.

Write

```text
E = sum_{h>=2}(z_h-z_h^min).
```

Since

```text
S >= r+4,
r = 17 + sum_{h>=2} z_h,
Q = S - sum_{h>=2} z_h^min,
```

one obtains

```text
0 <= E <= Q-21.
```

Thus the `Q=21` rows have no residual-tail slack, the `Q=22` rows have at most one unit, and the `Q=23` rows have at most two units.

Starting from `rho^min`, distributing `E` unit increments among the seventeen positive residual degrees, then sorting, enumerates every residual-degree multiset compatible with these tail lower bounds and total slack. After duplicate removal the 70 positive-demand profiles expand to exactly

```text
154 (s,rho) states.
```

The split is

```text
Q=21 : 49 states
Q=22 : 76 states
Q=23 : 29 states.
```

## 3. Full RX/Hall exact rejection

As a first trust-building step, the existing positive-demand RX/Hall necessary-condition model was run on all 154 states with parameters

```text
a=14, b=17, dmax=12.
```

Every state was numerically infeasible. More importantly, the numerical duals were then converted to exact integer Farkas certificates using the existing unit-density-bound repair procedure. All 154 certificates verify in integer arithmetic.

This already gives an exact finite exclusion conditional on the graph-to-RX/Hall bridge, but the certificates are much larger than necessary.

## 4. Compression to two rectangle layers

Use the BC coordinates from the potential-certificate lemma:

```text
d = R+s,
v = b-(R+x)
```

on the label side and

```text
alpha = rho+q-1,
w = b-(q+p)
```

on the source side.

For integer thresholds `D,V`, put

```text
B_{D,V}(d,v) = 1[d>=D and v>=V].
```

Every such rectangle is coordinatewise nondecreasing. Therefore selected-incidence compatibility gives the graph-level transport inequality

```text
sum_i x_i B_{D,V}(d_i,v_i)
    <=
sum_u q_u B_{D,V}(alpha_u,w_u).
```

A common inverse search over all 154 states showed first that **rectangle generators alone suffice**: no diagonal-slack correction is needed. Restricting further to only the adjacent `D=2` and `D=3` layers still covers every state.

The support can be reduced to the following nine rectangles with the small integer weights shown:

| D | V | weight |
|---:|---:|---:|
| 2 | 0  | 4 |
| 2 | 6  | 2 |
| 2 | 8  | 1 |
| 2 | 10 | 1 |
| 2 | 13 | 1 |
| 2 | 14 | 1 |
| 3 | 9  | 1 |
| 3 | 11 | 1 |
| 3 | 12 | 1 |

Thus define

```text
F = 4 B_{2,0}
  + 2 B_{2,6}
  +   B_{2,8}
  +   B_{2,10}
  +   B_{2,13}
  +   B_{2,14}
  +   B_{3,9}
  +   B_{3,11}
  +   B_{3,12}.
```

Because `b=17`, the same potential in the original `(d,h)` variables, where `h=R+x` on labels and `h=q+p` on sources, is

```text
F(d,h) = 4 1[d>=2]
       + 2 1[d>=2, h<=11]
       +   1[d>=2, h<=9]
       +   1[d>=2, h<=7]
       +   1[d>=2, h<=4]
       +   1[d>=2, h<=3]
       +   1[d>=3, h<=8]
       +   1[d>=3, h<=6]
       +   1[d>=3, h<=5].
```

This is the complete global potential: there are no fitted per-profile rectangle weights.

## 5. Exactification of the nine-term potential

The nine weights above were pinned exactly at their displayed integer values. Only the profile-specific scalar envelope coefficients from the potential-certificate lemma were allowed to vary.

The common finite system is feasible already at ray scale `1`. Rounding the profile-specific duals with denominator `100000`, followed by the established exact one-sided envelope repair, gives:

```text
positive-demand states:        154
contradiction margins:         154
nonnegative margins:             0
zero-RHS row violations:         0
bound violations:                0
repair count:                  269
repair total numerator:        582
worst contradiction numerator: -99891
```

Hence every contradiction margin is strictly negative in exact integer arithmetic.

The locally generated full certificate had SHA-256

```text
908c07e00ad93b94247ada11894e908d71effdb16c2f8322535e20da4b21a462
```

and its zero-suppressed representation had SHA-256

```text
1e9bd93496ed85d9a5209c2511a13f09f3dc2168c98dcab2eaf19944991a9704
```

The committed exactifier regenerates and checks the certificate rather than treating either hash as a proof premise.

By `POTENTIAL_CERTIFICATE_LEMMA.md`, once the displayed rectangle weights and the finite envelope inequalities are checked, the contradiction is elementary summation, threshold transport, and monotone incidence double counting. Linear programming is a discovery mechanism only.

## 6. The exceptional zero-demand profile

The sole zero-demand frontier is

```text
s=(0,3^13).
```

Here `S=39` and `Q=21`, so all score/tail inequalities are exact. In particular

```text
gamma_2(39)=gamma_3(39)=9,
r=35,
```

and the residual source degrees are exactly

```text
3^9,1^8.
```

Let `Z` be the nine residual-degree-three sources. The thirteen positive-demand labels each require three selected incidences, and selected-incidence forcing says all such incidences originate in `Z`. Thus at least 39 selected incidences originate in `Z`.

At threshold `h=2`, the capacity is exact:

```text
C_2(9)=39.
```

Therefore the same equality analysis as in the N31 `Delta=17,m=240` endpoint applies. If `J={u in Z:q_u>2}`, equality forces `|J|=6` or `7` and sends at least 33 selected exceptions back into `Z`, hence

```text
sum_{u in Z} p_u >= 33.
```

The nine high sources have total selected outdegree exactly 39. Since the thirteen positive-demand labels already require all 39 of those incidences, no high-source incidence can be spent on the zero-demand label; each positive label has selected degree exactly three.

For any active high source `u` and one of its positive selected labels `i`, the endpoint-load and source-degree inequalities give

```text
q_u+p_u <= R_i+x_i=d_i <= rho_u+q_u-1=q_u+2,
```

so `p_u<=2`. Hence

```text
sum_{u in Z} p_u <= 18,
```

contradicting the lower bound 33.

Thus the zero-demand profile is impossible by hand.

## 7. Consequence

Combining Sections 3-6:

```text
n=32, Delta=17, m=257
```

is impossible inside the current candidate bridge framework.

Together with the already hand-closed `m>=258` branch, this gives the **candidate N32 Turan upper bound**

```text
e(G) <= 256.
```

This is not yet the full reviewer-facing equality theorem. To conclude that equality occurs only for `K_{16,16}`, the `m=256` equality layer still has to be audited, in particular the `Delta=17,t=1` branch. The balanced `Delta=16` branch is expected to collapse separately by degree/witness rigidity.

## 8. Trust boundary

- The nine-term potential is exact finite evidence, not external validation.
- Its mathematical implication is conditional on the canonical graph-to-RX/Hall bridge and the potential-certificate lemma.
- The positive-demand finite envelope remains computer-checked; the global potential itself is only nine simple graph-level rectangle counts.
- The zero-demand row is excluded by the displayed hand argument.
- Independent specialist review and novelty assessment remain OPEN.
