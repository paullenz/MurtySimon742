# E=3 row-packing barrier in the mixed demand-4/5 near-Turan band

17 September 2026. Research directed by Paul Lenz; derivation and internal audit by ChatGPT/Geeps.

**Status: candidate bridge theorem; not promoted; external mathematical review remains open.** This continues the selected-excess attack at `(a,b,t)=(20,23,2)`. The preceding theorem proves `E>=3`. The full selected-incidence Hall theorem shows that aggregate endpoint/excess ledgers alone are too weak at `E=3`. The result below closes `E=3` by retaining two cheap consequences of the full selected-incidence system: per-source row packing and the global selected capacity of the demand-four labels.

## 1. Setup

Assume the all-positive-demand canonical bridge with

    a=20, b=23, t=2,

all twenty demands in `{4,5}`, and at least five residual sources of degree at least five. Let `k` be the number of demand-five labels. Write

    x_i=s_i+e_i,
    E=sum_i e_i.

This note treats `E=3`. Then

    r=sum_u rho_u=76+k,
    Q=sum_u p_u=sum_u q_u=sum_i x_i=83+k.

Every source has `rho_u>=1`. The established canonical restrictions include

    p_u<=rho_u+2,
    p_u+q_u<=22,
    rho_u+q_u<=20.

If `q_u>0`, every one of its `q_u` distinct selected labels satisfies

    s_i<=rho_u,
    e_i>=g_u:=max(0,p_u-rho_u+1).

Because the total excess is only three, row packing gives the universal implications

    g_u>=1 => q_u<=3,
    g_u>=2 => q_u<=1,
    g_u>=4 => q_u=0.                                  (1)

Also `q_u=0` when `rho_u<4`. When `rho_u=4`, every selected label has demand four, so

    q_u<=20-k.                                          (2)

Let

    T_4=sum_{u:rho_u=4} q_u.

Every selected incidence counted by `T_4` lands on a demand-four label. The total selected degree of all demand-four labels is

    4(20-k)+E_4 <=4(20-k)+3,

where `E_4` is the excess carried by those labels. Hence

> **Demand-four selected-capacity cut**
>
>     T_4 <=83-4k.                                      (3)

This is a direct projection of the full selected-incidence Hall system, not an independent relaxation assumption.

## 2. Universal label-side upper bound at E=3

The zero-excess endpoint calculation from the preceding small-excess theorem gives

    U_0(k)=624+13k+min(14k,76+k).

For fixed `s_i,R_i`, adding excess `e_i` changes the unweighted label contribution `x_i(R_i+x_i)` by

    e_i(d_i+s_i)+e_i^2,

where `d_i=R_i+s_i<=19` and `s_i<=5`. Therefore, when `E=3`,

    sum_i x_i(R_i+x_i)
      <= U_0(k)+24E+E^2
      = U_0(k)+81.                                     (4)

Call the right side `U_3(k)`.

The exact quadratic endpoint ledger requires

    sum_i x_i(R_i+x_i) >= W:=sum_u q_u(p_u+q_u).       (5)

Thus it is enough to force `W>U_3(k)`.

## 3. Finite local source-potential lemma

Put

    H_u=[rho_u>=5],
    I_u=[rho_u=4],
    W_u=q_u(p_u+q_u).

Under the local integer restrictions above, including (1) and (2), the following inequalities hold for every source. They are deliberately presented with integer coefficients.

For `0<=k<=2`,

    3W_u >= -42-42rho_u+28p_u+48q_u+32H_u.             (6a)

For `3<=k<=6`,

    W_u >= -19-14rho_u+11p_u+17q_u+3H_u-q_u I_u.       (6b)

For `7<=k<=13`,

    7W_u >= -133-98rho_u+77p_u+122q_u-10q_u I_u.       (6c)

For `k=14`,

    19W_u >= -460-332rho_u+264p_u+361q_u-24q_u I_u.    (6d)

For `k=15`,

    48W_u >= -1121-835rho_u+652p_u+912q_u-27q_u I_u.   (6e)

For `16<=k<=19`,

    3W_u >= -68-52rho_u+40p_u+57q_u.                   (6f)

For `k=20`,

    4W_u >= -109-71rho_u+60p_u+76q_u.                  (6g)

These are finite local inequalities, not a numerical optimization claim. `check_e3_row_packing.py` enumerates every legal integer `(k,rho,p,q)` state and verifies all of (6a)-(6g) exactly. A separately written C++ checker independently verifies the same 32,439 local states.

## 4. Summed source lower bounds

Sum the relevant inequality over all 23 sources. Use

    sum rho=76+k,
    sum p=sum q=83+k,
    sum H_u>=5,
    T_4<=83-4k.

This gives the following lower bounds `B(k)` for `W`:

| k | B(k) | U_3(k) | B(k)-U_3(k) |
|---:|---:|---:|---:|
|0|770|705|65|
|1|2344/3|732|148/3|
|2|2378/3|759|101/3|
|3|809|786|23|
|4|827|813|14|
|5|845|840|5|
|6|863|865|-2|
|7|881|879|2|
|8|6308/7|893|57/7|
|9|6449/7|907|100/7|
|10|6590/7|921|143/7|
|11|6731/7|935|186/7|
|12|6872/7|949|229/7|
|13|7013/7|963|272/7|
|14|19517/19|977|954/19|
|15|16961/16|991|1105/16|
|16|1085|1005|80|
|17|1100|1019|81|
|18|1115|1033|82|
|19|1130|1047|83|
|20|4685/4|1061|441/4|

Therefore (4)-(5) contradict every `k` except `k=6`.

The important point is that the source lower bound is obtained from a small local potential family plus exact global margins and the selected-incidence capacity (3). It is not a catalogue scan and does not enumerate graph realizations.

## 5. Hand closure of k=6

At `k=6`,

    U_0(6)=784,
    B(6)=863.

Only the very loosest excess placement can make the universal label upper reach 865.

### 5.1 Excess partition is not `(3)`

If the three units of excess are split as `(2,1)` or `(1,1,1)`, then

    sum e_i^2<=5.

Hence the label-side increment over `U_0(6)` is at most

    24*3+5=77,

so

    sum_i x_i C_i <=861<863<=W,

contradiction.

### 5.2 Partition `(3)` lies on a demand-four label

For the unique excess label, `s=4`, so `d+s<=19+4=23`. Its increment is at most

    3*23+9=78.

Thus

    sum_i x_i C_i <=862<863<=W,

again impossible.

### 5.3 Partition `(3)` lies on a demand-five label

Now there is no excess on any demand-four label. Therefore the exact demand-four selected capacity improves from the universal value 59 to

    T_4<=4(20-6)=56.                                   (7)

Summing the same local potential (6b) with (7) raises the source lower bound by three:

    W>=866.

But the universal label upper is still only

    U_3(6)=865.

So this final case is impossible as well.

Hence `k=6` is closed.

## 6. Bounded theorem

> **E=3 row-packing barrier.** In the canonical bridge at `(a,b,t)=(20,23,2)`, suppose all twenty demands lie in `{4,5}` and at least five residual sources have degree at least five. Then no bridge profile has total selected excess `E=3`.
>
> Combined with the preceding `E=0,1,2` theorem, every such bridge satisfies
>
>     E>=4.

This is a bridge-level structural result. It is not an unrestricted Murty-Simon proof and does not promote a fixed-order catalogue result.

## 7. Audit and strategic consequence

`check_e3_row_packing.py` verifies all 32,439 legal local source states, recomputes the exact rational summed lower bounds, checks every `k!=6` gap, and replays the three `k=6` closures. `check_e3_row_packing.cpp` independently verifies the local-potential family over the same 32,439 states.

The earlier exploratory E=3 transport screen is no longer needed as proof evidence for this bounded conclusion. Its useful lesson has been compressed into the row-packing restrictions and the demand-four capacity cut.

The next structural frontier is now `E=4`. Before enumerating it, reassess the excess partitions `(4)`, `(3,1)`, `(2,2)`, `(2,1,1)`, `(1,1,1,1)` under the same full selected-incidence hierarchy. The first question should be whether a comparable universal source-potential family pushes the lower bound through E=4, and if not, which exact excess partition survives.