# Excess-restricted quadratic potential closes total selected excess E=5

17 September 2026. Research directed by Paul Lenz; derivation and internal audit by ChatGPT/Geeps.

**Status: candidate hand theorem inside the canonical selected/residual bridge; not promoted; external mathematical review remains open.** This continues the mixed demand-4/5 near-Turán attack at `(a,b,t)=(20,23,2)`. The preceding two-potential argument closed `E=4`. At `E=5`, one additional restricted quadratic ledger produces a single potential that excludes every demand mixture.

## 1. Scope

Assume

    a=20, b=23, t=2,

all twenty positive demands satisfy `s_i in {4,5}`, and let `k` be the number of demand-five labels. Put

    x_i=s_i+e_i,
    E=sum_i e_i=5.

Then

    r=76+k,
    Q=sum_i x_i=85+k,
    sum_u rho_u=r,
    sum_u p_u=sum_u q_u=Q.

For every selected incidence `ui`, retain

    s_i<=rho_u,
    e_i>=g_u:=max(0,p_u-rho_u+1),
    C_i:=R_i+x_i>=p_u+q_u.                             (1)

Selected labels at one source are distinct, so

    q_u g_u<=E=5.                                      (2)

## 2. Three exact incidence projections

The global quadratic endpoint ledger gives

    W_0:=sum_u q_u(p_u+q_u)
      <= L_0:=sum_i x_i C_i.                           (3)

Restrict to sources with `rho_u=4`. Demand compatibility in (1) forces every selected label there to have `s_i=4`, so

    W_4:=sum_{rho_u=4}q_u(p_u+q_u)
      <= L_4:=sum_{s_i=4}x_iC_i.                       (4)

There is also an **excess-threshold restricted quadratic ledger**. Restrict to sources with

    g_u>=1.

Every selected incidence at such a source has `e_i>=g_u>=1`, hence summing endpoint load over only those incidences gives

    W_+:=sum_{g_u>=1}q_u(p_u+q_u)
      <= L_+:=sum_{e_i>=1}x_iC_i.                      (5)

This is the quadratic analogue of the earlier excess-threshold selected-incidence capacity cut.

Take the nonnegative combination

    12*(3) + 2*(4) + 1*(5).

Define source and label weights

    omega_B(u)=12+2[rho_u=4]+[g_u>=1],
    omega_A(i)=12+2[s_i=4]+[e_i>=1].

Then every actual bridge satisfies

>     K_B:=sum_u omega_B(u)q_u(p_u+q_u)
>       <= K_A:=sum_i omega_A(i)x_iC_i.                (6)

## 3. One uniform source potential

Every local source obeying the canonical caps

    p<=rho+2,
    p+q<=22,
    q+rho<=20 when q>0,
    q=0 when rho<4,

and the exact excess-budget consequence `qg<=5`, satisfies

>     omega_B q(p+q)
>       >= 141p+213q-177rho-246.                       (7)

The complete finite local domain has nonnegative slack. For active sources, the minimum slacks by class are:

| source class | g=0 | g=1 | g=2 | g=3 |
|---|---:|---:|---:|---:|
| `rho=4` | 9 | 0 | 33 | 0 |
| `rho>=5` | 0 | 11 | 67 | 35 |

The incoming cap `p<=rho+2` makes `g<=3`, so these are all active cases. Inactive `q=0` states are also nonnegative; equality occurs at `(rho,p,q)=(1,3,0)`.

Summing (7) over all 23 sources gives

    K_B >=354Q-177r-246*23.                            (8)

## 4. One uniform label potential

Positive demand gives `d_i=R_i+s_i<=19`. Also `C_i=d_i+e_i<=b=23`, and `0<=e_i<=5`.

Every label satisfies

>     omega_A x_iC_i
>       <=224+57R_i+118[s_i=5]+421e_i.                (9)

This can be checked algebraically.

### Demand four

If `e=0`, the left side is `14*4*(R+4)=56R+224`, so the slack is simply

    R>=0.

If `e>=1`, the weight is 15 and right minus left is

    -(15e+3)R +301e-15e^2-16.                         (10)

For `e=1,2,3,4`, the largest allowed `R` is 15; for `e=5`, the additional column cap `C=R+4+e<=23` gives `R<=14`. The minimum slacks for `e=1,...,5` are respectively

    0, 31, 32, 3, 22.

### Demand five

If `e=0`, the weight is 12 and right minus left is

    42-3R>=0

because `R<=14`.

If `e>=1`, the weight is 13 and right minus left is

    -(13e+8)R +291e-13e^2+17.                         (11)

For `e=1,...,4`, `R<=14`; for `e=5`, `C=R+5+e<=23` gives `R<=13`. The minimum slacks for `e=1,...,5` are

    1, 71, 115, 133, 198.

Thus (9) holds throughout the exact label domain.

Summing (9) over the twenty labels gives

    K_A
      <=224*20+57r+118k+421E.                         (12)

At `E=5`, this is

    K_A<=6585+57r+118k.

## 5. Contradiction for every mixture

Combine (6), (8), and (12). A necessary condition for a real bridge is

    354Q-177r-246*23
      <=224*20+57r+118k+421*5.

Equivalently, the source lower bound minus the label upper bound is

    354Q-234r-118k-12243.                              (13)

Substituting

    Q=85+k,
    r=76+k,

gives the exact gap

>     63+2k.                                           (14)

For every `k=0,...,20`,

    63+2k>0,

contradicting (6).

Therefore:

> **There is no canonical bridge profile at `(a,b,t)=(20,23,2)` with all twenty positive demands in `{4,5}` and total selected excess `E=5`.**

Combining with the earlier `E<=4` results gives the current barrier

>     E>=6

for any surviving mixed demand-4/5 bridge in the previously established near-Turán scope.

The E=5 proof itself does not use the earlier `h>=5` assumption; the combined E>=6 statement retains the scope assumptions required by the E<=2 predecessor.

## 6. Audit and strategic consequence

`check_e5_excess_restricted.py` exhaustively checks every integer source state allowed by the canonical caps plus `qg<=5`, every exact label state with `s in {4,5}`, `R+s<=19`, `R+s+e<=23`, `e<=5`, and the final gap `63+2k` for all `k=0,...,20`.

The conceptual gain is the new restricted ledger (5). The selected-excess condition is not only a local cap or Hall eligibility condition: it also allows endpoint load itself to be summed over excess-threshold incidence layers. The coefficient vector

    12 global + 2 demand-four + 1 positive-excess

is already enough to make one support potential work across the complete mixture range.

The next target is not merely `E=6`. First test whether the same three-ledger family supports a parameterized potential in `E`, perhaps with the positive-excess multiplier or affine coefficients depending on E. A stable family would convert the observed sequence of barriers into a genuine excess-growth theorem. If it breaks at E=6, preserve the smallest exact incidence-level obstruction and identify which new excess layer is responsible.
