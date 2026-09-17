# Quadratic endpoint continuation: selected excess at least three in the mixed 4/5 band

17 September 2026. Research directed by Paul Lenz; derivation and internal audit by ChatGPT/Geeps.

**Status: candidate bridge theorem; not promoted; external mathematical review remains open.** This continues the quadratic endpoint-load argument at the near-Turán scope `(a,b,t)=(20,23,2)`. The previous note treated zero selected excess. Here the exact selected-incidence system is used to show that total selected excess one or two is impossible as well.

## 1. Setup and notation

Work in the all-positive-demand canonical selected/residual bridge at

    a=20, b=23, t=2.

Assume all twenty positive demands satisfy

    s_i in {4,5}.

Let `k` be the number of demand-five labels. Write

    x_i = s_i + e_i,
    E = sum_i e_i,

where `e_i>=0` is selected excess. Let `R_i` be residual column degree, `rho_u` residual source degree, and `p_u,q_u` the incoming/outgoing orientation loads. Then

    S := sum_i s_i = 80+k,
    r = S-2t = 76+k,
    Q := sum_i x_i = S+E = 80+k+E,
    sum_u p_u = sum_u q_u = Q.

Assume at least five residual sources have `rho_u>=5`. As in the preceding mixed-band argument, positive residual activity gives `rho_u>=1` for every one of the 23 sources.

For every selected incidence `ui`, retain the established canonical facts

    C_i := R_i+x_i >= p_u+q_u,
    s_i <= rho_u,
    e_i >= g_u := max(0,p_u-rho_u+1).

Also selected labels at a fixed source are distinct.

## 2. General weighted incidence ledger

The quadratic endpoint lemma can be combined directly with the selected-excess inequality. For every real `lambda>=0`, every selected incidence satisfies

    C_i + lambda e_i
      >= p_u+q_u + lambda g_u.

Summing over the actual selected incidence matrix, whose row degrees are exactly `q_u` and whose column degrees are exactly `x_i`, gives

> **Weighted endpoint/excess ledger**
>
>     sum_i x_i(C_i+lambda e_i)
>       >= sum_u q_u(p_u+q_u+lambda g_u).              (1)

The case `lambda=0` is the previous quadratic endpoint-load lemma. This weighted form is retained for the later `E>=3` attack. The small-excess closure below needs only `lambda=0`, together with the fact that the total excess budget controls how many distinct selected labels can support a source with `g_u>0`.

## 3. The zero-excess label ceiling can be sharpened

Because all demands are positive, `s_i=d_i-R_i`, where `d_i` is the `F`-degree of label `i`. Since `a=20`,

    d_i=R_i+s_i <=19.

Thus a demand-five label has `R_i<=14` and a demand-four label has `R_i<=15`.

At zero excess the label side of the quadratic endpoint ledger is

    sum_i s_i(R_i+s_i)
      = 4r + R_5 + 320+9k,

where `R_5` is the total residual degree on the `k` demand-five labels. Hence

    R_5 <= min(14k,r)=min(14k,76+k)

and therefore

>     U_0(k)
>       := 624+13k+min(14k,76+k)                       (2)
>
> is a universal zero-excess upper bound on the label side.

This is slightly sharper than the earlier bound that used only disjointness of selected and residual B-incidences.

## 4. How much can one or two units of excess enlarge the label side?

For fixed `s_i,R_i`, replacing `x_i=s_i` by `x_i=s_i+e_i` changes the unweighted label contribution by

    (s_i+e_i)(R_i+s_i+e_i)-s_i(R_i+s_i)
      = e_i(d_i+s_i)+e_i^2.

Since `d_i<=19` and `s_i<=5`, this is at most

    24e_i+e_i^2.

Summing and using `sum e_i=E` and `sum e_i^2<=E^2` gives, for `E<=2`,

>     sum_i x_i C_i <= U_0(k)+24E+E^2.                 (3)

Thus the label side can rise by at most 25 when `E=1` and by at most 52 when `E=2`.

## 5. The source lower bound survives unchanged for E<=2

Retain the local support inequality used in the zero-excess proof:

    10p_u+15q_u-q_u(p_u+q_u)
      <= 10rho_u+20+delta_k [rho_u=4],                 (4)

where

    delta_k=6       for 0<=k<=14,
    delta_15=5,
    delta_16=2,
    delta_k=0       for 17<=k<=20.

For `q_u=0`, (4) follows from the incoming cap `p_u<=rho_u+2`.

Suppose `q_u>0`. If `p_u<=rho_u-1`, the preceding zero-excess proof applies verbatim. If `p_u>=rho_u`, then every one of the `q_u` distinct selected labels at the source has excess at least

    g_u=max(0,p_u-rho_u+1).

Therefore

    q_u g_u <= E.                                      (5)

When `E<=2`, the only additional possibilities are

    p=rho,   q<=2,
    p=rho+1, q<=1.

(The case `p>=rho+2` would have `g>=3` and is impossible.) Direct substitution gives

    p=rho,q=1:     10p+15q-q(p+q)=9rho+14,
    p=rho,q=2:     10p+15q-q(p+q)=8rho+26,
    p=rho+1,q=1:   10p+15q-q(p+q)=9rho+23.

Every active source has `rho>=4`, so each expression is at most `10rho+20`; for `rho=4` the additional nonnegative `delta_k` only helps. Hence (4) remains valid without modification for total selected excess zero, one or two.

Summing (4), using `sum p=sum q=Q`, gives

    sum_u q_u(p_u+q_u)
      >= 25Q-10r-20b-delta_k c_4,

where `c_4=#{u:rho_u=4}`. As before, at least five sources have residual degree at least five and every source has residual degree at least one, so

    r >= 5*5 + 4c_4 + (23-5-c_4),

hence

    c_4 <= floor((33+k)/3).                             (6)

Define

    L_0(k)
      :=780+15k-delta_k floor((33+k)/3).                (7)

Then for total excess `E<=2`,

>     sum_u q_u(p_u+q_u) >= L_0(k)+25E.                (8)

## 6. Finite arithmetic gap

For `k=0,...,20`, let

    G(k)=L_0(k)-U_0(k).

The exact values are

| k | G(k) | k | G(k) | k | G(k) |
|---:|---:|---:|---:|---:|---:|
|0|90|7|9|14|4|
|1|78|8|10|15|15|
|2|66|9|5|16|64|
|3|48|10|6|17|97|
|4|36|11|7|18|98|
|5|24|12|2|19|99|
|6|8|13|3|20|100|

Thus `G(k)>=2` for every mixture, with equality only at `k=12`.

Combining (3) and (8), any real bridge would require

    U_0(k)+24E+E^2
      >= L_0(k)+25E,

or equivalently

    G(k)+E-E^2 <=0.                                    (9)

For `E=0` this contradicts `G(k)>0`, recovering and strengthening the preceding zero-excess closure.

For `E=1`, the left side is `G(k)>0`, contradiction for every k.

For `E=2`, it is `G(k)-2`. This is positive for every `k!=12`. Only the arithmetic boundary `(k,E)=(12,2)` can attain equality in these relaxed bounds.

## 7. Hand closure of the sole boundary k=12,E=2

At `k=12`,

    r=88,
    Q=94,
    delta_k=6,
    c_4<=15.

Equality in (9) would force equality everywhere in the source and label estimates. In particular `c_4=15`. Equality in the residual-mass bound (6) then forces the residual source multiset

    rho=(5^5,4^15,1^3),                                (10)

because its minimum possible mass is already

    5*5+15*4+3*1=88=r.

Equality in the summed local source inequality (4) would require equality at every source. But:

- at `rho=1`, `q=0` and `p<=3`, so certainly `p<=3`;
- at `rho=4`, any equality state has `p<=3`: if `p>=4`, then (5) with `E=2` leaves only `(p,q)=(4,1),(4,2),(5,1)`, and direct substitution is strictly below the right side `66`; if `q=0`, equality is also impossible with `p<=6`;
- at `rho=5`, the incoming cap gives `p<=7` regardless.

Consequently, even if every source were locally tight, its total incoming load would satisfy

    sum_u p_u
      <= 3*3 + 15*3 + 5*7
      =89,

whereas the exact orientation ledger requires

    sum_u p_u=Q=94.

So the source bound is in fact strict by at least one integer unit at the only possible arithmetic equality point. This closes `(k,E)=(12,2)` as well.

## 8. Bounded theorem

> **Small selected-excess barrier.** In the canonical bridge at `(a,b,t)=(20,23,2)`, suppose all twenty demands lie in `{4,5}` and at least five residual sources have degree at least five. Then
>
>     E=sum_i(x_i-s_i) >=3.
>
> Equivalently, there is no such bridge profile with total selected excess `E=0,1,2`.

The result is a bridge-level structural theorem, not an unrestricted Murty–Simon proof and not a promotion of a fixed-order catalogue result.

## 9. Strategic consequence

The zero-excess obstruction has now moved a definite distance rather than merely changing shape. Any surviving mixed demand-4/5 near-Turán profile in this h>=5 scope must pay at least **three units of degree surplus on the A-label side**.

The weighted ledger (1) is the natural next tool. At `E>=3`, sources with incoming load above residual degree can exist, but every selected incidence at such a source consumes excess capacity. The next attack should use the threshold families

    sum_{u:g_u>=h} q_u
      <= sum_{i:e_i>=h} x_i,

for `h=1,2,3,...`, together with (1), pair/orientation uniqueness and the exact total excess budget. Do not return to a broad histogram census before exploiting these incidence-level excess capacities.
