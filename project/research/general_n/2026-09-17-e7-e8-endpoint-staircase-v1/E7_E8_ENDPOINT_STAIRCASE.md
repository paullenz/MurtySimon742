# Endpoint-tail staircases close total selected excess E=7 and E=8

17 September 2026. Research directed by Paul Lenz; derivation and internal audit by ChatGPT/Geeps.

**Status: candidate structural theorems with exact finite local verification; not promoted; external mathematical review remains open.** These continue the mixed demand-4/5 near-Turán attack at `(a,b,t)=(20,23,2)` after the E=6 endpoint-staircase theorem.

## 1. Common incidence-layer principle

Assume all twenty positive demands satisfy `s_i in {4,5}`. Let `k` be the number of demand-five labels and write total selected excess

    E=sum_i e_i,
    e_i=x_i-s_i.

Then

    r=76+k,
    Q=80+k+E.

For every selected incidence `ui`,

    s_i<=rho_u,
    e_i>=g_u:=max(0,p_u-rho_u+1),
    C_i:=R_i+x_i>=w_u:=p_u+q_u.

As before, every nonnegative combination of the following restricted endpoint-load inequalities is valid:

- `rho_u=4` sources versus `s_i=4` labels;
- `g_u>=1` sources versus `e_i>=1` labels;
- `w_u>=T` sources versus `C_i>=T` labels, for any threshold T.

The total excess budget and distinctness of selected labels at a source give

    q_u g_u<=E.

The two closures below use only these facts and the canonical local caps.

## 2. Total selected excess E=7

Define

    psi_7(z)=6[z>=6]+[z>=7]+2[z>=8]+[z>=9]+[z>=11].

Set

    omega_B=3[rho=4]+[g>=1]+psi_7(w),
    omega_A=3[s=4]+[e>=1]+psi_7(C).

The incidence-layer inequalities imply

    sum_u omega_B q_u w_u
      <= sum_i omega_A x_i C_i.                        (1)

Exact local integer verification gives the two support inequalities

    omega_B q(p+q)
      >=142p+224q-222rho-204,                          (2)

and

    omega_A xC
      <=48+84R+69[s=5]+392e.                          (3)

The checker verifies (2) over every integer source state satisfying the canonical caps and `qg<=7`, and verifies (3) over every label state with `s in {4,5}`, `R+s<=19`, `R+s+e<=23`, `0<=e<=7`.

Summing (2) and (3), using `Q=87+k` and `r=76+k`, gives source lower minus label upper

>     190-9k.                                          (4)

For `0<=k<=20`, this is at least 10. Hence E=7 is impossible.

## 3. Total selected excess E=8

Define

    psi_8(z)=8[z>=6]+2[z>=7]+2[z>=8]+[z>=9]+[z>=10]+[z>=11].

Set

    omega_B=4[rho=4]+3[g>=1]+psi_8(w),
    omega_A=4[s=4]+3[e>=1]+psi_8(C).

Again the exact incidence-layer inequalities imply

    sum_u omega_B q_u w_u
      <= sum_i omega_A x_i C_i.                        (5)

Every allowed source satisfies

    omega_B q(p+q)
      >=206p+308q-309rho-312,                          (6)

and every allowed label satisfies

    omega_A xC
      <=64+112R+93[s=5]+597e.                         (7)

These local inequalities are checked exactly on the complete bounded integer domains with `qg<=8` and `0<=e<=8`.

Summing and substituting

    Q=88+k,
    r=76+k,

produces the particularly simple gap

>     4.                                               (8)

The coefficient of `k` cancels identically. Thus E=8 is impossible for every demand mixture.

## 4. Current barrier

Together with the E<=6 work, these results give

> **Any surviving mixed demand-4/5 near-Turán bridge in the established scope must have total selected excess E>=9.**

The E=7 and E=8 arguments themselves do not use the earlier `h>=5` assumption; the combined barrier retains whatever scope assumptions are needed by the E<=2 predecessor.

## 5. First failure at E=9

The same support-potential hierarchy was tested at E=9 before adding unrelated machinery. This is the first excess level at which it ceases to close the whole mixture range.

A continuous dual search allowing:

- all endpoint thresholds `T=4,...,22`,
- excess thresholds `g>=1,2,3` versus `e>=1,2,3`,
- the demand-four restriction,
- and their demand/excess/endpoint intersections,

finds positive support-potential certificates for `k=0,...,4` and `k=19,20`, but no positive affine certificate for `k=5,...,18`. In particular, the failure persists after adding every endpoint threshold, so it is not merely a poor choice of staircase coefficients.

This is a **methodological obstruction**, not a graph realization and not a Murty-Simon counterexample. It marks the point where the full selected-incidence Hall system or another genuinely non-affine incidence argument should be applied rather than indefinitely enlarging scalar potential searches.

The exact E=9 diagnostic is not promoted as a theorem of feasibility. The next task is to freeze a smallest incidence-level survivor or close the middle `k` range with full Hall/transport.
