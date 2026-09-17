# Hall-count majorization closes total selected excess E=9

17 September 2026. Research directed by Paul Lenz; derivation and internal audit by ChatGPT/Geeps.

**Status: candidate structural theorem with exact finite local verification; not promoted; external mathematical review remains open.** This continues the mixed demand-4/5 near-Turán attack at `(a,b,t)=(20,23,2)`. The first endpoint-load affine potential search failed in the middle demand-mixture range, but retaining the threshold **counts** implied by the full selected-incidence Hall system yields a compact uniform certificate.

## 1. Scope

Assume

    a=20, b=23, t=2,

all twenty positive demands satisfy `s_i in {4,5}`. Let `k` be the number of demand-five labels and let

    E=sum_i e_i=9,
    e_i=x_i-s_i.

Then

    r=76+k,
    Q=sum_i x_i=89+k,
    sum_u rho_u=r,
    sum_u p_u=sum_u q_u=Q.

For every selected incidence `ui`,

    s_i<=rho_u,
    e_i>=g_u:=max(0,p_u-rho_u+1),
    C_i:=R_i+x_i>=w_u:=p_u+q_u.                       (1)

Selected labels at one source are distinct, so

    q_u g_u<=9.                                        (2)

## 2. Hall-count threshold family

Because a source with endpoint requirement `w_u` can use only labels with `C_i>=w_u`, the exact selected-incidence matrix gives, for every integer threshold T,

>     sum_{u:w_u>=T} q_u
>       <= sum_{i:C_i>=T} x_i.                         (3)

This is the count version of endpoint majorization: the multiset containing `q_u` copies of `w_u` must be threshold-dominated by the multiset containing `x_i` copies of `C_i`.

Likewise, a source with `rho_u=4` can select only demand-four labels, hence

>     sum_{u:rho_u=4}q_u
>       <= sum_{i:s_i=4}x_i.                           (4)

No endpoint-load sum, excess-threshold weighting, or graph enumeration is used below—only the Hall-count consequences (3)-(4), the local canonical caps, and the exact margins.

## 3. A short Hall staircase

Define

    phi_9(z)=
        2[z>=6]
       + [z>=7]
       +2[z>=8]
       + [z>=9]
       + [z>=10]
       + [z>=11]
       + [z>=12]
       + [z>=13]
       + [z>=14]
       + [z>=16]
       + [z>=18].                                      (5)

Take two copies of the demand-four count inequality (4) and the nonnegative combination of threshold inequalities (3) encoded by `phi_9`.

Set

    omega_B(u)=2[rho_u=4]+phi_9(w_u),
    omega_A(i)=2[s_i=4]+phi_9(C_i).

Then every actual bridge satisfies

>     H_B:=sum_u omega_B(u)q_u
>       <= H_A:=sum_i omega_A(i)x_i.                   (6)

## 4. Source support inequality

Every local source satisfying

    p<=rho+2,
    p+q<=22,
    q+rho<=20 when q>0,
    q=0 when rho<4,
    q*max(0,p-rho+1)<=9

obeys

>     omega_B q
>       >= 9p+16q-17rho-10.                            (7)

This is an exact small integer inequality. The checker enumerates the complete bounded domain `rho=1,...,20` and every allowed integer `(p,q)`; no negative slack occurs.

Summing (7) over all 23 sources gives

    H_B >=25Q-17r-10*23.                               (8)

## 5. Label support inequality

Every label with

    s in {4,5},
    0<=e<=9,
    R+s<=19,
    C=R+s+e<=23

obeys

>     omega_A x
>       <=8+5R+3[s=5]+18e.                            (9)

Again this is a finite local inequality over a very small exact domain, independently replayed by the checker.

Summing (9) over the twenty labels gives

    H_A
      <=8*20+5r+3k+18E.                               (10)

At E=9 this is

    H_A<=322+5r+3k.

## 6. Uniform contradiction

Combine (6), (8), and (10). The source lower bound minus label upper bound is

    25Q-22r-3k-(10*23+8*20+18*9).                     (11)

Substitute

    Q=89+k,
    r=76+k.

The coefficient of k cancels:

    25-22-3=0,

and the constant gap is exactly

>     1.                                                (12)

Thus every `k=0,...,20` would require the impossible inequality

    1<=0.

Therefore:

> **There is no canonical bridge profile at `(a,b,t)=(20,23,2)` with all twenty positive demands in `{4,5}` and total selected excess E=9.**

Combining with the earlier E<=8 work gives the current barrier

>     E>=10

for any surviving mixed demand-4/5 bridge in the previously established near-Turán scope.

The E=9 proof itself does **not** use the earlier assumption that at least five residual sources have degree at least five. The combined barrier retains whatever scope hypotheses are required by the E<=2 predecessor.

## 7. Discovery history and audit boundary

The first affine endpoint-load potential cone failed for the middle values `k=5,...,18`, even after all endpoint/excess/demand intersections were included. An exact threshold-Hall histogram model then showed infeasibility for all k. Its LP relaxation was also infeasible, proving that the phenomenon was linear rather than integrality-only. Dual compression produced the Hall staircase (5), after which the entire E=9 closure reduces to (7)-(12).

The failed affine route is preserved conceptually because it identifies the precise gain: **count majorization is information not recoverable from endpoint-load sums alone**.

`check_e9_hall_majorization.py` independently verifies every source state, every label state, and the constant global gap 1 for all 21 demand mixtures.

The next target is E=10. The natural first question is whether the same Hall-count architecture admits another short threshold staircase or whether E=10 is the first point where the full subset Hall system, rather than nested endpoint counts, becomes necessary.
