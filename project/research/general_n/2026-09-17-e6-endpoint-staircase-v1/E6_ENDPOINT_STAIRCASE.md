# Endpoint-tail staircase closes total selected excess E=6

17 September 2026. Research directed by Paul Lenz; derivation and internal audit by ChatGPT/Geeps.

**Status: candidate structural theorem with exact finite local verification; not promoted; external mathematical review remains open.** This continues the mixed demand-4/5 near-Turán attack at `(a,b,t)=(20,23,2)`. At `E=6`, the three-ledger potential used for `E=5` no longer suffices. Retaining endpoint-threshold incidence layers yields a compact staircase with a uniform contradiction independent of the demand mixture.

## 1. Scope

Assume

    a=20, b=23, t=2,

all twenty positive demands satisfy `s_i in {4,5}`. Let `k` be the number of demand-five labels and let total selected excess be

    E=sum_i e_i=6,
    e_i=x_i-s_i.

Then

    r=76+k,
    Q=sum_i x_i=86+k,
    sum_u rho_u=r,
    sum_u p_u=sum_u q_u=Q.

For every selected incidence `ui`, retain

    s_i<=rho_u,
    e_i>=g_u:=max(0,p_u-rho_u+1),
    C_i:=R_i+x_i>=w_u:=p_u+q_u.                       (1)

Selected labels at one source are distinct, hence

    q_u g_u<=6.                                        (2)

## 2. Restricted quadratic incidence layers

Three kinds of restriction are used.

### Demand-four layer

Sources with `rho_u=4` can select only labels with `s_i=4`, so

    sum_{rho_u=4} q_u w_u
      <= sum_{s_i=4} x_i C_i.                          (3)

### Positive-excess layer

Sources with `g_u>=1` can select only labels with `e_i>=1`, so

    sum_{g_u>=1} q_u w_u
      <= sum_{e_i>=1} x_i C_i.                         (4)

### Endpoint-threshold layers

For every integer threshold `T`, endpoint load in (1) gives

    sum_{w_u>=T} q_u w_u
      <= sum_{C_i>=T} x_i C_i.                         (5)

No Hall matching theorem is needed for (3)-(5): each follows by summing `w_u<=C_i` over the relevant actual selected incidences and then allowing all selected incidences on the compatible label side.

Define the endpoint staircase

    psi(z)=3[z>=5]+3[z>=7]+2[z>=8]+[z>=9]+[z>=11].     (6)

Take

- 3 copies of (3),
- 1 copy of (4),
- and the threshold combination encoded by `psi`, namely 3 copies at `T=5`, 3 at `T=7`, 2 at `T=8`, 1 at `T=9`, and 1 at `T=11`.

Thus define

    omega_B(u)=3[rho_u=4]+[g_u>=1]+psi(w_u),
    omega_A(i)=3[s_i=4]+[e_i>=1]+psi(C_i).

Every actual bridge satisfies

>     K_B:=sum_u omega_B(u) q_u w_u
>       <= K_A:=sum_i omega_A(i) x_i C_i.              (7)

This is a nonnegative combination of exact incidence-level necessary inequalities.

## 3. Source potential

Every source obeying the canonical local caps

    p<=rho+2,
    p+q<=22,
    q+rho<=20 when q>0,
    q=0 when rho<4,

and the total-excess consequence `qg<=6`, satisfies

>     omega_B q(p+q)
>       >= 134p+210q-214rho-188.                       (8)

The domain is tiny: the incoming cap implies `g<=3`. Exact integer checking of every allowed `(rho,p,q)` gives no negative slack. The minimum slack for each residual degree is:

| rho | min slack | attaining `(p,q)` |
|---:|---:|---:|
|1|0|(3,0)|
|2|80|(4,0)|
|3|160|(5,0)|
|4|0|(0,6)|
|5|2|(4,6)|
|6|162|(5,8)|
|7|302|(9,2)|
|8|404|(10,2)|
|9|506|(11,2)|
|10|608|(12,2)|
|11|710|(13,2)|
|12|812|(14,2)|
|13|914|(15,2)|
|14|1016|(16,2)|
|15|1108|(17,1)|
|16|1199|(18,1)|
|17|1280|(19,0)|
|18|1360|(20,0)|
|19|1440|(21,0)|
|20|1520|(22,0)|

This table is a compact exact local verification of (8), not an original-graph enumeration.

Summing (8) over the 23 sources gives

    K_B >=344Q-214r-188*23.                            (9)

## 4. Label potential

Positive demand gives `d_i=R_i+s_i<=19`; selected plus residual B-incidences also give

    C_i=R_i+s_i+e_i<=23.

For `s_i in {4,5}` and `0<=e_i<=6`, every label satisfies

>     omega_A x_iC_i
>       <=48+77R_i+53[s_i=5]+362e_i.                 (10)

Again this is an exact small local inequality. Minimum slacks by demand/excess are:

| demand | e | min slack |
|---:|---:|---:|
|4|0|0|
|4|1|102|
|4|2|163|
|4|3|133|
|4|4|75|
|4|5|38|
|4|6|1|
|5|0|4|
|5|1|122|
|5|2|286|
|5|3|329|
|5|4|350|
|5|5|382|
|5|6|414|

The minimum is taken over every integer `R` satisfying both `R+s<=19` and `R+s+e<=23`. Thus (10) holds throughout the exact label domain.

Summing (10) over all twenty labels gives

    K_A
      <=48*20+77r+53k+362E.                           (11)

At `E=6`,

    K_A<=3132+77r+53k.

## 5. Uniform contradiction

Combine (7), (9), and (11). The source lower bound minus the label upper bound equals

    344Q-291r-53k-(188*23+48*20+362*6).               (12)

Substitute

    Q=86+k,
    r=76+k.

The coefficient of `k` cancels exactly:

    344-291-53=0,

and the remaining gap is

>     12.                                               (13)

Thus every `k=0,...,20` would require the impossible inequality

    12<=0.

Therefore:

> **There is no canonical bridge profile at `(a,b,t)=(20,23,2)` with all twenty positive demands in `{4,5}` and total selected excess `E=6`.**

Combining with the earlier `E<=5` results gives the current barrier

>     E>=7

for any surviving mixed demand-4/5 bridge in the previously established near-Turán scope.

The E=6 argument itself does not use the earlier `h>=5` assumption; the combined barrier retains the scope assumptions required by the E<=2 predecessor.

## 6. Audit and strategic consequence

`check_e6_endpoint_staircase.py` independently enumerates every allowed local integer source state, every allowed label state, verifies all restricted-layer weights, and checks the final constant gap 12 for all 21 demand mixtures.

The important structural lesson is that `E=6` does not defeat the incidence programme; it defeats only the coarser three-ledger projection. The missing information is endpoint-tail distribution, and the threshold family (5) restores exactly that information. The staircase `psi` is short and fixed.

The next question should therefore be posed one level more generally: can endpoint-threshold weights be chosen as a function of total excess `E` so that a source/label support potential persists? Test `E=7` next, but preserve any first failure as an explicit endpoint-tail obstruction rather than immediately adding more unrelated machinery.
