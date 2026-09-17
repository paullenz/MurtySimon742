# Hall-ramp majorization closes the remaining mixed demand-4/5 selected-excess range

17 September 2026. Research directed by Paul Lenz; derivation and internal audit by ChatGPT/Geeps.

**Status: candidate structural theorem with exact finite local verification; not promoted; external mathematical review remains open.**

This note continues the canonical near-Turán bridge at

    (a,b,t)=(20,23,2),

with all twenty positive demands in `{4,5}`. Earlier packages exclude total selected excess `E=0,...,9`. The purpose here is to avoid another level-by-level census: three **range-uniform Hall-ramp certificates** exclude every arithmetically possible `E>=10`.

## 1. Exact incidence setup

Let `k` be the number of demand-five labels. Write

    s_i in {4,5},
    x_i=s_i+e_i,
    E=sum_i e_i,
    C_i=R_i+x_i,

and on the 23 source vertices write residual degree `rho_u`, incoming orientation load `p_u`, selected outdegree `q_u`, and

    w_u=p_u+q_u,
    g_u=max(0,p_u-rho_u+1).

The canonical ledgers are

    r=sum_i R_i=sum_u rho_u=76+k,
    Q=sum_i x_i=sum_u p_u=sum_u q_u=80+E+k.

Every selected incidence `ui` satisfies

    s_i<=rho_u,
    e_i>=g_u,
    C_i>=w_u.

Selected labels at one source are distinct, so

    q_u g_u<=E.                                      (1)

The local canonical caps used below are

    p_u<=rho_u+2,
    p_u+q_u<=22,

and, when `q_u>0`,

    rho_u>=4,
    q_u+rho_u<=20.                                  (2)

On the label side,

    R_i+s_i<=19,
    C_i<=23.                                        (3)

No graph catalogue or q-enumeration is used in this note.

## 2. Hall-count majorization and ramps

The exact selected-incidence matrix gives, for every integer threshold `T`,

>     sum_{u:w_u>=T} q_u
>       <= sum_{i:C_i>=T} x_i.                       (4)

Also, a source with `rho_u=4` can select only demand-four labels:

>     sum_{u:rho_u=4} q_u
>       <= sum_{i:s_i=4} x_i.                        (5)

For `L>=5` define the capped ramp

    H_L(z)=max(0,min(z,L)-4)
          =sum_{T=5}^L [z>=T].                       (6)

Therefore every nonnegative combination

    Phi(z)=sum_L c_L H_L(z),   c_L>=0,               (7)

is automatically a valid Hall-count potential. With a nonnegative demand-four weight `mu`, put

    omega_B(u)=mu[rho_u=4]+Phi(w_u),
    omega_A(i)=mu[s_i=4]+Phi(C_i).

Equations (4)-(5) imply

>     sum_u omega_B(u) q_u
>       <= sum_i omega_A(i) x_i.                     (8)

The three certificates below differ only in the short choice of `Phi`, `mu`, and two local affine support inequalities.

## 3. Range 10 <= E <= 15

Take

    Phi=4 H_9 + 12 H_12 + 4 H_19,
    mu=33.                                           (9)

For every source state satisfying (1)-(2) with the weakest restriction `qg<=15`,

>     omega_B q
>       >= 104p + 212q - 188rho - 124.               (10)

For every label state satisfying (3) with `0<=e<=15`,

>     omega_A x
>       <= 132 + 80R + 48[s=5] + 256e.               (11)

Summing (10), (11), and (8) gives a lower-minus-upper contradiction gap

    60E - 580.                                       (12)

This is at least `20` throughout `10<=E<=15`, independently of `k`.

## 4. Range 16 <= E <= 21

Take

    Phi=5 H_9 + 19 H_14,
    mu=40.                                           (13)

Every source state with `qg<=21` obeys

>     omega_B q
>       >= 127p + 261q - 236rho - 146,               (14)

and every label state with `0<=e<=21` obeys

>     omega_A x
>       <= 160 + 96R + 56[s=5] + 341e.               (15)

After summation the contradiction gap is

    47E - 750.                                       (16)

Its minimum on this range is `2`, at `E=16`.

## 5. Range 22 <= E <= 42

Take

    Phi=6 H_8 + 24 H_15,
    mu=46.                                           (17)

Every source state with `qg<=42` obeys

>     omega_B q
>       >= 153p + 333q - 311rho - 150,               (18)

and every label state obeys

>     omega_A x
>       <= 184 + 120R + 56[s=5] + 439e.              (19)

(The label domain is already bounded by `C<=23`, so allowing `e<=42` introduces no hidden large-excess states.)

The summed contradiction gap is

    47E - k - 1006.                                  (20)

For `22<=E<=42` and `0<=k<=20` this is at least

    47*22 - 20 - 1006 = 8.                           (21)

## 6. There is no E >= 43 case

The incoming cap in (2) already gives

    Q=sum_u p_u
      <= sum_u (rho_u+2)
      = r+46.

Using `Q=80+E+k` and `r=76+k` yields

>     E<=42.                                         (22)

Thus the three Hall-ramp bands cover **every** remaining arithmetically possible excess value `E>=10`.

Combining with the preserved `E=0,...,9` closures gives:

> **No canonical bridge in the established mixed demand-4/5 near-Turán scope `(a,b,t)=(20,23,2)` survives at any total selected excess `E`.**

The new `E>=10` argument itself does not use the older `h>=5` hypothesis. The combined all-E statement inherits whatever scope assumptions are still required by the preserved `E<=2` predecessor.

## 7. Why this is structurally preferable to level-by-level continuation

The key compression is the capped-ramp identity (6). Instead of adding a bespoke threshold staircase for each next value of `E`, the exact Hall-count system is used through only three range-uniform monotone potentials:

    10..15 : 4 H_9 + 12 H_12 + 4 H_19,
    16..21 : 5 H_9 + 19 H_14,
    22..42 : 6 H_8 + 24 H_15.

The final range is followed by the elementary global cap `E<=42`. So the previous `E>=10` barrier is not merely advanced: within this demand support the selected-excess dimension is exhausted completely.

`check_hall_ramp_all_excess.py` independently enumerates every local integer source and label state needed for (10)-(11), (14)-(15), and (18)-(19), and checks every global `(E,k)` gap exactly.

## 8. Audit boundary and next structural question

This closes one concrete scope frontier, not Murty-Simon itself. It does not prove that every remaining canonical bridge has demand support contained in `{4,5}`, nor does it replace the five-label exact-block theorem or its external review obligations.

The next high-value question is therefore **not E=43**. It is whether the Hall-ramp argument can be generalized to the next demand-support patterns, or whether the earlier structural bridge can force a surviving near-Turán configuration into the now-closed `{4,5}` support. That is the appropriate place to seek a compact scope theorem rather than returning to survivor-by-survivor exclusion.
